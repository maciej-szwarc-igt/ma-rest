# Chapter 4 Configuration Options

Machine Accounting configuration is divided into four areas: Configuration, Barcode Options, FJP Options, and User Options.

> Users must have appropriate permissions to access Configuration Options.

## 4.1 General Configuration

### Period

- **End of Period** — The hour when the accounting day ends (24-hour clock, e.g., 14 = 2:00 PM).
- **End of Hand Pay Period** — The hour when the casino cage day ends (24-hour clock).

### Variance Thresholds

Acceptable variance percentages/amounts between actual and metered values:

- **Soft Drop (%)** — Soft drop variance threshold
- **Hard Drop (%)** — Hard drop variance threshold
- **Voucher Drop (%)** — Voucher drop variance threshold
- **Coupon Drop (%)** — Coupon drop variance threshold
- **CEP Drop (%)** — CEP drop variance threshold
- **Jackpot ($)** — Jackpot variance threshold (dollar amount)
- **Tax Out ($)** — Tax out variance threshold (dollar amount)

> Any difference between metered and actual amounts greater than the variance percentage appears as a variance. Variances must be reconciled during the accounting process.

### Intervals, Periods, and Tolerances

A tolerance is the average daily maximum for a meter on a machine type for a gaming day. Numbers above or below the tolerance generate a variance.

- **Abandon Card (Minutes)** — Time-out interval in minutes for a player card with no activity
- **Clear Events (Days)** — Number of days (max 90) to retain events
- **Clear Meters (Days)** — Number of days (max 90) to retain meters
- **Meter Interval (Minutes)** — Frequency (in minutes) of meter readings
- **Meter Tolerance** — Default meter tolerance level; MA generates an exception report if exceeded
- **Denom Tolerance Enable** — Enables denomination-level tolerance settings in the Maintenance Console
- **Uncarded Session Timeout (Seconds)** — Seconds an EGM can be idle before a session ends

### Voucher/WAT

- **Voucher Machine System** — Ticketing system in use: None, IVS (requires EZ Pay), or Other
- **WAT System** — Wager Account Transfer system: None or EZ Pay
- **WAT Import Drop-to-Drop** — When enabled, imports WAT values on a drop-to-drop basis; when disabled, uses end-of-day to end-of-day basis

### Options

- **Carded Drop** — Indicates that the casino uses carded hard/soft drop (employee inserts a card into the machine during a drop)
- **Progressive Contribution Enabled** — Activates the Progressive Contribution % field on machines, allowing entry of an EGM's progressive contribution. This eliminates progressive contribution variances so auditors can investigate only true variances.
- **Manual Slip Number Edit** — Enables editing slip numbers for manually generated handpays
- **Group Based Promotion & Demotion** — Enables group-based promotions and demotions
- **Sync Week With Month** — Indicates that month end also ends the current week
- **Coupon Promo Enabled** — Enables coupon promotions
- **CEP Enabled** — Enables cashable electronic promotions
- **XC Reporting Matrix Enabled** — Activates effects on the Gaming XC Win report and enables XCPlayPercent on Machine Type Setup. Normalizes hold percentages for properties using Xtra Credit (XC).
- **Attendant Card Track** — The magnetic card track number used by all field attendants
- **PAI Configuration** — Permanent Asset ID settings:
  - Enable Permanent Asset ID
  - Assign PAI Manually (regulators provide specific PAIs)
  - System Assigned PAI (casino assigns; requires a starting value)

### Custom Meter Names

Defines new and abbreviated meter names to appear throughout the system. Both the full name and short name can be customized for any meter.

### Drop Times Setup

Configures drop times for hard and soft drops. Each drop time requires:

- **Start Time** and **End Time**
- **Drop Type** (hard or soft)
- **Description**

> The drop time must start at least one minute prior to the end of day. If it starts at or after the end of day, funds will be applied to the incorrect gaming day.

### Progressive Hit Event

Configures event codes that signify a progressive hit event for the progressive workbook (revenue auditing). Available event codes include:

| Event Code | Type | Description |
|-----------|------|-------------|
| 10004500 | BE2 | Hopper Paid Progressive |
| 10409600 | Machine | Progressive Hit |
| 10409700 | Machine | Progressive Reset |
| 13285200 | Jackpot | Progressive Jackpot |
| 13311200 | Jackpot | Progressive Bonus Paid |
| 13328200 | Jackpot | Progressive Jackpot Pending |
| 13328201 | Jackpot | Progressive Jackpot Pending W2G Request |
| 13328600 | Jackpot | Progressive Handpay Reset |

### Mandatory Tasks Setting

Configures which tasks are required for audit completion (tasks that must be completed before the audit day can be closed).

