# Chapter 11 Configuring Lease Machines

Use the Configure Lease Machines feature to configure a leased machine fee structure based on
meters or Machine Accounting fields. This is a fee-type structure, so it can also be used for
taxes and other fees.




![](MachineAccounting_UserGuide_images/161.2.png)




An accounting period must be open to modify or add a new setting.

Configure lease machines in the following order:

1\. Formula

2\. Rule(s)

3\. Lease settings

4\. Machine assignments

Note the following when configuring leased machines:

· Assign a machine to only one setting at a time.

· A setting may have multiple machines.

· A setting may have multiple rules assigned to it.

· A rule may only be assigned to one setting.

· Each rule contains a formula, which can be created.

· Assign each formula to only one rule.

· Retired machines must be part of a lease pool to maintain previous lease-participation
information. The lease participation information for a machine cannot be modified
after the machine is retired.


## To view lease machine information:

Navigate to IGT Spade > Configurations > Configure Lease Machines. The Lease
Machines window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="161" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 11 Configuring Lease Machines" -->




![Figure 11-1 Configure Lease Machines](MachineAccounting_UserGuide_images/162.1.png)




### 11.1 Lease Rules

Use lease rules to create user formulas. Lease rules also allow formulas to be overridden and
limit what the formulas apply to. A lease rule is not required if the machine is only using a
daily amount.


#### 11.1.1 Creating Lease Rules

To create a lease rule:

1\. Navigate to IGT Spade > Configuration > Configure Lease Machines. The Lease
Machines window appears.

2\. In the Rules assigned to setting pane of the Lease Machine window, click New Rule. The
Rule window appears.




