# Chapter 4 Configuration/Options

The IGT Advantage Machine Accounting Configuration/Options window provides access to
several configurable areas of the application. Refer to the following areas for complete
information on these settings.




![Figure 4-1 IGT Advantage Machine Accounting Configuration/Options](MachineAccounting_UserGuide_images/33.2.png)




Machine Accounting divides the configuration options into the following four areas:

· Configuration-General, Casino Information, Tax Rates / W2G, Taxable Accrual, and
Passwords.

· Barcode Options-Barcode and Printer Configuration.

· FJP Options-Banned Player, FJP Configuration, and S2S Configuration.

· User Options-Settings.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="33" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->

To view the IGT Machine Accounting Configuration/Options window:

Click Options in the Quick Access Toolbar OR navigate to IGT Spade > Options. The
IGT Advantage Machine Accounting Configuration/Options window appears.


## 4.1 General Configuration Options




![](MachineAccounting_UserGuide_images/34.1.png)




Users must have permission to access Configuration/Options.

To configure the General options:

Navigate to IGT Spade > Options > General. The IGT Advantage Machine Accounting
Configuration/Options window appears.




![](MachineAccounting_UserGuide_images/34.2.png)




Period

1\. Enter the hour when the accounting day ends in the End of Period field. (This uses a 24-
hour clock. For example, 14 is 2:00 PM.)

2\. Enter the hour when the casino cage day ends in the End of Hand Pay Period field. (This
uses a 24-hour clock. For example, 14 is 2:00 PM.)

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="34" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->


### Variance

Enter the acceptable percentage of variance between the actual amount and meter values in the
following fields:

· Soft Drop (%)

· Hard Drop (%)

· Voucher Drop (%)

· Coupon Drop (%)

· CEP Drop (%)

· Jackpot ($)

· Tax Out ($)




![](MachineAccounting_UserGuide_images/35.1.png)




Any difference between metered and actual amount greater than the variance
percentage appears as a variance. Reconcile variances during the accounting
process.


### Intervals/Periods/Tolerance

A tolerance is the average daily maximum for a meter on a machine type for a gaming day.
Numbers above or below the tolerance generate a variance.

1\. Enter the time-out interval in minutes for a player card with no activity in the Abandon
Card (Minutes) field.

2\. Enter the number of days (maximum of 90) to save events for in the Clear Events (Days)
field.

3\. Enter the number of days (maximum of 90) to save meters for in the Clear Meters (Days)
field.

4\. Enter how often (in minutes) to read meters in the Meter Interval (Minutes) field.

5\. Enter the default meter tolerance in the Meter Tolerance field. Machine Accounting
generates an exception report if the meter exceeds this value.

6\. Select the Denom Tolerance Enable check-box to set a denom tolerance level in the
Maintenance Console.

7\. Enter the number of seconds an EGM can be idle before a session ends in the Uncarded
Session Timeout (Seconds) field.


### Voucher/WAT

Set the following options for cashless wager account transfers.

1\. Select one of the following options from the Voucher Machine System drop-down list to
indicate a ticket system:

· None-No ticketing system used.

· IVS-Requires the EZ Pay Ticket System to process tickets.

· Other-Another ticketing system used.

2\. Select one of the following options from the WAT System drop-down list to select a wager
account transfer (WAT) system:

· None-No WAT system used.

· EZ Pay-EZ Pay used.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="35" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->

3\. Select the WAT Import Drop-to-Drop check box to import WAT values on a drop-to-drop
basis. (Leave the check box cleared for an end-of-day to end-of-day basis.)


#### Options

1\. Select the Carded Drop check box to indicate that the casino uses carded hard/soft drop.




![](MachineAccounting_UserGuide_images/36.1.png)




i
Carded drop requires an employee to insert a card into the machine while
performing a drop.

2\. Select the Progressive Contribution Enabled check box to activate the Progressive
Contribution % field on the Update Machine window. This allows for entering an EGM's
progressive contribution.




![](MachineAccounting_UserGuide_images/36.2.png)




Ť
Progressive jackpots can create variances between the actual hold percentage and
the theo hold percentage. Variances due to progressive contributions are
eliminated, and an auditor can investigate only the true variances.

3\. Select the Manual Slip Number Edit check box to enable editing slip numbers for
manually generated handpays.

4\. Select the Group based Promotion & Demotion check box to enable group-based
promotions and demotions.

5\. Select the Sync week with month check box to indicate that the month end also ends the
current week.

