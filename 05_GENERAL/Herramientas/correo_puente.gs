// Correo automático, plan C (Apps Script vinculado a la hoja de correos). Sustituye al flujo de Studio.
//
// Cada 5 minutos (activador basado en tiempo sobre `procesar`):
//   1. Busca en Gmail los correos nuevos dirigidos al buzón compartido (propiedad GRUPO),
//      excluye los del remitente de alertas de Rundeck (EXCLUIR) y los ya procesados.
//   2. Pide a Gemini (API, propiedad GEMINI_API_KEY, modelo MODELO) el JSON con asunto,
//      sintoma, resumen, fecha, es_ticket, motivo, entorno, categoria, prioridad, detalles y evento,
//      con salida JSON estricta. Las capturas (imágenes) y los PDF del correo van a Gemini
//      como partes multimodales, para que describa lo que muestran en `detalles`.
//      El script añade `adjuntos` (nombres de los ficheros) al JSON antes de enviarlo.
//   3. Escribe una fila en la hoja (registro) y, si es ticket, lo manda a GitHub como
//      repository_dispatch "correo" (propiedad GITHUB_TOKEN). La Action crea el ticket.
//   4. Apunta el id del mensaje en la pestaña "procesados" para no repetirlo nunca.
//   5. Latido: la primera ejecución de cada día laborable a partir de las 08:00 de
//      São Paulo publica en Google Chat (GCHAT_WEBHOOK, opcional) cuántos correos leyó ayer.
//   7. Foto del día: a las 08:55 Madrid, 08:55 São Paulo y 10:55 México pide a GitHub
//      (repository_dispatch "foto") que publique en Chat el resumen de tickets.
//   8. App de Chat (onMessage): responde a "@BAU NFQBAU-1545", "@BAU foto", "@BAU guardia" y
//      "@BAU ayuda" leyendo el vault en GitHub (contents API, con GITHUB_TOKEN). Solo lectura.
//      Requiere el script enlazado a un proyecto de Cloud con la Google Chat API y una
//      implementación (Implementar > Nueva implementación > Complemento) cuyo ID va en la
//      configuración de la API de Chat. Sin eso, el resto del script funciona igual.
//   6. Pestaña "estado": en cada ciclo reescribe última lectura, próxima prevista, correos
//      del ciclo y del día, último error. Es la respuesta a "¿llegó mi correo y no hay ticket?".
//
// `probar(n)` procesa los últimos n correos del grupo SIN enviar nada a GitHub ni marcar
// nada: escribe los resúmenes en la pestaña "pruebas" para compararlos antes de activar.
//
// Propiedades del script: GITHUB_TOKEN, GEMINI_API_KEY, GRUPO, EXCLUIR (opcional: lista de
// remitentes o fragmentos separados por comas), MODELO (lista de modelos separados por comas,
// de mejor a peor; cada uno tiene su propia cuota diaria en el plan gratuito, 20 los Flash y
// 500 los Flash Lite; por defecto la cadena de MODELOS_POR_DEFECTO), REINTENTOS (opcional, por
// defecto 3, solo ante 503), GCHAT_WEBHOOK (opcional), DESDE (se fija sola en la primera ejecución: solo se procesan
// correos posteriores; cambiarla a mano para reprocesar desde otra fecha, formato ISO).
//
// Primera ejecución: solo se arma (guarda DESDE) y no procesa nada, para no convertir en
// ticket correos antiguos que ya lo fueron. Tope de LOTE correos por ejecución.

var PROPS = PropertiesService.getScriptProperties();
var ZONA = 'America/Sao_Paulo';
var REPO = 'RicardoNfq/BAU-NFQ-vault';
var LOTE = 20;                     // correos como máximo por ejecución; el resto, en el siguiente ciclo
var MODELOS_POR_DEFECTO = 'gemini-3.8-flash, gemini-3.7-flash, gemini-3.6-flash, gemini-3-flash, gemini-2.5-flash, gemini-3.5-flash-lite, gemini-3.1-flash-lite';
var SIN_CUOTA = false;             // se pone a true cuando todos los modelos han dado 429: el ciclo se detiene

