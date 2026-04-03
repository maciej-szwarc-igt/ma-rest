# Chapter 7 Maintenance Workbook

Machine Accounting maintains detailed information on the location and configuration of
casino machines. Once machines are added to Machine Accounting using the Machine Wizard,
a user can do the following:

· View the locations of all machines

· Change a machine's information

· Test machine meters against actually deposited coins/bills

· View individual or groups of machines using system criteria over a selectable time
range

i

· Set up, define, and assign machines to drop zones

If the Machine Accounting system is connected to the IGT sbX™M system, the serial
numbers of all enrolled machines in Machine Accounting must match the cabinet
serial numbers in the IGT sbX system.


## To access the Maintenance Workbook:

Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance Workbook
window appears, with the Add/Retire Machines tab displaying a list of active machines.




![](MachineAccounting_UserGuide_images/111.2.png)




Select Warehouse to view only warehoused EGMs.




![](MachineAccounting_UserGuide_images/111.3.png)






![](MachineAccounting_UserGuide_images/111.4.png)




Enhancements to the Maintenance Workbook include the Protocol, Protocol
Version, and BE2 Version columns, as well as the Operator Payout tab.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="111" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->

The right side of the Maintenance Workbook window includes the following buttons:

· Machine Wizard-Adds a machine or changes the machine's system configuration.

· Machine Detail-Summarizes current information for active and warehoused machines.

· Detail Meters-Summarizes period information for active and warehoused machines.

· Current Meters-Summarizes current information as of the earliest opened accounting
period for active and warehoused machines.

· MGA Meters-Summarizes information about current meters for the paytable ID.

· Print Label-Prints barcode labels for machine identification.

· Print Workorder-Prints a work order for retiring or moving a machine.


## 7.1 Machine Wizard Overview

Use the Machine Wizard to add a machine or change a machine's system configuration. Access
the wizard from the Add/Retire Machines window.




![](MachineAccounting_UserGuide_images/112.1.png)




Verifying machine changes is an audit function and a part of the user task tree that
must be completed daily.

To display the Machine Wizard:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Click Machine Wizard. The Machine Wizard window opens.




![Figure 7-1 Machine Wizard](MachineAccounting_UserGuide_images/112.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="112" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->

Machine Wizard provides the options listed on the following table.


<table>
<tr>
<th>Function</th>
<th>Description</th>
</tr>
<tr>
<td>Verifying a machine Add, Retire or Move</td>
<td>Verify a machine's addition or move to, or retirement from, the casino floor within the audit process.</td>
</tr>
<tr>
<td>Update a machine</td>
<td>Change a machine's configuration change (for non-critical changes that do not affect the accounting data).</td>
</tr>
<tr>
<td>Add a new machine</td>
<td>Add a new machine to the casino floor.</td>
</tr>
<tr>
<td>Convert a machine</td>
<td>Change the denomination, game type or type code. Any change affecting the accounting data for the machine must be changed using this option. A machine conversion requires the machine (house) number to change.</td>
</tr>
<tr>
<td>Retire a machine</td>
<td>Remove a machine from the casino floor.</td>
</tr>
<tr>
<td>Change a machine's location</td>
<td>Move a machine to a different location on the casino floor.</td>
</tr>
<tr>
<td>Reset a machine's Unique ID/EGM ID</td>
<td>Change a machine's wiring harness and reset its unique ID. A harness might be changed due to a machine-communication failure or a harness update.</td>
</tr>
</table>


## 7.2 Adding New Machines




![](MachineAccounting_UserGuide_images/113.1.png)




If the IGT Advantage Machine Accounting system is connected to the IGT sbX
system, the serial numbers of all machines enrolled in Machine Accounting must
match the cabinet serial numbers in the IGT sbX system.

Asset numbers from Machine Accounting are automatically enrolled within the sbX
system.

To add a new machine:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.




![](MachineAccounting_UserGuide_images/113.2.png)




Ť
A brief description for each action appears when the corresponding option is
selected. All options are enabled if a specific machine is highlighted before the
Machine Wizard opens.

2\. Click Machine Wizard. The Machine Wizard window opens.

3\. Select I want to Add a new machine, then click Next. The Machine Setup Wizard window
appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="113" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/114.1.png)




<table>
<tr>
<th>Type ID</th>
<th>Description</th>
<th>Par</th>
<th>A</th>
</tr>
<tr>
<td>1</td>
<td>AVPGEMSIIFOUR</td>
<td>5.500</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>DC POKER</td>
<td>4.750</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>STARSTRUCK</td>
<td>5.250</td>
<td>E</td>
</tr>
<tr>
<td>5</td>
<td>1-CENT SAS 6</td>
<td>5.000</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>SB SERVICE WINDOW EGM</td>
<td>16.</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>VARIANCE</td>
<td>0.000</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>AUSTIN POKER</td>
<td>8.000</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>MNL 0.01</td>
<td>20 ..</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>SAS 5 1 CENT</td>
<td>8.330</td>
<td></td>
</tr>
<tr>
<td>22</td>
<td>NGX</td>
<td>5.000</td>
<td></td>
</tr>
<tr>
<td>27</td>
<td>SAS 6 LEGACY</td>
<td>5.590</td>
<td></td>
</tr>
<tr>
<td>32473</td>
<td>VARIANCE MACHINE</td>
<td>6.000</td>
<td></td>
</tr>
<tr>
<td>32475</td>
<td>SB - NONMDMG</td>
<td>0.000</td>
<td></td>
</tr>
<tr>
<td>32478</td>
<td>AUDIT .01 SAS 6 AFT</td>
<td>1.000</td>
<td></td>
</tr>
<tr>
<td>32479</td>
<td>AUDIT.01 SAS6 LEG</td>
<td>2.568</td>
<td>₹</td>
</tr>
<tr>
<td>1</td>
<td>TIT</td>
<td>1</td>
<td></td>
</tr>
</table>


The following table lists each information field listed on the Type ID pane:


<table>
<tr>
<th>Column</th>
<th>Description</th>
</tr>
<tr>
<td>Type ID</td>
<td>Assigned ID number for type</td>
</tr>
<tr>
<td>Description</td>
<td>Brief description of the machine type</td>
</tr>
<tr>
<td>Par</td>
<td>Hold percentage</td>
</tr>
<tr>
<td>Denom</td>
<td>Base denomination of the game</td>
</tr>
<tr>
<td>Max Bet</td>
<td>Maximum bet for each game-play opportunity</td>
</tr>
<tr>
<td>Lines</td>
<td>Number of lines available for game play</td>
</tr>
<tr>
<td>Credits/Points</td>
<td>Maximum number of credits/points played per line</td>
</tr>
<tr>
<td>Manufacturer</td>
<td>Manufacturer of the machine model (e.g., IGT or Bally)</td>
</tr>
</table>


4\. Use the following table as a reference for configuring the first page of the Machine Setup
Wizard settings.


