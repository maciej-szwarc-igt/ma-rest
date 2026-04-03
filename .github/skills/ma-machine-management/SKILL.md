---
name: ma-machine-management
description: "Manage machines and machine types in the Machine Accounting system via MA-API. Use when: adding a machine, listing machines, removing/retiring a machine, searching machines, viewing machine details, creating or updating machine types, approving or rejecting pending machines, moving machines, converting machines, or importing machines from Excel."
argument-hint: "Action: add, list, retire, search, details, move, convert, add-type, list-types, update-type, approve, reject, import"
---

# MA Machine Management Skill

Manage machines and machine types through the MA-API MCP server. This skill **only** handles machine and machine-type CRUD operations. If a required lookup entity (cabinet type, section, manufacturer, etc.) does not exist, **report it back to the user** rather than creating it.


## Scope

**In scope:** Add, list, search, view, update, retire, move, convert, approve/reject machines; create, list, update machine types.

**Out of scope:** Creating/modifying cabinet types, sections, display types, game types, manufacturers, denominations, equipment types, or any other configuration entities. If a value the user requests does not exist in the lookup tables, inform the user and list the available values.

## User Guide Chapters

Read only the chapters relevant to the current task:

| # | Chapter | When to read |
|---|---------|-------------|
| 06 | [Maintenance Console](../machine-accounting/user-guide/06_Chapter_6_Maintenance_Console.md) | Casino floor master data: cabinet types, sections, game types, display types, manufacturers, denominations, denomination ranges, and machine types. |
| 07 | [Maintenance Workbook](../machine-accounting/user-guide/07_Chapter_7_Maintenance_Workbook.md) | Machine lifecycle: adding, updating, converting, and retiring machines; viewing machine details; machine verification tasks during audits. |
| 08 | [Enabling and Disabling EGMs](../machine-accounting/user-guide/08_Chapter_8_Enabling_and_Disabling_EGMs.md) | Enabling/disabling individual machines or groups, creating EGM groups, and setting up automated enable/disable schedules. |

---

## MCP Tools Reference

### Machine CRUD

| Action | Tool | Key Parameters |
|--------|------|----------------|
| Add machine | `machines_create` | `mnum`, `machineTypeId`, `sectionName`, `bank`, `location` (2-char position code, max 2 chars), `serialNumber`, `cabinetType`, `purchaseDate`, ... |
| Get machine by ID | `machines_by_mnum_details` | `mnum` |
| Get machine info | `machines_by_mnum_machine_info` | `mnum` |
| Update machine | `machines_by_mnum_update` | `mnum` + fields to update |
| Retire machine | `machines_by_mnum_retire_update` | `mnum` |
| Move machines | `machines_location_update` | array of machine/location pairs |
| Convert machine | `machines_convert_create` | `mnum`, new `machineTypeId` |
| List machines (paged) | `machines` | `pageNumber`, `pageSize`, optional filters: `status`, `denom`, `description`, `zone` |
| Search machines | `machines_search` | search/filter criteria |
| Check location exists | `machines_location_by_machineLocation_exists` | `section`, `bank`, `location` |
| Check serial exists | `machines_serial_by_serialNumber_exists` | `serialNumber` |
| Check seal exists | `machines_seal_by_sealNumber_exists` | `sealNumber` |
| Import machines | `machines_import_create` | Excel file |
| Import preview | `machines_import_parse_create` | Excel file |
| Download template | `machines_import_template` | — |
| Reset EGM UID | `machines_by_mnum_egm_id_reset_update` | `mnum` |

### Machine Approval Workflow

| Action | Tool |
|--------|------|
| Approve pending Add/Move/Retire | `machines_by_mnum_verification_approve_create` |
| Reject pending Add/Move/Retire | `machines_by_mnum_verification_reject_create` |

### Machine Type CRUD

| Action | Tool | Key Parameters |
|--------|------|----------------|
| List all types | `machine_types` | — |
| Get type details | `machine_types_by_id` | `id` |
| Get next type ID | `machine_types_next_id` | — |
| Add type | `machine_types_create` | `id`, `denomination`, `manufacturerCode` (int), `description`, `holdPercent`, `gameTypeId` (int), `displayTypeId` (int), ... |
| Update type | `machine_types_by_id_update` | `id` + fields to update |
| Delete type | `machine_types_by_id_delete` | `id` |
| Get pay methods | `machine_types_pay_methods` | — |
| Get soft meter names | `machine_types_soft_meter_names` | — |
| Get par history | `machine_types_by_machineTypeId_par_history` | `id` |