var PROMPT = [
  'Eres el asistente de un equipo de soporte. Recibes un correo, casi siempre en portugués de Brasil, y devuelves SOLO un JSON con once campos, en español:',
  '- "asunto": el asunto del correo tal cual, sin cambiarlo.',
  '- "sintoma": una sola línea que diga cómo se manifiesta el problema (qué informe, job, tabla o pantalla falla y cómo). Sin nombres de personas.',
  '- "resumen": dos o tres líneas con qué pide el remitente, qué ha pasado y desde cuándo. Refiérete a las personas por su nombre de pila, la inicial de su primer apellido y su rol o empresa: "José Carlos N., contabilidad de fondos del cliente", "Ricardo C., responsable del Proyecto Apollo". Nunca el apellido completo. No incluyas direcciones de correo, teléfonos, enlaces, direcciones postales, claves de reunión ni firmas. Si hay adjuntos, di solo "adjunta capturas" o "adjunta un fichero".',
  '- "fecha": la fecha del correo en formato AAAA-MM-DD.',
  '- "es_ticket": true si el correo es una incidencia, un error, una petición o una consulta de un cliente o de un proveedor dirigida al equipo de soporte; false si es una notificación automática de un sistema (Drive, calendario, alertas, Jira), una newsletter, un acuse de recibo, un reenvío sin petición, o una conversación interna sin nada que resolver. En caso de duda, true.',
  '- "motivo": una línea que explique por qué es o no es ticket.',
  '- "entorno": "Producción" si el correo habla de producción, PRD, prod o produção; "UAT" si habla de UAT, homologação, homolog o teste; null si no se puede saber.',
  '- "categoria": una de "Rundeck" (jobs, cargas, flags, execuções), "BBDD" (tablas, funciones, vistas, PostgreSQL, consultas), "Qlik" (informes, relatórios, dashboards, paneles), "APIs" (servicios, integraciones, endpoints) u "Otros"; null si no se deduce.',
  '- "prioridad": "Alta" si es urgente, bloquea al cliente o producción está parada; "Baja" si es una mejora, una consulta o no tiene plazo; "Media" en el resto.',
  '- "detalles": todo dato técnico útil que aporte el correo o sus capturas: nombres de jobs, tablas, funciones, informes, mensajes de error literales, fechas o periodos de los datos afectados, cantidades, pasos para reproducir. Si hay capturas de pantalla, describe lo que muestran (qué pantalla, qué error). Varias líneas separadas por "; ". Sin datos de contacto. "" si no hay nada.',
  '- "evento": qué paso del circuito marca este correo, solo si lo dice de forma explícita: "aprobacion" si el cliente acepta el paquete o la solución propuesta; "desplegado_uat" si NTT (o el proveedor) confirma que ya ejecutó o desplegó el cambio en UAT u homologação; "aprobacion_uat" si el cliente confirma que las pruebas en UAT están bien; "aprobacion_prd" si el cliente da su conformidad ("de acordo", "pode seguir") para ejecutar en producción; "desplegado_prd" si NTT confirma que ya lo ejecutó en producción; "rechazo" si el cliente dice que no funciona, que falta algo o lo rechaza. null en cualquier otro caso: una pregunta, un "estamos verificando", un recordatorio o un correo interno. En caso de duda, null.',
  'Si el correo es una respuesta dentro de un hilo, resume solo lo nuevo que aporta: ignora el texto citado de correos anteriores.',
  ''
].join('\n');

// ---------------------------------------------------------------- utilidades
function hoja(nombre, cabeceras) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var h = ss.getSheetByName(nombre);
  if (!h) { h = ss.insertSheet(nombre); h.appendRow(cabeceras); }
  return h;
}
function marca() { return Utilities.formatDate(new Date(), ZONA, 'yyyy-MM-dd HH:mm'); }
function fechaDe(d) { return Utilities.formatDate(d, ZONA, 'yyyy-MM-dd'); }

function esParaElGrupo(msg, grupo) {
  var g = grupo.toLowerCase();
  var cab = [msg.getTo(), msg.getCc(), msg.getBcc(), msg.getHeader('Delivered-To'), msg.getHeader('X-Original-To')].join(' ').toLowerCase();
  return cab.indexOf(g) >= 0;
}

