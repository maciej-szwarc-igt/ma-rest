# Chapter 15 Opening the Audit Day

Machine Accounting collects the following casino floor information for the period when
opening a gaming day for audit:


<table>
<tr>
<th>Task</th>
<th>Description</th>
</tr>
<tr>
<td>Start Period</td>
<td>Starts the period within the Period Workbook.</td>
</tr>
<tr>
<td>Initialize Hand Pay Entries</td>
<td>Automatically gathers information</td>
</tr>
<tr>
<td>Get Period Meters</td>
<td>Automatically gathers information.</td>
</tr>
<tr>
<td>Get Opening Meters</td>
<td>Initialize Drop Meters and Create Period Tables-Checks the previously closed period, obtains ending meters for the last period, and creates a period structure in the database.</td>
</tr>
</table>


## 15.1 User Tasks List

View audit tasks (required, completed, or in process) in the User Tasks list or the Period
Timeline ribbon. The User Tasks list appears in the main window by default.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="195" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 15 Opening the Audit Day" -->




![Figure 15-1 User Tasks List](MachineAccounting_UserGuide_images/196.1.png)




### To toggle the User Tasks list:

Navigate to IGT Spade > View > User Tasks. The User Tasks list is toggled on or off.
OR

Click the Push Pin icon. The User Tasks list is auto-hidden
window.

\+

or docked

4
to the




![Figure 15-2 User Tasks List-Push Pin Icon](MachineAccounting_UserGuide_images/196.2.png)




<!-- PageNumber="196" -->
<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 15 Opening the Audit Day" -->

To access the User Tasks list:

1\. Navigate to IGT Spade > Options > Configuration > General. The General pane
opens.

2\. Click Mandatory Tasks Settings. The Mandatory Tasks pane opens.

3\. Click Modify. The mandatory user tasks appear.


### 15.1.1 User Tasks List Options

Remember the following about the User Tasks list:

· A period must be opened before any tasks display.

· All mandatory tasks must be completed before closing a day.

· Be aware that changing the displayed user tasks may hide mandatory tasks that must
be completed before closing a day.

The following table summarizes the major tasks and components of the User Tasks list:


<table>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
<tr>
<td>Verify Machine Changes</td>
<td>Verify all machine retirements, additions, moves, and conversions made in the open period. ! Retire machines only after the soft and hard drops are complete. This allows the retiring machine to make a final drop.</td>
</tr>
<tr>
<td>Correct Meter Variances</td>
<td>The operator may correct machine meter variances for the period.</td>
</tr>
<tr>
<td>Hand Pays</td>
<td>Determine and review hand pays for the current accounting period; manually add hand pay data; and review and correct jackpot, progressive, and credit variances. · Add Manual Hand Pays-Manually add hand pays not accounted for within Machine Accounting. · Balance With Cage-Reconcile the cage. · Correct Jackpot Variances-Reconcile and correct jackpot variances. · Correct Progressive Variances- Reconcile and correct progressive jackpot variances. · Correct Cancel Credit Variances-Reconcile and correct credit pay variances. · Correct Bonus Jackpot Variances-Reconcile and correct bonus jackpot variances.</td>
</tr>
<tr>
<td>Enter Manual Meters</td>
<td>Manually enter machine meters as required by an audit.</td>
</tr>
<tr>
<td rowspan="2">Hard Drop and Soft Drop</td>
<td>Obtain the hard drop and soft drop data for the machines, verify the accuracy of both, and make corrections. Any differences between the actual and metered hard and soft drop above the configured variance levels must be reviewed.</td>
</tr>
<tr>
<td>· Get Hard/Soft Drop-Obtain hard/soft drop data from the machines. · Actual Hard/Soft Drop-Actual hard/soft drop amount. · Metered Hard/Soft Drop-Metered hard/soft drop amount. · Correct Hard/Soft Drop Errors-Correct any hard/soft drop errors. · Correct Hard/Soft Drop Variances-Correct hard/soft drop variances.</td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="197" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 15 Opening the Audit Day" -->


