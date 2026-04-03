# Chapter 28 Audit Workbook

Machine Accounting correlates manual meter readings with electronic meter readings. This
process helps casino managers and regulators monitor machine performance and audit the
actual meters of a specific machine at various times. Use a special handheld computer called a
drop scanner to record machine meter readings manually. Machines may also be grouped to
indicate the day when a group of machines is audited.


# 28.1 Viewing Audit Meters

View audit meters with either the Machine Meters view or the Hard Meters view. These views
display two types of meters:

· Machine Meters-Electronic meters stored on the EGM that include ALL meters. All
machines have machine meters except for older machines that only have hard meters.

· Hard Meters-Physical odometers within a machine that serve as coin-in, coin-out,
drop, and jackpot meters. This type of meter is limited to older machines.

To view audit meters:

1\. Navigate to IGT Spade > Audit > Audit Test. The Audit Workbook window appears.

2\. Click the Audit Meters tab. The Audit Meters tab appears.

3\. Select Machine Meters or Hard Meters to filter the machines displayed.

4\. Enter the date for the audit meters (in mm/dd/yyyy format).

5\. Select the appropriate audit group from the Group drop-down list.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="305" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 28 Audit Workbook" -->




![Figure 28-1 Audit Workbook-Machine Meters Example](MachineAccounting_UserGuide_images/306.1.png)




# 28.2 Managing Audit Groups

Use the Audit Group feature to group machines into audit groups. This allows the property to
indicate the day on which a group of machines is audited, thereby increasing efficiency and
completion of audits over time.


# 28.2.1 Adding Audit Groups


## To add an audit group:

1\. Navigate to IGT Spade > Audit > Audit Test. The Audit Workbook window appears.

2\. Click the Audit Group Setup tab. The Audit Group Setup tab opens.

3\. Select <New> from the Group drop-down list.




![](MachineAccounting_UserGuide_images/306.2.png)




4\. Enter a name for the audit group in the Group field.

5\. Click Add. The audit group is created.


# 28.2.2 Adding Machines to Audit Groups

To add a machine to an audit group:

1\. Navigate to IGT Spade > Audit > Audit Test. The Audit Workbook window appears.

2\. Click the Audit Group Setup tab. The Audit Group Setup tab opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="306" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 28 Audit Workbook" -->

3\. Select the applicable group from the Group drop-down list.

4\. Select machines in the left panel.




![](MachineAccounting_UserGuide_images/307.1.png)




Hold CTRL and click to select multiple machines.

5\. Click Add. The machines are added to the audit group.


# 28.2.3 Removing Machines from Audit Groups

To remove a machine from an audit group:

1\. Navigate to IGT Spade > Audit > Audit Test. The Audit Workbook window appears

2\. Click the Audit Group Setup tab. The Audit Group Setup tab opens. The available
machines are shown in the left pane.

3\. Select the applicable group from the Group drop-down list.

4\. Select a machine in the right panel.




![](MachineAccounting_UserGuide_images/307.2.png)




Hold CTRL and click to select multiple machines.

5\. Click Remove. The machines are removed from the group.


# 28.2.4 Deleting Audit Groups

To delete an audit group:

1\. Navigate to IGT Spade > Audit > Audit Test. The Audit Workbook window appears.

2\. Click the Audit Group Setup tab. The Audit Group Setup tab opens.

3\. Click Group Modify. The Audit Group Modify window appears.




![](MachineAccounting_UserGuide_images/307.3.png)




4\. Select a group from the Groups list.

5\. Select Delete Group.

6\. Click OK. A confirmation message appears.

7\. Click OK. The audit group is deleted.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="307" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 28 Audit Workbook" -->


# 28.2.5 Renaming Audit Groups

To rename an audit group:

1\. Navigate to IGT Spade > Audit > Audit Test. The Audit Workbook window appears.

2\. Click the Audit Group Setup tab. The Audit Group Setup tab opens.

3\. Click Group Modify. The Audit Group Modify window appears.

4\. Select a group from the Groups list.

5\. Select Rename Group.

6\. Enter a new name for the group in the New Name field.

7\. Click OK. The new name saves.


# 28.3 Reading Floor Meters




![](MachineAccounting_UserGuide_images/308.1.png)




i
Instructions in this section apply to the Intermec® CN3 handheld scanner device.

To read floor meters:

1\. Locate the first machine of the Audit Group on the floor.

2\. Power up the handheld drop scanner collection device.

3\. Click 1. Meter Entry in the Advantage Scan window of the drop scanner. The Step 1
window appears. The drop scanner is now ready.

4\. Insert an audit card into the machine's card reader. An electronic reading of the meters is
taken and made available to Machine Accounting.




![](MachineAccounting_UserGuide_images/308.2.png)




i
This electronic meter reading is compared to either the hard meters or soft meters
of the machine. Property policy determines which set of meters is read and used.

5\. Use the following instructions for the floor meters to enter (hard or soft), then continue to
the Next Steps section.


## To enter hard meters:

1\. Locate the hard meters on the machine.