// Una llamada a Gemini con una lista de partes (texto e imágenes). Devuelve {ok, codigo, texto}. No lanza.
function llamarGemini(modelo, partes) {
  var url = 'https://generativelanguage.googleapis.com/v1beta/models/' + modelo + ':generateContent?key=' + PROPS.getProperty('GEMINI_API_KEY');
  var r = UrlFetchApp.fetch(url, {
    method: 'post', contentType: 'application/json', muteHttpExceptions: true,
    payload: JSON.stringify({
      contents: [{ parts: partes }],
      generationConfig: { responseMimeType: 'application/json', temperature: 0.2 }
    })
  });
  var codigo = r.getResponseCode();
  if (codigo != 200) return { ok: false, codigo: codigo, texto: r.getContentText().slice(0, 160) };
  var salida = JSON.parse(r.getContentText());
  return { ok: true, codigo: 200, texto: salida.candidates[0].content.parts.map(function (p) { return p.text; }).join('').trim() };
}

// Nombres de los ficheros adjuntos (incluye las imágenes en línea del cuerpo).
function nombresAdjuntos(msg) {
  return msg.getAttachments({ includeInlineImages: true }).map(function (a) { return a.getName(); });
}

// Capturas (imágenes) y PDF del correo como partes multimodales para Gemini.
// ponytail: tope de 3 ficheros de 30 KB a 2 MB. Por debajo de 30 KB son logos e iconos de firma;
// por encima, subirlos en base64 tarda demasiado (Apps Script corta a los 6 min). Excel y otros
// formatos solo se citan por nombre.
function adjuntosParaGemini(msg) {
  return msg.getAttachments({ includeInlineImages: true }).filter(function (a) {
    var tipo = a.getContentType() || '';
    return (tipo.indexOf('image/') === 0 || tipo === 'application/pdf') && a.getSize() >= 30 * 1024 && a.getSize() <= 2 * 1024 * 1024;
  }).slice(0, 3).map(function (a) {
    return { inline_data: { mime_type: a.getContentType(), data: Utilities.base64Encode(a.getBytes()) } };
  });
}

// Pide el JSON a Gemini recorriendo la cadena de modelos (MODELO, de mejor a peor):
//   - 429 (cuota agotada, por minuto o por día): ese modelo no se reintenta, se pasa al siguiente.
//     Reintentar gastaría la cuota que no hay. Si todos dan 429, se marca SIN_CUOTA y el
//     ciclo se detiene: los correos pendientes esperan al siguiente (cada 5 min).
//   - 503 (alta demanda): REINTENTOS intentos (por defecto 3) con esperas 2, 4, 8 s, y después
//     el siguiente modelo.
//   - cualquier otro error (404 por nombre de modelo mal escrito, 400...): siguiente modelo.
// Devuelve el texto JSON; lanza con el último error si todo falla. Un correo fallido no se
// marca como procesado y el siguiente ciclo lo reintenta desde cero durante 3 días.
function modelos() {
  return (PROPS.getProperty('MODELO') || MODELOS_POR_DEFECTO).split(',')
    .map(function (s) { return s.trim(); }).filter(function (s) { return s; });
}
function pedirAGemini(msg, soloPrincipal) {
  var lista = soloPrincipal ? modelos().slice(0, 1) : modelos();
  var intentos = Number(PROPS.getProperty('REINTENTOS')) || 3;
  var cuerpo = (msg.getPlainBody() || '').slice(0, 12000);
  var partes = [{ text: PROMPT + 'Asunto: ' + msg.getSubject() + '\nFecha: ' + fechaDe(msg.getDate()) + '\nRemitente: ' + msg.getFrom()
    + '\nAdjuntos: ' + (nombresAdjuntos(msg).join(', ') || 'ninguno') + '\nCuerpo:\n' + cuerpo }].concat(adjuntosParaGemini(msg));
  var ultimo = '', todos429 = true;
  for (var m = 0; m < lista.length; m++) {
    for (var i = 0; i < intentos; i++) {
      var r = llamarGemini(lista[m], partes);
      if (r.ok) { ULTIMO_MODELO = lista[m] + (i ? ' (intento ' + (i + 1) + ')' : ''); return r.texto; }
      ultimo = 'Gemini ' + r.codigo + ' con ' + lista[m] + ': ' + r.texto;
      if (r.codigo != 429) todos429 = false;
      if (r.codigo != 503) break;                       // 429 o error fijo: no insistir con este modelo
      Utilities.sleep(2000 * Math.pow(2, i));            // 2, 4, 8 s
    }
  }
  if (todos429) SIN_CUOTA = true;
  throw new Error(ultimo);
}
var ULTIMO_MODELO = '';