<table>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
<tr>
<td>Denomination</td>
<td>Do one of the following: · Select an existing denomination from the Denomination drop-down list. · If the denomination is not listed, enter the denomination in the Denomination field. A Confirm Action message appears. Click Yes to add the denomination. · Select the Type ID for a similar machine listed in the database from the window on the right. O 1 The denomination in this field is typically the accounting denomination. This is a low-level configuration setting in Machine Accounting that allows the Denomination field to be set to the wager denomination in environments with tokenized hoppers. If the system is set to use the wager denomination, all hoppers can be set to a single tokenized value. Contact an IGT Customer Service representative for more information.</td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="114" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->


<table>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
<tr>
<td>Manufacturer</td>
<td>Select a manufacturer from the drop-down list. If the manufacturer is not listed, enter the manufacturer's name in the Manufacturer field. A confirmation message appears. Click Yes to add the manufacturer.</td>
</tr>
<tr>
<td>Description</td>
<td>Enter a description of the machine. Automatically populates after selecting a type ID from the Type ID pane. O 1 For variance machines, enter the name "Variance" in the Description field.</td>
</tr>
<tr>
<td>Hold Percent</td>
<td>Enter the percentage held by the machine. Automatically populates after selecting a Type ID machine from the Type ID pane. O 1 This field is the theoretical percentage (or par) of coins played held by the machine. A machine keeping 10 coins out of 100 has a percentage payout of 90%. Some manufacturers specify percentages paid on machine par sheets. For example, convert the payout percentage (94.32%) held by subtracting the percentage paid from 100 (100% - 94.32% = 5.68%).</td>
</tr>
<tr>
<td rowspan="2">Vouchers</td>
<td>Select one of the following: · No Voucher Printer if the machine does not have an internal ticket printer. · Voucher Out Only if the machine only issues a ticket at cash out. Tickets from Ticket Out Only machine cash outs must be redeemed and cannot be played in a ticket-in, ticket-out machine. · Voucher In/Voucher Out if the machine is capable of play using tickets and has an internal ticket printer.</td>
</tr>
<tr>
<td>O 1 Selecting Voucher In/Voucher Out requires casino slot maintenance personnel to configure each machine as an enhanced machine.</td>
</tr>
<tr>
<td>Capture WAT Meters</td>
<td>Select if WAT is enabled on the machine.</td>
</tr>
</table>




![](MachineAccounting_UserGuide_images/115.1.png)




A warning box appears at the cursor's location when information is missing.

5\. Click Next. The second Machine Setup Wizard window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="115" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/116.1.png)




6\. Use the following table as a reference for configuring the remaining Machine Setup
Wizard settings:


<table>
<tr>
<th>Field/Button</th>
<th>Description</th>
</tr>
<tr>
<td>New</td>
<td>If active, click to auto-populate the Machine # field with the next available machine number.</td>
</tr>
<tr>
<td>Machine #</td>
<td>If the New button is not active (gray), enter a unique number for the machine. Override an auto-populated number by entering a new number (within the available range of values for the denom).</td>
</tr>
<tr>
<td>EGM ID</td>
<td>Enter the MAC address for server-based games. Self populates.</td>
</tr>
<tr>
<td>Purchase Date</td>
<td>Select the date the machine was purchased or leased. Use the up and down arrows, or the keyboard, to enter the month, day, and year.</td>
</tr>
<tr>
<td>Section Name</td>
<td>Select the floor section for the machine location from the drop-down list. If a section is not listed, enter the new section name in the Section Name field. If a Confirm Action message appears, click Yes to add the section.</td>
</tr>
<tr>
<td>Bank</td>
<td>Enter the bank number for the new machine.</td>
</tr>
<tr>
<td>Location</td>
<td>Enter the number associated with the machine's position in the bank.</td>
</tr>
<tr>
<td>Serial #</td>
<td>Enter the serial number from the manufacturer.</td>
</tr>
<tr>
<td>Cabinet Type</td>
<td>Select the cabinet type from the drop-down list. If the cabinet type is not listed, enter the new type. If a Confirm Action message appears, click Yes to add the cabinet type. A new value entered in this field may be modified further.</td>
</tr>
<tr>
<td>Give Aways</td>
<td>Enter information about any special giveaway promotions connected to the machine (for example, a car or a vacation package).</td>
</tr>
<tr>
<td>Model</td>
<td>Enter a description or identification number for the game.</td>
</tr>
<tr>
<td>Aux Print Loc</td>
<td>If a machine has an auxiliary print location, select or enter the location number.</td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="116" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->


<table>
<tr>
<th>Field/Button</th>
<th>Description</th>
</tr>
<tr>
<td>G/L Code</td>
<td>Enter the general ledger code for the machine.</td>
</tr>
<tr>
<td>Seal #</td>
<td>Enter the seal number for the machine.</td>
</tr>
<tr>
<td>Govt. Stamp</td>
<td>Enter the government- or state-assigned number for the machine.</td>
</tr>
<tr>
<td>Bags Per Fill</td>
<td>Enter the number of coin bags used to fill the machine hopper.</td>
</tr>
<tr>
<td>Max Bags in Aux Fill</td>
<td>Enter the maximum bags allowed in the auxiliary fill.</td>
</tr>
<tr>
<td>Hopper Level Adjustment</td>
<td>Enter a value to adjust the hopper from a standard fill to established fill requirements.</td>
</tr>
<tr>
<td>Hopper Variance Limit</td>
<td>Enter a whole dollar amount to signal an error on fill.</td>
</tr>
<tr>
<td>Progressive Contribution %</td>
<td>If available at the property: In Machine Accounting, progressive jackpots can create variances between the actual and theoretical hold percentages. Use this field to input the progressive contribution for an EGM. The result should eliminate progressive contribution variances and allow auditors to investigate true variances.</td>
</tr>
<tr>
<td rowspan="2">EPROM(S)</td>
<td>· To view inactive EPROM(s): Select Show Inactive EPROM(s) to display both active and inactive EPROMs. · To add a new EPROM to the machine: Click Add New, then enter a name in the EPROM field.</td>
</tr>
<tr>
<td>· To remove an active EPROM: Select an active EPROM, then click Deactivate. The EPROM is removed from the pane. · To activate an EPROM: Select an inactive EPROM, then click Activate. The EPROM is activated and the status changes to Active.</td>
</tr>
<tr>
<td>Bill Validator</td>
<td>Select Bill Validator if the machine is equipped with a bill validator.</td>
</tr>
<tr>
<td>Player Tracking</td>
<td>Select Player Tracking if the machine is player tracking enabled.</td>
</tr>
<tr>
<td>Manual Meters</td>
<td>Select Manual Meters if the machine meters are not read via the BEII.</td>
</tr>
<tr>
<td>Use MGA Legacy Key</td>
<td>Select MGA Legacy Key to avoid duplicate paytables when adding a new machine if the machine is SAS 6 or older.</td>
</tr>
<tr>
<td>Lab Game</td>
<td>Select the Lab Game check box if the machine is slated for use in the lab or as an X-Series game. 0 1 Also requires a change in the configuration table.</td>
</tr>
<tr>
<td>VIP Game</td>
<td>VIP Game check box identifies machines that are grouped together as VIP EGMs in required reports. Select the VIP Game check box if the machine is slated for VIP Xtra Credit status in Patron Management.</td>
</tr>
</table>