![](MachineAccounting_UserGuide_images/308.3.png)




Ť
The meters may be visible from the exterior of the machine OR may be located
inside the game cabinet. A door key is needed to open the machine door if the
meters are located inside the machine.)

2\. In the Step 1 window of the Drop Scanner, tap Entry Date.

3\. Select the date.

4\. Select a meter set from the Meter Set drop-down list.

5\. Scan the machine barcode.
OR
Enter the machine number in the Machine Number field.

6\. Click OK. The Machine #: window appears.

7\. Select Coin In from the Jump to Meter drop-down list.

8\. Enter the value of the first meter in the Meter Value field.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="308" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 28 Audit Workbook" -->

9\. Select the next meter from the Jump to Meter drop-down list, then enter the value of the
first meter in the Meter Value field.

10\. Repeat step 9 until all meters are entered.

To enter soft meters:

1\. Insert the reset key.

2\. Cycle through the displayed values until the Coin In (CI) soft meter appears.

3\. Scan the machine barcode.
OR
Enter the machine number in the Machine Number field.

4\. Cycle to the next soft meter, then scan the machine barcode OR enter the machine number
in the Machine Number field.

5\. Repeat step 4 until all soft meters are entered.

Next Steps

1\. Click Finish on the Drop Scanner. The Step 1 window appears.

2\. Click Cancel. The Advantage Scan window reappears. The number of unsent records
appears below 1. Meter Entry.

3\. Click 4. Sync Data Now. The meters are sent to the Machine Accounting database.

4\. Return to the accounting workstation, then place the drop scanner in the cradle.


# 28.4 Adjusting Machine Meters

Use the Meter Delta Variance report to assist with adjusting machine meters.

To adjust machine meters:

1\. Navigate to IGT Spade > View > Reports > Meter Delta Variance. The Meter Delta
Variance pane appears.

2\. Set the appropriate filters and generate the report.

3\. Navigate to IGT Spade > Audit > Audit Test. The Audit Workbook window appears.

4\. Verify that the correct date is selected.

5\. Select a machine.

6\. Click Meters. The Audit Machine Meters Adjustment window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="309" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 28 Audit Workbook" -->




![](MachineAccounting_UserGuide_images/310.1.png)




<table>
<tr>
<th>Meter</th>
<th>Prior Value</th>
<th>New Value</th>
<th>Difference</th>
</tr>
<tr>
<td>Physical Coin In</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Physical Coin Out</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Coin In</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Coin Out</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Games</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Total Drop</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>$1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>$2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>$5</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>$10</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>$20</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>$50</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>$100</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>NONE</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>NONE</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>NONE</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>5</td>
<td>6</td>
<td>0</td>
</tr>
</table>


7\. Select the machine to adjust from the Machine Number drop-down list.

8\. Compare the machine information in the Audit Machine Meters Adjustment window to
the information the Meter Delta Variance report. Note any readings not within
established tolerances.

9\. Enter the numbers necessary to bring the meters for the machine back into tolerance in
the New Value field.

10\. Click Save. The adjustments save.


# 28.5 Meters On Demand

Use the Meters On Demand function to request an immediate meter reading from all machines
or any active slot machine.

To view the Meters On Demand window:

1\. Navigate to IGT Spade > Audit > Meters on Demand. The Meters On Demand
window opens.

Limit Meters on Demand to no more than eight EGMs at a time.