// fila y cuando viajan con el correo: la Action los cita en el aviso de rechazo para
// localizar la línea en la hoja ("fila 143, leído a las 09:31").
function enviarAGitHub(textoJson, fila, cuando) {
  var r = UrlFetchApp.fetch('https://api.github.com/repos/' + REPO + '/dispatches', {
    method: 'post', contentType: 'application/json', muteHttpExceptions: true,
    headers: { Authorization: 'Bearer ' + PROPS.getProperty('GITHUB_TOKEN'), Accept: 'application/vnd.github+json' },
    payload: JSON.stringify({ event_type: 'correo', client_payload: { texto: textoJson, fila: fila, cuando: cuando } })
  });
  return r.getResponseCode();
}

function idsProcesados() {
  var h = hoja('procesados', ['id', 'cuando']);
  var ids = {};
  h.getDataRange().getValues().slice(1).forEach(function (f) { ids[String(f[0])] = true; });
  return ids;
}

function excluidos() {
  // EXCLUIR = "alerts_rundeck@..., otra@..., fragmento@" → lista en minúsculas sin vacíos
  return (PROPS.getProperty('EXCLUIR') || '').toLowerCase().split(',')
    .map(function (s) { return s.trim(); }).filter(function (s) { return s; });
}

function remitenteExcluido(msg) {
  var de = msg.getFrom().toLowerCase();
  return excluidos().some(function (x) { return de.indexOf(x) >= 0; });
}

function correosNuevos(dias) {
  var grupo = PROPS.getProperty('GRUPO');
  if (!grupo) throw new Error('Falta la propiedad GRUPO (dirección del buzón compartido)');
  var desde = new Date(PROPS.getProperty('DESDE'));
  var ya = idsProcesados();
  var consulta = '(to:' + grupo + ' OR cc:' + grupo + ' OR deliveredto:' + grupo + ') newer_than:' + dias + 'd';
  var mensajes = [];
  GmailApp.search(consulta, 0, 100).forEach(function (hilo) {
    hilo.getMessages().forEach(function (m) {
      if (ya[m.getId()]) return;
      if (m.getDate() <= desde) return;                 // anterior a la activación: no se toca
      if (!esParaElGrupo(m, grupo)) return;
      if (remitenteExcluido(m)) return;
      mensajes.push(m);
    });
  });
  mensajes.sort(function (a, b) { return a.getDate() - b.getDate(); });
  return mensajes.slice(0, LOTE);
}

