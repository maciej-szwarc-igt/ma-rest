---
description: "Test Correct Meter Variance (CMV) with no variances scenario. Sets up a machine, sends meters with varying Voucher In and WAT In values, and verifies CMV user task shows correct results."
agent: "machine-accounting"
---

# Correct Meter Variance — No Variances Test

Execute the following test scenario step by step. Use subagents for domain specific tasks. Wait for each step to complete before proceeding to the next. Report the result of each step.

## Parameters

- **DATE**: `{{DATE}}` — the accounting period date (format: YYYY-MM-DD). Must be a date that has no existing period.

## Preconditions

- MA API is running and accessible
- No period exists for DATE or the day prior to DATE

## Test Steps

### Step 0: Restore backup for day before DATE. Assume this is a linux backup.

### Step 1: Open period for DATE (day prior)

Open a period for the **day before DATE**. This is needed so the machine can be created and activated before the target period.

### Step 2: Create a new machine

Create a new machine (save its number as **machineNNN**) with:
- denomination: **0.01**
- tolerance level: **1000** for each meter
- no local manual meters (`manualMeters: false`)
- Use an existing section, bank, cabinet type, and machine type — or create them if needed. The machine type must have denom 0.01 and tolerance 1000 for all meters.

Record the returned machine number — this is **machineNNN**.

### Step 3: Increment parameter fix

The machine was created without manual meters, so set the increment parameter:
- Machine: **machineNNN**
- Increment value: **1** (= 1 cent for denom 0.01)

Use meters agent to set the increment parameter for machineNNN.

### Step 4: Send initial meter for machineNNN

Send an initial meter (type `I`) for **machineNNN** with **all meter fields equal to 1** and the date set to the **day before DATE**. This establishes the baseline for meter deltas.


### Step 5: Verify machineNNN to activate it

Approve the pending machine add for **machineNNN** to transition it from Pending Add (P) to Active (A).

Use `machines_by_mnum_verification_approve_create` with mnum = machineNNN and periodDate = day before DATE.

### Step 6: Close period (day prior)

Close the period for the **day before DATE**.

### Step 7: Send hourly meter — meter1

Send an hourly meter (`M`) for **DATE at 12:00:10** for **machineNNN** (alias: **meter1**):
- `voucherIn` = **11**
- `watIn` = **11**
- All other meter fields = **1** unless the fields are calculated as sum of other fields (e.g. `totalIn`), in which case set them to the correct calculated value.

Use `meters_by_mnum_update` with date = DATE, mnum = machineNNN.

### Step 8: Send hourly meter — meter2

Send another hourly meter (`M`) for **DATE at 13:00:10** for **machineNNN** (alias: **meter2**):
- `voucherIn` = **22**
- `watIn` = **11**
- All other meter fields = **1** unless the fields are calculated as sum of other fields (e.g. `totalIn`), in which case set them to the correct calculated value.

Use `meters_by_mnum_update` with date = DATE, mnum = machineNNN.

### Step 9: Open period for DATE

Open a period for **DATE**.

### Step 10: Verify Correct Meter Variance user task

Check the CMV (Correct Meter Variance) results for **machineNNN** on **DATE**.

**Expected results:**
- **No variance records** — all meter deltas should be within tolerance (1000)
- **No exception records**
- **One record for machineNNN** in the "All" view containing data from **meter2** (the latest hourly meter)

Report whether the expectations are met for each assertion.

## Cleanup

After the test completes (regardless of pass/fail), execute these cleanup steps in order:

1. **StartOver** period for **DATE**
2. **Reopen** period for the **day before DATE**
3. **StartOver** period for the **day before DATE**

Use `periods_by_date_start_over_create` and `periods_by_date_reopen_create` tools respectively.
