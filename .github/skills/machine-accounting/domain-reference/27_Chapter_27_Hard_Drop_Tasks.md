# Chapter 27 Hard Drop Tasks

The Hard Drop tasks complete the hard drop (coin drop) portion of the EGM audit. This involves retrieving hard drop data, resolving errors, and correcting variances. The process is structurally parallel to the Soft Drop tasks.

## 27.1 Actual Hard Drop

The hard drop data can be obtained from three sources:

- **From Disk** — Imports data from file (used as a fallback for network failure)
- **Enter Drop Manually** — Manual entry of hard drop details
- **No Drop Today** — Marks the hard drop task as complete without data entry (used when no hard drop occurred)

After retrieval, the hard drop results are displayed for review. Data can be filtered to show All Dropped machines or only Exceptions.

## 27.2 Hard Drop Manual Entry

Manual entry of hard drop details requires specifying the machine number and entering the coin drop amount.

## 27.3 Correcting Hard Drop Errors

Hard drop errors typically involve orphan buckets (drop buckets not matched to a machine) and orphan machines (machines not matched to a drop bucket).

To correct errors:

1. Review orphan buckets and orphan machines.
2. Assign orphan buckets to the correct orphan machines.
3. If a drop was incorrectly assigned, unassign it and reassign to the correct machine.
4. Complete the error correction when all buckets are matched.

## 27.4 Correcting Hard Drop Variances

### Accepting Variances

Variances within established guidelines can be accepted. Multiple machines can be selected for bulk acceptance. Acceptance requires confirmation.

### Swapping Variances

If drops were posted to the wrong machines, the actual drop amounts can be swapped between two machines.

> A warning is provided if the machines have different denominations.

### Unaccepting Variances

A previously accepted variance can be unaccepted for further investigation.

### Adjusting Hard Drop Actuals

For each machine, the actual hard drop amount can be adjusted:

- **Coin Drop Amount** — Corrected actual coin drop amount

### Adjusting Hard Drop Meters

Hard drop meters can be adjusted, though this is not recommended. The system automatically recalculates meters at day close.

## 27.5 Key Data Fields

| Field | Description |
|-------|-------------|
| Machine Number | Machine identifier |
| Coin Drop Amount | Actual coin drop value |
| Metered Amount | System-metered coin drop value |
| Variance Amount | Difference between actual and metered |