![](MachineAccounting_UserGuide_images/162.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="162" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 11 Configuring Lease Machines" -->

3\. Enter a description of the rule in the Rule description field.

4\. In the Select Formula field, select a formula to calculate with the percent or fixed amount
of the given options. (For example, select Meter Coin In with 3% for the lease machine
rule to calculate three percent of the metered coin in for the lease amount.)

5\. Enter the percentage to apply to the formula in the Percent field.

6\. Enter an amount that overrides or is added to the rule in the Fixed amount field. (This
only applies when the rule amount is in use.)

7\. Select how the fixed amount is applied from the Fixed amount behavior drop-down list:

· Fixed Amount Always Applies

· Fixed Amount Overrides if Larger

· Fixed Amount Overrides if Smaller

· No Fixed Amount

8\. In the Formula range pane, enter the lower and upper values in the corresponding text
boxes.




![](MachineAccounting_UserGuide_images/163.1.png)




Ť
Formula Range determines when the formula is valid. This helps to eliminate
negative values or to set up multiple percentages based on win or play. Limits do
not factor in the fixed amount. They only factor in the amount that the formula
generates.


### 11.1.2 Configuring Formulas


#### To configure formulas for a lease rule:

1\. Refer to Creating Lease Rules on page 162 for more information.

2\. Select a rule in the Rules assigned to setting section, then click Edit Selected Rule. The
Rule window appears.

3\. Click Config Formulas. The Formula Manager window appears.




![](MachineAccounting_UserGuide_images/163.2.png)




4\. Click New. The Formula builder window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="163" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 11 Configuring Lease Machines" -->




![](MachineAccounting_UserGuide_images/164.1.png)




5\. Enter the name of the formula in the Formula name field.

6\. Double-click a meter in the Available Meters pane to add that meter to the formula.

7\. Enter + or - next to the meter name to indicate added or subtracted.

8\. Add additional available meters and symbols as needed.




![](MachineAccounting_UserGuide_images/164.2.png)




9\. Click Validate to test the formula. A confirmation message appears with the validation
results.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="164" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 11 Configuring Lease Machines" -->




![](MachineAccounting_UserGuide_images/165.1.png)




10\. Click OK. The confirmation message closes.

11\. Click OK. The formula is added, and the Rule window reappears.

12\. Click OK. The settings save, and the Lease Machine window reappears.


### 11.1.3 Editing Lease Rules

To edit a lease rule:

1\. Navigate to IGT Spade > Configuration > Configure Lease Machines. The Lease
Machines window appears.

2\. Select a rule in the Rules assigned to setting section, then click Edit Selected Rule. The
Rule window appears.

3\. Edit the fields as necessary.

4\. Click OK. The settings save, and the Lease Machine window reappears.


### 11.1.4 Deleting Lease Rules

To delete a lease rule:

1\. Navigate to IGT Spade > Configuration > Configure Lease Machines. The Lease
Machines window appears.

2\. Select a setting from the Lease setting drop-down list.

3\. Highlight the rule to delete in the Rules assigned to setting section OR press and hold
CTRL to highlight multiple rules.

4\. Click Delete Selected Rule(s). A confirmation message appears.

5\. Click Yes. The selected rules are deleted.


### 11.2 Lease Settings

Create a lease setting BEFORE setting up a machine to use a lease formula. A lease setting is a
master controller of lease rules. It dictates the rules' behavior.


#### 11.2.1 Creating Lease Settings

To create a lease setting:

1\. Navigate to IGT Spade > Configuration > Configure Lease Machines. The Lease
Machines window appears.

2\. In the Lease setting pane, click New Setting. The Lease Setting window opens.

3\. Enter the setting's name in the Setting name field.

4\. Enter the lease amount in the Daily lease amount field.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="165" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 11 Configuring Lease Machines" -->




![](MachineAccounting_UserGuide_images/166.1.png)




This is a fixed amount per day that can be added to the machine's lease total.

5\. Click Daily lease amount behavior, then select one of the following options:

· Daily Amount Overrides when Larger

· Daily Amount Overrides when Smaller

· No Daily Amount-This inactivates the Daily lease amount field.
This setting controls how the daily amount is applied.




![](MachineAccounting_UserGuide_images/166.2.png)




6\. Click Lease rule behavior, then select one of the following options:

· Add All Rules

· Use Largest Rule

· Use Smallest Rule




![](MachineAccounting_UserGuide_images/166.3.png)




i
This controls how multiple rules interact with each other. The user has the
flexibility to base the lease amount on multiple rules and thresholds.

7\. Click OK. The lease setting is created, and the Lease Machine window reappears.


#### 11.2.2 Deleting Settings




![](MachineAccounting_UserGuide_images/166.4.png)




i
A lease setting cannot be deleted until all rules and machines associated with the
setting are disassociated.

To delete a lease setting:

1\. Navigate to IGT Spade > Configuration > Configure Lease Machines. The Lease
Machines window appears.

2\. Click the Lease setting drop-down list, then select a setting.

3\. Click Delete Setting. A confirmation prompt displays.

4\. Click Yes. The setting is deleted, and the Lease Machines window reappears.


#### 11.2.3 Editing Settings

To edit a lease setting:

1\. Navigate to IGT Spade > Configuration > Configure Lease Machines. The Lease
Machines window appears.

2\. Click the Lease setting drop-down list, then select a setting.

3\. Click Edit Setting. The Lease Setting window appears.

4\. Complete the necessary modifications.

5\. Click OK. The changes save, and the Lease Machine window reappears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="166" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 11 Configuring Lease Machines" -->


## 11.3 Assigning Machines to Lease Settings

Once lease settings are established, machines can be assigned to them.


### To assign a machine to a lease setting:

1\. Navigate to IGT Spade > Configuration > Configure Lease Machines. The Lease
Machines window appears.

2\. Click the Lease setting drop-down list, then select a setting.

3\. Click Add / Remove Machine(s). The Add / Remove Machines window opens.




![](MachineAccounting_UserGuide_images/167.1.png)




<table>
<tr>
<th>Mnum</th>
<th>Section</th>
<th>Bank</th>
<th>Location</th>
<th>Denom</th>
<th>Par</th>
<th>Manufacturer</th>
<th>Description</th>
</tr>
<tr>
<td>5015</td>
<td>A</td>
<td>01</td>
<td>05</td>
<td>0.01</td>
<td>5.00</td>
<td>IGT</td>
<td>IGT UPRIGHT</td>
</tr>
<tr>
<td>5021</td>
<td>A</td>
<td>01</td>
<td>06</td>
<td>0.01</td>
<td>5.00</td>
<td>IGT</td>
<td>IGT UPRIGHT</td>
</tr>
<tr>
<td>5031</td>
<td>A</td>
<td>01</td>
<td>08</td>
<td>0.01</td>
<td>5.00</td>
<td>IGT</td>
<td>IGT UPRIGHT</td>
</tr>
<tr>
<td>5009</td>
<td>A</td>
<td>01</td>
<td>10</td>
<td>0.01</td>
<td>5.00</td>
<td>IGT</td>
<td>MJP</td>
</tr>
</table>


Figure 11-2 Configure Lease Machines - Add / Remove Machines

4\. The Available unassign machines pane displays machines not assigned the selected lease
setting. Click the Section, Bank, Manufacturer, Denomination drop-down boxes to
select values and filter the machine display.

5\. Click Apply Select in the Available machines section to find the machines that match the
filter values indicated in the drop-down boxes.

6\. Select the machine to add to the lease setting, then click the UP arrow. The machine
appears in the Machines assigned to setting section.

· A machine can be assigned to only one lease setting.

· If a machine is assigned to a different setting, the Lease Setting drop-down box in the
Available machines section displays the description of the lease setting.

· Moving an already assigned machine will not assign it to the setting.

7\. Click OK. The machine is added, and the Lease Machines window reappears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="167" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 11 Configuring Lease Machines" -->

This page is intentionally left blank.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="168" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/169.1.png)