7\. Click Finish. The Machine Setup Wizard Summary window appears.




![](MachineAccounting_UserGuide_images/117.1.png)




i
A warning box prompts the user to provide information where the cursor is located
if the wizard is incomplete.

8\. Review the information in the Machine Setup Wizard Summary window.

9\. Click Print Label to print a barcode label for the machine.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="117" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/118.1.png)




<table>
<tr>
<td>Machine Number:</td>
<td>5032</td>
<td>A</td>
</tr>
<tr>
<td>Denomination:</td>
<td>0.01</td>
<td></td>
</tr>
<tr>
<td>Manufacturer:</td>
<td>IGT</td>
<td></td>
</tr>
<tr>
<td>Description:</td>
<td>IGT UPRIGHT</td>
<td></td>
</tr>
<tr>
<td>Par:</td>
<td>5.000</td>
<td></td>
</tr>
<tr>
<td>Section Name:</td>
<td>&lt;NEW&gt;</td>
<td></td>
</tr>
<tr>
<td>Bank:</td>
<td>09</td>
<td></td>
</tr>
<tr>
<td>Location:</td>
<td>23</td>
<td></td>
</tr>
<tr>
<td>Bill Validator:</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td>Cabinet Type:</td>
<td>BAR TOP</td>
<td></td>
</tr>
<tr>
<td>Model:</td>
<td></td>
<td>E</td>
</tr>
<tr>
<td>Special Giveaways:</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Player Tracking:</td>
<td>Y</td>
<td></td>
</tr>
<tr>
<td>Serial Number:</td>
<td>123456789</td>
<td></td>
</tr>
<tr>
<td>Government Stamp:</td>
<td></td>
<td></td>
</tr>
<tr>
<td>EPROM</td>
<td>123456</td>
<td></td>
</tr>
<tr>
<td>Aux Fill Print Location:</td>
<td>0</td>
<td></td>
</tr>
<tr>
<td>Purchase Date:</td>
<td>01/06/2011</td>
<td></td>
</tr>
<tr>
<td>Cabinet Number:</td>
<td>5032</td>
<td></td>
</tr>
<tr>
<td>Machine Protocol:</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Voucher Printer:</td>
<td>N</td>
<td></td>
</tr>
<tr>
<td rowspan="2">WAT Enabled:</td>
<td>N</td>
<td>₹</td>
</tr>
<tr>
<td>₼</td>
<td></td>
</tr>
</table>




![](MachineAccounting_UserGuide_images/118.2.png)




A barcode printer must be connected to the parallel printer port of the PC to print a
barcode label.

10\. Click OK to print a Machine Work Order.

11\. Attach the printed label to the work order, then forward both labels to slot technicians for
machine floor setup.


## 7.3 Updating Machines

To update an existing machine:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window opens.

2\. Select a machine, then click Machine Wizard. The Machine Wizard window appears.

3\. Select I want to Update a machine.

4\. Click Next. The Updating Machine window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="118" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/119.1.png)




The Updating Machine and Machine Wizard windows are identical in appearance
except for the title bar.




![](MachineAccounting_UserGuide_images/119.2.png)




5\. Edit the fields in the Updating Machine window, then click Next. The second Updating
Machine window appears.




![](MachineAccounting_UserGuide_images/119.3.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="119" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->

6\. Edit the fields in the second Updating Machine window.

7\. Click Finish. The Machine Setup Wizard summary window appears.




![](MachineAccounting_UserGuide_images/120.1.png)




<table>
<tr>
<td>Machine Number:</td>
<td colspan="2">100090 A</td>
</tr>
<tr>
<td>Denomination:</td>
<td colspan="2">0.01</td>
</tr>
<tr>
<td>Manufacturer:</td>
<td colspan="2">IGT</td>
</tr>
<tr>
<td>Description:</td>
<td colspan="2">SBX</td>
</tr>
<tr>
<td>Par:</td>
<td colspan="2">1.250</td>
</tr>
<tr>
<td>Section Name:</td>
<td colspan="2">A</td>
</tr>
<tr>
<td>Bank:</td>
<td colspan="2">01</td>
</tr>
<tr>
<td>Location:</td>
<td colspan="2">02</td>
</tr>
<tr>
<td>Bill Validator:</td>
<td colspan="2">Yes</td>
</tr>
<tr>
<td>Cabinet Type:</td>
<td colspan="2">UPRIGHT</td>
</tr>
<tr>
<td>Model:</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Special Giveaways:</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Player Tracking:</td>
<td colspan="2">Y</td>
</tr>
<tr>
<td>Serial Number:</td>
<td colspan="2">1905286</td>
</tr>
<tr>
<td>Govemment Stamp: Aux Fill Print Location:</td>
<td colspan="2">0</td>
</tr>
<tr>
<td>Purchase Date:</td>
<td colspan="2">06/28/2017</td>
</tr>
<tr>
<td>Cabinet Number:</td>
<td colspan="2">100090</td>
</tr>
<tr>
<td>Machine Protocol:</td>
<td colspan="2">$2s</td>
</tr>
<tr>
<td>Voucher Printer:</td>
<td colspan="2">Y</td>
</tr>
<tr>
<td>Voucher Meters:</td>
<td colspan="2">Y</td>
</tr>
<tr>
<td>WAT Enabled:</td>
<td colspan="2">Y V</td>
</tr>
<tr>
<td></td>
<td colspan="2">n</td>
</tr>
</table>


8\. If selecting I want to Update an SB Game, click Yes to confirm the game receives updates
from the server-based game system.

9\. Review the information in the Machine Setup Wizard window for accuracy.

10\. Click Print Label. A label prints.

11\. Click Done. The Maintenance Workbook reappears.


## 7.4 Converting Machines

Converting a machine involves retiring one machine and then adding it back as a new machine
with a different type code. New values entered during the conversion process may be modified
further.

To convert a machine:

1\. Select IGT Spade > Floor > Machine Maintenance. The Maintenance Workbook
window opens.

2\. Select the machine to convert, then click Machine Wizard. The Machine Wizard
window appears.

3\. Select I want to Convert a machine, then click Next. The Updating Machine window
appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="120" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/121.1.png)




i
The Updating Machine and Machine Wizard windows are identical in appearance
except for the title bar.

4\. Edit the fields in the Updating Machine window, then click Next. The second Updating
Machine window appears.




![](MachineAccounting_UserGuide_images/121.2.png)




İ
The number displayed in the Machine # field is system generated and is the next
available machine number for the denomination of the machine being converted.
Accept the number displayed or enter a specific number.

5\. Edit the fields in the second Updating Machine window, then click Finish. The Machine
Setup Wizard window appears.

OR
Click Cancel. The Maintenance Workbook reappears, and the machine is not updated.

6\. Review the information in the Machine Setup Wizard Summary window, then click Print
Label. A label prints.