### Lookup Tools (read-only — for dependency validation)

| Entity | Tool |
|--------|------|
| Cabinet types | `cabinet_types` |
| Display types | `display_types` |
| Game types | `game_types` |
| Manufacturers | `manufacturers` |
| Sections | `sections` |
| Section banks | `section_banks` |
| Denominations | `denominations` |
| Denomination ranges | `denomination_ranges` |
| Machine statuses | `machines_statuses` |
| Machine descriptions | `machines_descriptions` |
| Machine denominations | `machines_denoms` |
| Drop zones | `machines_drop_zones` |

---

## Dependencies & Validation

**CRITICAL REQUIREMENT:** When creating a machine, the location (combination of section, bank, and position code) **MUST be unique**. No other machine can occupy the same location. This is a hard constraint that must be validated before machine creation. Location availability is verified via `machines_location_by_machineLocation_exists`.

Before adding a machine or machine type, **always validate** that required lookup values exist. Call the lookup tools and check. If a value does not exist, **do not proceed** — report the missing entity to the user.

### Add Machine — Required Lookups

| Field | Lookup Tool | What to check |
|-------|-------------|---------------|
| `machineTypeId` | `machine_types` | Must be an existing machine type ID |
| `sectionName` + `bank` | `section_banks` | Section/bank combination must exist |
| `cabinetType` | `cabinet_types` | Must match an existing cabinet type name |
| `serialNumber` | `machines_serial_by_serialNumber_exists` | Must NOT already exist (unique) |
| `location` | `machines_location_by_machineLocation_exists` | **UNIQUENESS REQUIRED.** 2-char position code (max 2 chars). Full machine location = `{sectionName}{bank}{location}` (e.g., "AB"+"01"+"03" = "AB0103"). The complete location must be unique — **NO OTHER MACHINE can occupy this location**. Must NOT already be occupied. |
| `eproms` | At least one EPROM entry required. Each entry needs `epromNumber` (integer), `epromValue` (string), and `isActive` (bool). If the user does not provide EPROM details, derive them from an existing Active machine of the same type (`machines_by_mnum_details`) and use `epromNumber=1`, `epromValue=<assigned mnum as string>`, `isActive=true`. |

### Add Machine Type — Required Lookups

| Field | Lookup Tool | What to check |
|-------|-------------|---------------|
| `manufacturerCode` | `manufacturers` | Use the `id` (integer) from the returned list |
| `gameTypeId` | `game_types` | Use the `id` (integer) from the returned list |
| `displayTypeId` | `display_types` | Use the `id` (integer) from the returned list |
| `denomination` | `denominations` | Must match an existing denomination value |
| `id` | `machine_types_next_id` | Use to auto-assign the next available ID |

---

## Defaults

Apply these defaults autonomously when the user has not specified a value. Do **not** ask for confirmation unless the user explicitly requests it.

### Machine Defaults

| Field | Default | Reason |
|-------|---------|--------|
| `cabinetType` | First value returned by `cabinet_types` | Auto-selected from system |
| `purchaseDate` | today's date | Sensible default for new machines |
| `ticketPrinter` | `Y` | Most modern EGMs have ticket printers |
| `hasTicketMeters` | `true` | Required when `ticketPrinter=Y` and system uses IVS ticket config |
| `billValidator` | `true` | Standard on modern EGMs |
| `playerTracking` | `true` | Standard feature |
| `manualMeters` | `false` | Communicating machines by default |
| `useMgaLegacyKey` | `true` | Required field; matches existing machine configuration |
| `watEnabled` | `true` | Required field; matches existing machine configuration |

> **Do NOT send** `vipGame`, `labGame`, or `leased` unless the user explicitly requests them. Sending these fields (even as `false`) causes HTTP 422 validation errors for most machine types.

### Machine Type Defaults

