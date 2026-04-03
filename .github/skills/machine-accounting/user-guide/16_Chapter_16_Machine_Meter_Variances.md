# Chapter 16 Machine Meter Variances

The Machine Meters Variance window displays machines eith deltas that exceed defined
machine tolerances or with a negative meter value. A tolerance is the average daily maximum
for a meter on a machine type for a gaming day. Numbers above or below the tolerance
generate a variance.

Any variances must be investigated and corrected, or accepted. Variances over the defined
machine tolerances may be correct due to unusual play at the machine.

Machine variances may occur for the following reasons:

· Runaway meters-A problem with the machine meters.

· Rollover meters-A meter reaches the highest number of digits and resets to zero.

· Over tolerance-Meter delta is over the tolerance level set in the system.

· RAM clear-A procedure performed by a slot technician at the machine resets the
meters.

· Misapplied voucher meters-A voucher machine is configured incorrectly.

· Variance between the game total coin in and the cabinet to paytable coin in-
Commonly referred to as redline.




![Figure 16-1 User Tasks List-Correct Meter Variances Task](MachineAccounting_UserGuide_images/203.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="203" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->


## 16.1 Viewing Meter Variances

Meter variances on machines listed on the Machine Meter Variance window must be either
accepted or edited before the period audit closes. A tolerance is the average daily maximum for
a meter on a machine type for a gaming day. Numbers above or below the tolerance generate a
variance.

To view machines with a meter variance:

Click Correct Meter Variances in the User Tasks list. The Correct Meter Variances window
opens.




![](MachineAccounting_UserGuide_images/204.1.png)




Machines are automatically grouped by variance reason. Click and drag the
reason, description, or manufacturer columns to change the grouping.




![Figure 16-2 Correct Meter Variances](MachineAccounting_UserGuide_images/204.2.png)




The Correct Meter Variances window groups variances by the following reasons:


<table>
<tr>
<th>Variance</th>
<th>Reasons to Replace Types</th>
</tr>
<tr>
<td>Over Tolerance</td>
<td>Numbers that are either over or under the average daily maximum meter amount for the gaming day on a machine type.</td>
</tr>
<tr>
<td>Negative</td>
<td>Items appear in this category when a meter rolls over on a machine, causing a negative variance, unless the machine is also in the RAM Clear or AI Download category.</td>
</tr>
<tr>
<td>RAM Clear</td>
<td>A calculated category based on whether at least 50% of the meters for a non-SAS machine went negative. A machine does not appear in the negative category if it falls in this category.</td>
</tr>
<tr>
<td>AI Download</td>
<td>A calculated category based on whether at least 50% of the meters for an SAS machine went negative. A machine does not appear in the negative category if it falls in this category.</td>
</tr>
</table>


## 16.2 Adjusting Meter Variances

A meter variance may occur for several reasons. Audit departments are responsible for
resolving meter variances, regardless of the reason for the variance. Note the following about
adjusting meter variances:

· All variances should be researched and correctly adjusted rather than simply accepting
or entering the suggested system entries.

· Enter plus (+) or minus (-) in front of the change to enter a change without overwriting

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="204" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->

the existing value. For example, enter 50 to make the new value 50. Enter +50 to add
50 to the current value.


## To adjust meter variances:

1\. Click Correct Meter Variances in the User Tasks list. The Correct Meter Variances
window displays.




![](MachineAccounting_UserGuide_images/205.1.png)




2\. Click Exceptions to display the machines with meter exceptions.
OR
Click Show All to display all machines (including those with exceptions).

3\. Do one of the following:

· Click Reason to sort the reasons in ascending/descending order. (Variances are
grouped by reason by default.)

· Locate a specific machine by typing the machine ID in the Enter filter text here field.

· Select All or Meters with Variances from the Meter Filter list.

4\. Select the machine(s) and click View Meters OR double-click a machine. The Meter
Variances for Machine window appears.




![](MachineAccounting_UserGuide_images/205.2.png)




1
The Next Machine button is enabled if multiple machines are selected.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="205" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->




![](MachineAccounting_UserGuide_images/206.1.png)




<table>
<tr>
<th colspan="9"></th>
</tr>
<tr>
<th>Meter Filter All</th>
<th>V</th>
<th colspan="2">Machine Details</th>
<th>Events</th>
<th colspan="3">Current Meters</th>
<th>Tolerances</th>
</tr>
<tr>
<th></th>
<th></th>
<th rowspan="2">Today's Meter</th>
<th rowspan="2">Today's Value</th>
<th rowspan="2">Tolerance</th>
<th></th>
<th></th>
<th></th>
<th>Edit Coin In</th>
</tr>
<tr>
<th>Meter</th>
<th>Prior Meter</th>
<th>Variance</th>
<th colspan="2">Suggeste A</th>
<th rowspan="2">Accept/Unaccept</th>
</tr>
<tr>
<td>Coin In</td>
<td>9</td>
<td>9999999</td>
<td>788888.00</td>
<td>10001.00</td>
<td>778887.00</td>
<td>0.0</td>
<td></td>
</tr>
<tr>
<td>Coin Out</td>
<td>9</td>
<td>9999999</td>
<td>98989.00</td>
<td>10001.00</td>
<td>88988.00</td>
<td>0.0</td>
<td rowspan="2"></td>
<td rowspan="2">Calculate Meters</td>
</tr>
<tr>
<td>Legacy Coin Out</td>
<td>9</td>
<td>9999999</td>
<td>99999.90</td>
<td>10001.00</td>
<td>89998.90</td>
<td>O.C</td>
</tr>
<tr>
<td>Games</td>
<td>9</td>
<td>9999999</td>
<td>9999990</td>
<td>10001</td>
<td>9989989</td>
<td></td>
<td></td>
<td rowspan="2">Edit</td>
</tr>
<tr>
<td>Total Drop</td>
<td>169218</td>
<td>188019981198</td>
<td>1880198119.80</td>
<td>10001.00</td>
<td>1880188118.80</td>
<td>0.0</td>
<td></td>
</tr>
<tr>
<td>$1</td>
<td>9</td>
<td>9999999</td>
<td>9999990</td>
<td>10001</td>
<td>9989989</td>
<td></td>
<td>E</td>
<td rowspan="7"></td>
</tr>
<tr>
<td>$2</td>
<td>9</td>
<td>9999999</td>
<td>9999990</td>
<td>10001</td>
<td>9989989</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$5</td>
<td>9</td>
<td>9999999</td>
<td>9999990</td>
<td>10001</td>
<td>9989989</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$10</td>
<td>9</td>
<td>9999999</td>
<td>9999990</td>
<td>10001</td>
<td>9989989</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$ 20</td>
<td>9</td>
<td>9999999</td>
<td>9999990</td>
<td>10001</td>
<td>9989989</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$50</td>
<td>9</td>
<td>9999999</td>
<td>9999990</td>
<td>10001</td>
<td>9989989</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$ 100</td>
<td>9</td>
<td>9999999</td>
<td>9999990</td>
<td>10001</td>
<td>9989989</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bill In</td>
<td>169200</td>
<td>187999981200</td>
<td>1879998120.00</td>
<td>10001.00</td>
<td>1879988119.00</td>
<td>0.0</td>
<td></td>
<td rowspan="2"></td>
</tr>
<tr>
<td>Attendant Paid Cancelled Credits</td>
<td>9</td>
<td>9999999</td>
<td>99999.90</td>
<td>10001.00</td>
<td>89998.90</td>
<td>O.C</td>
<td></td>
</tr>
<tr>
<td>Attendant Paid External Bonus Payout</td>
<td>9</td>
<td>9999999</td>
<td>99999.90</td>
<td>10001.00</td>
<td>89998.90</td>
<td>O.C</td>
<td></td>
<td rowspan="4"></td>
</tr>
<tr>
<td>Attendant Paid Jackpots</td>
<td>9</td>
<td>9999999</td>
<td>99999.90</td>
<td>10001.00</td>
<td>89998.90</td>
<td colspan="2">O.C</td>
</tr>
<tr>
<td>Attendant Paid Progressive Payout</td>
<td>9</td>
<td>9999999</td>
<td>100000.90</td>
<td>10001.00</td>
<td>89999.90</td>
<td colspan="2">0.0</td>
</tr>
<tr>
<td>Machine Paid External Bonus Payout</td>
<td>9</td>
<td>9999999</td>
<td>99999.90</td>
<td>10001.00</td>
<td>89998.90</td>
<td colspan="2">O.C</td>
</tr>
<tr>
<td>Machine Paid Progressive Payout</td>
<td>0</td>
<td>0</td>
<td>0.00</td>
<td>10001.00</td>
<td>0.00</td>
<td>0.0</td>
<td></td>
<td rowspan="2"></td>
</tr>
<tr>
<td>Bonus</td>
<td>9</td>
<td>9999999</td>
<td>99999.90</td>
<td>10001.00</td>
<td>89998.90</td>
<td colspan="2">O.C</td>
</tr>
<tr>
<td>Point Play</td>
<td>9</td>
<td>9999999</td>
<td>99999.90</td>
<td>10001.00</td>
<td>89998.90</td>
<td colspan="2">0.0</td>
<td>Next Machine</td>
</tr>
<tr>
<td>Legacy Point Play</td>
<td>9</td>
<td>9999999</td>
<td>99999.90</td>
<td>10001.00</td>
<td>89998.90</td>
<td colspan="2">0.0</td>
<td rowspan="2">Done</td>
</tr>
<tr>
<td>Coin Drop</td>
<td>9</td>
<td>9999999</td>
<td>99999.90</td>
<td>0.00</td>
<td>0.00</td>
<td colspan="2">O.C V</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</table>




![](MachineAccounting_UserGuide_images/206.2.png)




Right-click on the selected machine(s) and select Export to Excel to export data to
Microsoft Excel®.

5\. Perform any of the following:

· Click the Today's Value column to enter a value.

. If the value in the Suggested column is blue, click it to auto-populate the Today's
Value column. (Do this only AFTER verifying the Today's Value number following
standard auditing processes for checking variances.)




![](MachineAccounting_UserGuide_images/206.3.png)




· Double-click a line item.

· Select a line item and click Edit. The Meter Adjustment for Machine window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="206" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->




![](MachineAccounting_UserGuide_images/207.1.png)




a. Enter the meter value in the Adjustment field.

b. Click Save. The meter adjustment saves.

c. Click Done. The Meter Variances for Machine window reappears.

6\. Click Done. The adjustments save.


### 16.2.1 Viewing Machine Details

To view machine details:

1\. Select a machine on the Meter Variances for Machine window.

2\. Click Machine Details. The Machine Record for Machine window appears.




![](MachineAccounting_UserGuide_images/207.2.png)



3\. If selecting multiple machines, click Next. The next machine's details appear.

4\. Click Done to return to the Meter Variances for Machine window.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="207" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->


### 16.2.2 Viewing Events and Meters

An event is something that happens at the machine, such as a jackpot or a door open. Each
event is assigned an event code. Refer to Event Codes and Descriptions on page 331 for more
information.


#### To view events and meters:

1\. Select a machine on the Meter Variances for Machine window.

2\. Select Events or Meters. The Machine Events window shows the selected type of
machine events.

3\. Enter applicable information in the Start/End Date, Machine, Event Code, Staff ID,
and/or Player ID fields. The machine events meeting the filters appear.




![](MachineAccounting_UserGuide_images/208.1.png)




4\. Click OK. The Meter Variances for Machine window reappears.


### 16.2.3 Viewing Current Meters

To view current meters:

1\. Select a machine on the Meter Variances for Machine window.

2\. Click Current Meters. The Current Meters for Machine window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="208" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->


<table>
<tr>
<th>Denom:</th>
<th>[0.01</th>
<th>Manufacturer: IGT</th>
</tr>
<tr>
<td>Meter Denom:</td>
<td>0.01</td>
<td></td>
</tr>
<tr>
<td rowspan="2">Description:</td>
<td>AVP</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</table>




![](MachineAccounting_UserGuide_images/209.1.png)




<table>
<tr>
<th>Meter Date</th>
<th>Meter Type</th>
<th>Physical Coin In</th>
<th>Physical Coin Out</th>
<th>Coin In</th>
<th>Legacy Coin Out</th>
<th>G</th>
<th>A</th>
</tr>
<tr>
<td>June 14 2010 00:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td>=</td>
</tr>
<tr>
<td>June 14 2010 00:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 00:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 01:00:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 01:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 01:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 01:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 02:00:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 02:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 02:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 02:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 03:00:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 03:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 03:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 03:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 04:00:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 04:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 04:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 04:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 05:00:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 05:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td></td>
</tr>
<tr>
<td>June 14 2010 05:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
<td>V</td>
</tr>
<tr>
<td>‹ IIII</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>&gt;</td>
<td></td>
</tr>
</table>


3\. Click OK. The Meter Variances for Machine window reappears.


### 16.2.4 Viewing Tolerances

A tolerance is the average daily maximum for a meter on a machine type for a gaming day.
Numbers above or below the tolerance generate a variance. Only adjust the tolerance for a
machine type if the variance that occurs (high or low) is consistent over a time period (for
example, too low for at least a week).

To view tolerances:

1\. Click Tolerances on the Meter Variances for Machine window. The Machine Type Setup
Wizard appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="209" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->




![](MachineAccounting_UserGuide_images/210.1.png)




## 2. Click Next. The Meter Tolerance Values pane appears.




![](MachineAccounting_UserGuide_images/210.2.png)




<table>
<tr>
<th>Meter Name</th>
<th>Tolerance Value</th>
<th>1</th>
</tr>
<tr>
<td>Physical Coin In</td>
<td>50000</td>
<td rowspan="4">E</td>
</tr>
<tr>
<td>Physical Coin Out</td>
<td>50000</td>
</tr>
<tr>
<td>Coin In</td>
<td>50000</td>
</tr>
<tr>
<td>Legacy Coin Out</td>
<td>50000</td>
</tr>
<tr>
<td>Games</td>
<td>50000</td>
<td rowspan="10">4</td>
</tr>
<tr>
<td>Total Drop</td>
<td>50000</td>
</tr>
<tr>
<td>Total Bills</td>
<td>50000</td>
</tr>
<tr>
<td>Attendant Paid Jackpots</td>
<td>50000</td>
</tr>
<tr>
<td>Attendant Paid Credits</td>
<td>50000</td>
</tr>
<tr>
<td>Attendant Paid Progressive</td>
<td>50000</td>
</tr>
<tr>
<td>Non-cashable EFT</td>
<td>50000</td>
</tr>
<tr>
<td>Machine Paid Ext Bonus</td>
<td>50000</td>
</tr>
<tr>
<td>Point Play</td>
<td>50000</td>
</tr>
<tr>
<td>Legacy Point Play</td>
<td>50000 PARAR</td>
</tr>
</table>


3\. Click Finish. The Machine Type Setup Wizard window closes.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="210" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->


## 16.3 Accepting Meter Variances

If a meter variance is deemed acceptable, it can be easily accepted for that accounting period.
An example is if the machine is over tolerance for that period only. If accepted, it can also be
unaccepted easily.

To accept a meter variance for a single machine:

1\. Click Correct Meter Variances in the User Tasks list. The Correct Meter Variances
window appears.

2\. Click Exceptions to display the machines with meter exceptions.

OR
Click Show All to display all machines (including those with meter exceptions).

3\. Double-on a single machine, then click View Meters.

4\. Select a meter variance that has not been accepted.

5\. Click Accept/Unaccept if the variance is within established guidelines. A confirmation
prompt appears.

6\. Click Yes. The variance is accepted.

To undo an accept of a meter variance for a single machine:

1\. Click Correct Meter Variances in the User Tasks list. The Correct Meter Variances
window appears.

2\. Click Exceptions to display the machines with meter exceptions.

OR
Click Show All to display all machines (including those with meter exceptions).

3\. Double-click a single machine, then click View Meters.

4\. Select a meter variance that has been accepted.

5\. Click Accept/Unaccept. A confirmation prompt appears.

6\. Click Yes. The variance is no longer accepted.


## 16.4 Editing Coin In

If there is a difference between the total coin in for the game and the individual paytable coin
in for the game, it must be accepted, unaccepted, or edited as with all paytable variances.
Follow the instructions below to edit the coin in for a game.

To edit coin in:

1\. Click Correct Meter Variances in the User Tasks list. The Correct Meter Variances
window appears.

2\. Click Exceptions to display the machines with meter exceptions.
OR
Click Show All to display all the machines, including Exceptions.

3\. Select the appropriate machine(s), then click View Meters OR double-click on a
machine. The Meter Variances for Machine window appears.




![](MachineAccounting_UserGuide_images/211.1.png)




If multiple machines are selected, the Next Machine button is enabled.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="211" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->

4\. If a red X appears in the Edit Coin In icon, click it. The Paytable Coin In Meter
Variances for Machine window appears.




![](MachineAccounting_UserGuide_images/212.1.png)




<table>
<tr>
<th colspan="3">Total Coin In: 0.00</th>
<th colspan="5">Paytables Total Coin In: 5.00</th>
<th>Difference:</th>
<th>-5.00</th>
<th colspan="3"></th>
<th>Edit Meters</th>
</tr>
<tr>
<th>PID</th>
<th>Prior Meter</th>
<th>Today's Meter</th>
<th>Today's Value</th>
<th>Tolerance</th>
<th>Variance</th>
<th>Accepted</th>
<th>Game ID</th>
<th>Paytable ID</th>
<th>Additional ID</th>
<th>Game Num</th>
<th>Base %</th>
<th>Description</th>
<th>Edit Total Coin In</th>
</tr>
<tr>
<td>14</td>
<td>0</td>
<td>0</td>
<td>5.00</td>
<td>10,000.00</td>
<td>0.00</td>
<td>Yes</td>
<td>sb</td>
<td>IGT_AVV012330</td>
<td>IGT_Enchanted Unicorn</td>
<td>0</td>
<td>94.06</td>
<td>IGT_Enchanted Unicorn</td>
<td rowspan="2">Unaccept</td>
</tr>
<tr>
<td>15</td>
<td>109,835</td>
<td>109,835</td>
<td>0.00</td>
<td>10,000.00</td>
<td>0.00</td>
<td></td>
<td>sb</td>
<td>IGT_AVV023151</td>
<td>IGT_Betti the Yetti</td>
<td>0</td>
<td>94.98</td>
<td>IGT_Betti the Yetti</td>
</tr>
<tr>
<td>16</td>
<td>1,694</td>
<td>1,694</td>
<td>0.00</td>
<td>10,000.00</td>
<td>0.00</td>
<td></td>
<td>sb</td>
<td>IGT_AVV028005</td>
<td>IGT_Game014001FU9001</td>
<td>0</td>
<td>94.94</td>
<td>IGT_Game014001FU9001</td>
<td>Current Meters</td>
</tr>
<tr>
<td>17</td>
<td>0</td>
<td>0</td>
<td>0.00</td>
<td>10,000.00</td>
<td>0.00</td>
<td></td>
<td>sb</td>
<td>IGT_AVV028006</td>
<td>IGT_Game014001FU9001</td>
<td>0</td>
<td>96.54</td>
<td>IGT_Game014001FU9001</td>
<td>Paytable Edik</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Distribute</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td rowspan="16"></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Done</td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


5\. Complete the following tasks as needed on the Paytable Coin In Meter Variances for
Machine window:

· Click Edit Total Coin In to edit the total coin in. The Meter Adjustment for Machine
window appears. Enter the value in the Adjustment field, then click Save. The Meter
Adjustment for Machine window closes.




![](MachineAccounting_UserGuide_images/212.2.png)




· Click Distribute to distribute the difference between the cabinet coin in and the
paytable(s) coin in. A prompt appears to confirm the distribution. Click Yes to
distribute the difference or No to cancel. The confirmation window closes.




![](MachineAccounting_UserGuide_images/212.3.png)




· Select a paytable, then click Edit Meters to adjust the paytable meter. The Meter
Adjustment for Paytable window opens. Enter a new value in the Adjustment field,
then click Save. The Meter Adjustment for Paytable window closes.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="212" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->




![](MachineAccounting_UserGuide_images/213.1.png)




· Select a paytable, then click Edit Total Coin In to adjust a paytable's coin-in meter.
The Meter Adjustment for Machine window appears. Enter a new value in the
Adjustment field, then click Save. The Meter Adjustment for Paytable window closes.




![](MachineAccounting_UserGuide_images/213.2.png)




· Click Accept to accept the paytable variance. A confirmation appears. Click Yes. The
paytable variance is accepted, and the confirmation window closes.




![](MachineAccounting_UserGuide_images/213.3.png)




· Click Current Meters to view the paytable's current meters. The Current Meters for
Paytable window displays the paytable's current meters. Click OK to close the Current
Meters for Paytable window.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="213" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->




![](MachineAccounting_UserGuide_images/214.1.png)




<table>
<tr>
<th>Paytable ID</th>
<th>Meter Date</th>
<th>Meter Type</th>
<th>Coin In</th>
<th>Weighted Average Theo Hold</th>
<th>A</th>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 12:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 12:30AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td>E</td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 1:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 1:30AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 2:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 2:30AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 3:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 3:30AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 4:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 4:30AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 5:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 5:30AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 6:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 6:30AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 7:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 7:30AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 7:45AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 8:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 8:30AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 9:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 9:30AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 9:58AM</td>
<td>On Demand</td>
<td>2,600</td>
<td>5.07</td>
<td></td>
</tr>
<tr>
<td>254</td>
<td>Jun 14 2010 10:00AM</td>
<td>Hourly</td>
<td>2,600</td>
<td>5.07</td>
<td>V</td>
</tr>
</table>


· Click Paytable Edit to edit the paytable information. The Paytable Edit window
appears. Adjust any information required, then click Save. The Paytable Edit window
closes.




![](MachineAccounting_UserGuide_images/214.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="214" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->

6\. Click Done. The Paytable Coin In Meter Variances for Machine window closes, and the
coin-in adjustments save.


## 16.5 Calculating Meters

Use the Calculate Meters function to correct all meters simultaneously based on a specific
criterion. The Calculate Meters function is only recommended after a RAM clear. All meters are
reset to zero in the gaming day when a RAM clear is completed. As a result, the end-of-day
meter is less than the prior day's meter, which results in a negative value for all meters. In this
case, the Calculating Meters function makes correcting the meters much faster since all meters
are adjusted at the same time.




![](MachineAccounting_UserGuide_images/215.1.png)




!
Calculating meters in this manner is suggested only as a last resort. All meters are
affected. If a machine has only several meters with a variance, it is recommended
that just those meters be adjusted.

Select the last good meter (registered before the RAM clear) AND the first good meter after the
RAM clear. The system performs two separate calculations for each and adds them together.
Each meter is updated with the resulting total. For example:


<table>
<tr>
<th>Coin In</th>
<th>Coin Out</th>
</tr>
<tr>
<td>80000</td>
<td>82000</td>
</tr>
<tr>
<td>81000</td>
<td>82999</td>
</tr>
<tr>
<td>85000</td>
<td>84000</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>5</td>
<td>10</td>
</tr>
<tr>
<td>15</td>
<td>35</td>
</tr>
</table>


In the example above:

· The Coin-In formula is: (85000 - 80000) + (15 - 0) = 5015

· The Coin-Out formula is: (84000 - 82000) + (35 - 0) = 2035

The totals are multiplied by the denomination of the machine to obtain the amount appearing
in the Today's Value field for the meters.

To use the Calculate Meters function:

1\. Click Correct Meter Variances in the User Tasks list. The Correct Meter Variances
window displays.

2\. Click Exceptions to display the machines with meter exceptions.

OR
Click Show All to display all the machines, including those with meter exceptions.

3\. Select a machine or hold CTRL and click to select multiple machines, then click View
Meters. The Meter Variances for Machine window appears.

OR
Double-click a machine. The Meter Variances for Machine window appears.

i
If multiple machines are selected, the Next Machine button is enabled.




![](MachineAccounting_UserGuide_images/215.2.png)




4\. Select a meter with a variance, then click Calculate Meters. The Meter Calculations for
Machine window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="215" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 16 Machine Meter Variances" -->




![](MachineAccounting_UserGuide_images/216.1.png)




<table>
<tr>
<th colspan="10"></th>
</tr>
<tr>
<th></th>
<th>Meter</th>
<th>Prior Meter</th>
<th>New Ending</th>
<th>New Beg.</th>
<th>Current Meter</th>
<th>Delta</th>
<th>Variance</th>
<th>A</th>
<th>Accept</th>
</tr>
<tr>
<td></td>
<td>Coin In</td>
<td>24,187</td>
<td></td>
<td></td>
<td>24,317</td>
<td>1.30</td>
<td>0.00</td>
<td rowspan="5"></td>
<td rowspan="2">Select Meters</td>
</tr>
<tr>
<td></td>
<td>Coin Out</td>
<td>10,491</td>
<td></td>
<td></td>
<td>10,551</td>
<td>0.60</td>
<td>0.00</td>
</tr>
<tr>
<td></td>
<td>Legacy Coin Out</td>
<td>47,216</td>
<td></td>
<td></td>
<td>47,346</td>
<td>1.30</td>
<td>0.00</td>
<td rowspan="2">Cancel</td>
</tr>
<tr>
<td></td>
<td>Games</td>
<td>1,621</td>
<td></td>
<td></td>
<td>1,647</td>
<td>26.00</td>
<td>0.00</td>
</tr>
<tr>
<td></td>
<td>Total Drop</td>
<td>582,424</td>
<td></td>
<td></td>
<td>582,924</td>
<td>5.00</td>
<td>0.00</td>
<td rowspan="3"></td>
</tr>
<tr>
<td></td>
<td>$1</td>
<td>23</td>
<td></td>
<td></td>
<td>23</td>
<td>0.00</td>
<td>0.00</td>
<td rowspan="3">E</td>
</tr>
<tr>
<td></td>
<td>$2</td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td></td>
<td>$5</td>
<td>11</td>
<td></td>
<td></td>
<td>11</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td></td>
<td>$10</td>
<td>9</td>
<td></td>
<td></td>
<td>9</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$ 20</td>
<td>7</td>
<td></td>
<td></td>
<td>7</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$50</td>
<td>3</td>
<td></td>
<td></td>
<td>3</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
<td rowspan="2"></td>
</tr>
<tr>
<td></td>
<td>$ 100</td>
<td>3</td>
<td></td>
<td></td>
<td>3</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Bill In</td>
<td>75,800</td>
<td></td>
<td></td>
<td>75,800</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
<td rowspan="2"></td>
</tr>
<tr>
<td></td>
<td>Attendant Paid Cancelled Credits</td>
<td>38,472</td>
<td></td>
<td></td>
<td>38,472</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Attendant Paid External Bonus Payout</td>
<td>360</td>
<td></td>
<td></td>
<td>360</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
<td rowspan="4"></td>
</tr>
<tr>
<td></td>
<td>Attendant Paid Jackpots</td>
<td>2,665</td>
<td></td>
<td></td>
<td>2,665</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Attendant Paid Progressive Payout</td>
<td>10,030</td>
<td></td>
<td></td>
<td>10,030</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Machine Paid External Bonus Payout</td>
<td>6,055</td>
<td></td>
<td></td>
<td>6,125</td>
<td>0.70</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Machine Paid Progressive Payout</td>
<td>6,055</td>
<td></td>
<td></td>
<td>6,125</td>
<td>0.70</td>
<td>0.00</td>
<td rowspan="2"></td>
<td rowspan="2"></td>
</tr>
<tr>
<td rowspan="2"></td>
<td>Bonus</td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>Point Play</td>
<td>8,000</td>
<td></td>
<td></td>
<td>8,500</td>
<td>5.00</td>
<td>0.00</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Legacy Point Play</td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td>0.00</td>
<td>0.00</td>
<td>V</td>
<td rowspan="2"></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


5\. Select a meter or press and hold CTRL to select multiple meters, then click Select
Meters. The Select Meters window appears.




![](MachineAccounting_UserGuide_images/216.2.png)




<table>
<tr>
<th></th>
<th>Meter Date</th>
<th>Meter Type</th>
<th>Physical Coin In</th>
<th>Physical Coin Out</th>
<th>Coin In</th>
<th>Legacy Coin Out</th>
<th>A</th>
</tr>
<tr>
<td rowspan="26"></td>
<td>June 14 2010 06:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 06:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 06:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td>I</td>
</tr>
<tr>
<td>June 14 2010 07:00:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 07:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 07:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 07:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 08:00:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 08:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 08:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 08:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 09:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 09:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 09:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,037</td>
<td>47,116</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 10:00:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 10:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 10:30:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 10:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 10:47:44</td>
<td>Soft Drop Outside Window</td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 10:48:13</td>
<td>Soft Drop Outside Window</td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 11:00:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 11:15:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 11:45:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 12:00:00</td>
<td>Hourly</td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td></td>
</tr>
<tr>
<td>June 14 2010 12:15:00</td>
<td></td>
<td>0</td>
<td>82</td>
<td>24,187</td>
<td>47,216</td>
<td>V</td>
</tr>
<tr>
<td>&lt; IIII</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>&gt;</td>
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
<td></td>
</tr>
</table>


6\. Click Last Good Meter (before the problem meter) to select the machine's last good
meter reading, then click OK. The Meter Calculations for Machine window appears.
OR
Click First Good Meter (after the problem meter) to select the machine's first good
meter reading, then click OK. The Meter Calculations for Machine window appears.

7\. Click Accept. The Meter Change Confirmation window appears.

8\. Click Yes. The change is saved.




![](MachineAccounting_UserGuide_images/216.3.png)




To calculate meters manually, calculate the meters in Excel, then enter the
adjustments. Many properties prefer to enter meter calculations manually in order
to retain source documents of the changes made.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="216" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/217.1.png)