OR

Click Cancel. The Maintenance Workbook reappears, and the machine is not updated.

7\. Click OK. A machine work order prints.

8\. Attach the printed label to the work order, and forward both to the slot technicians for
machine floor setup.


## 7.5 Retiring Machines

Prior to a machine being removed from the floor, machine meters must be read (take a
snapshot) one last time. To ensure this step is done, turn off the machine and remove it from
OL (online). It can then be turned back on as "Out of Service."


### To retire a machine:




![](MachineAccounting_UserGuide_images/121.3.png)




Retire machines only after the soft and hard drops are complete. This allows the
retiring machine to make a final drop.

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Select the machine to retire and click Machine Wizard. The Machine Wizard window
opens.

3\. Select I want to Retire a machine, then click Finish. The Retire Machine window
appears.




![Figure 7-2 Retire Machine](MachineAccounting_UserGuide_images/121.4.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="121" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/122.1.png)




All selections do the same action. The only difference is the final disposal.

A machine retired by selecting Other cannot be returned to the floor. It is used for
games taken off the floor and returned to the manufacturer or used for spare parts.

4\. Select the appropriate disposition, then click OK. A work order prints for the retired
machine.


## 7.5.1 Viewing Retired Machines

To view retired machines:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Click the Warehouse option in the Add/Retire Machine pane. The pane displays all
machines removed from the floor and retired to the warehouse.

Sold machines do not appear.




![](MachineAccounting_UserGuide_images/122.2.png)




## 7.6 Warehouse EGM Conversion

Use the Warehouse EGM Conversion feature to convert an EGM in Warehouse status. Before
this feature's implementation, any warehouse machine placed in warehouse status had to be
brought back in with the exact configuration (denomination, par %, and machine number) as
when it was placed in the warehouse.

Use a permanent asset identifier (PAI) to convert EGMs in warehouse status back to the floor
in a different configuration. The PAI remains the same, but the mnum changes. This allows the
machine to be analyzed separately from the original configuration.

Configure this feature to use it. It is only available to properties using manually assigned PAIS.


<table>
<tr>
<th>Machine</th>
<th>Denom</th>
<th>Location</th>
<th>Manufacturer</th>
<th>Par</th>
<th>Description</th>
<th>Status</th>
</tr>
<tr>
<td>100000 100001</td>
<td>0.01 0.01</td>
<td>B0101 B0102</td>
<td>IGT IGT</td>
<td>1.00 1.00</td>
<td>SBX THEO SBX THEO</td>
<td>Inactive Inactive</td>
</tr>
<tr>
<td>100002</td>
<td>0.01</td>
<td>B0103</td>
<td>IGT</td>
<td>1.25</td>
<td>BETTI THE YETTI</td>
<td>Inactive</td>
</tr>
<tr>
<td>100003</td>
<td>0.01</td>
<td>B0104</td>
<td>IGT</td>
<td>1.00</td>
<td>SBX THEO</td>
<td>Inactive</td>
</tr>
</table>




![Figure 7-3 Maintenance Workbook-Conversion](MachineAccounting_UserGuide_images/122.3.png)




<!-- PageNumber="122" -->
<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->

To convert a machine from warehouse status:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Select Warehouse. The Add/Retire Machines pane displays warehoused machines.

3\. Select the machine to convert, then click Machine Wizard. The Machine Wizard
window opens.

4\. Select I want to Convert a machine, then click Next. The Updating Machine window
appears.

5\. Edit the fields in the Updating Machine window, then click Next. The second Updating
Machine window appears.

6\. Edit the fields in the second Updating Machine window, then click Finish. The Machine
Wizard window appears.

7\. Review the information in the Machine Wizard window, then click Print Label. A label
prints.

8\. Click OK. A machine work order prints.

9\. Attach the printed label to the work order, then forward both to the slot technicians for
machine floor setup.


## 7.7 Changing Machine Locations

To change the location for a machine:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Select a machine, then click Machine Wizard. The Machine Wizard window opens.

3\. Select the machine(s) for the location change, then click Machine Wizard.
Use the CTRL key to select multiple machines.




![](MachineAccounting_UserGuide_images/123.1.png)




4\. Click I want to Change a machine's location, then click Finish. The Move Machines
window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="123" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/124.1.png)




5\. Select a machine, then enter the new location (not already assigned to another machine)
in the New Location field.

6\. Click Update. The new location appears.

7\. Click OK. A work order prints for the machine to be moved.


## 7.8 Resetting Unique Machine IDs

To reset a machine's unique ID:

1\. Select IGT Spade > Floor > Machine Maintenance. The Maintenance Workbook
window appears.

2\. Select the machine to reset, then click Machine Wizard. The Machine Wizard window
opens.

3\. Click I want to Reset a machine's Unique ID/EGM ID, then click Finish. A
confirmation window appears.

O
Ť

If the IGT Advantage Machine Accounting system is connected to the IGT sbX
system, the serial numbers of all machines enrolled in Machine Accounting must
match the cabinet serial numbers in the IGT sbX system.

Asset numbers from Machine Accounting are enrolled automatically within the sbX
system and can be viewed within sbX My Casino.




![](MachineAccounting_UserGuide_images/124.2.png)




4\. Click Yes. The machine's Unique ID changes.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="124" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->


## 7.9 Verifying Machine Changes

The Verify Machine Changes window maintains detailed information on the location and
configuration of casino machines. Navigate here after adding machines to Machine Accounting
in order to do the following:

· Make machine changes

· Test meters

· Assign machines to drop zones




![](MachineAccounting_UserGuide_images/125.1.png)




Do not retire a machine until the machine audit is complete. All jackpots, fills, cash,
coin, and vouchers must be posted to the game, and soft/hard drops must be
completed. This allows the retiring machine to make a final drop.




![Figure 7-4 Verify Machine Changes Sub-Task List](MachineAccounting_UserGuide_images/125.2.png)




Click Verify Machine Changes to access the Machine Wizard. Complete the following tasks
from the Machine Wizard:


<table>
<tr>
<th>Task</th>
<th>Description</th>
</tr>
<tr>
<td>Verify a Machine: · Add · Retire · Move</td>
<td>Use to finalize a machine add, retire, or move.</td>
</tr>
<tr>
<td>Update a Machine</td>
<td>Use to modify fields that do not affect the accounting process.</td>
</tr>
<tr>
<td>Add a New Machine</td>
<td>Use to create a new machine ready for placement on the floor.</td>
</tr>
<tr>
<td>Convert a Machine</td>
<td>Use to retire an existing machine and create a new machine with a different type code.</td>
</tr>
<tr>
<td>Retire a Machine</td>
<td>Use to move a machine off the floor.</td>
</tr>
<tr>
<td>Change a Machine Location</td>
<td>Use to change a machine's location without creating a new machine number.</td>
</tr>
<tr>
<td>Restart a Machine's Unique ID/EGM ID</td>
<td>Use to reset the machine's unique ID.</td>
</tr>
</table>


<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="125" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->


## To verify machine changes:

1\. Navigate to Verify Machine Changes on the User Tasks list or Period Timeline. The
Machine Wizard window appears.




![](MachineAccounting_UserGuide_images/126.1.png)




### 2. Select I want to Verify a machine Add, Retire or Move, then click Next.


<table>
<tr>
<th>Date</th>
<th>Type</th>
<th>Machine</th>
<th>Denom</th>
<th>Location</th>
<th>Meter</th>
</tr>
<tr>
<td>05/25/2017 12:00 AM</td>
<td>Move</td>
<td>3483</td>
<td>0.01</td>
<td>SAS69799</td>
<td>No</td>
</tr>
<tr>
<td>05/17/2017 12:00 AM</td>
<td>Add</td>
<td>3107</td>
<td>0.01</td>
<td>MAJNO101</td>
<td>Yes</td>
</tr>
<tr>
<td>05/17/2017 12:00 AM</td>
<td>Retire</td>
<td>3495</td>
<td>0.01</td>
<td>MA9797</td>
<td>No</td>
</tr>
<tr>
<td>05/17/2017 12:00 AM</td>
<td>Retire</td>
<td>3496</td>
<td>0.01</td>
<td>BC9797</td>
<td>No</td>
</tr>
</table>




![](MachineAccounting_UserGuide_images/126.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="126" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->

3\. Select the machine for which to verify the addition, move, or retirement, then click Next.

4\. Follow the wizard steps to complete the verification of the machine's addition, move, or
retirement.

5\. Click Finish when complete.


#### 7.9.1 Verifying Machine Additions

A completed machine work order from the slot department is required before verifying an
addition.

To verify a machine addition:

1\. Navigate to Verify Machine Changes on the User Tasks list or Period Timeline. The
Machine Wizard window appears.

2\. Select I want to Verify a machine Add, Retire or Move, then click Next. The next
screen appears.

3\. Select a machine addition to verify.




![](MachineAccounting_UserGuide_images/127.1.png)




1
Only machines with Yes in the Meter column may be verified (machines with
electronic meters that have been received).

1\. Click Next. The Verifying the Addition of Machine window appears.
OR

Click Defer for machines with No in the Meter column (electronic meters have not been
received) to delay completing the selected addition until the next accounting cycle. The
machine is removed from the verification process and made available during the next
accounting cycle.




![](MachineAccounting_UserGuide_images/127.2.png)




!
The Verifying the Addition of Machine and Machine Setup Wizard windows are
identical in appearance except for the title bar. After verifying a machine addition,
it will also need to be assigned to a drop zone.

2\. Click Finish. The Verify Machine window appears.


#### 7.9.2 Verifying Machine Moves

A completed machine work order from the slot department is required before verifying a
location move.

To verify a machine move:

1\. Click Verify Machine Changes in the User Tasks list or Period Timeline. The Machine
Wizard window opens.

2\. Select a machine move to verify.

i
Only machines with Yes listed in the Meter column (with electronic meters received)
may be verified.




![](MachineAccounting_UserGuide_images/127.3.png)




1\. Click Next to open the Verifying the Location Change of Machine window.
OR

Click Defer for machines with No in the Meter column (electronic meters have not been
received) to delay completing the selected move until the next accounting cycle. The
machine is removed from the verification process and made available during the next
accounting cycle.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="127" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/128.1.png)




<table>
<tr>
<th>Machine</th>
<th>Meter Date</th>
<th>Type</th>
<th>Coin In</th>
<th>Legacy Coin Out</th>
<th>Games</th>
<th>Coin Drop</th>
<th>Soft1</th>
</tr>
<tr>
<td>3311</td>
<td>July 15 2009 00:00:00</td>
<td>P</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>3311</td>
<td>July 14 2009 23:55:00</td>
<td>I</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>3311</td>
<td>July 14 2009 00:00:00</td>
<td>P</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</table>


2\. Click Next to accept the highlighted item as the final meter reading for the machine move.

3\. Click Next. The Verifying the Location Change of Machine window appears.




![](MachineAccounting_UserGuide_images/128.2.png)




i
The Verifying the Location Change of Machine window and the Machine Wizard
dialog boxes are identical except for the title bar.

4\. Click Finish. The Machine Setup Wizard window appears.

5\. Review the information in the Machine Setup Wizard window for accuracy.

6\. Click OK. The Verify Machine window appears.


## 7.10 Meter Test

Use meter tests to test a specific machine's meters and produce information vital to casino floor
maintenance.


### To access the meter test function:

1\. Select IGT Spade > Audit > Meter Test. The Maintenance Workbook window
appears.

2\. Select the Meter Test tab. The Meter Test tab opens.




![Figure 7-5 Maintenance Workbook - Meter Test](MachineAccounting_UserGuide_images/128.3.png)




# 7.10.1 Running Meter Tests

Use meter tests to test a specific machine's meters. Meter readings are taken prior to an exact
number of coins (including bills) played and then compared to meter readings after the test.


## To run a meter test:

1\. Select IGT Spade > Audit > Meter Test. The Maintenance Workbook window
appears.

2\. Select the Meter Test tab. The Meter Test tab opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="128" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->

3\. Click the Test Date to select the test date (current date).

4\. On the gaming floor, do the following at the machine(s):

a. Insert a meter test card into the machine's card reader, then manually record the
machine number and time (in hh: mm format) the test card was inserted.

b. Manually record the necessary meters as the beginning meters for the meter test.

c. Insert a fixed number of coins into the game and play the machine, then manually
record the exact counts of coin in, coin out, total drop, and number of games played
for the coin test. (For example, a $1 bill inserted into a 5¢ game will increment the
coin-in meter by 20, whereas incrementing the $1 meter by one increases the total
drop by $1.)

d. If testing with paper currency, manually record meters for bill denominations ($1, $5,
$10, $20, $50, or $100), as well as total bills and total drop meters for the
denomination incrementing of the game. (For example, a $5 bill inserted into a 25¢
game will increment the coin-in meter by 20, while incrementing the $5 meter by one
increases the total drop by $5.)

e. Insert a fixed number of paper bills into the game, play the machine, and manually
record meters for bill denominations ($1, $5, $10, $20, $50, or $100), as well as total
bills and total drop meters for the denomination incrementing of the game.

f. Remove the meter test card.

g. Repeat the meter test for additional machines.




![](MachineAccounting_UserGuide_images/129.1.png)




5\. Print the Meter Test report for the current date.
To print the Meter Test report, click the IGT Spade and select View > Reports >
System Maintenance > Meter Test.

6\. In Machine Accounting, click the Meter Test tab in the Maintenance Workbook, then
click Test Date and select the current date.

7\. Click the Machine drop-down, then select the number of the machine being tested. The
machine test time automatically populates the Test Time field.

8\. Click the Test Time drop-down, then select the correct test time, if the machine was
tested more than once during the current day.

9\. Compare the actual meter data from the meter test to the information displayed on the
Meter Test report and on the Meter Test Delta displayed in the Meter Test window.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="129" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/130.1.png)