| Field | Default | Reason |
|-------|---------|--------|
| `manufacturer` | `IGT` (id: 6) | Most common manufacturer in system |
| `gameType` | `UPRIGHT` | Most common game type |
| `displayType` | `SLOT` (id: 6) | Most common display type |
| `holdPercent` (par) | `2` | Common par percentage |
| `payMethod` | `B` (Bi-Line) | Standard pay method |
| `maxCoins` | `9999` | Common max |
| `payLines` | `40` | Common multi-line configuration |
| `maxJP` | `99999` | Standard jackpot limit |
| `tokenDenom` | same as `denomination` | Token matches base denom |
| `coinsForPointAward` | `10` | Standard loyalty config |
| `pointCount` | `2` | Standard point multiplier |
| `sbEGM` | `true` | Server-based gaming enabled |
| `multiDenomMultiGame` | `true` | MDMG enabled |
| Default meter variances | `10000` | Standard tolerance per meter |

---

## Procedures

### 1. List Machines

1. Call `machines` with `pageNumber: 1`, `pageSize: 25`.
2. Optionally filter by `status`, `denom`, `description`, or `zone`.
3. Present results as a table: machine number, denomination, location, manufacturer, description, status.
4. Report `totalElements` so the user knows total count.

### 2. Get Machine Details

1. Call `machines_by_mnum_details` with the machine number.
2. Present all returned fields in a readable format.

### 3. Add a Machine

This procedure is **fully autonomous**. If the user does not provide any field values, derive all of them from the system without asking. Only interrupt the user if a hard error occurs that cannot be self-resolved.

**Step 1 — Resolve missing inputs (run all lookups in parallel):**

| Field | How to resolve if not provided by user |
|-------|----------------------------------------|
| `machineTypeId` | Call `machine_types`; pick the first returned type's `id`. |
| `sectionName` + `bank` | Call `section_banks`; pick the first returned combination. |
| `cabinetType` | Call `cabinet_types`; pick the first returned type. |
| `location` | **UNIQUENESS-REQUIRED PROBE.** Call `machines_location_by_machineLocation_exists` with 2-char codes ("01", "02", "03", …) until a free one is found. The location returned must have NO OTHER MACHINE assigned to it. Stop on first available unique location. |
| `serialNumber` | Generate as `"SN-<timestamp>"` (e.g. `"SN-20260402"`); verify unique via `machines_serial_by_serialNumber_exists`. Increment suffix if taken. |
| `purchaseDate` | Use today's date in ISO 8601 format. |
| `eproms` | Use `[{"epromNumber": 1, "epromValue": "<assigned-mnum>", "isActive": true}]`. The assigned mnum is only known after the create call succeeds, so use any unique string (e.g. the serial number) as a placeholder epromValue — or call `machines_by_mnum_details` on any existing Active machine and mirror its EPROM structure with a new unique value. |

**Step 2 — Pre-flight uniqueness checks (run in parallel) — MANDATORY:**

1. **`machines_serial_by_serialNumber_exists`** — serial number must not exist (unique required).
2. **`machines_location_by_machineLocation_exists`** — LOCATION MUST BE UNIQUE. Call with `section`, `bank`, and `location` parameters. The combination {section}{bank}{location} must be free. **If occupied, the location is not available and must be rejected. Do NOT create the machine at that location.** Try available locations up to a reasonable limit (e.g., 10 attempts) before informing the user that no locations are available.

If the serial check fails, adjust the serial number (try next increment) and recheck. If the location check fails, probe systematically for the next available location code. Do **not** stop to ask the user unless locations are exhausted.

**Step 3 — Call `machines_create` with these fields:**

| Parameter | Value |
|-----------|-------|
| `machineTypeId` | resolved above |
| `sectionName` | resolved above |
| `bank` | resolved above |
| `location` | resolved above (2-char code, max 2 chars) |
| `cabinetType` | resolved above |
| `serialNumber` | resolved above |
| `purchaseDate` | today's date |
| `ticketPrinter` | `"Y"` |
| `hasTicketMeters` | `true` |
| `billValidator` | `true` |
| `playerTracking` | `true` |
| `manualMeters` | `false` |
| `useMgaLegacyKey` | `true` |
| `watEnabled` | `true` |
| `eproms` | `[{"epromNumber": 1, "epromValue": "<unique-string>", "isActive": true}]` |

> **Do NOT include:** `vipGame`, `labGame`, `leased`, or any field not listed above unless the user explicitly requested it. Sending `vipGame` or `labGame` (even as `false`) causes HTTP 422 for most machine types.

**Step 4 — Report result:**

The API returns `{"machineNumber": <mnum>, "workOrderId": <id>}`. Report the assigned mnum, work order ID, and full parameter list used.

