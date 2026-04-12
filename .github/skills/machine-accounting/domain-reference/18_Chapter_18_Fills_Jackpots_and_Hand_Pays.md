# Chapter 18 Fills, Jackpots, and Hand Pays

All hand pays (including fills, jackpots, progressives, cancel credits, and bonus jackpots) must be verified between the system and the cage. Any variance must be investigated and corrected, or accepted.

Each booth is audited and balanced with the cage documents for the total number of tickets and total amount. The process is complete after all booths are balanced for fills and jackpots with the cage.

## 18.1 Viewing Fills and Jackpots

The Fills/Hand Pays data displays fill and jackpot slips created at various FJP stations. In addition, slips can be entered manually or voided.

Data can be filtered by:

- **Booth** — Specific fill and jackpot station, or all stations
- **Type** — Fills or Hand Pays

To verify all booths at once (if all balance):

1. Accept the total count.
2. Accept the total amount.

## 18.2 Adding Manual Hand Pays

Manual hand pays may be needed due to machine malfunction, bonus jackpot, progressive jackpot, short pay, or other reasons.

The following information is required:

| Field | Description |
|-------|-------------|
| Slip Number | Number of the slip being added |
| Date | Date of the hand pay |
| Machine Number | The machine's number |
| Type | Transaction type: Aux Fill, Bonus Jackpot, Cancel Credit, Fill, Jackpot, Progressive, SAS 6 Bonus, SBX Bonus, or Short Pay |
| Amount ($) | Amount of the slip |
| Coins Registered | Number of coins (for jackpot tickets) |
| Symbol | Winning reel strip or combination (for jackpot tickets) |
| Machine Paid | Jackpot amount paid to the hopper |
| Progressive Level | Jackpot level |
| Comment Number | Comment code and reason (pre-defined in Maintenance Console) |
| Employee | Employee completing the transaction |
| Witness | Employee witnessing the transaction |
| Override | Employee authorized to override the transaction |
| Booth Number | Booth number of the transaction |

W2G tax form entry may be required for qualifying jackpots (see Tax-Form Entry below).

> The W2-G feature is not supported if the Win Tax feature is enabled.

## 18.3 Editing Slip Numbers

Slip numbers can be modified for existing hand pay records.

## 18.4 Voiding Slips

Slips created at an FJP station cannot be edited directly. The original slip must be voided, then a new slip entered with the correct information.

To void a slip:

1. Select the slip.
2. Mark it as void.
3. Select a reason for the void from the predefined list.

## 18.5 Aux Fills

The Aux Fills data displays all auxiliary fills generated when a machine produces a hopper-empty event. Manual aux fills can be added and existing aux fill slips can be voided.

> Slips created at a Fill and Jackpot station can only be voided, not edited. Void the slip and enter a new one with correct information.

### Adding Manual Aux Fills

The same fields as manual hand pays are required, with the booth number corresponding to the aux fill station.

### Voiding Aux Fill Slips

Aux fill slips can be voided with a reason selected from the predefined list.

## 18.6 Jackpot Variances

The JPC Variance data displays actual and metered jackpot amounts for the following variance types:

- **Jackpot** variances
- **Progressive** variances
- **Cancel Credit** variances
- **Bonus Jackpot** variances

Multiple variance types can be viewed simultaneously.

### Filtering Variances

- **Show All Variances** — Display all machines
- **Show Exceptions** — Display only machines with variances

### Accepting Variances

Variances within established guidelines can be accepted. Multiple machines can be selected and accepted at once.

Variances can also be unaccepted if further investigation is required.

### Adjusting Meter Values

Metered values can be adjusted for individual machines. Enter the new value in the Adjustment field.

> To make relative changes: enter + or - in front of the amount.

## 18.7 Tax-Form Entry (W2G)

When a jackpot meets the taxable threshold, W2G tax form information must be recorded. The following patron information is captured:

- Name, Address, Social Security Number
- Date of Birth, Identification documents
- Jackpot type and amount
- Tax withholdings (federal, state, city/local)

## 18.8 Operator Payouts

The Operator Payout tab displays payout information for machines, including operator-paid jackpots and adjustments.
