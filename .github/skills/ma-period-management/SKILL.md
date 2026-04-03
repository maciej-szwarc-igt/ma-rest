---
name: ma-period-management
description: "Manage accounting periods in the Machine Accounting system via MA-API. Use when: opening a period, closing a period, reopening a period, starting over a period, checking period status, viewing period dates, machine verification during periods, deferring verification, fixing missing meters, assigning zero drops, viewing operator payouts, adjusting payouts, managing period comments, or querying meter readings for a period."
argument-hint: "Action: open, close, reopen, start-over, status, verify, defer, fix-meters, zero-drop, payouts, comments, meters"
---

# MA Period Management Skill

Manage accounting periods through the MA-API MCP server. This skill handles the daily audit cycle: opening periods, verifying machines, resolving issues, and closing periods.

## Scope

**In scope:** Open, close, reopen, start-over periods; query period statuses and dates; machine verification and deferral; fix missing meters; assign zero drops for close; operator payout adjustments; period comments; meter queries.

**Out of scope:** Machine CRUD (use ma-machine-management), drop zone/time/schedule configuration, EGM enable/disable schedules, machine groups, MGA paytable management, maintenance console entities. If the user needs these, direct them to the appropriate skill.

## User Guide Chapters

Read only the chapters relevant to the current task:

| # | Chapter | When to read |
|---|---------|-------------|
| 14 | [Audit Checklist](../machine-accounting/user-guide/14_Chapter_14_Audit_Checklist.md) | Complete 25-step daily audit workflow from period opening through closing, including all checkpoint validations. |
| 15 | [Opening the Audit Day](../machine-accounting/user-guide/15_Chapter_15_Opening_the_Audit_Day.md) | Period opening: starting the period, initializing handpay entries, retrieving period meters, User Tasks list, and Period Timeline Ribbon. |
| 18 | [Fills, Jackpots, and Hand Pays](../machine-accounting/user-guide/18_Chapter_18_Fills_Jackpots_and_Hand_Pays.md) | Verifying and balancing hand pays between system and cage, manual handpay entry, slip editing/voiding, and jackpot variance acceptance. |
| 24 | [Soft Drop Tasks](../machine-accounting/user-guide/24_Chapter_24_Soft_Drop_Tasks.md) | Soft drop audit: retrieving actual soft drops, assigning orphan cans, accepting/swapping variances, and adjusting soft drop amounts and meters. |
| 26 | [Closing the Audit Period](../machine-accounting/user-guide/26_Chapter_26_Closing_the_Audit_Period.md) | Final period closure: verifying machine retirements after drops are complete and closing the period to freeze audit information. |
| 27 | [Hard Drop Tasks](../machine-accounting/user-guide/27_Chapter_27_Hard_Drop_Tasks.md) | Hard drop audit: retrieving actual hard drops, assigning orphan buckets, accepting/swapping variances, and adjusting hard drop amounts and meters. |
| 29 | [Reprinting Work Orders](../machine-accounting/user-guide/29_Chapter_29_Reprinting_Work_Orders.md) | Reprinting work orders for machines pending retirement or relocation, with filters for date, user, type, and machine number. |

---

## Domain Rules

### Period Lifecycle

1. A period can be **opened** for a specific day, marking it as an Open Accounting Period.
2. A period can only be opened for a day that was **not** previously opened or closed.
3. Multiple periods can be open simultaneously; you can switch between them.
4. It is **impossible** to open a period for a future date.
5. If a period is already open, a new period can only be opened for the day **after** the last opened period (or later).
6. An opened period can be **started over** — the day reverts to a regular (non-period) day.
7. An opened period can be **closed**.
   - If multiple periods are open, only the **oldest** open period can be closed.
8. A closed period marks the day as a Closed Accounting Period.
9. A closed period can be **reopened**, reverting to Open status.
   - Only the **last** closed period can be reopened.
10. Days between two closed periods that had no period operations cannot be chosen or opened.
11. **Period cannot be closed if there are unresolved variances** for any machine on that day.
12. **Period cannot be closed if a mandatory User Task is not marked as done.**


---

## MCP Tools Reference

### Period Lifecycle

| Action | Tool | Key Parameters |
|--------|------|----------------|
| Open a period | `periods_by_date_open_create` | `date` (YYYY-MM-DD) |
| Close a period | `periods_by_date_close_create` | `date` (YYYY-MM-DD) |
| Reopen a closed period | `periods_by_date_reopen_create` | `date` (YYYY-MM-DD) |
| Start over a period | `periods_by_date_start_over_create` | `date` (YYYY-MM-DD) |

### Period Queries

| Action | Tool | Key Parameters |
|--------|------|----------------|
| Get period statuses | `periods_status` | `Start`, `End` (date range) |
| Get most recent period | `periods_status_latest` | optional `status` filter |

### Machine Verification (during periods)