The machine enters **Pending Add** status.

**STOP here — do NOT proceed to approve or reject the machine.** The next required step is for the user to send an **Initial Meter** (via the ma-meters skill) while the machine is still in Pending Add status. Only after the initial meter has been sent can the machine be approved (Procedure 5). Approval is a separate workflow that must be explicitly requested by the user.

### 4. Retire a Machine

1. Call `machines_by_mnum_details` to verify the machine exists and show current details.
2. Confirm with the user.
3. Call `machines_by_mnum_retire_update` with the machine number.
4. The machine enters **Pending Retire** status. Inform the user it needs approval.

### 5. Approve or Reject Pending Machines

> **For Pending Add machines:** An Initial Meter (`I`) must have been sent (via the ma-meters skill) before approval. Do not approve a Pending Add machine if no initial meter has been sent.

1. List machines with `status: Pending Add`, `Pending Retire`, or `Location Change` using `machines`.
2. User selects which machine(s) to approve or reject.
3. Call `machines_by_mnum_verification_approve_create` or `machines_by_mnum_verification_reject_create`.

### 6. Move a Machine

> **Important:** A machine move is a formal process that transitions the machine to **Pending Move** status requiring verification/approval. Only use `machines_location_update` when the user explicitly asks to **move** a machine. To simply update the location field (e.g. correcting a typo or setting location during setup), use `machines_by_mnum_update` instead.
>
> **`machines_location_update` CANNOT be used on machines in Pending Add status.** If the machine is in Pending Add, use `machines_by_mnum_update` to change its location.

1. Verify the machine is **not** in Pending Add status → `machines_by_mnum_details`.
2. Validate the target location is not occupied → `machines_location_by_machineLocation_exists`.
3. Call `machines_location_update` with the machine number and new location.

### 7. Convert a Machine (Change Type)

1. Validate the new `machineTypeId` exists → `machine_types`.
2. Call `machines_convert_create` with the machine number and new type ID.

### 8. Add a Machine Type

**Pre-flight checks:**

1. Ask user for: denomination, manufacturer, description, par (hold %), game type, display type.
2. Get next available ID → `machine_types_next_id`.
3. Validate manufacturer → `manufacturers`.
4. Validate game type → `game_types`.
5. Validate display type → `display_types`.
6. Validate denomination → `denominations`.
7. If ANY check fails, report and list valid options.
8. Propose defaults for remaining fields. Confirm with user.
9. Call `machine_types_create`.

### 9. List Machine Types

1. Call `machine_types`.
2. Present as a table: ID, manufacturer, denomination, description, par, game type, display type.

### 10. Import Machines from Excel

1. Call `machines_import_template` to get the template format.
2. User fills in the template.
3. Call `machines_import_parse_create` for validation preview.
4. If preview is clean, call `machines_import_create`.

---

## Examples

### Example 1: List all active machines

```
User: List all active machines
Action: machines(pageNumber=1, pageSize=50, status="Active")
```

### Example 2: Add a machine with no user input

```
User: Add a new machine

Autonomous resolution (all in parallel):
  1. machine_types → first result: id=1 (IGT, $0.01, AVP)
  2. section_banks → first result: AB/01
  3. cabinet_types → first result: "Bar Top"
  4. machines_location_by_machineLocation_exists(AB, 01, 01) → occupied
     machines_location_by_machineLocation_exists(AB, 01, 02) → occupied
     machines_location_by_machineLocation_exists(AB, 01, 03) → free ✓
  5. machines_serial_by_serialNumber_exists("SN-20260402") → free ✓

Call: machines_create(
  machineTypeId=1,
  sectionName="AB", bank="01", location="03",
  cabinetType="Bar Top",
  serialNumber="SN-20260402",
  purchaseDate="2026-04-02T00:00:00Z",
  ticketPrinter="Y", hasTicketMeters=true,
  billValidator=true, playerTracking=true,
  manualMeters=false,
  useMgaLegacyKey=true, watEnabled=true,
  eproms=[{epromNumber:1, epromValue:"SN-20260402", isActive:true}]
)
Result: {machineNumber: 10282, workOrderId: 30} → Machine 10282 created in Pending Add status.
```

### Example 3: Retire machine 10210