<table>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
<tr>
<td>Non-Cashable Electronic Promotion Drop</td>
<td>· Non-Cashable Electronic Promotion Drop-Determine and review the non- cashable electronic promotion summaries in the Bonus by Machine report from Patron Management and compare them to the Point Play or Xtra Credit column in Machine Accounting.</td>
</tr>
<tr>
<td>OR</td>
<td>OR</td>
</tr>
<tr>
<td>Cashable Electronic Promotion Drop</td>
<td>· Cashable Electronic Promotion Drop-Determine and review the cashable electronic promotion summaries in the Bonus by Machine report from Patron Management and compare them to the Point Play or Xtra Credit column in Machine Accounting.</td>
</tr>
<tr>
<td>Voucher Drop - IVS</td>
<td>Determine and review voucher summaries for the current accounting period, balance ticket batches, and correct voucher in and voucher out variances. · Import Voucher Information-Imports the system voucher-in and system voucher-out revenue summaries by machine. · Audit Voucher Meters-Audit and correct voucher-in and voucher-out variances between actual and meters.</td>
</tr>
<tr>
<td>Coupon Promotion Drop</td>
<td>Determine and review coupon-promotion drop summaries for the current accounting period, balance batches, and correct variances. · Import Coupon Promotion Drop Information-Imports the system coupon in and system coupon out revenue summaries by machine. · Audit Coupon Promotion Meters-Audit and correct coupon in and coupon out variances between actual and meters.</td>
</tr>
<tr>
<td>Progressive Workbook</td>
<td>Review the active progressives and progressive movements based on the meter activity of associated machines.</td>
</tr>
<tr>
<td rowspan="2"></td>
<td>Determine and review EZ Pay® Smart Card™ OR EZ Pay Mag Card summaries for the current accounting period, balance batches, and correct variances. When reconciliation and/or acceptance of drop summaries match system totals, the status in the Period Timeline Ribbon changes to green.</td>
</tr>
<tr>
<td>· Import EZ Pay Smart Card Information-Imports the EZ Pay Smart Card system voucher-in and voucher-out revenue summaries by machine.</td>
</tr>
<tr>
<td>EZ Pay Cashless Drop</td>
<td>· Audit EZ Pay Smart Card Meters-Audit and correct EZ Pay Smart Card system voucher-in and voucher-out variances between actual and meters. OR · Import EZ Pay Mag Card Information-Imports the EZ Pay Mag Card system voucher-in and voucher-out revenue summaries by machine. · Audit EZ Pay Mag Card Meters-Audit and correct EZ Pay Mag Card system Voucher In and Voucher Out variances between actual and meters.</td>
</tr>
<tr>
<td>Close Period</td>
<td>When all tasks listed above are complete, close the accounting period and finalize all data. No further changes to this accounting period can occur. The status in the Period Timeline Ribbon changes to green after the period closes. O 1 All periods prior to the period being worked on must be closed before the current period can be closed.</td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="198" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 15 Opening the Audit Day" -->


## 15.1.2 Period Timeline Ribbon

The Period Timeline Ribbon provides a linear view of the User Tasks list.




![Figure 15-3 Period Timeline Ribbon](MachineAccounting_UserGuide_images/199.1.png)




The Period Timeline ribbon includes the following graphical elements:

· Blue Circle-Click to view sub-tasks

· Red Diamond-Indicates the current task

· White Dot-Click to navigate left or right on the timeline

· Black Check Mark-Indicates a completed sub-task

The following colors of the status bar represent a task's status:

· Black-Not started

· Orange-Started

· Yellow-About to finish

· Green-Finished




![Figure 15-4 Period Timeline with Sub-Tasks Displayed for Soft Drop](MachineAccounting_UserGuide_images/199.2.png)




## 15.1.3 Active and Inactive Variance Comments

Use the Comment button to add a comment when accepting a meter, jackpot, voucher, CEP,
soft drop, or hard drop variance in order to explain why the action was taken.


### To add a comment to a variance:

1\. Click Comment in the appropriate window (for example, the Audit CEP Meters window).
The Comment window appears.




![](MachineAccounting_UserGuide_images/199.3.png)




<table>
<tr>
<th colspan="2">CEP In ☒ CEP OUR ☐</th>
<th>Count: Amount($):</th>
<th>8 0.00</th>
<th>☐ Al Machines ☐ Exceptions</th>
<th></th>
<th colspan="2">Comment Actual</th>
</tr>
<tr>
<th>Machine</th>
<th>Location</th>
<th colspan="2">Denom CEPI Meter Legacy</th>
<th>Non-Deduct Meter</th>
<th>Total CEPI Meter Actual Xbra Credit: (PM)</th>
<th>Actual Promo Credit (EZPay)</th>
<th>Actual Credit Meter</th>
</tr>
<tr>
<td>3329</td>
<td>519180</td>
<td>0.01</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00 0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>3395</td>
<td>58939933</td>
<td>0.01</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00 0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="199" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 15 Opening the Audit Day" -->




![](MachineAccounting_UserGuide_images/200.1.png)




2\. Select a comment from the Comment drop-down list OR enter a comment in the Comment
field.

3\. If entering a comment, select Active Comment to add the comment to the Comment
drop-down list for future use.

4\. Click OK. The comment is added to the variance


## 15.1.3.1 Modifying the Active Comments List


### To modify the list of available comments in the Comment drop-down list:

1\. Click Comment in the appropriate window (for example, the Audit CEP Meters window).
The Comment window appears.

2\. Click Advanced. The Comment Status window appears.




![](MachineAccounting_UserGuide_images/200.2.png)




· To activate a comment in the Inactive column: Highlight the comment, then click >.

· To inactivate a comment in the Active column: Highlight the comment, then click <.

3\. Click OK on the Comments Status window. The changes save, and the Comment Status
window closes.

4\. Click OK on the Comments window. The Comments window closes.


### 15.1.3.2 Deleting Comments from the Comments List


#### To delete a comment from in the Comment drop-down list:

1\. Click Comment in the appropriate window (for example, the Audit CEP Meters window).
The Comment window appears.

2\. Click Advanced. The Comment Status window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="200" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 15 Opening the Audit Day" -->




![](MachineAccounting_UserGuide_images/201.1.png)




3\. Highlight the comment to delete.

4\. Click Delete. The comment is deleted.

5\. Click OK on the Comments Status window. The Comment Status window closes.

6\. Click OK on the Comments window. The Comments window closes.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="201" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 15 Opening the Audit Day" -->

This page is intentionally left blank.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="202" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/203.1.png)




