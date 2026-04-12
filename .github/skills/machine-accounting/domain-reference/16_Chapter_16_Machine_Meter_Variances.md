# Chapter 16 Machine Meter Variances

The Machine Meter Variances function displays machines with deltas that exceed defined tolerances or that have negative meter values. A tolerance is the average daily maximum for a meter on a machine type for a gaming day. Numbers above or below the tolerance generate a variance.

All variances must be investigated and corrected, or accepted. Variances over the defined machine tolerances may be correct due to unusual play at the machine.

## Causes of Machine Variances

- **Runaway meters** — A problem with the machine meters
- **Rollover meters** — A meter reaches the highest number of digits and resets to zero
- **Over tolerance** — Meter delta exceeds the tolerance level set in the system
- **RAM clear** — A procedure performed by a slot technician resets the meters
- **Misapplied voucher meters** — A voucher machine is configured incorrectly
- **Cabinet-to-paytable coin in variance** — Difference between game total coin in and cabinet-to-paytable coin in (commonly called "redline")

## Variance Categories

| Category | Description |
|----------|-------------|
| Over Tolerance | Numbers over or under the average daily maximum meter amount for the gaming day on a machine type |
| Negative | A meter rolls over on a machine, causing a negative variance (unless also in RAM Clear or AI Download category) |
| RAM Clear | Calculated when at least 50% of meters for a non-SAS machine went negative |
| AI Download | Calculated when at least 50% of meters for an SAS machine went negative |

## 16.1 Viewing Meter Variances

Meter variances must be either accepted or edited before the period audit closes.

Machines can be filtered to show:

- **Exceptions only** — Machines with meter exceptions
- **Show All** — All machines including those with exceptions
- **Meter Filter** — All meters or only meters with variances

Machines are grouped by variance reason by default. Grouping can be changed by column.

## 16.2 Adjusting Meter Variances

All variances should be researched and correctly adjusted rather than simply accepting or entering suggested system entries.

For each machine with a variance, the following meter information is available:

| Column | Description |
|--------|-------------|
| Meter | Name of the meter |
| Prior Meter | Previous period's meter value |
| Today's Meter | Current meter reading |
| Today's Value | Current dollar/count value |
| Tolerance | Tolerance threshold |
| Variance | Difference from expected value |
| Suggested | System-suggested value (if available, shown in blue) |

### Adjustment Methods

- **Direct edit** — Enter a new value in the Today's Value column
- **Accept Suggested** — If the Suggested column value is blue, it can be used to auto-populate Today's Value. This should only be done after verifying following standard auditing processes.
- **Meter Adjustment** — Enter the adjustment amount in the Adjustment field. The meter value is updated by the adjustment amount.
- **Calculate Meters** — Let the system calculate corrections automatically

> To make relative changes without overwriting the existing value: enter + or - in front of the amount. For example, entering `50` sets the value to 50, whereas entering `+50` adds 50 to the current value.

### Accept / Unaccept

After investigating a variance, it can be accepted (acknowledged as reviewed) or unaccepted if further investigation is needed.

### Export

Machine meter data can be exported to Excel for delta calculations and analysis.