<table>
<tr>
<th>Description</th>
<th>Coin Test Start</th>
<th>Coin Test End</th>
<th>Coin Test Delta</th>
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
<td>57206243</td>
<td>57207218</td>
<td>975</td>
</tr>
<tr>
<td>Coin Out</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Legacy Coin Out</td>
<td>51618057</td>
<td>51618157</td>
<td>100</td>
</tr>
<tr>
<td>Games</td>
<td>3382080</td>
<td>3382090</td>
<td>10</td>
</tr>
<tr>
<td>Total Drop</td>
<td>19564705</td>
<td>19564705</td>
<td>0</td>
</tr>
<tr>
<td>$1</td>
<td>7749</td>
<td>7749</td>
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
<td>13829</td>
<td>13829</td>
<td>0</td>
</tr>
<tr>
<td>$10</td>
<td>11800</td>
<td>11800</td>
<td>0</td>
</tr>
<tr>
<td>$20</td>
<td>19817</td>
<td>19817</td>
<td>0</td>
</tr>
<tr>
<td>$50</td>
<td>420</td>
<td>420</td>
<td>0</td>
</tr>
<tr>
<td>$100</td>
<td>428</td>
<td>428</td>
<td>0</td>
</tr>
<tr>
<td>Bill In</td>
<td>13100680</td>
<td>13100680</td>
<td>0</td>
</tr>
<tr>
<td>Attendant Paid Jackpots</td>
<td>64188</td>
<td>64188</td>
<td>0</td>
</tr>
<tr>
<td>Attendant Paid Cancelled Credits</td>
<td>202287</td>
<td>202287</td>
<td>0</td>
</tr>
<tr>
<td>Attendant Paid Progressive Payout</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Non-Cashable Electronic Promotion In</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Machine Paid External Bonus Payout</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</table>


Figure 7-6 Meter Test


# 7.11 Machine Events

Use the Machine Events tab to view event codes or meters for an individual machine or a group
of machines over a specific time period. Refine events by selecting a Staff ID or Player ID.




![](MachineAccounting_UserGuide_images/130.2.png)




Refer to Event Codes and Descriptions for more information on event codes and
their meanings.


# 7.11.1 Viewing Machine Events


## To view machine events:

1\. Navigate to IGT Spade > Floor > Machine Maintenance > Machine Events tab.
The Machine Events tab appears.




![](MachineAccounting_UserGuide_images/130.3.png)




2\. Set a date range using the Start Date and End Date fields.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="130" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/131.1.png)




i
These fields default to the current date and time.

Click
...
in the Machine field to select machines. The Select Filter Items window
appears.




![](MachineAccounting_UserGuide_images/131.2.png)




<table>
<tr>
<th>Machine</th>
<th>Denom</th>
<th>Location</th>
<th>Manufacturer</th>
<th>Par</th>
<th>Description</th>
</tr>
<tr>
<td>☐ 5006</td>
<td>0.01</td>
<td>A0107</td>
<td>IGT</td>
<td>5.00</td>
<td>IGT UPRIGHT</td>
</tr>
<tr>
<td>☐ 5009</td>
<td>0.01</td>
<td>A0110</td>
<td>IGT</td>
<td>5.00</td>
<td>MJP</td>
</tr>
<tr>
<td>☐ 5015</td>
<td>0.01</td>
<td>A0105</td>
<td>IGT</td>
<td>5.00</td>
<td>IGT UPRIGHT</td>
</tr>
<tr>
<td>☐ 5021</td>
<td>0.01</td>
<td>A0106</td>
<td>IGT</td>
<td>5.00</td>
<td>IGT UPRIGHT</td>
</tr>
<tr>
<td rowspan="2">☐ 5031</td>
<td rowspan="2">0.01</td>
<td rowspan="2">A0108</td>
<td>IGT</td>
<td rowspan="2">5.00</td>
<td rowspan="2">IGT UPRIGHT</td>
</tr>
<tr>
<td></td>
</tr>
</table>


4\. Select the applicable machine(s) using one of the following methods:

· Select the check box(es) in the Machine column.

· Click Select All to select all machines.

5\. If needed, click one or more of the following items to further filter the search criteria:

· Denomination

· Section

· Bank

· Manufacturer

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="131" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/132.1.png)




6\. Click Select after each chosen option. The filtered machines are selected.

7\. Click OK on the Select Filter Items window. The selections appear in the Machine Events
window.

8\. Click ...
...
in the Event Code field. The Select Filter Items window appears.




![](MachineAccounting_UserGuide_images/132.2.png)



9\. Select the check boxes next to individual events in the Event Code field.
OR
Click Select All to select all events.

10\. Click OK. The selections appear in the Machine Events window.

11\. If appropriate, click ... in the Staff ID field. The Staff ID column appears in the Select
Filter Items window.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="132" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/133.1.png)




12\. Select the check box next to individual ID numbers in the Staff ID column.
OR
Click Select All to select all IDs.

13\. Click OK. The selections appear in the Machine Events window.

14\. Enter a unique ID number in the Player ID field to filter by player.
IGT Advantage Player Tracking must be running for this feature to work.




![](MachineAccounting_UserGuide_images/133.2.png)




15\. Click Select when all fields are configured. The Machine Events window displays the
machine events matching the filter criteria.

Selecting too many filters slows the system response time for machine events.




![](MachineAccounting_UserGuide_images/133.3.png)




## 7.12 Machine Detail

The Machine Detail option summarizes current information for both active and warehoused
machines.

To view machine details:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Select the Add/Retire Machines tab. The Add/Retire Machines tab appears.

3\. Select the machine to view, or press and hold CTRL to select multiple machines, then
click Machine Detail. The Machine Record window opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="133" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![Figure 7-7 Maintenance Workbook-Machine Detail](MachineAccounting_UserGuide_images/134.1.png)




4\. Click Next Machine (if selecting multiple machines) to view the information for the next
machine.

5\. Click Done to return to the Maintenance Workbook window.


# 7.12.1 Detail Meters

The Detail Meters option summarizes period information for both active and warehoused
machines. Periods covered include week-to-date, month-to-date, quarter-to-date, year-to-date,
and life-to-date. This information is useful in determining a particular machine's profitability.


## To view detail meters:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Select the Add/Retire Machines tab. The Add/Retire Machines tab appears.

3\. Select the machine to view or press and hold CTRL to select multiple machines, then click
Detail Meters. The Detail Information window opens.

<!-- PageNumber="134" -->
<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->


