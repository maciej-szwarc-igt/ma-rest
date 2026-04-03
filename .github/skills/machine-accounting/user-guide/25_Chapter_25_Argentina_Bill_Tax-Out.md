# Chapter 25 Argentina Bill Tax-Out

The default setting for the Argentina Bill TaxOut feature (mandatory or non-mandatory) is
determined at the time of installation. Configure this feature at Options > General >
Argentina Tax Deduction. Refer to Argentina Tax Feature on page 349 for more
information.

The following tasks are available for completing the Argentina Bill TaxOut portion of the audit:

· Import Bill TaxOut Information-Retrieve and display information.

· Audit Bill TaxOut Meters-View details for bill tax-out meters.


## To access the Argentina Bill TaxOut tasks:

Click Argentina Bill TaxOut in the User Tasks list OR Period Timeline. The Argentina Bill
TaxOut tasks appear.




![](MachineAccounting_UserGuide_images/289.2.png)




Figure 25-1 User Tasks List-Argentina Bill TaxOut Tasks

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="289" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 25 Argentina Bill Tax-Out" -->


# 25.1 Importing Bill Tax-Out Information

To import the Argentina bill tax-out information:

1\. If necessary, select Open Period from the toolbar. The current audit period appears.

2\. Click Argentina Bill TaxOut in the User Tasks list or Period Timeline. The Argentina
Bill TaxOut tasks appear.

3\. Click Import Bill TaxOut Information. The Retrieving Drop window appears.




![](MachineAccounting_UserGuide_images/290.1.png)




4\. Click Done when the tax out post is complete. The Retrieving Drop window closes.


# 25.2 Auditing Bill Tax-Out Meters

To process the current Audit Bill TaxOut Meters information:

1\. Click Argentina Bill TaxOut in the User Tasks list or Period Timeline. The Argentina
Bill TaxOut tasks appear.




![](MachineAccounting_UserGuide_images/290.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="290" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 25 Argentina Bill Tax-Out" -->




![](MachineAccounting_UserGuide_images/291.1.png)




If not already completed, click Import Bill TaxOut Information before
continuing. Refer to Importing Bill Tax-Out Information on page 290 for more
information.

2\. Click Audit Bill TaxOut Meters. The Argentina Bill Taxout Audit window appears.




![](MachineAccounting_UserGuide_images/291.2.png)




<table>
<tr>
<th>Mnum</th>
<th>Location</th>
<th>Denom</th>
<th>Meter Bill Taxout</th>
<th>Actual Bill Taxout</th>
<th>Variance</th>
<th>Percent</th>
<th>Accepted</th>
<th>Comment</th>
<th>PreviousVariance</th>
</tr>
<tr>
<td>4006</td>
<td>BUFF0C02</td>
<td>0.01</td>
<td>0.00</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td></td>
<td></td>
<td>-0.25</td>
</tr>
<tr>
<td>4023</td>
<td>BUFFOA03</td>
<td>0.01</td>
<td>0.00</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td></td>
<td></td>
<td>0.00</td>
</tr>
<tr>
<td>4024</td>
<td>BUFFOA08</td>
<td>0.01</td>
<td>0.00</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td></td>
<td></td>
<td>-0.02</td>
</tr>
<tr>
<td>4025</td>
<td>BUFF0C08</td>
<td>0.01</td>
<td>0.00</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td></td>
<td></td>
<td>-0.02</td>
</tr>
<tr>
<td>4026</td>
<td>BUFFOJ01</td>
<td>0.01</td>
<td>0.00</td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td></td>
<td></td>
<td>0.00</td>
</tr>
</table>




![](MachineAccounting_UserGuide_images/291.3.png)




Select All Machines or Exceptions to filter the displayed machines.

3\. Select a machine with a variance, then click Actual. The Actual Bill Taxout Adjust for
Machine window appears.




![](MachineAccounting_UserGuide_images/291.4.png)




4\. If needed, enter the correct amount in the Actual Amount field.

5\. Click OK OR click Next Machine, then repeat step 4 for each machine meter variance.

6\. Highlight the same machine with the variance, then click Meters. The Bill Taxout Meter
Adjustment for Machine window appears.




![](MachineAccounting_UserGuide_images/291.5.png)




7\. Enter the amount of the adjustment in the Adjustment field.

8\. Click OK OR click Next Machine and repeat step 7 for each machine adjustment.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="291" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 25 Argentina Bill Tax-Out" -->

9\. Highlight the same machine with the variance, then click Comment. The Comment
window appears.




![](MachineAccounting_UserGuide_images/292.1.png)




10\. Select a comment from the Comment drop-down list. If the applicable comment is not
listed:

a. Click Advanced. The Comment Status window appears.




![](MachineAccounting_UserGuide_images/292.2.png)




b. Select an applicable comment from the Inactive column.

c. Click > to move the comment from the Inactive column to the Active column.
OR
Click >> to move all options from the Inactive column to the Active column.

d. Click OK. The Comment Status changes save.

e. Select an applicable comment from the Comment drop-down list on the Comment
window.

11\. Click OK.

12\. Highlight the same machine with the variance, then click Accept. The Argentina Bill
Taxout Audit window updates with the new information.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="292" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 25 Argentina Bill Tax-Out" -->


<table>
<caption>The following table lists and describes each column in the Argentina Bill Taxout Audit table:</caption>
<tr>
<th colspan="2">Argentina Bill Tax-Out Audit Column Description</th>
</tr>
<tr>
<td>Mnum</td>
<td>Machine number</td>
</tr>
<tr>
<td>Location</td>
<td>Location of the machine</td>
</tr>
<tr>
<td>Denom</td>
<td>Primary denomination of the machine</td>
</tr>
<tr>
<td>Meter Bill Taxout</td>
<td>Taxout bill meter amount</td>
</tr>
<tr>
<td>Actual Bill Taxout</td>
<td>Actual bill taxout amount</td>
</tr>
<tr>
<td>Variance</td>
<td>Difference between the Meter Bill Taxout and Actual Bill Taxout amounts</td>
</tr>
<tr>
<td>Percent</td>
<td>Bill tax rate percentage</td>
</tr>
<tr>
<td>Accepted</td>
<td>Can be Yes or No</td>
</tr>
<tr>
<td>Comment</td>
<td>Comments made concerning the variance and/or acceptance of the variance</td>
</tr>
<tr>
<td>Previous Variance</td>
<td>Amount of variance for the previous audit period</td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="293" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 25 Argentina Bill Tax-Out" -->

This page is intentionally left blank.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="294" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/295.1.png)




