# Chapter 1 System Overview

The Machine Accounting (MA) system simplifies the casino accounting process and provides real-time network communications of financial information, as well as machine and player events from floor games as they occur.

## 1.1 The Accounting Period

The accounting period is the core of MA. It separates slot machine play data into manageable time intervals. After the gaming day is over, the information is collected and data is entered for the accounting period. The system collects much of this data; the auditor is responsible for ensuring its accuracy.

MA can be configured to open the gaming day automatically; however, most properties open each day manually when they are ready to audit.

## 1.2 Voucher System

IGT EZ Pay is the typical voucher system used with Machine Accounting. Vouchers are audited using EZ Pay voucher-audit procedures. Voucher imports into MA are also audited.

## 1.3 Report Features

MA includes many reports to assist in the auditing process, including reports on the overall MA system and reports for actual and metered win amounts.

## 1.4 System Components

### Accounting Workstation

The Accounting Workstation is the system's central hub and provides a complete record of slot machine data and activity through its connectivity to the IGT ADVANTAGE Bonusing System.

Key capabilities:

- A User Tasks list displays the status of complete and incomplete accounting tasks.
- Maintenance of all aspects of a machine within Machine Accounting.
- Generation of category-specific reports for analysis of casino operations.
- Maintenance of floor personnel and their access levels.
- Configuration of Machine Accounting and system administrator functions.

### Fills and Jackpot Station (FJP)

The Fills and Jackpot Station (FJP) operates with the IGT ADVANTAGE communications network and posts completed transactions to Machine Accounting. Attendants use the station to complete hopper fills and handpay jackpots.

FJP Server is configured in Configuration Workstation (CWS).

### Attendant Workstation

The Attendant Workstation is typically a touchscreen workstation used for:

- Activating and deactivating attendant cards
- Activating audits, coin tests, soft drops, hard drops, and combined drop cards
- Overriding on- and off-shift information or promoting an attendant's job type
- Issuing and returning attendant equipment at the beginning and end of a shift

The workstation includes a card encoder for staff cards and a barcode scanner for issuing equipment.

### Drop Utility

The Drop Utility can be configured to work with various hardware components such as coin scales, bill counters, and ticket scanners. Located in the hard- and/or soft-count rooms, the output from these components streamlines the accounting process and increases accounting efficiency.

### Bonusing System

The IGT ADVANTAGE Bonusing System is a data-collection and bonusing system using proprietary technology. The system gathers play information from EGMs for use in determining bonus promotions, and transmits data to the Machine Accounting system.

Bonusing programs allow a property to promote awards for active players, such as additional progressive or random jackpots, or multiplied standard jackpots. Casino-wide bonuses are also available.

### Ticket Redemption Terminal

Used to redeem tickets, validate tickets, and balance ticket batches. Individual tickets can also be audited.

### Radio Pager

The Radio Pager interface sets up zoning information for the paging server and alerts floor staff to events. The Pager Trigger monitors events that trigger a floor page; the Paging Zone program assigns specific staff positions to floor-paging zones.

## 1.5 Machine Accounting Functions

Machine Accounting provides the following major functions:

| Name | Description |
|------|-------------|
| Open Period | Opens a period (date) to perform tasks |
| Close Period | Closes the current period |
| Audit Test | Defines audit groups and completes coin tests; allows manual entry of machine meters |
| Meter Test | Tests machine meters |
| Taxable Accrual | Associates multiple tax accrual events with a single tax form (W2G) |
| Meters On Demand | Requests an immediate meter reading for an active slot machine |
| Machine Maintenance | Views and edits machines |
| Maintenance Console | Views and edits machine codes and information used in Machine Maintenance |
| EGM Enable/Disable | Enables or disables individual machines or groups on a preset schedule |
| Work Order Reprint | Reprints work orders |
| Floor Staff Information | Views and manages floor staff records; establishes equipment types and maintains equipment custody |
| Equipment | Adds, modifies, and deletes floor equipment |
| Equipment Types | Adds, modifies, and deletes floor equipment types |
| Pagers | Defines, modifies, or deletes pager zones and triggers |
| User Management | Views and manages all system users |
| Player ID Locales | Adds and deletes country and state abbreviations |
| Flash Report Tasks | Creates reports run as a user task during the audit |
| Accounting Calendar | Defines dates for end-of-month configuration |
| Lease Machines | Defines lease settings for groups of machines |
| Progressive Workbook | Adds, edits, or deletes progressive workbook items |
| User Tasks | Lists tasks to be completed for the current period |
| Reports | Lists available system reports |

## 1.6 The Accounting Period

Each accounting period covers a defined time interval (typically a gaming day). The period lifecycle is:

1. **Open** — Collect machine data and begin audit tasks.
2. **Audit** — Complete all required tasks (meter verification, drops, hand pays, vouchers, etc.).
3. **Close** — Finalize all data for the period. No further changes are allowed.

## 1.7 Machine Data Records

Machine Accounting manages the complete record of each machine's data including its location, configuration, meter readings, drop amounts, and accounting history.
