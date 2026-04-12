# Chapter 7 Maintenance Workbook

Machine Accounting maintains detailed information on the location and configuration of casino machines. Once machines are added to the system, the following operations are available:

- View the locations of all machines
- Change a machine's information
- Test machine meters against actually deposited coins/bills
- View individual or groups of machines using system criteria over a selectable time range
- Set up, define, and assign machines to drop zones

> If the Machine Accounting system is connected to the IGT sbX system, the serial numbers of all enrolled machines in Machine Accounting must match the cabinet serial numbers in the IGT sbX system.

## 7.1 Machine Wizard Overview

The Machine Wizard provides the following operations:

| Function | Description |
|----------|-------------|
| Verify a Machine Add, Retire or Move | Verify a machine's addition, move, or retirement within the audit process |
| Update a Machine | Change a machine's non-critical configuration (changes that do not affect accounting data) |
| Add a New Machine | Add a new machine to the casino floor |
| Convert a Machine | Change the denomination, game type, or type code. Any change affecting accounting data must use this option. Requires a new machine (house) number. |
| Retire a Machine | Remove a machine from the casino floor |
| Change a Machine's Location | Move a machine to a different floor location |
| Reset a Machine's Unique ID/EGM ID | Change a machine's wiring harness and reset its unique ID (e.g., due to communication failure or harness update) |

> Verifying machine changes is an audit function and a part of the user task tree that must be completed daily.

## 7.2 Adding New Machines

To add a new machine, the following information is required:

### Machine Type Configuration (Page 1)

| Field | Description |
|-------|-------------|
| Denomination | Accounting denomination. Select an existing denomination or add a new one. Optionally select a matching Type ID from the existing database. |
| Manufacturer | Machine manufacturer. Select existing or add a new one. |
| Description | Description of the machine. Auto-populates when selecting an existing Type ID. For variance machines, use "Variance". |
| Hold Percent | Theoretical hold percentage. Convert from payout percentage if needed (e.g., 100% - 94.32% = 5.68%). |
| Vouchers | No Voucher Printer, Voucher Out Only, or Voucher In/Voucher Out. Voucher In/Out requires enhanced machine configuration by slot maintenance. |
| Capture WAT Meters | Whether WAT is enabled on the machine |

### Machine Details (Page 2)

| Field | Description |
|-------|-------------|
| Machine # | Unique machine number (auto-generated or manually entered within the denomination's range) |
| EGM ID | MAC address for server-based games (self-populates) |
| Purchase Date | Date the machine was purchased or leased |
| Section Name | Floor section for the machine location (select existing or add new) |
| Bank | Bank number for the machine |
| Location | Position number within the bank |
| Serial # | Manufacturer serial number |
| Cabinet Type | Cabinet type (select existing or add new) |
| Give Aways | Special giveaway promotions connected to the machine |
| Model | Description or identification number for the game |
| Aux Print Loc | Auxiliary print location number (if applicable) |
| G/L Code | General ledger code |
| Seal # | Seal number |
| Govt. Stamp | Government- or state-assigned number |
| Bags Per Fill | Number of coin bags used to fill the hopper |
| Max Bags in Aux Fill | Maximum bags allowed in auxiliary fill |
| Hopper Level Adjustment | Value to adjust hopper from standard fill to established requirements |
| Hopper Variance Limit | Whole dollar amount to signal an error on fill |
| Progressive Contribution % | Progressive contribution percentage (if enabled at the property) |
| EPROM(s) | EPROM identifiers; can add, activate, or deactivate EPROMs |
| Bill Validator | Whether the machine has a bill validator |
| Player Tracking | Whether player tracking is enabled |
| Manual Meters | Whether meters are read manually (not via BE2) |
| Use MGA Legacy Key | Avoids duplicate paytables for SAS 6 or older machines |
| Lab Game | Whether the machine is for lab use or X-Series game |
| VIP Game | Whether the machine is designated as VIP for reporting |

> If the Machine Accounting system is connected to IGT sbX, asset numbers are automatically enrolled within the sbX system.

After machine setup, a summary is generated. A barcode label can be printed for the machine, and a Machine Work Order is generated.

## 7.3 Updating Machines

To update an existing machine's non-critical configuration:

1. Select the machine to update.
2. Modify the applicable fields from the same field set used during machine creation.
3. Review the summary for accuracy.
4. A new barcode label can be printed.

> Updates are for non-critical changes that do not affect accounting data. For changes affecting accounting data (denomination, game type, type code), use the Convert operation instead.

## 7.4 Converting Machines

Converting a machine involves retiring the existing machine and adding it back as a new machine with a different type code. The process:

1. Select the machine to convert.
2. Modify the machine type fields (denomination, game type, type code, etc.).
3. A new machine number is automatically assigned (next available for the denomination), or a specific number can be entered.
4. Review the summary and print labels.
5. A work order is generated for slot technicians.

> New values entered during conversion may be modified further.

## 7.5 Retiring Machines

Prior to a machine being removed from the floor, machine meters must be read one final time. To ensure this:

1. Turn off the machine and remove it from OL (online).
2. Turn it back on as "Out of Service" to take the final meter snapshot.
3. Select the machine to retire.
4. Review and confirm the retirement.
5. A work order is generated.

> Retire machines only after soft and hard drops are complete to allow the machine to make a final drop.

## 7.6 Changing Machine Location

To move a machine to a different floor location:

1. Select the machine to move.
2. Specify the new location details (Section, Bank, Location).
3. Review and confirm the move.
4. A work order is generated.

## 7.7 Resetting Machine Unique ID / EGM ID

To reset a machine's wiring harness and unique ID (typically due to communication failure or harness update):

1. Select the machine.
2. The unique ID is reset.
3. The machine re-establishes communication with the new harness.

## 7.8 Machine Detail

Summarizes current information for active and warehoused machines.

## 7.9 Detail Meters

Summarizes period meter information for active and warehoused machines.

## 7.10 Current Meters

Summarizes current information as of the earliest opened accounting period for active and warehoused machines.

## 7.11 MGA Meters

Summarizes information about current meters for the paytable ID (Multi-Game Accounting).

## 7.12 Print Label

Prints barcode labels for machine identification.

## 7.13 Print Work Order

Prints a work order for retiring or moving a machine.
