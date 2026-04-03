# Correct Meter Variance (CMV)

## Overview

CMV checks if there are variances for any machine during the audit process. A variance is accepted by turning it into an **exception**.

## Variance Types

| Reason | ReasonNum | SBG Flag | Machine Type | Root Cause |
|--------|-----------|----------|--------------|------------|
| RAM Clear | 4 | `N` | Traditional/Legacy slot | Physical RAM wipe (hardware or firmware reset) |
| AI Download | 3 | `Y` | Server-Based Game (SBG) | Game content download from central server resets meters |
| Negative | 1 | any | any | One or more meters went backwards (below zero) |
| Over Tolerance | 2 | any | any | Meter delta exceeded the configured tolerance threshold |
| Meter Mismatch | -1 | any | MGA machines | Cabinet-level meters don't match sum of MGA paytable-level meters |
| N/A | 0 | any | any | No variances or exceptions — machine is clean for the period |

## CMV Grouping

Machines are grouped into:
- **Variances** — machines with active variances
- **Exceptions** — machines with accepted exceptions
- **All** — machines with variances OR exceptions OR correct values

There is always **one row per machine** showing the number of variances and variance type.

## Calculation

- **Today's value** for each meter = `(prior meter - today's meter) × denom`
- If **today's value > tolerance**, then **variance = today's value − tolerance**

## Core Detection Logic

Gaming machines maintain running counters (meters). Each period stores a delta. A **negative variance** means a meter went backwards.

If a machine has **too many negative variances** (more than 50% of its relevant meter count, called `TooManyBad`), the system assumes all meters **reset to zero** rather than blaming each individually. The distinction between AI Download and RAM Clear depends on the machine's `SBG` flag.

### Detection SQL (from `dbo.Proc_MeterVariance`)

```sql
-- TooManyBad = 50% of the machine's relevant meter count
'TooManyBad' = mb.BadCount * 0.5

-- Assign ReasonNum in dbo.Period:
WHEN (O.TotalVariances - O.OverTolerance) > O.TooManyBad
    AND O.SBG = 'Y' THEN 3   -- AI Download  (SBG machine)
WHEN (O.TotalVariances - O.OverTolerance) > O.TooManyBad
    AND O.SBG = 'N' THEN 4   -- RAM Clear    (legacy machine)
WHEN O.Negative > 0 THEN 1   -- Negative
ELSE 2                        -- Over Tolerance
```

- `TotalVariances - OverTolerance` = count of negative variances only.
- Over-tolerances are excluded as they don't indicate a full meter reset.

## RAM Clear (ReasonNum = 4, SBG = 'N')

Happens on traditional (non-SBG, legacy) machines. A deliberate or accidental erasure of battery-backed RAM where meters are stored. Related event codes: `041` → Ram Clear, `040` → Ram Error.

## AI Download (ReasonNum = 3, SBG = 'Y')

Happens on Server-Based Game (SBG) machines. New game content is pushed from a central server, resetting meters. This is a normal operational event for SBG machines.

## Period Closure Constraint

**Period cannot be closed if there are unresolved variances for any machine on the specific day.** All variances must be accepted (converted to exceptions) or resolved before closing.