6\. Select the Coupon Promo Enabled check box to enable coupon promos.

7\. Select the Cashable Electronic Promo Enabled (CEP) check box to enable cashable
electronic promos.

8\. Select the XC Reporting Matrix Enabled check box to activate the effects on the Gaming
XC Win report and enable the XCPlayPercent on the Machine Type Setup Wizard.




![](MachineAccounting_UserGuide_images/36.3.png)




i
The XC Reporting Matrix Enabled feature normalizes the hold percentages for
properties using Xtra Credit (XC) by reporting the hold factoring when using XC.
This provides properties with a view of the anticipated hold. For example, a player
receiving $5 has an anticipated spend of $50.

9\. Select the magnetic card track number used by all field attendants from the Attendant
Card Track drop-down list.

10\. Select the PAI Configuration check box to set the Permanent Asset ID (PAI). The PAI
Configuration window appears. (Jurisdiction regulations determine the availability of this
option.)




![](MachineAccounting_UserGuide_images/36.4.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="36" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->

a. Select the Enable Permanent Asset ID check box if the jurisdiction requires PAIS.

b. Select the Assign PAI Manually check box if regulators provide specific PAIs for each
machine and the ID is input manually during the add process.

c. Select the System Assigned PAI check box if the casino can assign each machine ID.
Assign a starting value in the PAI Starting Value field. The first machine is assigned
this entered value, and each subsequent machine receives the next ID in sequential
order.

d. Click OK to save the settings.


# Custom Meter Names

Use the Custom Meter Names options to define new and abbreviated meter names to appear
on the user interface. Names and abbreviations chosen for meters appear throughout the MA
application.

1\. In the Custom Meter Names options, click Custom Meter Names Setup. The
Configuration/Options window appears.

2\. Select Current or Abbreviated. The current meter names appear.




![](MachineAccounting_UserGuide_images/37.1.png)




3\. Highlight the name of the meter to change in the Default Names list, then enter the new
name in the corresponding Current Name or Short Name field. Repeat for all names to
change.

4\. Click OK. The meter names update, and the Configuration/Options window closes.


## Drop Times Setup

Use the Drop Setup options to set and configure drop times.

1\. In the Drop Setup options, select Drop Times Setup. The Drop Setup window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="37" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->




![](MachineAccounting_UserGuide_images/38.1.png)




2\. Select a previously configured drop time to edit or delete it. Click Edit to modify that drop
time setting OR click Delete to delete that drop time configuration.

3\. Click Add to add a new drop time for hard and soft drop.




![](MachineAccounting_UserGuide_images/38.2.png)




The drop time must start at least one minute prior to the end of day. If it starts at
the end of day or after the day ends, the funds will be applied to the incorrect
gaming day.




![](MachineAccounting_UserGuide_images/38.3.png)




4\. Configure the new drop time as follows:

a. Enter the Start Time and End Time for the drop.

b. Select the Drop Type that the times correspond to.

c. In the Description field, enter a name for the drop.

5\. Click OK to save the drop time configuration settings.


# Progressive Hit Event

Use the Progressive Hit Event options to configure the event codes signifying a progressive hit
event has occurred for the progressive workbook, for revenue auditing.

1\. Click Progressive Hit Event. The Select Filter Items window opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="38" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->




![](MachineAccounting_UserGuide_images/39.1.png)



2\. Select event codes to associate with progressive hit events. The following table provides
the event codes available on the Select Filter Items window. Refer to Event Codes and
Descriptions on page 1 for more information.


<table>
<tr>
<th>Event Code</th>
<th>Type</th>
<th>Description</th>
</tr>
<tr>
<td>10004500</td>
<td>BE2</td>
<td>Hopper Paid Progressive</td>
</tr>
<tr>
<td>10409600</td>
<td>Machine</td>
<td>Progressive Hit</td>
</tr>
<tr>
<td>10409700</td>
<td>Machine</td>
<td>Progressive Reset</td>
</tr>
<tr>
<td>13285200</td>
<td>Jackpot</td>
<td>Progressive Jackpot</td>
</tr>
<tr>
<td>13311200</td>
<td>Jackpot</td>
<td>Progressive Bonus Paid</td>
</tr>
<tr>
<td>13328200</td>
<td>Jackpot</td>
<td>Progressive Jackpot Pending</td>
</tr>
<tr>
<td>13328201</td>
<td>Jackpot</td>
<td>Progressive Jackpot Pending W2G Request</td>
</tr>
<tr>
<td>13328600</td>
<td>Jackpot</td>
<td>Progressive Handpay Reset</td>
</tr>
</table>


3\. Click OK. The progressive hit events update.


# Mandatory Tasks Setting

Use the Mandatory Tasks Setting window to configure the tasks required for audit completion
(tasks requiring a check mark to close the audit day).

1\. Click Mandatory Tasks Setup. The Mandatory Tasks Setting window appears.

2\. Use the arrow buttons to move tasks between All Groups and Mandatory Groups.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="39" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->




![](MachineAccounting_UserGuide_images/40.1.png)



3\. Click OK. The mandatory tasks update, and the Mandatory Tasks Setting window closes.


### Flash Report Limit

In the Flash Report Limit field, set the maximum number of reports that can be sent in
the flash reports (1-50 possible).


### Meters On Demand

Use the Meters On Demand section to set the display timing and timeout of requests and
for immediate meter reading from all machines or any active slot machine.

1\. In the Active Refresh Timer (Seconds) field, enter the interval in seconds for the display to
refresh in the Detail Meters window.

2\. In the Active Request Timeout (Minutes) field, enter the amount of time in minutes an
incomplete meter request continues polling before timing out and listing the request as
failed in the Detail Meters window.

A value of zero disables the refresh of the timeout feature.




![](MachineAccounting_UserGuide_images/40.2.png)




### Cabinet Coin In to Paytable Coin In

1\. Select Auto Adjust Paytable Coin In to set whether the system automatically
distributes differences between cabinet-level coin in and paytable coin in based on the
distribution method whenever a new period is opened.

2\. Select Auto Adjust Tolerance Amount ($) to enter the tolerance amount for
automatic adjustments.

3\. Select Adjustment Distribution Option to select the distribution method used when
adjusting paytable coin in to match cabinet coin in.

4\. Click OK to save the settings.
OR
Click Cancel to reset the fields.


### Greek Regulation

Use the Greek Regulation options to edit options related to Greek regulations.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="40" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->

1\. Click Slip Print Folder, then enter the path/URL of the slip printer.

2\. Click Greek slip text export enabled, then select Yes or No.

3\. Click Export Jackpot Slip Language Id, then enter the identification number of the
desired language.

4\. Click OK to save the settings.
OR
Click Cancel to reset the fields.


### Argentina Tax Deduction

Use the Argentina Tax Deduction options to configure the Argentina tax feature.

1\. Select Bill tax enabled to enable the bill tax feature.

2\. If needed, enter a different value in the Bill tax rate% field.




![](MachineAccounting_UserGuide_images/41.1.png)




When enabled, the bill tax rate defaults to 0.9500% but is editable to any value
between 0 to 5.0000%.

3\. Select Win tax enabled to enable the win tax feature.




![](MachineAccounting_UserGuide_images/41.2.png)




i
When enabled, the Argentina Win Tax percentage is only deducted from the cash
portion of a handpay jackpot processed at the FJP Station. The win tax is not
deducted from any portion of the jackpot returned to the player as an EZ Pay
Purchase ticket.

i
Enable the FJP Handpay Split Payment option (Options > FJPConfiguration)
to divide a single jackpot into a cash-and-purchase-ticket payment.
Refer to FJP Options on page 48 for more information.

4\. If needed, enter a different value in the Win tax rate% field.




![](MachineAccounting_UserGuide_images/41.3.png)




Ť
When enabled, the win tax rate defaults to 2.0000% but is editable to any value
between 0 and 10.0000%.

Final Step

Click OK. The settings update.


#### 4.2 Casino Information

The Casino Information options contain the casino's name and address, as well as other
pertinent information specific to the casino.

To configure Casino Information options:

1\. Navigate to IGT Spade > Options > Casino Information.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="41" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->




![](MachineAccounting_UserGuide_images/42.1.png)




2\. Enter information in the following fields:

· Casino Name

· Address

· City

· State

· Zip Code

· Phone

· Fed ID Number-Federal tax identification number for the casino

· State ID Number-State tax identification number for the casino

3\. Click OK. The settings save.


#### 4.3 Tax Rates / W2G

Set federal, state, city, and local tax rates in the Tax Rates / W2G options. Mandatory rates are
applied to players who do not furnish a Social Security identification card upon issuance of a
W2G form. Voluntary rates apply to customers providing a Social Security. Configure other
W2G parameters and legal age requirements in the in the Tax Rates / W2G options as well.

To configure Tax Rates/W2G options:

Navigate to IGT Spade > Options > Tax Rates / W2G. The Tax Rates / W2G pane opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="42" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->




![](MachineAccounting_UserGuide_images/43.1.png)




<table>
<tr>
<th colspan="9"></th>
</tr>
<tr>
<th rowspan="5"></th>
<th colspan="2">Configuration</th>
<th colspan="2">Voluntary (%)</th>
<th colspan="2">2.45</th>
<th>A</th>
<th></th>
</tr>
<tr>
<th colspan="2" rowspan="5">General Casino Information + Tax Rates / W2G Taxable Accrual Passwords Barcode</th>
<th rowspan="2"></th>
<th>☒</th>
<th>City and Local Taxes</th>
<th colspan="2"></th>
<th rowspan="2"></th>
<th></th>
</tr>
<tr>
<td></td>
<td>Mandatory (%)</td>
<td>1.55</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Voluntary (%)</td>
<td>0.95</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>☒</td>
<td>Legal Requirements</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="3"></td>
<td></td>
<td>Legal Age</td>
<td>21</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2" rowspan="2">Printer Configuration FJP</td>
<td></td>
<td>Number of ID's</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">☒ Form Printing</td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="2"></td>
<td rowspan="2"></td>
<td rowspan="2">Banned Player FJP Configuration 525 Configuration</td>
<td></td>
<td>W2G Form</td>
<td>FJP W2G_4 Part</td>
<td>¥</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>1042S Form</td>
<td>FJP 1042S</td>
<td>¥</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td colspan="2" rowspan="9">User Options Settings</td>
<td></td>
<td>Accrual W2G Form</td>
<td>FJP Accrual W2G_3 Part</td>
<td>4</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>W2G Printer</td>
<td>Microsoft XPS Document Writer</td>
<td>¥</td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="2"></td>
<td>☒</td>
<td>Settings</td>
<td></td>
<td></td>
<td>E</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Can Edit W2G Info</td>
<td>☒</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Round Up Taxes</td>
<td>☒</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Print Rounded Win on W2G Form</td>
<td>☒</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>W2G Full Cashier Name</td>
<td>☒</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Show Tax Rates in FJP Accrual Account Window</td>
<td>☒</td>
<td></td>
<td>1</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


#### Jurisdictional

1\. Select Produce Tax Forms to print a W2G form when a taxable jackpot limit is reached.

2\. Enter a jackpot limit dollar amount in the Taxable Jackpot Limit field.

3\. Enter the tax format in the Tax ID Format field.


#### Federal Taxes

1\. Enter the required federal tax percentage for a W2G issued to players not providing a
Social Security card in the Mandatory field.

2\. Enter the required federal tax percentage for a W2G issued to players providing a Social
Security card in the Voluntary field.


#### State Taxes

1\. Enter the required state tax percentage for a W2G issued to players not providing a Social
Security card in the Mandatory field.

2\. Enter the required state tax percentage for a W2G issued to players providing a Social
Security card in the Voluntary field.

3\. Enter the mandatory state tax percentage withheld when a player is not a resident of the
state in the Mandatory Non-Resident (%) field.


#### City and Local Taxes

1\. Enter the required city and local tax percentage for a W2G issued to players not providing
a Social Security card in the Mandatory field.

2\. Enter the required city and local tax percentage for a W2G issued to players providing a
Social Security card in the Voluntary field.


#### Legal Requirements

1\. Enter the legal age for gambling in the jurisdiction in which Machine Accounting operates
in the Legal Age field.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="43" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->

2\. Enter the number of additional player IDs required (beyond a Social Security number)
when a W2G is issued in the Number of ID's field.




![](MachineAccounting_UserGuide_images/44.1.png)




The IGT Advantage System automatically requests a Social Security number. For
example, two forms of ID are required if this field reads 1.


#### Form Printing

Use the Form Printing options to configure printing for the accounting department. These
settings do not affect form printing for W2G forms or printing at the FJP station.

1\. Select Standard or Custom from the following drop-down lists:

· W2G Form

· 1042 S Form

· Accrual W2G Form

2\. Select the network location of the W2G printer from the W2G Printer drop-down list.


#### Settings

1\. Select Can Edit W2G Info to allow users to edit W2G information.

2\. Select Round Up Taxes to round all tax calculations up to the nearest nickle.

3\. Select Print Rounded Win on W2G Form to round jackpot wins up to the nearest
five cents.

4\. Select Cashier Name to display the cashier's full name on tax forms.

5\. Select Show Tax Rates in FJP Taxable Accrual box to display tax rates in the FJP
Taxable Accrual window (as configured in Machine Accounting).

Final Step

Click OK. The settings save.


### 4.4 Taxable Accrual

The Taxable Accrual options provide options for associating multiple taxable events with a
single W2G tax form.




![](MachineAccounting_UserGuide_images/44.2.png)




i
Users must have the appropriate user permissions defined prior to setting the Tax
Accrual options.

To configure Taxable Accrual options:

Navigate to IGT Spade > Options > Taxable Accrual. The Taxable Accrual pane opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="44" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->




![](MachineAccounting_UserGuide_images/45.1.png)




#### Accrual Settings

Configure the following settings:

· Enable Taxable Accrual-Select to enable taxable accruals.

· Session End-Indicate the time when taxable accrual sessions end.

· Auto Re-Enroll Enable-Select to enable auto re-enrollment in taxable accrual sessions.


#### Accrual Process Thresholds

Accrual Process Thresholds determine who must enter a PIN number to accrue a taxable
jackpot and at what dollar amount. The Accrual Process Thresholds settings only apply to
patrons enrolled in taxable accrual.

Set the accrual process thresholds in dollar amounts for:

· Guest Self Serve

· Staff Only

· Guest & Staff


#### Final Step

Click OK. The taxable accrual settings save.


### 4.5 Passwords

To set parameters for password creation:
Navigate to IGT Spade > Options > Passwords. The Passwords pane opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="45" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->




![](MachineAccounting_UserGuide_images/46.1.png)




#### Password Security

1\. In Days Until Password Expires, enter the number of days required between password
changes.

2\. In Password Expire Warning (Days), enter the number of days prior to password
expiration when the user is warned.

3\. In Pin Expire Warning (Days), enter the number of warning days employees receive
before the PIN expires. Employees may change their own PIN numbers at the Attendant
Workstation.




![](MachineAccounting_UserGuide_images/46.2.png)




Setting this configuration to zero disables the feature, meaning no warning
messages are sent before the PIN expires.

4\. In Failed Login Attempts Allowed, enter the number of failed login attempts before a
user's account is locked.

5\. In Account Auto-Unlock Timeout (minutes), enter the number of minutes before a locked
account is unlocked.


#### Password Settings

1\. In Unique Password History Count, enter the number of past passwords stored and
compared before a repeated password is allowed.

2\. In Password Character Complexity Count, enter the number of character classes a
password must contain to be accepted. The character classes acceptable are: uppercase
letters (A-Z), lowercase letters (a-z), numbers (0-9), and special characters (!@#$%^&*
[]<>).

3\. In Minimum Password Length, enter the minimum number of characters required for a
valid password.


#### Final Step

Click OK. The settings save.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="46" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->


##### 4.6 Barcode Options

Use the Barcode options to configure barcode printers for printing labels.
To configure the Barcode options:

1\. Click Options in the Quick Access Toolbar OR click IGT Spade > Options.

2\. Navigate to Barcode > Printer Configuration.




![Figure 4-2 Barcode Options](MachineAccounting_UserGuide_images/47.1.png)




3\. Use the following table as a reference for configuring the Barcode settings.


<table>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
<tr>
<td colspan="2">Definition</td>
</tr>
<tr>
<td>Printer</td>
<td>Click the drop-down menu to select the printer.</td>
</tr>
<tr>
<td>Type</td>
<td>Click the drop-down menu to select the barcode type.</td>
</tr>
<tr>
<td>Orientation</td>
<td>Click the drop-down menu to select the printing orientation.</td>
</tr>
<tr>
<td colspan="2">Communication</td>
</tr>
<tr>
<td colspan="2">Consult the barcode printer documentation to enter the correct settings for the Communication section.</td>
</tr>
<tr>
<td>Com Port</td>
<td>Click the drop-down menu to select the communication com port.</td>
</tr>
<tr>
<td>Baud Rate</td>
<td>Click the drop-down menu to select the communication Baud Rate.</td>
</tr>
<tr>
<td>Parity</td>
<td>Click the drop-down menu to select the communication parity.</td>
</tr>
<tr>
<td>Data Bits</td>
<td>Enter the data bit definition for the scanner in the Data Bits field.</td>
</tr>
<tr>
<td>Stop Bits</td>
<td>Enter the stop bit definition for the scanner in the Stop Bits field.</td>
</tr>
<tr>
<td colspan="2">Position</td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="47" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->


<table>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
<tr>
<td colspan="2">Consult the barcode printer documentation to enter the correct settings in the Position section.</td>
</tr>
<tr>
<td>X Axis</td>
<td>Click to set the bar code's horizontal relative position.</td>
</tr>
<tr>
<td>Y Axis</td>
<td>Click to set the bar code's vertical relative position.</td>
</tr>
<tr>
<td>Height</td>
<td>Click to set the bar code's height.</td>
</tr>
<tr>
<td>Minimum Width</td>
<td>Click to set the bar code's minimum relative width.</td>
</tr>
<tr>
<td>Maximum Width</td>
<td>Click to set the bar code's maximum relative width.</td>
</tr>
</table>


4\. Click OK. The settings save.


##### 4.7 FJP Options

Use the FJP pane of the Options window to configure banned-player, FJP, and S2S settings.
Refer to the following steps for complete information on configuration options.


###### 4.7.1 Accessing the FJP Options

To access the FJP options:

Click Options in the Quick Access Toolbar OR navigate to IGT Spade > Options > FJP. The
FJP option categories appear on the left pane.


###### 4.7.2 Banned Player Options

Access the Banned Player pane to set banned-player options and permissions.




![](MachineAccounting_UserGuide_images/48.1.png)




Ť
Users must have the appropriate user permissions defined prior to setting the
Banned Player options.

To configure the Banned Player settings:

1\. Click Options in the Quick Access Toolbar OR navigate to IGT Spade > Options > FJP
\> Banned Player. The Banned Player pane opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="48" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->




![](MachineAccounting_UserGuide_images/49.1.png)




2\. Configure the Banned Player settings. The following table lists and describes each setting.


<table>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
<tr>
<td colspan="2">Banned Player</td>
</tr>
<tr>
<td>Enable Banned Player Checking</td>
<td>Select to enable banned player checking.</td>
</tr>
<tr>
<td>Allow Handpay Transaction Payment</td>
<td>Select to allow handpay transaction payments. 0 1 Permissions are required to process payments.</td>
</tr>
<tr>
<td colspan="2">Workstation Notification</td>
</tr>
<tr>
<td>Message Displayed at the Workstation</td>
<td>Enter the message to display at the workstation when a player is identified.</td>
</tr>
<tr>
<td>Display Card# With Message</td>
<td>Select to display the player's card number with the notification message at the FJP station.</td>
</tr>
<tr>
<td>Uncarded Player Verification</td>
<td></td>
</tr>
<tr>
<td>Level of Control</td>
<td>Select a level of control for uncarded player verification. O 1 This setting determines when banned player checking is required.</td>
</tr>
<tr>
<td>Verification Required</td>
<td>Select to require the attendant to search for the patron's status once at the FJP station. Leaving this option cleared allows the attendant to cancel the search.</td>
</tr>
</table>

3\. Click OK. The FJP configuration settings update.


###### 4.7.3 FJP Configuration Options

The FJP Configuration options are used to configure timer settings, limit settings, slip
sequences, and the max fill counts for fills and jackpots.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="49" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->


# To configure the FJP Configuration options:

1\. Click Options in the Quick Access Toolbar OR navigate to IGT Spade > Options >
FJP > FJP Configuration. The FJP Configuration options appear.




![Figure 4-3 FJP Configuration Pane (Top)](MachineAccounting_UserGuide_images/50.1.png)






![Figure 4-4 FJP Configuration Pane (Bottom)](MachineAccounting_UserGuide_images/50.2.png)




2\. Configure the FJP Configuration settings. The following table lists and describes each
setting.

<!-- PageNumber="50" -->
<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->


<table>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
<tr>
<td>General</td>
<td></td>
</tr>
<tr>
<td>Input Manual Handpay Date</td>
<td>Select Y to display Event Date menus on the Create New Entry window.</td>
</tr>
<tr>
<td>Timer Settings</td>
<td></td>
</tr>
<tr>
<td>Completed Event Timeout (Hours)</td>
<td>Number of hours a completed event is available to be voided.</td>
</tr>
<tr>
<td>Max Paged/Pending Event Life (Hours)</td>
<td>Number of hours any non-completed event (except pouch pays) remains on the system before it is removed. Default is 6 (six hours).</td>
</tr>
<tr>
<td>Max Pouch Pay Life (Days)</td>
<td>Number of days pouch pay events remain on the system before being removed. Default is 2 (two days).</td>
</tr>
<tr>
<td>Witness Timeout (Minutes)</td>
<td>Number of minutes the FJP system displays the AWAITING WITNESS RETURN scrolling message on EGMs for FJP events requiring a witness. 1 If no witness event is received from this machine in the number of configured minutes, the system clears the EGM, and the FJP event is completed as a non-witnessed event. The default value is 30 (30 minutes).</td>
</tr>
<tr>
<td>Limit Settings</td>
<td></td>
</tr>
<tr>
<td>Executive Limit ($)</td>
<td>The maximum award attendants can redeem without executive approval.</td>
</tr>
<tr>
<td>No-Witness Limit ($)</td>
<td>The maximum award attendants can redeem.</td>
</tr>
<tr>
<td>FJP Handpay Enable Split</td>
<td>Allows handpays comprising different pay types (for example, a purchase ticket AND cash for a single handpay).</td>
</tr>
<tr>
<td>Key to Credit Limit ($)</td>
<td>Maximum dollar amount that attendants can apply from a handpay back to the credit meter.</td>
</tr>
<tr>
<td>Key to Credit Limit High-Limit Limit ($)</td>
<td>Maximum dollar amount that attendants can apply from a handpay back to the credit meter.</td>
</tr>
<tr>
<td>FJP Slip Sequence</td>
<td></td>
</tr>
<tr>
<td>By Event</td>
<td>If selected, FJP uses a slip number sequence by event type (Jackpot, Fill, Aux fill). Usable in conjunction with FJP Slip Sequence By Booth.</td>
</tr>
<tr>
<td>By Booth</td>
<td>If selected, FJP uses a slip number sequence by booth number.</td>
</tr>
<tr>
<td colspan="2">Max Fill Count</td>
</tr>
<tr>
<td>Enable</td>
<td>Check Enable in the Max Fill Count section to have the FJP System track fill counts on machines.</td>
</tr>
<tr>
<td>Max Allowed Fill Count (Fills)</td>
<td>Number of fills within a 24-hour period on each machine that is acceptable. Any machine needing more than the set number requires a supervisor override to complete.</td>
</tr>
<tr>
<td>Fill Count Rollover Hour (24 Hour)</td>
<td>Maximum number of fills before alert is issued.</td>
</tr>
<tr>
<td>Ticket Reprint</td>
<td></td>
</tr>
<tr>
<td>Max Allowed Reprints</td>
<td>Maximum number of reprints allowed for a single FJP event of completed status.</td>
</tr>
<tr>
<td>Max Hours to Reprint</td>
<td>Maximum number of hours that an FJP slip can be reprinted.</td>
</tr>
<tr>
<td colspan="2">Marker Trax Integration</td>
</tr>
<tr>
<td>Enable Marker Trax Integration with FJP</td>
<td>Select the check-box to enable/disable Marker Trax with the FJP system. Refer to the FJP 9.7.5 User Guide (document number 90-210473-XX) for more information.</td>
</tr>
</table>


3\. Click OK. The FJP configuration settings update.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="51" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->


## 4.7.4 S2S Configuration Options

The S2S Configuration pane defines options for system-to-system (S2S) fills and jackpot
workstations.




![](MachineAccounting_UserGuide_images/52.1.png)




Configure the following options in the CWS for a SAS floor.


### To configure the S2S FJP Configuration window:

1\. Click Options in the Quick Access Toolbar OR navigate to IGT Spade > Options > FJP
\> S2S Configuration. The S2S Configuration pane opens.




![](MachineAccounting_UserGuide_images/52.2.png)




2\. Configure the S2S Configuration settings. The following table lists and describes each
setting.


<table>
<tr>
<th>Field</th>
<th colspan="2">Description</th>
</tr>
<tr>
<td>Enable/Disable</td>
<td colspan="2"></td>
</tr>
<tr>
<td>Enable Balance with Cage - Verify All</td>
<td rowspan="9">Select to enable.</td>
<td rowspan="8"></td>
</tr>
<tr>
<td>Enable Pouch Pay</td>
</tr>
<tr>
<td>Enable Hand Pay</td>
</tr>
<tr>
<td>Enable Hopper Fills</td>
</tr>
<tr>
<td>Enable Aux Fills</td>
</tr>
<tr>
<td>Enable Pouch Pay for Jackpots</td>
</tr>
<tr>
<td>Enable Pouch Pay for Cancel Credits</td>
</tr>
<tr>
<td>Enable Pouch Pay for Progressives</td>
</tr>
<tr>
<td>Enable Pouch Pay for Bonuses</td>
<td></td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="52" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->


<table>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
<tr>
<td colspan="2">Limits</td>
</tr>
<tr>
<td>Max Pouch Pay ($)</td>
<td rowspan="9">Enter a numeric value.</td>
</tr>
<tr>
<td>Jackpot Display Limit</td>
</tr>
<tr>
<td>Bonus Display Limit</td>
</tr>
<tr>
<td>Maximum Fill Bags</td>
</tr>
<tr>
<td>Pouch Pay Witness Floor Limit</td>
</tr>
<tr>
<td>Hand Pay Witness Floor Limit</td>
</tr>
<tr>
<td>Hopper Fill Witness Floor Limit</td>
</tr>
<tr>
<td>Aux Fill Witness Floor Limit</td>
</tr>
<tr>
<td>PIN Configuration</td>
</tr>
<tr>
<td>PIN required to enter attendant menu</td>
<td rowspan="5">Select to enable.</td>
</tr>
<tr>
<td>PIN required to process a handpay</td>
</tr>
<tr>
<td>PIN required to process a pouchpay</td>
</tr>
<tr>
<td>PIN required to process a fill</td>
</tr>
<tr>
<td>PIN required to sign off a witness</td>
</tr>
<tr>
<td>Supervisor Settings</td>
<td></td>
</tr>
<tr>
<td>Required for change in fill amount</td>
<td rowspan="5">Select to enable.</td>
</tr>
<tr>
<td>Required for a change to a handpay</td>
</tr>
<tr>
<td>Required to process manual handpays</td>
</tr>
<tr>
<td>Required for any witness event</td>
</tr>
<tr>
<td>Witness Configuration</td>
</tr>
<tr>
<td>Pouch Pay Witness</td>
<td rowspan="5">Select one of the following options: Not Required, Always Required, Greater than No Witness Limit, or Greater than Pouch Pay Floor Witness Limit.</td>
</tr>
<tr>
<td>Hand Pay Witness</td>
</tr>
<tr>
<td>Hopper Fill Witness</td>
</tr>
<tr>
<td>Aux Fill Witness</td>
</tr>
<tr>
<td>Mask Limit Configuration 0 Ť Determines how limits are applied to each group.</td>
</tr>
<tr>
<td>Attendant Mask Limit</td>
<td rowspan="3">Select one of the following options: Ignore Mask Limit, Money Enabled for Mask Limit, Enforce Mask Limit as Witness, or Enforce Mask Limit at Game (no menu if over mask limit).</td>
</tr>
<tr>
<td>Supervisor Mask Limit</td>
</tr>
<tr>
<td>Non-Cash Win Witness Configuration</td>
</tr>
<tr>
<td>Non-Cash (Zero) Progressives</td>
<td rowspan="3">Select one of the following options: No Witness, Witness Required, or Supervisor Required.</td>
</tr>
<tr>
<td>Non-Cash (Zero) Bonus</td>
</tr>
<tr>
<td>Non-Cash (Zero) Jackpot</td>
</tr>
</table>


3\. Click OK. The FJP configuration settings update.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="53" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 4 Configuration/Options" -->


## 4.8 User Options

Use the User Options pane to set the color configurations of the active field and text color, and
to set the computer clock.


### To configure the User Options:

1\. Click Options in the Quick Access Toolbar OR navigate to IGT Spade > Options >
User Options > Settings. The Settings pane appears.




![](MachineAccounting_UserGuide_images/54.1.png)




2\. Click ... ... in the Background field. The Color window appears. Select the desired color
for the active field, then click OK.

3\. Click ... ... in the Text field. The Color window appears. Select the desired color for the
active text, then click OK.

4\. Select Display Clock on Status Bar to display the time on the status bar.

Ť
O
The MA terminal requires a restart for the Display Clock on Status Bar setting to
take effect.




![](MachineAccounting_UserGuide_images/54.2.png)




5\. Select Correct Meter Variance - Warn on accept to display a confirmation window
when accepting a variance.

6\. Select Correct Meter Variance - Warn on use suggested to display a window when
using a suggested value.

7\. Click OK. The User Options settings update.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="54" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/55.1.png)




