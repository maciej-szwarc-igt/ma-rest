# Chapter 28 Audit Workbook

The Audit Workbook correlates manual (physical) meter readings with electronic meter readings for auditing machine performance. It also provides Meters On Demand capability.

## 28.1 Viewing Audit Meters

Audit meters can be viewed in two modes:

- **Machine Meters** — Electronic meter readings from the system
- **Hard Meters** — Physical odometer readings taken manually

Data can be filtered by date and audit group.

## 28.2 Audit Groups

Audit groups organize machines for targeted audit testing.

### Adding an Audit Group

Provide a **Group Name** to create a new audit group.

### Adding Machines to a Group

Machines can be added to an existing audit group. Multiple machines can be selected at once.

### Removing Machines from a Group

Machines can be removed from an audit group.

### Deleting an Audit Group

An audit group can be permanently removed.

### Renaming an Audit Group

An existing audit group can be renamed.

## 28.3 Reading Floor Meters

Physical floor meter readings can be captured using handheld scanners (e.g., Intermec CN3):

1. Insert an audit card into the scanner.
2. Scan the machine barcode or enter the machine number manually.
3. Record meter readings:
   - **Hard meters** — Visible odometer readings on the machine
   - **Soft meters** — Display cycling meter values
4. Sync the data back to the Machine Accounting database via the scanner cradle.

## 28.4 Adjusting Machine Meters

Machine meters can be adjusted based on the Meter Delta Variance report. For each machine, the following meter data is available:

| Meter | Description |
|-------|-------------|
| Physical Coin In | Physical coin-in odometer |
| Physical Coin Out | Physical coin-out odometer |
| Coin In | Electronic coin-in meter |
| Coin Out | Electronic coin-out meter |
| Games | Game count |
| Total Drop | Total drop value |
| Bill denominations ($1–$100) | Individual bill denomination counts |
| Bill In | Total bill-in value |
| Attendant Paid Cancelled Credits | Attendant-paid cancel credit meter |
| Attendant Paid External Bonus | Attendant-paid external bonus meter |
| Attendant Paid Jackpots | Attendant-paid jackpot meter |
| Attendant Paid Progressive | Attendant-paid progressive meter |

For each meter, the following columns are displayed:

- **Prior Value** — Previous meter reading
- **New Value** — Current meter reading (editable)
- **Difference** — Calculated delta

## 28.5 Meters On Demand

Meters On Demand allows requesting an immediate meter reading from any active slot machine (up to 8 machines at a time).

The following information is displayed for each requested machine:

| Column | Description |
|--------|-------------|
| Status | Request status (Pending, Complete, Failed) |
| Mnum | Machine number |
| Location | Machine location |
| Paytable | Paytable identifier |
| Base Percentage | Hold percentage |
| Game Number | Game identifier |
| Meter columns | Current meter values |

The display can be paused and resumed. The refresh interval and request timeout are configured in the General Configuration settings.
