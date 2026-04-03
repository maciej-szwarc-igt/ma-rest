# MGA Paytable-Level Meters

## Overview

MGA (Multi-Game Accounting) tracks meters at the paytable level for machines with multiple active game themes.

## Key Tables

- `MGAPaytable` — paytable definitions
- `Machine_MGAPaytable` — paytables assigned per machine
- `MGAMeterTransaction` — raw meter inserts (staging)
- `MGAMeter` — final meter data (moved by the `Accounting MGAMeter Move` job)
- `MGAMeterDay` — daily aggregated values displayed in the paytables window
- `MGAPeriod` — period records created when audit starts; adjustments modify values here

## Querying Paytables

```sql
-- Paytables for a machine
SELECT * FROM Machine_MGAPaytable WHERE MachineNum = <MNum>

-- Machines with more than one active paytable
SELECT COUNT(*), MachineNum
FROM Machine_MGAPaytable
WHERE To_DateTime IS NULL
GROUP BY MachineNum
HAVING COUNT(*) > 1
```

## Inserting MGA Meters

Generate meters for each paytable and machine:

```sql
EXEC Proc_TranslatorMGAMeterInsert
  '<Date>',           -- e.g. '2025-03-21'
  <MachineNum>,       -- e.g. 10209
  '<MeterType>',      -- e.g. 'M'
  <PaytableCode>,     -- e.g. AVV033
  '<AssetId>',        -- e.g. 'A2'
  <param6..paramN>    -- meter values
```

Then insert the corresponding cabinet-level meter:

```sql
EXEC Proc_TranslatorMeterInsertEx
  'M', '<DateTime>', <UniqueID>, <MachineNum>, <values...>
```

## Processing Pipeline

1. MGA meters first land in `MGAMeterTransaction`.
2. The `Accounting MGAMeter Move` SQL job moves them to `MGAMeter`.
3. This job can be triggered manually.
4. Values appear in `MGAMeterDay` for display in the UI.
5. When audit starts, a record is created in `MGAPeriod`.
6. Adjustments during audit modify `MGAPeriod` values.

## Meter Mismatch Variance

If cabinet-level meters don't match the sum of MGA paytable-level meters, a **Meter Mismatch** variance (ReasonNum = -1) is raised. This applies only to MGA-enabled machines.
