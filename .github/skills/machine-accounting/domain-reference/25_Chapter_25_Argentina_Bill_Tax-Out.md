# Chapter 25 Argentina Bill Tax-Out

The Argentina Bill Tax-Out feature is specific to Argentina jurisdictions and handles bill tax-out auditing.

> This feature's configuration is set during installation (mandatory vs. non-mandatory) via the Argentina Tax Deduction settings in the General Configuration options.

The following tasks are available:

| Task | Description |
|------|-------------|
| Import Bill TaxOut Information | Retrieves and displays bill tax-out data |
| Audit Bill TaxOut Meters | View and resolve meter vs. actual bill tax-out variances |

## 25.1 Importing Bill Tax-Out Information

The import process retrieves bill tax-out data into the system for audit.

## 25.2 Auditing Bill Tax-Out Meters

The audit display includes the following columns:

- Mnum (Machine Number)
- Location
- Denomination
- Meter Bill Taxout
- Actual Bill Taxout
- Variance
- Percent
- Accepted status
- Comment
- Previous Variance

Data can be filtered to show All Machines or only Exceptions.

### Adjusting Actuals

For each machine with a variance, the actual bill tax-out amount can be corrected.

### Adjusting Meters

Meter bill tax-out values can be adjusted for individual machines by entering the adjustment amount.

### Adding Comments

Comments can be added when accepting or adjusting variances. Comments can be selected from a predefined list or entered as free text.

### Accepting Variances

Variances within established guidelines can be accepted.
