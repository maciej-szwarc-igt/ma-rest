# Chapter 31 Progressive Workbook Tasks

The Progressive Workbook tracks progressive jackpots by estimating their size daily based on meter movement.

> This feature is currently in development.

## 31.1 Enabling the Progressive Workbook

The Progressive Workbook is not enabled by default. To enable it, move "Progressive Workbook" from the available task groups to the selected task groups in the Modify User Tasks configuration.

## 31.2 Using the Progressive Workbook

When opened during the audit, the Progressive Workbook displays active progressives with estimated movement. The following fields are available:

| Field | Description |
|-------|-------------|
| Total Value | Current estimated total value of the progressive |
| Prior Total | Previous period's total value |
| Change | Change in value since prior period |
| Progressive Hit? | Indicates whether a progressive hit occurred during the period |

## 31.3 Configuring the Progressive Workbook

Progressives are managed through a configuration list.

### Adding a Progressive

The following information is required:

| Field | Description |
|-------|-------------|
| Description | Name/description of the progressive |
| Progressive Type | L = Linked, M = Manual, S = Stand Alone |
| PC-ID-Bonus | Progressive controller bonus ID |
| PC-ID-Pool ID | Progressive controller pool ID |
| Contribution % | Contribution percentage |
| Reset Value | Reset value after a progressive hit |

### Assigning Machines to a Progressive

Machines are assigned to participate in a progressive. Machine selection supports filtering by:

- Denomination
- Section
- Bank
- Manufacturer

Multiple machines can be selected at once, or all machines can be selected.

### Progressive List Columns

| Column | Description |
|--------|-------------|
| Description | Progressive name |
| Type | L (Linked), M (Manual), S (Stand Alone) |
| Contribution % | Percentage contributed per play |
| Reset Value | Value after hit |
| Max Amount | Maximum progressive amount |
| Bonus ID | Associated bonus ID |
| Pool ID | Associated pool ID |

### Editing a Progressive

Existing progressive settings can be modified.

### Deleting a Progressive

Progressives can be removed. Deletion requires confirmation.
