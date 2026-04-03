---
name: ma-meters
description: "Manage meter generation and inquiry in the Machine Accounting system via SQL Server. Use when: inserting meters (hourly, audit, final, on-demand, initial, soft/hard drop), querying meter readings, generating MGA paytable-level meters, inserting events, querying events, fixing meter increments, updating meter values, investigating meter variances, or working with the MGA meter pipeline."
argument-hint: "Action: insert-meter, query-meters, insert-mga-meter, query-events, insert-event, meter-on-demand, fix-increment, update-meter"
---

# MA Meters Skill

Generate and query meters and events through SQL Server stored procedures. This skill handles meter insertion (all types), MGA paytable-level meter generation, event insertion, and meter/event queries.

## Scope

**In scope:** 
Insert cabinet-level meters via `Proc_TranslatorMeterInsertEx`, 
insert MGA paytable meters via `Proc_TranslatorMGAMeterInsert`, 
insert events via `Proc_TranslatorEventInsert`, 
query meter reads, query events, fix meter increments, update meter values, meter-on-demand workflow.

**Out of scope:** Machine CRUD (use ma-machine-management), period lifecycle (use ma-period-management), drop zone/schedule configuration. If the user needs these, direct them to the appropriate skill.

---

## References

Detailed reference material for each domain:

- [Meters reference](./references/meters.md) — meter type codes, stored procedures, cabinet-level rules, querying and updating meters, meter-on-demand workflow.
- [Events reference](./references/events.md) — event insertion procedures, event code definitions, querying events.
- [MGA Meters reference](./references/mga-meters.md) — MGA meter generation, paytable queries, the MGAMeter job pipeline, meter mismatch variance.

## User Guide Chapters

Read only the chapters relevant to the current task:

| # | Chapter | When to read |
|---|---------|-------------|
| 16 | [Machine Meter Variances](../machine-accounting/user-guide/16_Chapter_16_Machine_Meter_Variances.md) | Investigating and correcting meter variances: runaway meters, rollover, over-tolerance, RAM clears, misapplied voucher meters, meter adjustments, coin-in editing, tolerance management, and paytable reconciliation. |
| 17 | [Manual Meters](../machine-accounting/user-guide/17_Chapter_17_Manual_Meters.md) | Entering and adjusting manual meter entries for non-communicating machines that require manual meter reads. |
| 28 | [Audit Workbook](../machine-accounting/user-guide/28_Chapter_28_Audit_Workbook.md) | EGM meter auditing: viewing electronic/physical meters, creating audit groups, reading floor meters with drop scanners, adjusting machine meters, and requesting immediate meter readings. |

---

## Domain Rules

### Meter Insertion Rules

1. Each meter must have a **unique UniqueID** — take the latest UniqueID for the day and increment it.
2. **Total Bills In** = sum of Soft1 through Soft7.
3. **Total Drop** = Total Bills In + EFT In + Voucher In + WAT In.
4. The date/time must be from the **current day** (while audit is open).
5. Audit must not be closed when inserting meters.
6. For Meter On Demand (type `X`), the date must match exactly with the `MeterOnDemandRequest` record.

### Event Insertion Rules

1. There **cannot be more than one event for the same machine at the same time**.
2. Events first land in `EventTrans`, then a job moves them to the `Event` table.

### MGA Meter Rules

1. MGA meters must be inserted for **each active paytable** on a machine.
2. A corresponding cabinet-level meter must also be inserted via `Proc_TranslatorMeterInsertEx`.
3. MGA meters land in `MGAMeterTransaction`, then the `Accounting MGAMeter Move` job moves them to `MGAMeter`.
4. If cabinet-level meters don't match the sum of MGA paytable-level meters, a **Meter Mismatch** variance (ReasonNum = -1) is raised.

---

## Procedures

### 1. Insert a Cabinet-Level Meter

1. Determine the meter type (see [meters reference](./references/meters.md) for codes).
2. Query for the latest UniqueID for the day:
   ```sql
   SELECT MAX(UniqueID) FROM MeterRead WHERE CONVERT(DATE, MeterDate) = '<date>'
   ```
3. Execute `Proc_TranslatorMeterInsertEx` with the appropriate parameters.
4. Verify by querying the `MeterRead` and `MeterReadDetail` tables.

### 2. Query Meters for a Machine

1. Run the meter query from the [meters reference](./references/meters.md).
2. Filter by machine number and date.
3. Join `MeterNames` for human-readable meter names.

### 3. Insert MGA Paytable Meters

1. Query active paytables for the machine:
   ```sql
   SELECT * FROM Machine_MGAPaytable WHERE MachineNum = <MNum> AND To_DateTime IS NULL
   ```
2. For each paytable, execute `Proc_TranslatorMGAMeterInsert`.
3. Insert the corresponding cabinet-level meter via `Proc_TranslatorMeterInsertEx`.
4. Trigger or wait for the `Accounting MGAMeter Move` job.
5. Verify in `MGAMeterDay`.

### 4. Insert an Event

1. Execute `Proc_TranslatorEventInsert` with the machine number, date, and event parameters.
2. Verify the event landed in `EventTrans`.
3. Wait for the job to move it to the `Event` table.

### 5. Meter On Demand

1. Create a request in MA (Audit → Meter On Demand → New).
2. Query `MeterOnDemandRequest` for the request date.
3. Execute `Proc_TranslatorMeterInsertEx` with type `'X'` — **dates must match exactly**.
4. Verify the result in the `MeterOnDemand` table.

### 6. Fix Meter Increment

1. Execute `Proc_TranslatorMeterIncrementUpdate` with the machine number and denomination value.
2. This sets `mtrIncrement` and recalculates `mtrMoney`.
