---
titulo: "I06 — Catálogo de interfaces obligatorias"
familia: I
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/I
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "interfaces, catálogo, prefijos obligatorios, MEGA, lista oficial, 130"
---

# I06 — Catálogo de interfaces obligatorias

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** interfaces, catálogo, prefijos obligatorios, MEGA, lista oficial, 130

## En una línea

La lista de ~130 prefijos que el sistema considera el conjunto oficial, codificada dentro de un
script de shell.

## Dónde está

En el código de `LLamada Rundeck Flags Obligatorios`, como un array de Bash:

```bash
PREFIJOS=(
    "MEGAACCOUNTING_EndOfDay" "MEGAACCOUNTING_EndOfMonth" "MEGAACCOUNTING_EndOfWeek"
    "MEGAACCOUNTING_IntraDay" "MEGACUSTODY_IntraDay" "AccountCategory" "AccountNature"
    ...
)
```

```bash
grep -A45 "PREFIJOS=(" "/nfq/data/cfg/LLamada Rundeck Flags Obligatorios.sh"
```

**No está en base de datos.** Es la única definición de «el conjunto completo» que existe como
lista fija. Ver [R4_01_que_es_un_set_completo](../R4%20-%20Sets%20incompletos/R4_01_que_es_un_set_completo.md).

## Qué contiene

**5 prefijos de flag:** `MEGAACCOUNTING_EndOfDay`, `_EndOfMonth`, `_EndOfWeek`, `_IntraDay`,
`MEGACUSTODY_IntraDay`.

**~125 nombres de interfaz**, de `AccountCategory` a `YieldCurve`. Agrupados por dominio:

| Dominio | Ejemplos |
|---|---|
| Catálogos fiscales y de clasificación | `TaxPayerCategory`, `ClassificationFATCA`, `FiscalClassification`, `FiscalNature`, `CVMLongClassification`, `CVMShortClassification`, `NationalClassification` |
| Entidades | `Issuer`, `Guarantor`, `Custodian`, `CSD`, `Broker`, `Counterparties`, `FundAdministrator`, `FundAuditor`, `FundManager`, `AssetManager`, `AssetController`, `RiskAgent`, `FiduciaryAgent`, `AutonomousAgent`, `Consultant`, `Regulators` |
| Activos | `Equity`, `Bonds`, `Unit`, `Right`, `Future`, `Forward`, `Commodity`, `Fund`, `STI`, `CashAsset`, `OptionConfiguration`, `SwapAssetTypeOption` |
| Cuentas y clientes | `ClientCashAccount`, `ClientSecAccount`, `ContractualClient`, `NostroSecAccount`, `ExternalCashAccount`, `ClientCashAccbySecAcc` |
| Posiciones y eventos | `CGCPosition`, `EligiblePosition`, `ValorizedPosition`, `DepoValorizedPosition`, `CA`, `CAConfiguration`, `ClientEntitlement` |
| Efectivo | `CashMovement`, `CashTransferOrder`, `CashTransactionType`, `CashAccountingEntry`, `ClientBalance`, `DetailedCashFlow` |
| Valoración y rentabilidad | `NetAssetValue`, `NavDetails`, `Rentability`, `RentabilityFA`, `NAVRentabilityDetails`, `IndexRentabilityDetails`, `performance`, `BenchmarkPerformance`, `SecurityPrice`, `ValuationPriceSLA` |
| Comisiones | `FixRateFeeRule`, `FixAmountFeeRule`, `ScaledFeeRule`, `ManagementFeesSLA`, `FeesType`, `FeesDetails`, `BrokerCommissionSLA`, `MarketTradeCommSLA` |
| Calendarios y referencias | `CountryCalendar`, `CSDCalendar`, `MutualFundCalendar`, `MainEntityCalendar`, `ReferenceRate`, `ReferenceRatePrice`, `ForeignExchangeRate`, `Currency`, `Country`, `Market` |
| Bloqueos y préstamos | `PledgeAndBlock`, `DepledgeAndUnblockRequest`, `PledgingReason`, `SecuritiesLendingRegister`, `ShortSellingSLA` |

## Cómo se usa

El script compara los ficheros presentes en el directorio contra esta lista y decide:

| Resultado | Acción |
|---|---|
| Están **todos** | El lote anterior no se consumió: no pide ficheros nuevos |
| Faltan **algunos** | «ERROR CRÍTICO: Carga incompleta», aborta |
| No hay **ninguno** | Pide un lote nuevo a la API de Megara |

Ver [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md).

## Y el otro catálogo, el de conversión

`lookup_java.txt` y `lookup_java_flag.txt` tienen **148 entradas cada uno**, una por interfaz, con
su XSD. Son el catálogo de lo que el conversor sabe procesar.

```bash
wc -l /nfq/data/cfg/lookup_java_flag.txt      # 148
cut -d'|' -f7 /nfq/data/cfg/lookup_java_flag.txt | sort   # los nombres de fichero
```

**148 en conversión frente a ~125 interfaces en la lista de obligatorias**: no son el mismo
conjunto. Hay interfaces convertibles que no son obligatorias.

## Los tres catálogos que conviven

| Catálogo | Dónde | Cuántos | Para qué |
|---|---|---|---|
| Prefijos obligatorios | Script de shell | ~130 | Decidir si el lote está consumido |
| Conversión | `lookup_java*.txt` | 148 | Qué XML se sabe convertir |
| Cargas | `lookup_stg.txt` | 573 líneas | Qué fichero va a qué tabla |

Que un nombre esté en uno no implica que esté en los otros. Ante «esta interfaz no se procesa»,
comprueba en cuál de los tres falta.

## Ver también

[R4_01_que_es_un_set_completo](../R4%20-%20Sets%20incompletos/R4_01_que_es_un_set_completo.md) · [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md) · [C03_lookup_java_formato](../C%20-%20Conversion%20Java/C03_lookup_java_formato.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md)