// ---------------------------------------------------------------- principal
function procesar() {
  if (!PROPS.getProperty('DESDE')) {                   // primera ejecución: solo se arma
    PROPS.setProperty('DESDE', new Date().toISOString());
    hoja('correos', ['cuando', 'fecha correo', 'remitente', 'asunto', 'json', 'resultado', 'modelo'])
      .appendRow([marca(), '', '', '(activado)', '', 'a partir de ahora se procesan los correos nuevos']);
    return;
  }
  var registro = hoja('correos', ['cuando', 'fecha correo', 'remitente', 'asunto', 'json', 'resultado', 'modelo']);
  var procesados = hoja('procesados', ['id', 'cuando']);
  var mensajes = correosNuevos(3);
  mensajes.forEach(function (m) {
    if (SIN_CUOTA) return;                             // todos los modelos agotados: el resto espera al siguiente ciclo
    // La fila se escribe ANTES de enviar, para mandar su número a GitHub; luego se completa.
    var cuando = marca();
    registro.appendRow([cuando, fechaDe(m.getDate()), m.getFrom().replace(/<.*>/, '').trim(), m.getSubject(), '', 'procesando', '']);
    var fila = registro.getLastRow();
    var resultado, json = '';
    try {
      json = pedirAGemini(m);
      var d = JSON.parse(json);
      d.adjuntos = nombresAdjuntos(m);                 // lo pone el script, no Gemini: así no se inventa nombres
      json = JSON.stringify(d);
      // Se envía siempre: solo la Action sabe si el hilo tiene un ticket vivo que actualizar.
      // es_ticket decide allí si se abre uno nuevo cuando no lo hay.
      var codigo = enviarAGitHub(json, fila, cuando);
      resultado = (codigo == 204 ? 'enviado a GitHub' : 'error GitHub ' + codigo)
        + (d.es_ticket === false ? ' (Gemini: no es ticket, solo actualizaría un hilo vivo)' : '');
    } catch (e) {
      resultado = 'error: ' + String(e).slice(0, 160);
    }
    registro.getRange(fila, 5, 1, 3).setValues([[json, resultado, ULTIMO_MODELO]]);
    if (resultado.indexOf('error') !== 0) procesados.appendRow([m.getId(), marca()]);   // un error se reintenta en el siguiente ciclo
    if (resultado.indexOf('error') === 0) {
      ULTIMO_ERROR = cuando + ' ' + m.getSubject() + ': ' + resultado;
      registro.getRange(fila, 1, 1, 7).setBackground('#f4cccc');   // rojo claro: se ve de un vistazo entre muchas
    }
  });
  estado(mensajes.length);
  latido(mensajes.length);
  fotoDelDia();
}
var ULTIMO_ERROR = '';

// Pestaña "estado": una foto del ciclo, reescrita cada vez. Quien dude de si su correo
// entró mira aquí la última lectura y la próxima; el detalle por correo está en "correos".
function estado(leidosAhora) {
  var h = hoja('estado', ['qué', 'valor']);
  var ahora = new Date(), hoy = fechaDe(ahora);
  var filas = hoja('correos', []).getDataRange().getValues().slice(1);
  var deHoy = filas.filter(function (f) { return String(f[0]).indexOf(hoy) === 0; }).length;
  if (!ULTIMO_ERROR) ULTIMO_ERROR = PROPS.getProperty('ULTIMO_ERROR') || '';
  PROPS.setProperty('ULTIMO_ERROR', ULTIMO_ERROR);
  h.clearContents();
  h.appendRow(['qué', 'valor']);
  h.appendRow(['Última lectura del buzón', marca()]);
  h.appendRow(['Próxima lectura prevista', Utilities.formatDate(new Date(ahora.getTime() + 5 * 60000), ZONA, 'yyyy-MM-dd HH:mm') + ' (aproximada: Google la lanza cada 5 min)']);
  h.appendRow(['Correos leídos en este ciclo', leidosAhora]);
  h.appendRow(['Correos leídos hoy', deHoy]);
  h.appendRow(['Último error', ULTIMO_ERROR || 'ninguno']);
  h.appendRow(['Modelos', modelos().join(', ')]);
  h.appendRow(['Hora', 'America/Sao_Paulo']);
}

// Prueba sin consecuencias: resume los últimos n correos del grupo en la pestaña "pruebas".
// Por defecto 2: cada correo gasta una petición del modelo principal (20 al día en el plan gratuito).
function probar(n) {
  n = n || 2;
  var grupo = PROPS.getProperty('GRUPO');
  var h = hoja('pruebas', ['cuando', 'modelo', 'asunto', 'json']);
  var vistos = 0;
  GmailApp.search('(to:' + grupo + ' OR cc:' + grupo + ') newer_than:30d', 0, 30).some(function (hilo) {
    return hilo.getMessages().some(function (m) {
      if (!esParaElGrupo(m, grupo) || remitenteExcluido(m)) return false;
      var json; try { json = pedirAGemini(m, true); } catch (e) { json = 'error: ' + e; }   // solo el modelo principal: no gasta la cuota del resto
      h.appendRow([marca(), ULTIMO_MODELO || modelos()[0], m.getSubject(), json]);
      return ++vistos >= n;
    });
  });
}