```
User: Retire machine 10210

Pre-flight:
  1. machines_by_mnum_details(10210) → status: Active, location: IN0310 ✓
  2. User confirms retirement.

Call: machines_by_mnum_retire_update(mnum=10210)
Result: Machine 10210 moved to Pending Retire status.
```

### Example 4: Create a new machine type for Bally $0.25 slots

```
User: Create a machine type for Bally quarter slots, 5% hold

Pre-flight:
  1. machine_types_next_id → returns 26
  2. manufacturers → "BALLY" exists (id: 2) ✓
  3. game_types → "UPRIGHT" exists ✓
  4. display_types → "SLOT" exists ✓
  5. denominations → 0.25 exists ✓

Call: machine_types_create(
  id=26, denomination=0.25, manufacturerCode=2,
  description="BALLY_QUARTER", holdPercent=5,
  gameTypeId=2, displayTypeId=6,
  tokenDenom=0.25, maxCoins=9999, payLines=25,
  maxJP=99999, payMethod="B", coinsForPointAward=10,
  pointCount=1, sbEGM=true, multiDenomMultiGame=true
)
Result: Machine type 26 created.
```

### Example 5: Move machine 10210 to a new location

```
User: Move machine 10210 to section AB, bank 01, location 05

Pre-flight:
  1. machines_location_by_machineLocation_exists("AB","01","05") → not occupied ✓

Call: machines_location_update([{mnum: 10210, section: "AB", bank: "01", location: "05"}])
Result: Machine 10210 moved to Location Change status (pending approval).
```

### Example 6: Dependency missing — report to user

```
User: Add a machine type for manufacturer "KONAMI"

Pre-flight:
  1. manufacturers → "KONAMI" not found

Response: "Manufacturer 'KONAMI' does not exist in the system.
  Available manufacturers: ANCHOR, BALLY, CDS, GAMES OF CHANCE, GLOBAL, IGT,
  P&M COIN, SIGMA, UNIV, VLC, SILICON, WILLIAMS, MIKOHN, SCI, VARIANCE,
  ARISTOCRAT, Extreme Slot, Atronic, Bermoy, IGT Europe.
  Please add the manufacturer first via the Maintenance Console, or choose an existing one."
```

---

## Current System Configuration

> These values were captured from the live system. Use them for validation and default proposals.

### Denominations
| Value | Soft Drop Var | Machine# Range |
|-------|--------------|----------------|
| 0.00 | 0 | 0–1000 |
| 0.01 | 500 | 10000–11999 |
| 0.05 | 500 | 12000–12499 |
| 0.10 | 500 | 12500–12999 |
| 0.25 | 500 | 13000–13499 |
| 0.50 | 500 | 13500–13999 |
| 1.00 | 500 | 14000–14499 |

### Sections (with banks)
| Section | Banks |
|---------|-------|
| AB | 01, 02, 03, 05, 10, 11, 22, 25, 44, 50, 90 |
| B2 | 01, 11, 23, 43, 44, 77 |
| ET | 05, 10, 25, 50, 69, 90 |
| IN | 01, 03, 07, 12, 27, 52, 65, 92 |
| IP | 06, 11, 26, 51, 91 |
| KVS | 01 |
| NG | 06, 11, 26, 51, 91 |
| POLB | 0A |
| RN | 01 |
| WAW | 01 |
| XX | XX |
| YZ | 44 |

### Cabinet Types
Bar Top, Bar Tops, FGG, LOUNGE TOP, LOW, QQQ1, Round Top, Slant, Specialty, Square Top, STANDING, TestCabinet1, Upright

### Display Types
FLIPIT (1), MECH (2), PLASMA (3), REEL (4), REEL 4 (5), SLOT (6)

### Game Types
SLANTTOP (1), UPRIGHT (2), BARTOP (3)

### Manufacturers
ANCHOR (1), BALLY (2), CDS (3), GAMES OF CHANCE (4), GLOBAL (5), IGT (6), P&M COIN (7), SIGMA (8), UNIV (9), VLC (10), SILICON (12), WILLIAMS (13), MIKOHN (14), SCI (16), VARIANCE (17), ARISTOCRAT (18), Extreme Slot (28), Atronic (200010), Bermoy (200011), IGT Europe (200012)

### Pay Methods
B = Bi-Line, L = Line, M = Multiply

### Machine Statuses
Active, Location Change, Pending Add, Pending Retire