### Flash Report Limit

Sets the maximum number of reports that can be sent in flash reports (1–50).

### Meters On Demand

- **Active Refresh Timer (Seconds)** — Interval in seconds for the meter display to refresh
- **Active Request Timeout (Minutes)** — Time in minutes before an incomplete meter request times out and is listed as failed. A value of zero disables the timeout.

### Cabinet Coin In to Paytable Coin In

- **Auto Adjust Paytable Coin In** — When enabled, automatically distributes differences between cabinet-level coin in and paytable coin in when a new period is opened
- **Auto Adjust Tolerance Amount ($)** — Tolerance amount for automatic adjustments
- **Adjustment Distribution Option** — Distribution method for adjusting paytable coin in to match cabinet coin in

### Greek Regulation

Options related to Greek regulatory requirements:

- **Slip Print Folder** — Path/URL of the slip printer
- **Greek Slip Text Export Enabled** — Yes or No
- **Export Jackpot Slip Language ID** — Language identification number

### Argentina Tax Deduction

Options for configuring Argentina-specific tax features:

- **Bill Tax Enabled** — Enables the bill tax feature (default rate: 0.9500%, configurable 0–5%)
- **Win Tax Enabled** — Enables the win tax feature (default rate: 2.0000%, configurable 0–10%)

> When win tax is enabled, the Argentina Win Tax percentage is only deducted from the cash portion of a handpay jackpot processed at the FJP Station. The win tax is not deducted from any portion returned as an EZ Pay Purchase ticket.

## 4.2 Casino Information

The following casino identification fields are configured:

- Casino Name
- Address, City, State, Zip Code
- Phone
- Fed ID Number (Federal tax identification)
- State ID Number (State tax identification)

## 4.3 Tax Rates / W2G

### Jurisdictional

- **Produce Tax Forms** — Enables printing a W2G form when a taxable jackpot limit is reached
- **Taxable Jackpot Limit** — Dollar threshold for triggering a W2G
- **Tax ID Format** — Format of tax identification numbers

### Federal Taxes

- **Mandatory** — Federal tax percentage for players not providing a Social Security card
- **Voluntary** — Federal tax percentage for players providing a Social Security card

### State Taxes

- **Mandatory** — State tax percentage for players not providing a Social Security card
- **Voluntary** — State tax percentage for players providing a Social Security card
- **Mandatory Non-Resident (%)** — State tax percentage for non-resident players

### City and Local Taxes

- **Mandatory** — City/local tax percentage for players not providing a Social Security card
- **Voluntary** — City/local tax percentage for players providing a Social Security card

### Legal Requirements

- **Legal Age** — Legal gambling age for the jurisdiction
- **Number of IDs** — Additional player IDs required beyond Social Security number for W2G issuance

> The system automatically requests a Social Security number. For example, setting Number of IDs to 1 requires two forms of ID total.

### Form Printing

- **W2G Form** — Standard or Custom
- **1042S Form** — Standard or Custom
- **Accrual W2G Form** — Standard or Custom
- **W2G Printer** — Network location of the W2G printer

### Settings

- **Can Edit W2G Info** — Allows editing of W2G information
- **Round Up Taxes** — Rounds all tax calculations up to the nearest nickel
- **Print Rounded Win on W2G Form** — Rounds jackpot wins up to the nearest five cents
- **W2G Full Cashier Name** — Displays the cashier's full name on tax forms
- **Show Tax Rates in FJP Taxable Accrual** — Displays tax rates in the FJP Taxable Accrual area

## 4.4 Taxable Accrual

Provides options for associating multiple taxable events with a single W2G tax form.

> Users must have appropriate permissions defined prior to setting Tax Accrual options.

### Accrual Settings

- **Enable Taxable Accrual** — Enables taxable accruals
- **Session End** — Time when taxable accrual sessions end
- **Auto Re-Enroll Enable** — Enables automatic re-enrollment in taxable accrual sessions

### Accrual Process Thresholds

Determines who must enter a PIN to accrue a taxable jackpot and at what dollar amount. Applies only to patrons enrolled in taxable accrual:

- **Guest Self Serve** — Threshold for guest self-service
- **Staff Only** — Threshold for staff-only processing
- **Guest & Staff** — Threshold for combined processing

## 4.5 Passwords

Password policy parameters:

- Minimum password length
- Password complexity requirements
- Password expiration period
- Account lockout thresholds

## 4.6 Barcode Options

Configuration for barcode printing and scanning used for machine identification labels and equipment tracking.

## 4.7 FJP Options

Configuration for Fill and Jackpot stations including:

- **Banned Player** settings
- **FJP Configuration** settings
- **S2S Configuration** settings