| Action | Tool | Key Parameters |
|--------|------|----------------|
| List machines pending verification | `machines_pending_verification` | `periodDate` |
| List deferred machines | `machines_pending_verification_deferred` | `periodDate` |
| Defer verification to next period | `machines_by_mnum_verification_defer_create` | `mnum`, `periodDate` |
| Undo most recent defer | `machines_by_mnum_verification_undo_defer_create` | `mnum` |

### Meter Operations

| Action | Tool | Key Parameters |
|--------|------|----------------|
| Get meters for a machine | `meters` | `mnum` |
| Get meter detail | `meters_by_mnum` | `mnum`, `meterType` |
| Upsert a meter reading | `meters_by_mnum_update` | `mnum`, `meterType`, `value` |
| Fix missing meter | `periods_by_date_fix_missing_meter_create` | `mnum` |
| Get current meters | `machines_by_mnum_current_meters` | `mnum` |
| Get detail meters | `machines_by_mnum_detail_meters` | `mnum` |
| Get available meter readings | `machines_by_mnum_meters` | `mnum` |
| Get MGA current meters | `machines_by_mnum_mga_meters` | `mnum` |
| Check final meter support | `machines_by_mnum_paytables_final_meter_supported` | — |

### Close Period Support

| Action | Tool | Key Parameters |
|--------|------|----------------|
| Get machines with missing drop errors | `periods_by_date_close_missing_drops` | `periodDate` |
| Assign zero drop to EGMs | `periods_by_date_close_zero_drop_create` | `periodDate`, machine list |
| Check pending drop for retire verification | `machines_by_mnum_verification_pending_drop` | `mnum` |

### Operator Payouts

| Action | Tool | Key Parameters |
|--------|------|----------------|
| Get payouts for a period | `op_payouts_by_periodDate` | `periodDate` |
| Adjust payout | `op_payouts_by_periodDate_adjusted_payout_by_mnum_upda` | `mnum`, `periodDate`, `amount` |
| Delete adjusted payout | `op_payouts_by_periodDate_adjusted_payout_by_mnum_dele` | `mnum`, `periodDate` |

### Comments

| Action | Tool | Key Parameters |
|--------|------|----------------|
| Get comment for machine/period | `op_payouts_by_periodDate_comments_by_mnum` | `mnum`, `periodDate` |
| Update comment for machine/period | `op_payouts_by_periodDate_comments_by_mnum_update` | `mnum`, `periodDate`, `text` |
| List all comments | `op_payouts_comments` | optional `status` filter |
| Create a comment | `op_payouts_comments_create` | `text`, ... |
| Delete a comment | `op_payouts_comments_by_commentNumber_delete` | `commentId` |
| Update comment status | `op_payouts_comments_by_commentNumber_status_update` | `commentId`, `status` |

### Lookup Tools (read-only — for context)

| Entity | Tool |
|--------|------|
| User jobs | `user_jobs` |
| User job by ID | `user_jobs_by_userJobId` |
| Configuration value | `configuration_by_configurationName` |
| Tolerance levels | `tolerance_levels` |
| Work order types | `work_orders_types` |
| Work orders | `work_orders` |

---

## Dependencies & Validation

### Before Opening a Period

1. Call `periods_status_latest` to find the last period date.
2. The new period date must be **after** the last opened period date and **not in the future**.
3. Call `periods_status` for the target date range to confirm the date has no existing period.

### Before Closing a Period

1. If multiple periods are open, only the **oldest** can be closed. Call `periods_status` to verify.
2. Call `periods_by_date_close_missing_drops` — if machines have missing drops, they must be assigned zero drops first.
3. All machine variances must be resolved (accepted as exceptions).
4. All mandatory User Tasks must be marked done.
5. Call `machines_pending_verification` — pending machines should be verified or deferred.

### Before Reopening a Period

1. Only the **last** closed period can be reopened. Call `periods_status_latest` with `status=Closed` to confirm.

---

## Procedures

### 1. Open a Period

1. Call `periods_status_latest` to get the last period date and status.
2. Determine the next valid date (day after last opened period, up to today).
3. Confirm the date with the user.
4. Call `periods_by_date_open_create` with the date.
5. Report success. The period is now Open.

### 2. Check Period Status

1. Ask user for a date range (or default to last 30 days).
2. Call `periods_status` with `Start` and `End`.
3. Present results as a table: date, status.
4. Also call `periods_status_latest` for a quick summary.

### 3. Close a Period

**Pre-flight checks (all required):**