![](MachineAccounting_UserGuide_images/310.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="310" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 28 Audit Workbook" -->


<table>
<caption>Figure 28-2 Meters on Demand</caption>
<tr>
<th colspan="12">Meters On Demand: Request #11 ... 4 ×</th>
</tr>
<tr>
<th>Status</th>
<th>Mnum</th>
<th>Location</th>
<th>Paytable</th>
<th>Base Percentage</th>
<th>Game Number</th>
<th>Physical Coin In</th>
<th>Physical Coin Out</th>
<th>Coin In</th>
<th>Legacy Coin Out</th>
<th>Games</th>
<th>Select ...</th>
</tr>
<tr>
<td>Complete</td>
<td>5006</td>
<td>A0107</td>
<td></td>
<td></td>
<td></td>
<td>0</td>
<td>-1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td></td>
</tr>
<tr>
<td>Complete</td>
<td>5006</td>
<td>A0107</td>
<td>sb-IGT_AVV029991-IGT_100 Ladies</td>
<td>96.52</td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td></td>
<td></td>
<td>Refresh</td>
</tr>
<tr>
<td>Complete</td>
<td>5006</td>
<td>A0107</td>
<td>sb-IGT_AVV012334-IGT_Enchanted Unicom</td>
<td>98.01</td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td></td>
<td></td>
<td>Pause</td>
</tr>
<tr>
<td>Complete</td>
<td>5006</td>
<td>A0107</td>
<td>sb-IGT_AW019238-IGT_Pharaoh's Fortune</td>
<td>98.05</td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td></td>
<td></td>
<td rowspan="14"></td>
</tr>
<tr>
<td>Complete</td>
<td>5006</td>
<td>A0107</td>
<td>sb-IGT_AVV028609-IGT_Kossack Kash</td>
<td>96.51</td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Complete</td>
<td>5006</td>
<td>A0107</td>
<td>sb-IGT_AVV027487-IGT_Mystical Princess</td>
<td>98.02</td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Complete</td>
<td>5009</td>
<td>A0110</td>
<td></td>
<td></td>
<td></td>
<td>0</td>
<td>0</td>
<td>300</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Complete</td>
<td>5009</td>
<td>A0110</td>
<td>sb-IGT_AVV037220-IGT_Game014001IF8 ...</td>
<td>89.08</td>
<td>0</td>
<td></td>
<td></td>
<td>300</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Complete</td>
<td>5015</td>
<td>A0105</td>
<td></td>
<td></td>
<td></td>
<td>0</td>
<td>0</td>
<td>170,318</td>
<td>26,617</td>
<td>129</td>
</tr>
<tr>
<td>Complete</td>
<td>5015</td>
<td>A0105</td>
<td>sb-IGT_AVV028064-IGT_Kilimanjaro</td>
<td>88.90</td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Complete</td>
<td>5015</td>
<td>A0105</td>
<td>sb-IGT_AVV028067-IGT_Kilimanjaro</td>
<td>92.99</td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Failed</td>
<td>5021</td>
<td>A0106</td>
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
<td>Failed</td>
<td>5021</td>
<td>A0106</td>
<td>sb-IGT_AW028605-IGT_Kossack Kash</td>
<td>89.93</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Failed</td>
<td>5021</td>
<td>A0106</td>
<td>sb-IGT_AVV028606-IGT_Kossack Kash</td>
<td>91.51</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Failed</td>
<td>5021</td>
<td>A0106</td>
<td>sb-IGT_AW012328-IGT_Enchanted Unicom</td>
<td>90.04</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Failed</td>
<td>5021</td>
<td>A0106</td>
<td>sb-IGT_AW012331-IGT_Enchanted Unicom</td>
<td>94.95</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Failed</td>
<td>5021</td>
<td>A0106</td>
<td>sb-IGT_AVV012333-IGT_Enchanted Unicom</td>
<td>97.41</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


2\. Click Select. The Meter Set Selection window appears.

Accessing the Meter Set Selection dialog box requires the Meters on Demand-
Access permission.




![](MachineAccounting_UserGuide_images/311.1.png)






![](MachineAccounting_UserGuide_images/311.2.png)




<table>
<tr>
<th>Request ID</th>
<th>Date</th>
<th>MachineCount</th>
<th>Pending</th>
<th>Active</th>
<th>1</th>
</tr>
<tr>
<td>116</td>
<td>01/05/2011 3:56 PM</td>
<td>1</td>
<td>0</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td>115</td>
<td>01/05/2011 3:38 PM</td>
<td>5</td>
<td>0</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td>114</td>
<td>12/23/2010 11:51 AM</td>
<td>1</td>
<td>0</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td>113</td>
<td>12/23/2010 11:49 AM</td>
<td>1</td>
<td>0</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td>112</td>
<td>12/23/2010 11:45 AM</td>
<td>1</td>
<td>0</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td>111</td>
<td>12/22/2010 1:40 PM</td>
<td>2</td>
<td>0</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td>110</td>
<td>12/22/2010 1:33 PM</td>
<td>2</td>
<td>0</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td>109</td>
<td>12/22/2010 1:32 PM</td>
<td>2</td>
<td>0</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td>108</td>
<td>12/22/2010 1:25 PM</td>
<td>2</td>
<td>0</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td>107</td>
<td>12/22/2010 1:23 PM</td>
<td>2</td>
<td>0</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td>106</td>
<td>12/22/2010 1:13 PM</td>
<td>2</td>
<td>0</td>
<td>N</td>
<td>¥</td>
</tr>
</table>


Figure 28-3 Meters On Demand Selection

3\. To view one of the listed meter sets, select the desired date, then click OK. The Detail
Meters window opens.




![](MachineAccounting_UserGuide_images/311.3.png)




O
The EGMs appear in red or green to indicate whether the meters were obtained.
Green indicates success, and red indicates failure.

A failure to obtain meters can indicate that the EGM is not connected, not working
properly, or having communication problems.




![Figure 28-4 Meters On Demand-Detail Meters](MachineAccounting_UserGuide_images/311.4.png)




4\. Mouse over the tab to view the date and time being displayed.

5\. Click Refresh to refresh the display or Pause to pause the display.




![](MachineAccounting_UserGuide_images/311.5.png)




O
Every time a Meters On Demand request is made or canceled, Machine Accounting
logs the date and time of the request and the identity of the individual making the
request. Perform reporting in the Period Log.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="311" -->




![](MachineAccounting_UserGuide_images/311.6.png)




<!-- PageBreak -->

<!-- PageHeader="Chapter 28 Audit Workbook" -->

This page is intentionally left blank.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="312" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/313.1.png)




