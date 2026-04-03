# Machine Status Transitions

## State Diagram

```
Status: P (Pending Add)
           │
           │ ← INITIAL METER (Type = 'I') — REQUIRED (sent while still Pending Add)
           │ ← APPROVE (verification_approve) — REQUIRED after initial meter
           ▼
Status: A (Active)
           │
           │ ← HOURLY METERS (Type = 'M') — recurring
           │ ← SOFT DROP METER (Type = 'S')
           │ ← HARD DROP METER (Type = 'H')
           │ ← AUDIT METER (Type = 'A')
           │
           ▼
  MOVE MACHINE
Status: L (Pending Move)
           │
           │ ← LOCATION METER (Type = 'L') — REQUIRED
           ▼
Status: A (Active) — new location
           │
           │ ← continues HOURLY METERS
           │
           ▼
  RETIRE MACHINE
Status: R (Pending Retire)
           │
           │ ← FINAL METER (Type = 'F') — REQUIRED
           ▼
Status: X (Pending Close) — waiting for period close
           │
           │ ← Close Period
           ▼
Status: I/S/W (Inactive / Sold / Warehouse)
```

## Key Rules

- **Pending Add → Active**: Requires an Initial meter (`I`) sent first, then approval via `machines_by_mnum_verification_approve_create`. The initial meter is sent while the machine is still in Pending Add status; approval comes after.
- **Active → Pending Move**: Machine is assigned a new location; requires a Location meter (`L`).
- **Active → Pending Retire**: Requires a Final meter (`F`).
- **Pending Close → Inactive/Sold/Warehouse**: Happens automatically during period close.

## Hard Drop Mode

To set a machine type to hard drop mode (non-coinless):

```sql
UPDATE MachineType SET Coinless = 'N' WHERE MachineTypeId = <id>
```