1. Call `periods_status` to identify the oldest open period (that's the one to close).
2. Call `periods_by_date_close_missing_drops` for that date.
   - If machines have missing drops → ask user whether to assign zero drops.
   - If yes → call `periods_by_date_close_zero_drop_create`.
3. Call `machines_pending_verification` for that date.
   - If machines are pending → inform user. They can defer or resolve before closing.
4. Confirm with the user.
5. Call `periods_by_date_close_create` with the date.
6. Report success. The period is now Closed.

### 4. Reopen a Period

1. Call `periods_status_latest` with `status=Closed` to find the last closed period.
2. Confirm the date with the user (only the last closed period can be reopened).
3. Call `periods_by_date_reopen_create` with the date.
4. Report success. The period is now Open again.

### 5. Start Over a Period

1. Call `periods_status` to identify open periods.
2. Confirm with the user — starting over reverts the day to a non-period state.
3. Call `periods_by_date_start_over_create` with the date.
4. Report success. The day is no longer an accounting period.

### 6. Machine Verification

1. Call `machines_pending_verification` with the period date.
2. Present the list of machines awaiting verification.
3. User can:
   - **Defer** a machine → call `machines_by_mnum_verification_defer_create`.
   - **Undo defer** → call `machines_by_mnum_verification_undo_defer_create`.
4. Call `machines_pending_verification_deferred` to show already-deferred machines.

### 7. Fix Missing Meters

1. Call `machines_by_mnum_current_meters` or `meters` to see what meters exist.
2. If meters are missing, call `periods_by_date_fix_missing_meter_create` with the machine number.
3. Verify with `meters` again.

### 8. View/Adjust Operator Payouts

1. Call `op_payouts_by_periodDate` with the period date.
2. Present payouts per machine.
3. To adjust: call `op_payouts_by_periodDate_adjusted_payout_by_mnum_upda`.
4. To delete adjustment: call `op_payouts_by_periodDate_adjusted_payout_by_mnum_dele`.

### 9. Assign Zero Drops

1. Call `periods_by_date_close_missing_drops` to list affected machines.
2. Confirm with the user which machines should receive zero drops.
3. Call `periods_by_date_close_zero_drop_create` with the machine list.
4. Verify by re-calling `periods_by_date_close_missing_drops`.

### 10. Manage Period Comments

1. To view: call `op_payouts_by_periodDate_comments_by_mnum` or `op_payouts_comments`.
2. To create: call `op_payouts_comments_create`.
3. To update: call `op_payouts_by_periodDate_comments_by_mnum_update` or `op_payouts_comments_by_commentNumber_status_update`.
4. To delete: call `op_payouts_comments_by_commentNumber_delete`.

---

## Examples

### Example 1: Check recent period statuses

```
User: What periods have been opened this month?
Action: periods_status(Start="2025-03-01", End="2025-03-31")
Result: 8 periods from 2025-03-14 to 2025-03-21, all Closed.
```

### Example 2: Open the next period

```
User: Open the next period

Pre-flight:
  1. periods_status_latest → 2025-03-21 (Closed)
  2. Next valid date: 2025-03-22

Call: periods_by_date_open_create(date="2025-03-22")
Result: Period for 2025-03-22 is now Open.
```

### Example 3: Close a period with missing drops

```
User: Close the period for 2025-03-22

Pre-flight:
  1. periods_status(Start="2025-03-22", End="2025-03-22") → status: Open ✓
  2. periods_by_date_close_missing_drops → machines 10210, 10211 have missing drops
  3. User confirms zero drop assignment
  4. periods_by_date_close_zero_drop_create(periodDate="2025-03-22", machines=[10210, 10211])
  5. machines_pending_verification → none pending ✓

Call: periods_by_date_close_create(date="2025-03-22")
Result: Period for 2025-03-22 is now Closed.
```

### Example 4: Reopen the last closed period

```
User: Reopen the last period

Pre-flight:
  1. periods_status_latest(status="Closed") → 2025-03-21

Call: periods_by_date_reopen_create(date="2025-03-21")
Result: Period for 2025-03-21 is now Open again.
```

### Example 5: Defer machine verification

```
User: Defer verification for machine 10210 on today's period

Pre-flight:
  1. machines_pending_verification(periodDate="2025-03-22") → 10210 is pending ✓

Call: machines_by_mnum_verification_defer_create(mnum=10210, periodDate="2025-03-22")
Result: Machine 10210 verification deferred to the next period.
```

### Example 6: View operator payouts and adjust

```
User: Show payouts for 2025-03-21 and adjust machine 10210 to $500

Action: op_payouts_by_periodDate(periodDate="2025-03-21")
Result: Shows payouts per machine.

Call: op_payouts_by_periodDate_adjusted_payout_by_mnum_upda(mnum=10210, periodDate="2025-03-21", amount=500)
Result: Payout for machine 10210 adjusted to $500.
```

### Example 7: Start over a period

```
User: Start over the period for 2025-03-22

Pre-flight:
  1. periods_status(Start="2025-03-22", End="2025-03-22") → status: Open ✓
  2. User confirms start-over.

Call: periods_by_date_start_over_create(date="2025-03-22")
Result: Day 2025-03-22 is no longer an accounting period.
```
