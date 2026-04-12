# Chapter 24 Soft Drop Tasks

The Soft Drop tasks complete the soft drop (bill drop) portion of the EGM audit. This involves retrieving soft drop data, resolving errors, and correcting variances.

## 24.1 Actual Soft Drop

The soft drop data can be obtained from three sources:

- **From Disk** — Imports data from file (used as a fallback for network failure)
- **Enter Drop Manually** — Manual entry of soft drop details
- **No Drop Today** — Marks the soft drop task as complete without data entry (used when no soft drop occurred)

After retrieval, the soft drop results are displayed for review. Data can be filtered to show All Dropped machines or only Exceptions.

## 24.2 Soft Drop Manual Entry

Manual entry of soft drop details requires specifying the machine number and entering the drop amount.

## 24.3 Correcting Soft Drop Errors

Soft drop errors typically involve orphan cans (drop cans not matched to a machine) and orphan machines (machines not matched to a drop can).

To correct errors:

1. Review orphan cans and orphan machines.
2. Assign orphan cans to the correct orphan machines.
3. If a drop was incorrectly assigned, unassign it and reassign to the correct machine.
4. Complete the error correction when all cans are matched.

## 24.4 Correcting Soft Drop Variances

### Accepting Variances

Variances within established guidelines can be accepted. Multiple machines can be selected for bulk acceptance. Acceptance requires confirmation.

### Swapping Variances

If drops were posted to the wrong machines, the actual drop amounts can be swapped between two machines.

> A warning is provided if the machines have different denominations, as swapping may not be appropriate.

### Unaccepting Variances

A previously accepted variance can be unaccepted for further investigation.

### Adjusting Soft Drop Actuals

For each machine, the actual soft drop amount can be adjusted:

- **ActualSoft1** — Corrected actual soft drop amount

### Adjusting Soft Drop Meters

Soft drop meters can be adjusted, though this is not recommended. The system automatically recalculates meters at day close.

## 24.5 Assign Zero Drops

For machines that were not dropped, zero drop values can be assigned to indicate that the machine was intentionally skipped.
