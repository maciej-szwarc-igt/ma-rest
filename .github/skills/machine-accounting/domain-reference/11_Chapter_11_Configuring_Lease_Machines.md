# Chapter 11 Configuring Lease Machines

The Lease Machines feature configures a leased machine fee structure based on meters or Machine Accounting fields. It can also be used for taxes and other fee structures.

> An accounting period must be open to modify or add a new setting.

Lease machine configuration follows this order:

1. Formula
2. Rule(s)
3. Lease settings
4. Machine assignments

### Key constraints:

- A machine can only be assigned to one setting at a time.
- A setting may have multiple machines.
- A setting may have multiple rules assigned to it.
- A rule may only be assigned to one setting.
- Each rule contains a formula, which can be created.
- Each formula can only be assigned to one rule.
- Retired machines must remain in a lease pool to maintain previous lease-participation information. Lease participation information cannot be modified after the machine is retired.

## 11.1 Lease Rules

Lease rules apply formulas to calculate lease fees. A rule is not required if the machine only uses a daily amount.

### Creating a Lease Rule

The following information is required:

- **Rule Description** — Description of the rule
- **Select Formula** — The formula to use for calculation (e.g., Meter Coin In with a percentage)
- **Percent** — The percentage to apply to the formula
- **Fixed Amount** — An amount that overrides or supplements the rule
- **Fixed Amount Behavior** — How the fixed amount is applied:
  - Fixed Amount Always Applies
  - Fixed Amount Overrides if Larger
  - Fixed Amount Overrides if Smaller
  - No Fixed Amount
- **Formula Range** — Lower and upper values determining when the formula is valid. Limits only factor in the formula-generated amount, not the fixed amount.

> Formula Range helps eliminate negative values or set up multiple percentages based on win or play.

### Configuring Formulas

Formulas are built from available meters using addition and subtraction operators.

To create a formula:

- **Formula Name** — Name of the formula
- **Available Meters** — Select meters to include in the formula
- **Operators** — Use + or - to combine meters
- **Validate** — Test the formula for correctness

### Editing Lease Rules

Existing rules can be modified, including the formula, percentage, fixed amount, and range.

### Deleting Lease Rules

Rules can be removed from a lease setting. Multiple rules can be selected for deletion simultaneously.

## 11.2 Lease Settings

A lease setting groups rules together and controls their behavior.

### Creating a Lease Setting

The following information is required:

- **Setting Name** — Name of the setting
- **Daily Lease Amount** — A fixed daily amount added to the machine's lease total
- **Daily Lease Amount Behavior**:
  - Daily Amount Overrides when Larger
  - Daily Amount Overrides when Smaller
  - No Daily Amount (disables the daily lease amount)
- **Lease Rule Behavior** — How multiple rules interact:
  - Add All Rules
  - Use Largest Rule
  - Use Smallest Rule

### Editing Lease Settings

Existing settings can be modified.

### Deleting Lease Settings

> A lease setting cannot be deleted until all rules and machines associated with it are disassociated.

## 11.3 Assigning Machines to Lease Settings

Once lease settings are established, machines can be assigned to them.

Assignment supports filtering by Section, Bank, Manufacturer, and Denomination to locate machines.

Key constraints:

- A machine can only be assigned to one lease setting at a time.
- If a machine is already assigned to a different setting, it must first be removed from that setting.