<table>
<tr>
<th colspan="8"></th>
</tr>
<tr>
<th>Description</th>
<th>Period</th>
<th>Wtd</th>
<th>Mtd</th>
<th>Qtd</th>
<th>Ytd</th>
<th>Ltd</th>
<th>A</th>
</tr>
<tr>
<td>Accrued Hard Drop</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td rowspan="2"></td>
</tr>
<tr>
<td>Accrued Netwin</td>
<td>3874.10</td>
<td>3874.10</td>
<td>3874.10</td>
<td>6608.60</td>
<td>6707.60</td>
<td>6707.60</td>
</tr>
<tr>
<td>Accrued Soft Drop</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>65.00</td>
<td>65.00</td>
<td rowspan="3"></td>
</tr>
<tr>
<td>Accrued Total Drop</td>
<td>3886.10</td>
<td>3886.10</td>
<td>3886.10</td>
<td>6888.60</td>
<td>7053.60</td>
<td>7053.60</td>
</tr>
<tr>
<td>Accrued Voucher Drop</td>
<td>3886.10</td>
<td>3886.10</td>
<td>3886.10</td>
<td>6888.60</td>
<td>6988.60</td>
<td>6988.60</td>
</tr>
<tr>
<td>Accrued WAT Drop</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td rowspan="7">E</td>
</tr>
<tr>
<td>Accumulated Coupon</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>Accumulated Hard</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>Accumulated Soft</td>
<td>65.00</td>
<td>65.00</td>
<td>65.00</td>
<td>65.00</td>
<td>65.00</td>
<td>65.00</td>
</tr>
<tr>
<td>Accumulated Voucher</td>
<td>3102.50</td>
<td>3102.50</td>
<td>3102.50</td>
<td>3102.50</td>
<td>3102.50</td>
<td>3102.50</td>
</tr>
<tr>
<td>Accumulated WAT</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>Act Fills</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>Act Hard Drop</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td rowspan="2"></td>
</tr>
<tr>
<td>Act Jackpots</td>
<td>12.00</td>
<td>12.00</td>
<td>12.00</td>
<td>280.00</td>
<td>346.00</td>
<td>346.00</td>
</tr>
<tr>
<td>Act Soft Drop</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>Act Total Drop</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>Act Voucher Drop</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>Act WAT Drop</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td></td>
</tr>
<tr>
<td>Bonus</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td rowspan="2"></td>
</tr>
<tr>
<td>Cashable Electronic Promo Played</td>
<td>30.50</td>
<td>30.50</td>
<td>30.50</td>
<td>90.50</td>
<td>444.50</td>
<td>444.50</td>
</tr>
<tr>
<td>Cashable Electronic Promotion In</td>
<td>30.50</td>
<td>30.50</td>
<td>30.50</td>
<td>30.50</td>
<td>30.50</td>
<td>30.50</td>
<td rowspan="4">-</td>
</tr>
<tr>
<td>Coin In</td>
<td>121.00</td>
<td>121.00</td>
<td>121.00</td>
<td>1526.30</td>
<td>1527.30</td>
<td>1527.30</td>
</tr>
<tr>
<td>Coin Out</td>
<td>109.20</td>
<td>109.20</td>
<td>109.20</td>
<td>152.20</td>
<td>2474.70</td>
<td>2474.70</td>
</tr>
<tr>
<td>Coupon Promo In</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
</table>




![Figure 7-8 Maintenance Workbook-Detail Meters](MachineAccounting_UserGuide_images/135.1.png)




4\. Click Next Machine (if selecting multiple machines) to view the information for the next
machine.

5\. Click Done. The Maintenance Workbook window reappears.


# 7.12.2 Current Meters

The Curent Meters option summarizes current information as of the earliest opened accounting
period for both active and warehoused machines.

Configure periods within the Machine Accounting Configuration options.




![](MachineAccounting_UserGuide_images/135.2.png)




## To view current meters:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Select the Add/Retire Machines tab. The Add/Retire Machines tab appears.

3\. Select the machine to view or press and hold CTRL to select multiple machines, then click
Current Meters. The Current Meters window opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="135" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/136.1.png)




<table>
<tr>
<th></th>
<th>Meter Date</th>
<th>Meter Type</th>
<th>Physical Coin In</th>
<th>Physical Coin Out</th>
<th>Coin In</th>
<th>Legacy</th>
<th>Coin Out</th>
<th>Gam</th>
<th></th>
</tr>
<tr>
<td rowspan="2"></td>
<td>01/03/11 12:15:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td>☐</td>
</tr>
<tr>
<td>01/03/11 12:30:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 12:45:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 1:00:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 1:15:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 1:30:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 1:45:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 2:00:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 2:15:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 2:30:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 2:45:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 3:00:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>/03/11 3:15:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 3:30:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td></td>
<td>01/03/11 3:45:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td></td>
</tr>
<tr>
<td rowspan="2"></td>
<td>01/03/11 4:00:00 AM</td>
<td>Hourly</td>
<td>0</td>
<td>0</td>
<td>206645</td>
<td>253970</td>
<td></td>
<td>249</td>
<td>-</td>
</tr>
<tr>
<td>1 TII</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>,</td>
<td></td>
</tr>
</table>


Figure 7-9 Maintenance Workbook-Current Meters

4\. Click Next Machine (if selecting multiple machines) to view the information for the next
machine.

5\. Click OK. The Maintenance Workbook window reappears.


## 7.12.3 MGA Meters

The MGA Meters option summarizes information about current meters for the paytable ID.

To view the current meters for paytables:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window opens.

2\. Select the Add/Retire Machines tab. The Add/Retire Machines tab appears.

3\. Select the machine to view or press and hold CTRL to select multiple machines, then click
MGA Meters. The Current Meters for Paytable window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="136" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->


<table>
<tr>
<th colspan="13">Current Meters for Paytable - 3395</th>
</tr>
<tr>
<th>Machine</th>
<th>Information</th>
<th rowspan="2">Manufacturer: IGT</th>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th colspan="2" rowspan="2"></th>
<th colspan="2" rowspan="2">Next Machine</th>
</tr>
<tr>
<th></th>
<th>Denom: 0.01</th>
</tr>
<tr>
<td colspan="2">Meter Denom: 0.01</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2">OK</td>
</tr>
<tr>
<th colspan="3">Description: SB SERVICE WINDOW EGM</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th colspan="2"></th>
</tr>
<tr>
<th>Paytable ID</th>
<th>Meter Date</th>
<th>Meter Type</th>
<th>Coin In</th>
<th>Weighted ...</th>
<th>Coin Out</th>
<th>Jackpot</th>
<th>Games Played</th>
<th>Attendant Paid Jackpot</th>
<th>Attendant Paid Progre ...</th>
<th>Machine Paid Progre ..</th>
<th>Paytable Win</th>
<th>.</th>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 12:00 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td>E</td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 12:30 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 01:00 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 01:30 AM</td>
<td>Hourly</td>
<td>76.022.656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330.640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 02:00 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67.330,640</td>
<td>3.411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 02:30 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 03:00 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 03:30 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 04:00 AM</td>
<td>Hourly</td>
<td>76.022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 04:30 AM</td>
<td>Hourly</td>
<td>76.022.656</td>
<td>8.46</td>
<td>67.330,640</td>
<td>3.411,385</td>
<td>207,588</td>
<td>3.411,385</td>
<td>0</td>
<td>0</td>
<td>67.330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 05:00 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3.411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 05:30 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 06:00 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 06:30 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 07:00 AM</td>
<td>Hourly</td>
<td>76.022.656</td>
<td>8.46</td>
<td>67.330,640</td>
<td>3.411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67.330.640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 07:30 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67.330,640</td>
<td>3.411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 08:00 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 08:30 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 09:00 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 09:30 AM</td>
<td>Hourly</td>
<td>76.022,656</td>
<td>8.46</td>
<td>67.330,640</td>
<td>3,411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 10:00 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67.330,640</td>
<td>3.411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td></td>
</tr>
<tr>
<td>437</td>
<td>12/16/2014 10:30 AM</td>
<td>Hourly</td>
<td>76,022,656</td>
<td>8.46</td>
<td>67,330,640</td>
<td>3.411,385</td>
<td>207,588</td>
<td>3,411,385</td>
<td>0</td>
<td>0</td>
<td>67,330,640</td>
<td>-</td>
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
<td colspan="2"></td>
</tr>
</table>