// Foto del día: pide a GitHub (repository_dispatch "foto") que publique en Chat el resumen de
// tickets, en días laborables, a las 08:55 de Madrid, 08:55 de São Paulo y 10:55 de Ciudad de
// México, cada hora en su zona (el cambio de hora de España no afecta). El cron de GitHub se
// retrasaba hasta una hora o se perdía; este script corre cada 5 min y es puntual, así que la
// foto llega entre las :55 y las :00. Una vez por zona y día (propiedad FOTO_<zona>).
var FOTOS = [['Europe/Madrid', 8, 55], ['America/Sao_Paulo', 8, 55], ['America/Mexico_City', 10, 55]];
function fotoDelDia() {
  var ahora = new Date();
  FOTOS.forEach(function (f) {
    var zona = f[0], hoy = Utilities.formatDate(ahora, zona, 'yyyy-MM-dd');
    var dia = Number(Utilities.formatDate(ahora, zona, 'u'));
    var min = Number(Utilities.formatDate(ahora, zona, 'H')) * 60 + Number(Utilities.formatDate(ahora, zona, 'm'));
    var clave = 'FOTO_' + zona;
    if (dia > 5 || min < f[1] * 60 + f[2] || PROPS.getProperty(clave) === hoy) return;
    var r = UrlFetchApp.fetch('https://api.github.com/repos/' + REPO + '/dispatches', {
      method: 'post', contentType: 'application/json', muteHttpExceptions: true,
      headers: { Authorization: 'Bearer ' + PROPS.getProperty('GITHUB_TOKEN'), Accept: 'application/vnd.github+json' },
      payload: JSON.stringify({ event_type: 'foto', client_payload: { zona: zona } })
    });
    if (r.getResponseCode() == 204) PROPS.setProperty(clave, hoy);
  });
}

// Latido: una vez por día laborable, la primera ejecución después de las 08:00 de São Paulo.
function latido(leidosAhora) {
  var webhook = PROPS.getProperty('GCHAT_WEBHOOK');
  if (!webhook) return;
  var ahora = new Date();
  var hoy = fechaDe(ahora), hora = Number(Utilities.formatDate(ahora, ZONA, 'H'));
  var dia = Number(Utilities.formatDate(ahora, ZONA, 'u'));           // 1 = lunes ... 7 = domingo
  if (hora < 8 || dia > 5 || PROPS.getProperty('ULTIMO_LATIDO') === hoy) return;
  var ayer = fechaDe(new Date(ahora.getTime() - 86400000));
  var filas = hoja('correos', []).getDataRange().getValues().slice(1);
  var deAyer = filas.filter(function (f) { return String(f[0]).indexOf(ayer) === 0; });
  var tickets = deAyer.filter(function (f) { return String(f[5]).indexOf('enviado') === 0; }).length;
  var texto = 'Correo automático vivo. Ayer ' + ayer + ': ' + deAyer.length + ' correo(s) leído(s), ' + tickets + ' enviado(s) como ticket.';
  UrlFetchApp.fetch(webhook, { method: 'post', contentType: 'application/json', payload: JSON.stringify({ text: texto }), muteHttpExceptions: true });
  PROPS.setProperty('ULTIMO_LATIDO', hoy);
}

// ---------------------------------------------------------------- app de Chat (solo lectura)
function github(ruta) {
  // Contenido de un fichero o listado de una carpeta del vault en GitHub. null si no existe.
  var r = UrlFetchApp.fetch('https://api.github.com/repos/' + REPO + '/contents/' + ruta, {
    muteHttpExceptions: true,
    headers: { Authorization: 'Bearer ' + PROPS.getProperty('GITHUB_TOKEN'), Accept: 'application/vnd.github+json' }
  });
  if (r.getResponseCode() != 200) return null;
  var j = JSON.parse(r.getContentText());
  return Array.isArray(j) ? j : Utilities.newBlob(Utilities.base64Decode(j.content)).getDataAsString();
}

