# Chapter 15 Opening the Audit Day

When opening a gaming day for audit, Machine Accounting collects the following information from the casino floor:

| Task | Description |
|------|-------------|
| Start Period | Starts the period within the system |
| Initialize Hand Pay Entries | Automatically gathers handpay information |
| Get Period Meters | Automatically gathers meter readings |
| Get Opening Meters | Initializes drop meters and creates period tables — checks the previous closed period, obtains ending meters, and creates a period structure in the database |

## 15.1 User Tasks List

The User Tasks list displays all audit tasks and their status (required, completed, or in process). Key behaviors:

- A period must be opened before any tasks display.
- All mandatory tasks must be completed before closing a day.
- Tasks can be configured per auditor based on their duties.
- Changing displayed user tasks may hide mandatory tasks.

### Major User Tasks

| Task | Description |
|------|-------------|
| Verify Machine Changes | Verify all machine retirements, additions, moves, and conversions. Retire machines only after soft and hard drops are complete. |
| Correct Meter Variances | Correct machine meter variances for the period |
| Hand Pays | Review hand pays: Add Manual Hand Pays, Balance With Cage, Correct Jackpot/Progressive/Cancel Credit/Bonus Jackpot Variances |
| Enter Manual Meters | Manually enter machine meters for machines not communicating with the system |
| Hard Drop / Soft Drop | Obtain drop data, verify accuracy, correct errors and variances |
| NCEP Drop | Import and audit non-cashable electronic promotion data |
| CEP Drop | Import and audit cashable electronic promotion data |
| Voucher Drop - IVS | Import voucher data, audit variances, balance ticket batches |
| Coupon Promotion | Import coupon data, audit variances |
| Progressive Workbook | Review active progressives and meter-based movement |
| EZ Pay Cashless Drop | Import and audit WAT (Wager Account Transfer) data |
| Close Period | Close the accounting period after all tasks are complete |

### Period Timeline

The Period Timeline provides a visual representation of task completion progress:

- Tasks are displayed linearly with sub-tasks
- Status colors: Black (not started), Orange (started), Yellow (about to finish), Green (finished)
- Completed sub-tasks display a check mark

## 15.2 Variance Comments

When accepting a meter, jackpot, voucher, CEP, soft drop, or hard drop variance, a comment can be added to explain the reason for acceptance.

### Managing Comments

- Comments can be selected from a predefined list or entered as free text.
- New comments can be marked as "Active" to add them to the predefined list for future use.
- Comments can be moved between Active and Inactive status.
- Comments can be permanently deleted from the list.

> Adding a comment when accepting variances is recommended throughout Machine Accounting.