![](MachineAccounting_UserGuide_images/137.1.png)




Figure 7-10 Maintenance Workbook-Current Meters for Paytable

4\. Click Next Machine (if selecting multiple machines) to view the information for the next
machine.

5\. Click OK. The Maintenance Workbook window reappears.


## 7.12.4 Printing Labels

Click the Print Label button to print a barcode label for machine identification. See the
system administrator to confirm printer setup and configuration, if necessary.




![](MachineAccounting_UserGuide_images/137.2.png)




Printing barcode labels requires an authorized thermal barcode printer.


# 7.13 Drop Zone Setup

Create machine groupings in Machine Accounting to organize hard- and soft-drop schedules.
Use the Drop Zone Setup feature to designate the machine drops to collect and those allowed
to accumulate.


# 7.13.1 Adding Machines to Drop Zones

To add machines to a drop zone:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Click the Drop Zone Setup tab. The Drop Zone Setup tab displays machines not
assigned to a drop zone in the left pane.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="137" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/138.1.png)




3\. Click Drop Zone, then select a specific drop zone. The machines assigned to the selected
zone appear in the right pane.




![](MachineAccounting_UserGuide_images/138.2.png)




4\. Highlight a machine in the left pane OR press and hold CTRL to select multiple
machines.

5\. Click Add >. The selected machines are added to the drop zone and appear in the right
pane.


# 7.13.2 Removing Machines from Drop Zones

To remove machines from a drop zone:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window opens.

2\. Click the Drop Zone Setup tab. The Drop Zone Setup tab appears.




![](MachineAccounting_UserGuide_images/138.3.png)




3\. Click Drop Zone, then select a specific drop zone. The machines assigned to the selected
zone appear in the right pane.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="138" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/139.1.png)




4\. Highlight a machine in the right pane OR press and hold CTRL to select multiple
machines.

5\. Click < Remove. The selected machines are removed from the drop zone and appear on
the left pane.


# 7.13.3 Drop Zone Schedules

Remember the following when configuring a drop zone schedule:

· Make any changes to drop times BEFORE the end of the gaming day BUT after the
audit for the previous day is closed.

· Associate at least one drop time with each created zone.

· If configuring multiple drop times, do not associate overlapping drop times to one
zone.


# 7.13.4 Adding New Drop Times




![](MachineAccounting_UserGuide_images/139.2.png)




Another way to set drop times is to click Drop Times on the Configuration/Option
window under the Options menu.

To create a new drop time:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Click the Drop Zone Setup tab. The Drop Zone Setup tab appears.

3\. Select New from the Drop Zone drop-down menu.

4\. Click Schedule. The Drop Zone Schedule window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="139" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/140.1.png)




### 5. Click the Drop Times tab. The Drop Times tab appears.




![](MachineAccounting_UserGuide_images/140.2.png)




6\. Click Add. The Add/Edit Drop Time window opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="140" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/141.1.png)




7\. Enter the Start Time and End Time.

8\. Select the drop type: Hard or Soft.

9\. Add a description of the drop time in the Description field (for example, Swing Shift or
Gaming Day).

10\. Click OK. The Add/Edit Drop Time window closes.

11\. Click OK. The Drop Zone Schedule window closes, and the drop zone is saved.


# 7.13.5 Modifying Existing Drop Times


## To modify an existing drop time:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Click the Drop Zone Setup tab. The Drop Zone Setup tab appears.

3\. Select New from the Drop Zone drop-down menu.

4\. Click Schedule. The Drop Zone Schedule window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="141" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/142.1.png)




#### 5. Click the Drop Times tab. The Drop Times window appears.




![](MachineAccounting_UserGuide_images/142.2.png)




6\. Click Edit. The Add/Edit Drop Time window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="142" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/143.1.png)




7\. Make the desired changes.

8\. Click OK. The Add/Edit Drop Time window closes.

9\. Click OK. The changes save, and the Drop Zone Schedule window closes.


# 7.13.6 Deleting Existing Drop Times


## To delete a drop time:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Click the Drop Zone Setup tab. The Drop Zone Setup tab appears.

3\. Select New from the Drop Zone drop-down menu.

4\. Click Schedule. The Drop Zone Schedule window appears.




![](MachineAccounting_UserGuide_images/143.2.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="143" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->


### 5. Click the Drop Times tab. The Drop Times tab appears.




![](MachineAccounting_UserGuide_images/144.1.png)




6\. Click Delete. A confirmation message appears.

7\. Click OK. The drop time is deleted.

8\. Click OK. The Drop Zone Schedule window closes.


# 7.13.7 Creating New Drop-Zone Schedules

To create a new drop-zone schedule:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Click the Drop Zone Setup tab. The Drop Zone Setup tab appears.

3\. Select New from the Drop Zone drop-down menu.

4\. Click Schedule. The Drop Zone Schedule window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="144" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/145.1.png)



5\. Select one of the following options in the Occurs pane:

· Recurring-Select the Starting - Gaming Day and the number of days that the drop
reoccurs.

· Daily-Select the day(s) of the week when the drop occurs (not the gaming date on
which the money is posted).

6\. Select an existing drop time from the existing Drop Times list. Refer to Adding New Drop
Times on page 139 if the appropriate drop time is not listed.

7\. Click OK. The drop zone schedule is added.


# 7.13.8 Modifying Existing Drop-Zone Schedules


## To modify an existing drop-zone schedule:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Select the Drop Zone Setup tab. The Drop Zone Setup tab appears.

3\. Select an existing drop zone, then click Schedule. The Drop Zone Schedule window
appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="145" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 7 Maintenance Workbook" -->




![](MachineAccounting_UserGuide_images/146.1.png)




4\. Make applicable changes.

5\. Click OK. The changes save, and the Drop Zone Schedule window closes.


# 7.13.9 Deleting Existing Drop-Zone Schedules

To delete an existing drop-zone schedule:

1\. Navigate to IGT Spade > Floor > Machine Maintenance. The Maintenance
Workbook window appears.

2\. Click the Drop Zone Setup tab. The Drop Zone Setup tab appears.

3\. Select an existing drop zone, then click Delete. A confirmation message appears.

4\. Click OK. The drop zone is deleted.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="146" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/147.1.png)




