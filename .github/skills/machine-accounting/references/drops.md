# Drops and EFT Imports

## Drop Types

- **S** — Soft Drop: pulling the cassette from the EGM; generates an S-signal/S-drop meter.
- **H** — Hard Drop: physical coin drop.
- **W** — WAT (Wagering Account Transfer) drop in `ActualDrop`.
- **B** — EFT (Electronic Funds Transfer) drop in `ActualDrop`.
- **T** — Voucher/Ticket drop in `ActualDrop`.

## Drop-to-Drop

When Drop-to-Drop is enabled, it applies to WAT and EFT. Meters J (Soft Drop Outside Window) and K (Hard Drop Outside Window) are related to Drop-to-Drop. Meter S triggers Drop-to-Drop processing; meter H for hard drops.

If WAT/EFT are not configured for Drop-to-Drop, they appear greyed out in the UI.

## Soft Drop Manual Entry

1. In Audit, choose **Verify Machine Changes** → Cancel first prompt → opens Maintenance Workbook.
2. Select an Active machine → Machine Wizard → "I want to update the machine" → check WAT → Next → Finish.
3. Select **Soft Drop Manual Entry** in audit tasks → enter machine number and actual soft values → Save → Confirm → Done.
4. Run **Close Period** → in the dialog, select radio buttons and click **Assign Zero Drop**, selecting the machine.
5. The drop becomes visible in Audit EFT under "All drops".

## Zero Drop

Zero drops appear in the **Drop Reconciliation** audit report. Without zero drops, the report is empty. After assigning zero drops, zeroes appear.

A drop zone has machines assigned to it with a schedule for S (Soft Drop). When the cassette is pulled, an S-drop meter is received.

## Simulating EFT Import (Proc_EFTTempImport)

```sql
DECLARE @parPeriodDate datetime = CAST('<date>' AS datetime)
DECLARE @parCheckForConnection int = 0
DECLARE @parGetImportCount int = 0

EXECUTE [dbo].[Proc_EFTTempImport]
  @parPeriodDate,
  @parCheckForConnection,
  @parGetImportCount
```

Records land in `ActualDrop` (W for WAT, B for EFT). Details are in `ActualDropDetail` joined on `DropID`. Meter names are in `MeterNames` joined on ID.

### Querying Drops

```sql
-- All WAT and EFT drops for a date
SELECT * FROM ActualDrop
WHERE DropDay = '<date>' AND DropType IN ('W', 'B')
ORDER BY MNum

-- Drop details
SELECT * FROM ActualDropDetail WHERE DropID = <id>

-- All drops with amounts > 1 for specific machines
SELECT ad.DropDay, ad.MNum, addt.MeterNamesID, mn.DefaultName, addt.Amount
FROM ActualDrop ad
JOIN ActualDropDetail addt ON ad.DropID = addt.DropID
JOIN MeterNames mn ON mn.ID = addt.MeterNamesID
WHERE ad.MNum IN (<machines>)
  AND ad.DropDay LIKE '<date>%'
  AND addt.Amount > 1
ORDER BY ad.DropDay
```

## Simulating EFT/EasyPay Errors

In `Proc_EFTTempImport`, the linked server call can be replaced with NULL inserts to simulate connection failures:

```sql
-- Instead of calling EZFunds linked server:
INSERT INTO #EFTReturnSet (...) VALUES (NULL, NULL, NULL, NULL, NULL, NULL)
```

Same pattern applies in `Proc_EFTDropToDropImport` for Drop-to-Drop errors.

## Audit Meters

1. Create a group and add hosts.
2. Open the meters window, select a host, and **Save** — creates a record in the `Audit` table.
3. Simulate floor meters:

```sql
EXEC Proc_AuditEGMMeterUpdate
  '<Date>',         -- e.g. '2025-03-21 00:00:00.000'
  <MachineNum>,     -- e.g. 10201
  <GroupId>,        -- e.g. 1003
  <meter values...>
```

**The MNum and Date must match the audit record exactly.**

## Audit EFT Variance Calculation

When closing audit, the system compares meters from the floor (777 → Detailed Meters) against values from the EFT service. Floor values appear in the `Meter Drop` field in Audit EFT In Meters. Values can be modified via the Meters button, and changes reflect in the 777 detail view.

## Vouchers

- Voucher Out displays records from the period for all hosts **that have a printer configured**.
- In the drop table, voucher records have type `T`.
- Drop detail contains records with MeterNamesID 122 and 140 (should be 120=SystemTicketsOut and 122=ActualTicketsIn).
- **Exception**: an accepted variance value.
- **Empty filter**: shows only variances.
- **All filter**: shows everything.
