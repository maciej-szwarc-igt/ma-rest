# Chapter 23 Cashable Electronic Promotion (CEP)

During the cashable electronic promotion (CEP) audit, review the Xtra Credit and/or PointPlay
used in the player-tracking system and compare it to the actual meter movement.


## To audit cashable electronic promotion (CEP):

Navigate to the Period Timeline or User Tasks list, then click Cashable Electronics
Promotion.




![Figure 23-1 User Tasks List-CEP Tasks](MachineAccounting_UserGuide_images/269.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="269" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->

Access the following tasks as part of the Cashable Electronic Promotion portion of the audit:

· Import CEP Information-Imports system CEP-in and system CEP-out revenue
summaries by machine.

· Audit CEP Meters-Audit and correct CEP-in and CEP-out variances between actual
and meters.


<table>
<tr>
<th colspan="2" rowspan="2">CEP In ☒ Count: CEP Out ☐ Amount($):</th>
<th>0</th>
<th>☐ Al Machines</th>
<th></th>
<th></th>
<th colspan="2" rowspan="2">Comment Act</th>
<th></th>
<th></th>
<th></th>
<th>Comment</th>
<th>Actual</th>
<th>Meters Accept</th>
</tr>
<tr>
<td>☐ 0.00</td>
<td colspan="2">☐ Exceptions</td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>Machine Location</th>
<th>Denom CEPI</th>
<th>Meter Legacy</th>
<th>Non-Deduct Meter</th>
<th>Total CEPI Meter</th>
<th>Actual Xtra Credit (PM)</th>
<th>Actual Promo Credit (EZPay) Actual Credit Meter</th>
<th>Actual Point Play Total System CEPI</th>
<th>NR. Bonus Meter</th>
<th>Net System CEPI</th>
<th>Variance</th>
<th>Percent</th>
<th>Accepted</th>
<th>Comment PreviousVariance</th>
</tr>
</table>




![](MachineAccounting_UserGuide_images/270.1.png)




Figure 23-2 Columns for CEP In




![](MachineAccounting_UserGuide_images/270.2.png)




<table>
<caption>Figure 23-3 Columns for CEP Out The following table lists and describes the meter columns on the CEP Audit window:</caption>
<tr>
<th>Column</th>
<th>CEP IN</th>
<th>CEP Out</th>
<th>Description</th>
</tr>
<tr>
<td>Machine</td>
<td>☒ X</td>
<td>☒ X</td>
<td>Machine ID</td>
</tr>
<tr>
<td>Location</td>
<td>☒ X</td>
<td>☒ X</td>
<td>Location of the machine</td>
</tr>
<tr>
<td>Denom</td>
<td>☒ X</td>
<td>☒ X</td>
<td>Denomination of the machine</td>
</tr>
<tr>
<td>EZ Pay CEP Out</td>
<td></td>
<td>☒ X</td>
<td>Information sent from EZ Pay</td>
</tr>
<tr>
<td>CEPI In (Cashable Electronic Promotion In)</td>
<td>☒ X</td>
<td></td>
<td>SAS 6 (AFT Bonusing) and G2S games only. Includes Xtra Credit, PointPlay, and Bonus meters</td>
</tr>
<tr>
<td>Legacy Non-Deduct Meter</td>
<td>☒ X</td>
<td></td>
<td>SAS 4 and 5, not including Xtra Credit, or SAS 6 before code, which includes PointPlay and Bonus meters</td>
</tr>
<tr>
<td>Total CEPI Meter</td>
<td>☒ X</td>
<td></td>
<td>CEPI Meter + Legacy Non-Deduct Meter</td>
</tr>
<tr>
<td>CEPO Meter</td>
<td></td>
<td>☒ X</td>
<td>Cashable Electronic Promo Out Meter</td>
</tr>
<tr>
<td>Actual Xtra Credit (PM)</td>
<td>☒ X</td>
<td></td>
<td>Information comes from player tracking</td>
</tr>
<tr>
<td>Actual Promo Credit (EZ Pay)</td>
<td>☒ X</td>
<td></td>
<td>Information comes from EZ Pay</td>
</tr>
<tr>
<td>Actual Credit Meter</td>
<td>☒ X</td>
<td></td>
<td>Bonus payments to the meter (taxed)</td>
</tr>
<tr>
<td>Actual Point Play</td>
<td>☒ X</td>
<td></td>
<td>PointPlay to Credit Meter</td>
</tr>
<tr>
<td>Total System CEPI</td>
<td>☒ X</td>
<td></td>
<td>Actual Xtra Credit PM + Actual Promo Credit (EZ Pay) + Actual Credit Meter + Actual PointPlay</td>
</tr>
<tr>
<td>NR Bonus Meter</td>
<td>☒ X</td>
<td></td>
<td>Legacy Xtra Credit (non-taxed) SAS 4 and 5</td>
</tr>
<tr>
<td>Net System CEPI</td>
<td>☒ X</td>
<td></td>
<td>Total System CEPI + NR Bonus Meter</td>
</tr>
<tr>
<td>Variance</td>
<td>☒ X</td>
<td>☒ X</td>
<td>Net System CEPI - Total CEPI</td>
</tr>
<tr>
<td>Percent</td>
<td>☒ X</td>
<td>☒ X</td>
<td>Percentage of variance</td>
</tr>
<tr>
<td>Accepted</td>
<td>☒ X</td>
<td>☒ X</td>
<td>Checked or unchecked</td>
</tr>
<tr>
<td>Comment</td>
<td>☒ X</td>
<td>☒ X</td>
<td>Comment on the audit</td>
</tr>
<tr>
<td>Previous Variance</td>
<td>☒ X</td>
<td>☒ X</td>
<td>Variance on the previous audit period</td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="270" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->


### 23.1 Importing CEP Drop Data

To import CEP drop data:

1\. Click Cashable Electronics Promotion in the Period Timeline or User Tasks list. A list
of options appears.

2\. Click Import CEP Information. The Retrieving Drop progress window appears.




![](MachineAccounting_UserGuide_images/271.1.png)




3\. Click Done after the CEP drop is complete. The CEP drop information is imported.


### 23.2 CEP Variances

Resolve CEP variances by accepting them or by adjusting a drop or meter.


#### 23.2.1 Accepting CEP Variances

To accept a CEP variance:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit window opens.




![](MachineAccounting_UserGuide_images/271.2.png)




3\. Select a machine.

4\. Click Accept in the CEP Audit window if the variance is within established guidelines. A
confirmation prompt appears.

5\. Click Yes. The variance is accepted. The updated CEP Audit window reappears without
the the machine voucher variance.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="271" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->


#### 23.2.2 Adjusting CEP Drops

To adjust a CEP drop:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit window opens.

3\. Select All Machines or Exceptions. The audit CEP meters displayed filter accordingly.

4\. Select a machine.

5\. Click Actual. The System CEP Adjust for Machine window appears.




![](MachineAccounting_UserGuide_images/272.1.png)




<table>
<tr>
<th colspan="5">System CEP Adjust for Machine - 100000 X</th>
</tr>
<tr>
<th>Machine Number:</th>
<th>100000</th>
<th></th>
<th colspan="2">Next Machine</th>
</tr>
<tr>
<td>Actual Xtra Credit:</td>
<td>0.00</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td>Actual Point Play:</td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Actual Bonus To Credit Meter:</td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="4">Non-restricted Bonus Meter: Net System CEPI: Total CEPI Meter: Variance:</td>
<td>0.00</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>0.00</td>
<td></td>
<td colspan="2">OK</td>
</tr>
<tr>
<td>0.00</td>
<td></td>
<td>Cancel</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</table>


6\. Enter the adjusted amounts in the Actual Xtra Credit, Actual Point Play, and Actual
Bonus To Credit Meter fields.

7\. Click OK. The adjustments save.


#### 23.2.3 Adjusting CEP Meter Variances

To adjust a CEP meter variance:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit window opens.

3\. Select All Machines or Exceptions. The audit CEP meters displayed filter accordingly.

4\. Select a machine.

5\. Click Meters. The CEP Meter Adjustment for Machine window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="272" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->




![](MachineAccounting_UserGuide_images/273.1.png)




<table>
<tr>
<td colspan="6">CEP Meter Adjustment for Machine - 30001 ☒ X</td>
</tr>
<tr>
<td colspan="6">CEPI Meter</td>
</tr>
<tr>
<td></td>
<td>Prior Meter</td>
<td>4,500</td>
<td>Adjustment</td>
<td></td>
<td>Next Machine</td>
</tr>
<tr>
<td></td>
<td>Today's Meter</td>
<td>5,000</td>
<td>New Value</td>
<td>5.00</td>
<td></td>
</tr>
<tr>
<td colspan="2">Mtr Value ($)</td>
<td>5.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="6">Legacy Non-Deduct Meter</td>
</tr>
<tr>
<td></td>
<td>Prior Meter</td>
<td>0</td>
<td>Adjustment</td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Today's Meter</td>
<td>0</td>
<td>New Value</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td colspan="2">Mtr Value ($)</td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="6">Non-Restricted Bonus Meter</td>
</tr>
<tr>
<td></td>
<td>Prior Meter</td>
<td>6,325</td>
<td>Adjustment</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Today's Meter</td>
<td>6,395</td>
<td>New Value</td>
<td>0.70</td>
<td>OK</td>
</tr>
<tr>
<td colspan="2">Mtr Value ($)</td>
<td>0.70</td>
<td></td>
<td></td>
<td>Cancel</td>
</tr>
<tr>
<td colspan="6"></td>
</tr>
</table>


6\. Enter the meter values in the CEPI Meter, Legacy Non-Deduct Meter, and Non-Restricted
Bonus Meter fields, as applicable.

7\. Click OK. The adjustments save.


#### 23.3 CEP-In Variances

The CEP In is obtained through EZ Pay and Player Tracking.


##### 23.3.1 Viewing Audit CEP Meters

To view audit CEP-in meters:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit Meters window opens.




![](MachineAccounting_UserGuide_images/273.2.png)




<table>
<tr>
<th>Machine</th>
<th>Location</th>
<th>Denom</th>
<th>CEPI Meter</th>
<th>Legacy Non-Deduct Meter</th>
<th>Total CEPI Meter</th>
<th>Actual Xbra Crede (PMI)</th>
<th>Actual Promo Credit (EZPay)</th>
<th>Actual Credit Meter</th>
</tr>
<tr>
<td>3329</td>
<td>519180</td>
<td>0.01</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>3395</td>
<td>58939933</td>
<td>0.01</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
</table>


3\. Select CEP In. The CEP Audit Meters window displays audit CEP-in meters.

4\. Select All Machines or Exceptions to filter which CEP data appears.


##### 23.3.2 Adjusting CEP-In Meter Variances

To adjust CEP in meter variances:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit Meters window opens.

3\. Select a machine.

4\. Click Meters. The CEP In Meter Adjustment for Machine window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="273" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->




![](MachineAccounting_UserGuide_images/274.1.png)




5\. Enter the adjusted meter values in the adjustment fields in the CEPI Meter, Legacy Non-
Deduct Meter, and Non-Restricted Bonus Meter areas, as needed.

6\. Click OK. The adjustments save.


##### 23.3.3 Accepting CEP-In Variances

To accept CEP-in variances:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit Meters window opens.

3\. Select a machine.
OR
Press Ctrl + click to select multiple machines.

4\. Click Accept if the variances are within established guidelines. A confirmation message
appears.

5\. Click Yes. The variances are accepted.


##### 23.3.4 Unaccepting CEP-In Variances

To unaccept a CEP-in variance:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit Meters window opens.

3\. Select a machine.

4\. Click Unaccept if the variance is not within established guidelines. A confirmation
message appears.

5\. Click Yes. The variance is no longer accepted.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="274" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->


##### 23.4 CEP-Out Variances

The CEP-out drop is obtained from the EZ Pay end-of-day.

To display CEP-out variances:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit Meters window opens.


<table>
<tr>
<th colspan="2" rowspan="2">CEP In ☐ CEP Out ☒</th>
<th colspan="2" rowspan="2">Count: Amount($):</th>
<th>8</th>
<th colspan="4" rowspan="2">☐ All Machines ☐ Exceptions</th>
</tr>
<tr>
<th>0.00</th>
</tr>
<tr>
<th>Machine</th>
<th>Location</th>
<th>Denom</th>
<th colspan="2">CEPO Meter EZPay</th>
<th>CEP Out</th>
<th>Variance</th>
<th>Percent</th>
<th>Accepted Comment</th>
</tr>
<tr>
<td>3329</td>
<td>S19180</td>
<td>0.01</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>3395</td>
<td>58939933</td>
<td>0.01</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>3401</td>
<td>58931212</td>
<td>0.01</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>3441</td>
<td>MA930301</td>
<td>0.01</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>3443</td>
<td>589301</td>
<td>0.01</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>3445</td>
<td>NGX9302</td>
<td>0.01</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>3446</td>
<td>MA930101</td>
<td>0.01</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>4604</td>
<td>SAS69301</td>
<td>0.05</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
</table>




![](MachineAccounting_UserGuide_images/275.1.png)




3\. Select CEP Out.

4\. Select All Machines or Exceptions to filter the displayed vouchers.


#### 23.4.1 Adjusting CEP-Out Meter Variances

To adjust CEP-out variances:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit Meters window opens.

3\. Select a machine.

4\. Click Meters. The CEP Out Meter Adjustment for Machine window appears.




![](MachineAccounting_UserGuide_images/275.2.png)




<table>
<tr>
<td colspan="2">CEP Out Meter Adjustment for Machine - 3433</td>
<td colspan="3">X</td>
</tr>
<tr>
<td>Value Meter</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Prior Meter</td>
<td>2,150</td>
<td>Adjustment</td>
<td></td>
<td>Next Machine</td>
</tr>
<tr>
<td>Today's Meter</td>
<td>2.150</td>
<td>New Value</td>
<td>300.00</td>
<td></td>
</tr>
<tr>
<td>Mtr Value [$)</td>
<td>300.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Count Meter</td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>Prior Meter</td>
<td>N/A</td>
<td>Adjustment</td>
<td>N/A</td>
<td></td>
</tr>
<tr>
<td>Today's Meter</td>
<td>N/A</td>
<td>New Count</td>
<td>0</td>
<td>OK</td>
</tr>
<tr>
<td>Mtr Count</td>
<td>N/A</td>
<td></td>
<td></td>
<td>Cancel</td>
</tr>
</table>


5\. Enter the adjusted meter value in the Adjustment field on the Value Meter pane.

6\. Click OK. The adjustment is saved.


#### 23.4.2 Accepting CEP-Out Variances

To accept CEP-out variances:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit Meters window opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="275" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->

3\. Select a machine.
OR
Press Ctrl + click to select multiple machines.

4\. Click Accept if the variances are within established guidelines. A confirmation prompt
appears.

5\. Click Yes. The variances are accepted.


### 23.4.3 Unaccepting CEP-Out Variances

To unaccept a CEP-out variance:

1\. Click Cashable Electronic Promotion in the Period Timeline or the User Tasks list. A
list of tasks appears.

2\. Click Audit CEP Meters. The CEP Audit Meters window opens.

3\. Select a machine.

4\. Click Unaccept if the variance is not within established guidelines. A confirmation
prompt appears.

5\. Click Yes. The variance is no longer accepted.


### 23.5 CEP Audit Checklist

The CEP Audit Checklist provides a step-by-step list needed to complete the CEP audit. If
desired, print the following table for use as a checklist while completing each task.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="276" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->


# CEP Audit Checklist




![](MachineAccounting_UserGuide_images/277.1.png)




<table>
<tr>
<th>Audit Date:</th>
<th colspan="4"></th>
</tr>
<tr>
<td>Audit Signature:</td>
<td colspan="4"></td>
</tr>
<tr>
<td></td>
<td colspan="4"></td>
</tr>
<tr>
<td rowspan="5">Importing CEP Information</td>
<td rowspan="5">☐ Step 1</td>
<td colspan="3">1. Click Cashable Electronic Promotion in the User Task Tree, then click Import CEP Information.</td>
</tr>
<tr>
<td rowspan="4"></td>
<td>Retrieving Drop</td>
<td></td>
</tr>
<tr>
<td>= Drop Retrieval $ Drop data is being retrieved. Please wait</td>
<td rowspan="2"></td>
</tr>
<tr>
<td>Retrieving CEP Drop ...</td>
</tr>
<tr>
<td>Cancel Done</td>
<td></td>
</tr>
<tr>
<td>Audit CEP Meters Window</td>
<td>☐ Step 2</td>
<td colspan="3">The CEP Audit window displays information in columns as follows: · CEPI Meter. SAS 6 Aft Bonusing and SBX (G2S) games only. This meter includes Xtra Credit, PointPlay, and Bonus meters. · Legacy Non-Deduct Meter: SAS 4, 5, and 6 Legacy Bonusing games. Includes PointPlay and Bonus meters. Does not include Xtra Credit. · Total CEPI Meter: CEPI meter + legacy non-deduct meter. · Actual Xtra Credit: Amount comes from Patron Management. · Actual Credit Meter: Bonus payments transferred to the credit meter. · Actual Point Play: PointPlay transferred to the credit meter. · Total system CEPI: Actual Xtra Credit + actual credit meter + actual point play. · NR Bonus Meter: Xtra Credit meter movement in Machine Accounting. . Net System CEPI: Total system CEPI + NR bonus meter. · Variance: Net System CEPI - Total System CEPI.</td>
</tr>
<tr>
<td></td>
<td></td>
<td colspan="3">1. Click Audit CEP Meters in the User Tasks list. 2. Select All Machines. Right-click and export this screen to Excel. Remove unnecessary columns. Auto-sum each column. 3. In MA, print the Gaming Meter Report in summary view. Balance the Non-Restricted Bonus column to the NR Bonus Meter column from the CEP Audit window.</td>
</tr>
<tr>
<td rowspan="3">Audit CEP Meters</td>
<td rowspan="3">☐ Step 3</td>
<td colspan="3">4. For hybrid floors (SAS amd G2S)-In MA, print the Metered Slot Win with Promo Report in summary view. Balance the CEPI numbers to the corresponding column from the CEP Audit window.</td>
</tr>
<tr>
<td colspan="3">5. In MA, print the Non-Deductible Detail Report. Confirm that the numbers balance to the corresponding columns from the CEP Audit window.</td>
</tr>
<tr>
<td colspan="3">6. In Patron Management (PM), print the Bonus Activity by Machine report in summary view. Balance the Xtra Credit Used column on the PM report to the Actual Xtra Credit column from the CEP Audit window.</td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="277" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->


<table>
<tr>
<td></td>
<td></td>
<td colspan="4">CEP Audit Checklist</td>
</tr>
<tr>
<td rowspan="2">Investigate CEP Audit Variances</td>
<td rowspan="2">☐ Step 4</td>
<td colspan="4">1. In the CEP Audit Meter window, clear all machines so that only the machines showing variances remain. 2. Review machine events for the games with variances. Investigate Xtra Credit payment failures according to internal controls.</td>
</tr>
<tr>
<td colspan="4">3. In PM, print the Bonus Adjustment Report in summary view. Review the Xtra Credit adjustments. Investigate and document any exceptions according to internal controls.</td>
</tr>
<tr>
<td rowspan="6">Troubleshooting Tips</td>
<td rowspan="6">☐ Step 5</td>
<td colspan="4">Confirm that the meters are accurately corrected within Correct Meter Variances.</td>
</tr>
<tr>
<td colspan="4">Was the player card still in event mode? Did they remove their card after EOD? The players account updates when the card is removed from the game.</td>
</tr>
<tr>
<td colspan="4">Was there a communication loss on the game or system?</td>
</tr>
<tr>
<td colspan="4">PointPlay can be used at the machine in two ways (based on the PM configuration):</td>
</tr>
<tr>
<td colspan="4">1. The system is configured to convert PointPlay to playable-only Xtra Credit. This is the most common option used. 2. The system is configured to send PointPlay directly to the credit meter. This option is cashable and taxable.</td>
</tr>
<tr>
<td colspan="4">For hybrid floors (SAS and G2S): If there is a difference between the CEP in and CEP played, this amount goes into the non-deductible column on the Metered Slot Win with Promo report. Reconcile amounts in this column according to internal controls.</td>
</tr>
<tr>
<td rowspan="9">Placing Machine Comments</td>
<td rowspan="9">☐ Step 6</td>
<td colspan="4">1. After completing the investigation, select the machine, then click Comment. The Machine Comment window displays.</td>
</tr>
<tr>
<td rowspan="6"></td>
<td colspan="3">Comment x</td>
</tr>
<tr>
<td colspan="3">Comment Information</td>
</tr>
<tr>
<td>Machine:</td>
<td>10001</td>
<td>OK</td>
</tr>
<tr>
<td rowspan="3">Period Date: Comment: Active Comment</td>
<td>07/23/2012</td>
<td>Cancel</td>
</tr>
<tr>
<td colspan="2">Machine Malfunction Advanced</td>
</tr>
<tr>
<td colspan="2">☒</td>
</tr>
<tr>
<td colspan="4">2. Click the Comment drop-down, then select a reason, or select &lt;New&gt; to enter a new comment.</td>
</tr>
<tr>
<td colspan="4">1 Select Active Comment if the comment will be used repeatedly. Select Advanced to configure active and inactive comments.</td>
</tr>
<tr>
<td>Accepting CEP Variances</td>
<td>☐ Step 7</td>
<td colspan="4">1. After completing the investigation, select the machine, then click Accept. A confirmation message appears. 2. Click Yes. The variance is accepted, and the window no longer displays the machine.</td>
</tr>
</table>




![](MachineAccounting_UserGuide_images/278.1.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="278" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->


<table>
<tr>
<th colspan="9">CEP Audit Checklist</th>
</tr>
<tr>
<th rowspan="5"></th>
<th rowspan="5"></th>
<th colspan="7">1. Select the machine to adjust. Click Actual. The System CEP Adjust for Machine window appears.</th>
</tr>
<tr>
<td></td>
<td colspan="6">System CEP Adjust for Machine - 30001</td>
</tr>
<tr>
<td rowspan="2"></td>
<td>Machine Number:</td>
<td>30001</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Actual Xtra Credit:</td>
<td></td>
<td>6.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Actual Point Play:</td>
<td></td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="5">Adjusting Actual CEP Information</td>
<td rowspan="5">☐ Step 8</td>
<td></td>
<td>Actual Bonus To Credit Meter:</td>
<td></td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Non-restricted Bonus Meter:</td>
<td></td>
<td>0.70</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Net System CEPI:</td>
<td></td>
<td>5.30</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Total CEPI Meter:</td>
<td></td>
<td>5.00</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Variance:</td>
<td colspan="2">0.30</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td></td>
<td></td>
<td colspan="7" rowspan="2">2. Enter the corrected information in the Actual Xtra Credit, Actual Point Play, or Actual Bonus to Credit Meter field. Click OK.</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="15">Adjusting Metered CEP Information</td>
<td rowspan="14">☐ Step 9</td>
<td colspan="7">1. Select the machine to adjust. Click Meters. The CEP Meter Adjustment for Machine window appears.</td>
</tr>
<tr>
<td rowspan="10"></td>
<td colspan="6">CEP Meter Adjustment for Machine - 30001 ×</td>
</tr>
<tr>
<td>CEPI Meter</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Prior Meter</td>
<td>4,500</td>
<td>Adjustment</td>
<td></td>
<td>Next Machine</td>
<td></td>
</tr>
<tr>
<td>Today's Meter</td>
<td>5,000</td>
<td>New Value</td>
<td>5.00</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mtr Value ($)</td>
<td>5.00</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Legacy Non-Deduct Meter</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Prior Meter</td>
<td>0</td>
<td>Adjustment</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Today's Meter</td>
<td>0</td>
<td>New Value</td>
<td>0.00</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mtr Value ($)</td>
<td>0.00</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Non-Restricted Bonus Meter</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="3"></td>
<td>Prior Meter</td>
<td>6,325</td>
<td>Adjustment</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Today's Meter</td>
<td>6,395</td>
<td>New Value</td>
<td>0.70</td>
<td>OK</td>
<td></td>
</tr>
<tr>
<td>Mtr Value ($)</td>
<td>0.70</td>
<td></td>
<td></td>
<td colspan="2">Cancel</td>
</tr>
<tr>
<td></td>
<td colspan="7" rowspan="2">2. Enter the correct amount in the CEPI Meter, Legacy Non-Deduct Meter, or Non-Restricted Bonus Meter field. To make adjustments to the meter values without overwriting the existing value, enter a plus (+) or minus (-) in front of the change. 3. Click OK.</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</table>




![](MachineAccounting_UserGuide_images/279.1.png)






![](MachineAccounting_UserGuide_images/279.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="279" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 23 Cashable Electronic Promotion (CEP)" -->

This page is intentionally left blank.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="280" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/281.1.png)




