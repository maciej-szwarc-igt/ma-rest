# Chapter 2 Starting Machine Accounting

## 2.1 Authentication

To access Machine Accounting, the following credentials are required:

- **User Name**
- **Password**

After successful authentication, the user is prompted to select an accounting period (date).

## 2.2 Selecting the Audit Date

Upon successful login, the user selects the accounting period to work on.

Key behaviors when selecting a date:

- **Open date (available)** — Select the date to begin or continue auditing.
- **Closed date** — Select to review the period in read-only mode.
- **Re-Open** — Select a closed date and re-open it to make updates to meters and actuals.
- **Start Over** — Restarts the accounting day and resets the period tasks.

> **Warning:** Start Over resets the selected accounting day AND all subsequent days. Any previously completed work must be performed again.

## 2.3 Defining the Accounting Calendar

The accounting calendar defines the parameters that govern the fiscal calendar for Machine Accounting.

To define the accounting calendar, the following parameters must be configured:

- **Calendar Type** — The type of fiscal calendar
- **Start Date** — Must be the first day of the fiscal year
- **End of Week** — Day that ends the fiscal week
- **Years To Generate** — Number of years to generate
- **Days To Warn Before Calendar End** — Number of days before the calendar end date to display a warning

After setting the parameters, the calendar is generated. Weeks can be inserted as needed.

> A warning notice appears when the accounting calendar is near its end date. The end date is extendable for up to 10 years.

## 2.4 Changing Passwords

Users may change their own password after successfully logging in. The following information is required:

- Current password
- New password
- Confirmation of new password
