# Accounting Periods

## Rules

1. A period can be opened for a specific day, marking it as an **Open Accounting Period**.
2. A period can only be opened for a day that was not previously opened or closed.
   - Multiple periods can be open simultaneously.
   - You can switch between opened periods.
   - It is impossible to open a period for a future date.
3. If a period is already open, a new period can only be opened for the day **after** the last opened period (or later).
4. An opened period can be **started over** — the day reverts to a regular (non-period) day.
5. An opened period can be **closed**.
   - If multiple periods are open, only the **oldest** open period can be closed.
6. A closed period marks the day as a **Closed Accounting Period**.
7. A closed period can be **reopened**, reverting to Open Accounting Period status.
   - Only the **last** closed period can be reopened.
8. Days between two closed periods that had no period operations cannot be chosen or opened.
9. **Period cannot be closed if there are unresolved variances** for any machine on that day.
10. **Period cannot be closed if a mandatory User Task is not marked as done.**

## Common Errors

When opening a period fails due to missing ending meters, run the repair procedure:

```sql
EXEC Util_NoEndingMeterFix '2026-03-01'
```

When a machine lacks `mtrIncrement` and `mtrMoney` values from the floor system, fix with:

```sql
EXEC Proc_TranslatorMeterIncrementUpdate <MachineNum>, <DenomValue>
-- Example: EXEC Proc_TranslatorMeterIncrementUpdate 10278, 1
-- where 1 = 1 cent for denomination 0.01
```

## Database

- Period-related records and variance data are stored in `dbo.Period`.
- Transaction log: `SELECT * FROM TransactionLog ORDER BY Date DESC`
- Process descriptions: `SELECT * FROM ProgressDescription`
- Error log: `SELECT * FROM DatabaseErrorLog`
