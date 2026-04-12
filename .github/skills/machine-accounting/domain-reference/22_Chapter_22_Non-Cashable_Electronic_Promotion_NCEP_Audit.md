# Chapter 22 Non-Cashable Electronic Promotion (NCEP) Audit

The NCEP audit reviews non-cashable electronic promotion credits transferred to/from the player-tracking system versus actual meter movement.

The following tasks are available:

| Task | Description |
|------|-------------|
| Import NCEP Information | Import system NCEP-in and NCEP-out revenue summaries by machine |
| Audit NCEP Meters | Audit and correct NCEP-in and NCEP-out variances between actual and meters |

## NCEP Meter Columns

| Column | NCEP In | NCEP Out | Description |
|--------|---------|----------|-------------|
| Machine | ✓ | ✓ | Machine ID |
| Location | ✓ | ✓ | Machine location |
| Denom | ✓ | ✓ | Denomination |
| MtrNCEPromoIn | ✓ | | G2S games only. Non-cashable Xtra Credit transfers in to the EGM |
| MtrNCEPromoOut | | ✓ | G2S games only. Non-cashable transfers out from the EGM |
| ActualNCEPromoIn | ✓ | | Actual NCEP in (from EZ Pay) |
| ActualNCEPromoOut | | ✓ | Actual NCEP out (from EZ Pay) |
| Variance | ✓ | ✓ | Net System NCEP minus Total NCEP |
| Percent | ✓ | ✓ | Percentage of variance |
| Accepted | ✓ | ✓ | Acceptance status |
| Comment | ✓ | ✓ | Audit comment |
| Previous Variance | ✓ | ✓ | Variance from the previous audit period |

## 22.1 Importing NCEP Information

The import process retrieves NCEP drop data from player tracking.

## 22.2 Adjusting NCEP Variances

### Accepting NCEP Variances

Variances within established guidelines can be accepted. Acceptance requires confirmation.

### Adjusting NCEP Drops (Actuals)

System NCEP amounts can be adjusted for each machine:

- **Actual Xtra Credit** — Corrected Xtra Credit amount
- **Actual Point Play** — Corrected Point Play amount
- **Actual Bonus To Credit Meter** — Corrected bonus credit meter amount

## 22.3 NCEP-In Variances

NCEP-in information is obtained from player tracking data gathered during the NCEP import at end of day.

### Viewing NCEP-In Meters

Data can be filtered to show All Machines or only Exceptions. NCEP In is the default view.

### Adjusting NCEP-In Meters

Meter values can be adjusted for individual machines.

### Accepting NCEP-In Variances

Variances can be accepted or unaccepted. Multiple machines can be selected for bulk operations.

## 22.4 NCEP-Out Variances

### Viewing NCEP-Out Meters

Data can be filtered to show All Machines or only Exceptions.

### Adjusting NCEP-Out System Amounts

System amounts and counts can be adjusted for WAT-out data.

### Adjusting NCEP-Out Meters

Meter values can be adjusted for individual machines.

### Accepting NCEP-Out Variances

Variances can be accepted or unaccepted.

### NCEP Comments

Adjustments can be documented with comments. Comments can be selected from a predefined list or entered as free text. Active comments are saved for reuse.