function campo(texto, clave) {
  // Valor de `clave:` en el frontmatter, sin comillas ni comentario.
  var m = texto.match(new RegExp('^' + clave + ':[ \\t]*([^\\n#]*)', 'm'));
  return m ? m[1].trim().replace(/^["']|["']$/g, '') : '';
}

function buscarTicket(id) {
  // Ruta del ticket NFQBAU-NNNN en Abiertos o Archivo, o null.
  var carpetas = ['02_TICKETS/Abiertos', '02_TICKETS/Archivo'];
  for (var i = 0; i < carpetas.length; i++) {
    var lista = github(carpetas[i]) || [];
    for (var j = 0; j < lista.length; j++) if (lista[j].name.indexOf(id + ' ') === 0) return lista[j].path;
  }
  return null;
}

function resumenTicket(id) {
  var ruta = buscarTicket(id);
  if (!ruta) return 'No encuentro el ' + id + '.';
  var t = github(ruta);
  var hist = t.split('## Histórico de interacciones')[1] || '';
  var lineas = hist.split('\n').filter(function (l) { return l.indexOf('- ') === 0; });
  var ultima = lineas.length ? lineas[lineas.length - 1].slice(0, 300) : '(sin histórico)';
  return '*' + ruta.split('/').pop().replace(/\.md$/, '') + '*\n'
    + 'Estado: ' + campo(t, 'estado') + ' · Prioridad: ' + campo(t, 'prioridad') + ' · Responsable: ' + (campo(t, 'responsable') || 'sin responsable') + '\n'
    + 'Entorno: ' + (campo(t, 'entorno') || '-') + ' · Límite: ' + (campo(t, 'fecha_limite') || '-') + '\n'
    + 'Última interacción: ' + ultima;
}

function fotoAhora() {
  // Misma foto que la Action, calculada aquí desde los tickets abiertos.
  var lista = github('02_TICKETS/Abiertos') || [];
  var porResp = {}, porEstado = {}, abiertos = 0;
  lista.forEach(function (f) {
    if (f.name.indexOf('NFQBAU-') !== 0) return;
    var t = github(f.path);
    var e = campo(t, 'estado');
    if (e === 'Resuelto') return;
    abiertos++;
    var r = campo(t, 'responsable') || 'sin responsable';
    porResp[r] = (porResp[r] || 0) + 1; porEstado[e] = (porEstado[e] || 0) + 1;
  });
  var fmt = function (o) { return Object.keys(o).sort(function (a, b) { return o[b] - o[a]; }).map(function (k) { return k + ' ' + o[k]; }).join(', '); };
  return '*Foto ahora mismo*\nAbiertos: ' + abiertos + '. ' + fmt(porResp) + '.\nPor estado: ' + fmt(porEstado) + '.\n' + guardiaAhora();
}

function guardiaAhora() {
  var t = github('05_GENERAL/Guardia-de-tickets.md') || '';
  var quien = campo(t, 'responsable'), desde = campo(t, 'actualizado');
  if (!quien || quien === 'nadie') return 'Sin responsable de guardia para los tickets nuevos.';
  var horas = desde ? (new Date() - new Date(desde.replace(' ', 'T') + ':00-03:00')) / 3600000 : 99;
  return horas > 12 ? 'Sin responsable de guardia (la marca de ' + quien + ' caducó).' : 'De guardia: ' + quien + ' (desde ' + desde + ').';
}

// Punto de entrada de la app de Chat: Google llama aquí con cada mensaje dirigido a la app.
function onMessage(evento) {
  var texto = (evento.message && evento.message.argumentText || evento.message && evento.message.text || '').trim();
  var id = (texto.match(/NFQBAU-\d+/i) || [''])[0].toUpperCase();
  var r;
  try {
    if (id) r = resumenTicket(id);
    else if (/^foto/i.test(texto)) r = fotoAhora();
    else if (/^guardia/i.test(texto)) r = guardiaAhora();
    else r = 'Puedo con: un id (NFQBAU-1545), "foto", "guardia" o "ayuda".';
  } catch (e) { r = 'Error leyendo el vault: ' + String(e).slice(0, 120); }
  return { text: r };
}
function onAddedToSpace() { return { text: 'Hola. Escríbeme un id de ticket, "foto" o "guardia".' }; }
function onRemovedFromSpace() {}
