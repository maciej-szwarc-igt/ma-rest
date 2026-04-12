# Chapter 23 Cashable Electronic Promotion (CEP) Audit

The CEP audit reviews cashable electronic promotion (Xtra Credit and PointPlay) credits from the player-tracking system versus actual meter movement.

The following tasks are available:

| Task | Description |
|------|-------------|
| Import CEP Information | Imports system CEP-in and CEP-out revenue summaries by machine |
| Audit CEP Meters | Audit and correct CEP-in and CEP-out variances between actual and meters |

## CEP Meter Columns

### CEP In

| Column | Description |
|--------|-------------|
| Machine | Machine ID |
| Location | Machine location |
| Denom | Denomination |
| CEPI Meter | CEP-in meter value |
| Legacy Non-Deduct Meter | Legacy non-deductible meter |
| Non-Restricted Bonus Meter | Non-restricted bonus meter |
| Total CEPI Meter | Total CEP-in meter |
| Actual Xtra Credit (PM) | Actual Xtra Credit from Patron Management |
| Actual Promo Credit (EZ Pay) | Actual promo credit from EZ Pay |
| Actual Credit Meter | Actual credit meter |
| Actual Point Play | Actual point play |
| Total System CEPI | Total system CEP-in |
| NR Bonus Meter | Non-restricted bonus meter |
| Net System CEPI | Net system CEP-in |
| Variance | Difference between meter and actual |
| Percent | Variance percentage |
| Accepted | Acceptance status |
| Comment | Audit comment |
| Previous Variance | Variance from previous period |

### CEP Out

| Column | Description |
|--------|-------------|
| Machine | Machine ID |
| Location | Machine location |
| Denom | Denomination |
| CEPO Meter | CEP-out meter value |
| Variance | Difference between meter and actual |
| Percent | Variance percentage |
| Accepted | Acceptance status |
| Comment | Audit comment |
| Previous Variance | Variance from previous period |

## 23.1 Importing CEP Information

The import process retrieves CEP drop data from the player-tracking system.

## 23.2 Accepting CEP Variances

Variances within established guidelines can be accepted. Acceptance requires confirmation.

## 23.3 Adjusting CEP Drops (Actuals)

System CEP amounts can be adjusted for each machine:

- **Actual Xtra Credit** — Corrected Xtra Credit amount
- **Actual Point Play** — Corrected Point Play amount
- **Actual Bonus To Credit Meter** — Corrected bonus credit meter amount

## 23.4 CEP-In Variances

### Viewing CEP-In Meters

Data can be filtered to show All Machines or only Exceptions.

### Adjusting CEP-In Meters

Meter values can be adjusted for individual machines:

- **CEPI Meter** — CEP-in meter adjustment
- **Legacy Non-Deduct Meter** — Legacy non-deduct meter adjustment
- **Non-Restricted Bonus Meter** — Non-restricted bonus meter adjustment

### Accepting CEP-In Variances

Variances can be accepted or unaccepted. Multiple machines can be selected for bulk operations.

## 23.5 CEP-Out Variances

### Viewing CEP-Out Meters

Data can be filtered to show All Machines or only Exceptions.

### Adjusting CEP-Out Meters

Meter values can be adjusted for individual machines.

### Accepting CEP-Out Variances

Variances can be accepted or unaccepted.
