---
responsable: Matheus Fransoni
tags:
  - guardia
  - bau
actualizado: 2026-11-07 11:58
actualizado_por: Matheus Fransoni
---

# Responsable de guardia

Quien atiende los tickets nuevos que llegan por correo. El correo automático asigna cada ticket nuevo a esta persona y, cuando llega una respuesta a un ticket de otro, le avisa en Google Chat para que lo tenga a la vista.

> [!abstract] Guardia
> Responsable de los tickets nuevos: `INPUT[inlineSelect(option('nadie'),option('Antonio Montoro'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`

- Al asumir la guardia, elige tu nombre. Al dejarla, elige `nadie`.
- El dato caduca a las 12 horas de la última marca, para que los tickets nuevos no se asignen a quien ya no los atiende. Si la guardia dura más, vuelve a elegir tu nombre.
- Sin responsable de guardia, los tickets nuevos nacen sin responsable y Chat lo avisa, como siempre.
- La marca de fecha y hora la pone el hook en el siguiente commit; no hay que escribir nada más.
