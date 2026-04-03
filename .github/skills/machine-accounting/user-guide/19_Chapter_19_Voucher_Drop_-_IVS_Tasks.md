# Chapter 19 Voucher Drop - IVS Tasks

Vouchers are audited and voucher summary balances are accepted through the Audit Voucher
Meters window.

The following tasks are available for completing the Voucher Drop - IVS portion of the audit:


<table>
<tr>
<th>Task</th>
<th>Description</th>
</tr>
<tr>
<td>Import Voucher Information</td>
<td>Imports the system Voucher In and system Voucher Out revenue summaries by machine.</td>
</tr>
<tr>
<td>Audit Voucher Meters</td>
<td>Audit and correct Voucher In and Voucher Out variances between actual and meters.</td>
</tr>
</table>


## To access the Audit Voucher Meters window:

Click Voucher Drop - IVS in the Period Timeline or in the User Tasks list. The options for
Voucher Drop - IVS appear.




![Figure 19-1 User Tasks List-Voucher Drop - IVS Tasks](MachineAccounting_UserGuide_images/241.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="241" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 19 Voucher Drop - IVS Tasks" -->


### 19.1 Retrieving Voucher Drops

Voucher-out drops are obtained from the EZ Pay end-of-day issuance. Voucher in is obtained
through soft count vouchers.


#### To retrieve the actual voucher drop:

1\. Click Voucher Drop - IVS in the Period Timeline or the User Tasks list. The options for
Voucher Drop - IVS appear.

2\. Click Import Voucher Information. The Retrieving Drop message appears.




![](MachineAccounting_UserGuide_images/242.1.png)




3\. Click Done when the voucher drop completes. The Retrieving Drop message closes.


### 19.2 Voucher-In Variances

Vouchers in are obtained through soft-count vouchers.


#### 19.2.1 Viewing Audit Voucher Meters

To view audit voucher meters:

1\. Click Voucher Drop - IVS on the Period Timeline or User Task list.

2\. Click Audit Voucher Meters. The Audit Voucher Meters window appears.




![](MachineAccounting_UserGuide_images/242.2.png)




3\. Select Vouchers In. The vouchers-in audit meters appear.

4\. Select All Dropped or Exceptions to filter the displayed vouchers.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="242" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 19 Voucher Drop - IVS Tasks" -->


#### 19.2.2 Adjusting Voucher-In Meter Variances


##### To adjust voucher-in meter variances:

1\. Click Voucher Drop - IVS on the Period Timeline or User Task list.

2\. Click Audit Voucher Meters. The Audit Voucher Meters window appears.




![](MachineAccounting_UserGuide_images/243.1.png)




3\. Select a machine.

4\. Click Meters. The Voucher In Meter Adjustment for Machine window appears.




![](MachineAccounting_UserGuide_images/243.2.png)




5\. Enter the meter value in the Value Meter and Count Meter fields, as needed.




![](MachineAccounting_UserGuide_images/243.3.png)




i
To make value changes without overwriting the existing value: Enter + or minus -
in front of the change. For example, entering 50 makes the new value 50, whereas
entering +50 adds 50 to the current value to create the new amount.

6\. Click OK. The adjustment is confirmed.


#### 19.2.3 Accepting Voucher-In Variances

To accept voucher-in variances:

1\. Click Voucher Drop - IVS on the Period Timeline or User Task list.

2\. Click Audit Voucher Meters. The Audit Voucher Meters window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="243" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 19 Voucher Drop - IVS Tasks" -->




![](MachineAccounting_UserGuide_images/244.1.png)




3\. Select a machine.
OR

Press Ctrl + click to select multiple machines.

4\. Click Accept in the Audit Voucher Meters window IF the variances are within established
guidelines. A confirmation prompt appears.

5\. Click Yes. The variances are accepted.


### 19.2.4 Unaccepting Voucher-In Variances


#### To unaccept a voucher-in variance:

1\. Click Voucher Drop - IVS on the Period Timeline or User Task list.

2\. Click Audit Voucher Meters. The Audit Voucher Meters window appears.




![](MachineAccounting_UserGuide_images/244.2.png)




3\. Select a machine.

4\. Click Unaccept in the Audit Voucher Meters window IF the variance is not within
established guidelines. A confirmation prompt appears.

5\. Click Yes. The variance is no longer accepted.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="244" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 19 Voucher Drop - IVS Tasks" -->


##### 19.3 Voucher-Out Meter Variances

The voucher-out drop is obtained from the EZ Pay end-of-day issuance.
To display voucher-out meter variances:

1\. Click Voucher Drop - IVS on the Period Timeline or User Tasks list. The options for
Voucher Drop - IVS appear.

2\. Click Audit Voucher Meters. The Audit Voucher Meters window appears.




![](MachineAccounting_UserGuide_images/245.1.png)




<table>
<tr>
<th>Machine</th>
<th>Location</th>
<th>Denom</th>
<th>Meler Drop</th>
<th>Meler Count:</th>
<th>System Count</th>
<th>Actual Drop</th>
<th>Actual Count</th>
<th>Variance</th>
<th>Percent</th>
<th>Aco</th>
</tr>
<tr>
<td>40000</td>
<td>B0101</td>
<td>0.05</td>
<td>0.00</td>
<td>0</td>
<td>0</td>
<td>0.00</td>
<td>0</td>
<td>0.00</td>
<td>0.00</td>
<td>Yes</td>
</tr>
<tr>
<td>50000</td>
<td>ABCD0202</td>
<td>10.00</td>
<td>0.00</td>
<td>0</td>
<td>0</td>
<td>0.00</td>
<td>0</td>
<td>0.00</td>
<td>0.00</td>
<td>Yos</td>
</tr>
<tr>
<td>50007</td>
<td>ABCDO505</td>
<td>10.00</td>
<td>Ū ŌŪ</td>
<td>0</td>
<td>0</td>
<td>Ū.ŪŌ</td>
<td>0</td>
<td>0.00</td>
<td>Ū.ŪŌ</td>
<td>Yes</td>
</tr>
<tr>
<td>150009</td>
<td>ABCDO606</td>
<td>10.00</td>
<td>0.00</td>
<td>0</td>
<td>0</td>
<td>0.00</td>
<td>0</td>
<td>0.00</td>
<td>0.00</td>
<td>Yes</td>
</tr>
<tr>
<td>50010</td>
<td>ABC0606</td>
<td>10.00</td>
<td>0.00</td>
<td>0</td>
<td>0</td>
<td>0.00</td>
<td>0</td>
<td>0.00</td>
<td>0.00</td>
<td>Yes</td>
</tr>
<tr>
<td>50011</td>
<td>ABCD0707</td>
<td>10.00</td>
<td>0.00</td>
<td>0</td>
<td>0</td>
<td>0.00</td>
<td>0</td>
<td>0.00</td>
<td>0.00</td>
<td>Yes</td>
</tr>
<tr>
<td>50090</td>
<td>VV0404</td>
<td>10.00</td>
<td>0.00</td>
<td>0</td>
<td>0</td>
<td>Ū.ŪŌ</td>
<td>0</td>
<td>0.00</td>
<td>0.00</td>
<td>Yes</td>
</tr>
</table>


3\. Select Vouchers Out. The voucher-out meter variances appear.

4\. Select All Dropped or Exceptions to filter the displayed vouchers.


###### 19.3.1 Adjusting Voucher-Out Meter Variances

To adjust voucher-out variances:

1\. Click Voucher Drop - IVS on the Period Timeline or User Task list.

2\. Click Audit Voucher Meters. The Audit Voucher Meters window appears.

3\. Select a machine.

4\. Click Meter. The Voucher Out Meter Adjustment for Machine window appears.




![](MachineAccounting_UserGuide_images/245.2.png)




5\. If needed, enter the adjusted value in the Adjustment field in the Value Meter pane.

6\. If needed, enter the adjusted value in the Adjustment field in the Count Meter pane.

7\. Click OK. The adjustment is confirmed.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="245" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 19 Voucher Drop - IVS Tasks" -->


###### 19.3.2 Accepting Voucher-Out Variances


####### To accept voucher-out variances:

1\. Click Voucher Drop - IVS on the Period Timeline or User Task list. The options for
Voucher Drop - IVS appear.

2\. Click Audit Voucher Meters. The Audit Voucher Meters window appears.

3\. Select Voucher Out.

4\. Select a machine.
OR
Press Ctrl + click to select multiple machines.

5\. Click Accept in the Audit Voucher Meters window IF the variances are within established
guidelines. A confirmation prompt appears.

6\. Click Yes. The variances are accepted.


###### 19.3.3 Unaccepting Voucher-Out Variances


####### To unaccept a voucher-out variance:

1\. Click Voucher Drop - IVS on the Period Timeline or User Task list. The options for
Voucher Drop - IVS appear.

2\. Click Audit Voucher Meters. The Audit Voucher Meters window appears.

3\. Select Voucher Out.

4\. Select a machine.

5\. Click Unaccept IF the variance is not within established guidelines. A confirmation
prompt appears.

6\. Click Yes. The variance is no longer accepted.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="246" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/247.1.png)




