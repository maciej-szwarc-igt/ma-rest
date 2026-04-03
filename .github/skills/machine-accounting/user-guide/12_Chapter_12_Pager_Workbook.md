# Chapter 12 Pager Workbook

The Pager Workbook feature alerts specified floor staff to a variety of machine events using
pagers and/or e-mail notifications. In addition, use this feature to create zoning information for
the paging server.

To access the Pager Workbook:

Select IGT Spade > Floor > Pagers. The Pager Workbook window opens to the Paging
Trigger tab.




![Figure 12-1 Pager Workbook](MachineAccounting_UserGuide_images/169.2.png)




## 12.1 Paging Triggers

Add, view, modify, and delete paging triggers and actions in the Paging Trigger window.
Configure machine events, such as a large jackpot, to trigger the paging server.


### 12.1.1 Adding Pager Triggers

To add a pager trigger:

1\. Click IGT Spade > Floor > Pagers. The Pager window opens.

2\. Click Add. The Pager Trigger Update window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="169" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 12 Pager Workbook" -->




![Figure 12-2 Pager Trigger Update](MachineAccounting_UserGuide_images/170.1.png)




3\. Click ...
...
in the Event Code field. The Select an Item window opens.




![Figure 12-3 Pager Trigger-Select an Item](MachineAccounting_UserGuide_images/170.2.png)




4\. Select one or more event codes, then click OK. The Pager Trigger Update window
reappears.

Refer to Event Codes and Descriptions on page 331 for more information.




![](MachineAccounting_UserGuide_images/170.3.png)




5\. Click the Bonus drop-down, then select the bonus dollar amount triggering a page.

6\. Enter the minimum and maximum dollar amounts initiating a paging trigger in the
Minimum Amount (\$) and Maximum Amount (\$) fields.

7\. Enter a description of the paging trigger in the Description field.

8\. Click ...
...
in the Clear Event field. The Select an Item window appears.

9\. Select an event code to clear the page trigger, then click OK. The Pager Trigger Update
window reappears.

10\. Select one of the following options:

<!-- PageNumber="170" -->
<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 12 Pager Workbook" -->

. No Escalation to configure the page trigger to send only one page.

· Active to activate the page trigger.

· Notification Only to send a single e-mail message.

11\. Click Save. The paging trigger is created, and the updated Pager window reopens.
OR

Click Cancel. The Pager Trigger Update window closes without the paging trigger saving.


### 12.1.2 Modifying Pager Triggers

To modify an existing pager trigger:

1\. Click IGT Spade > Floor > Pagers. The Pager window appears.

2\. Select a trigger, then click Modify. The Pager Trigger Update window opens.

3\. Edit the fields as needed, then click Save. The paging trigger updates, and the updated
Paging Trigger window reappears.
OR

Click Cancel. The paging trigger updates do not save, and the Pager window reappears.


### 12.1.3 Deleting Paging Triggers

To delete an existing pager trigger:

1\. Click IGT Spade > Floor > Pagers. The Pager window appears.

2\. Select a specific trigger in the Paging Trigger tab, then click Delete. A confirmation
prompt appears.

3\. Click Yes. The trigger is deleted, and the Pager window reappears.


### 12.1.4 Updating Pager Actions

The Pager Action Update window specifies which staff members are paged when the pager
trigger is activated. Select an existing level to view the staff assigned to that level, or click
<new> to create a new level of action.

To update a pager action:

1\. Click IGT Spade > Floor > Pagers. The Pager window appears.

2\. Select a trigger, then click Action. The Pager Action Update window opens.




![](MachineAccounting_UserGuide_images/171.1.png)




İ
No Escalation displays to the right of the Pager Level drop-down list if it is selected
on the Pager Trigger Update window.

3\. Click the Pager Level drop-down, then select <New> or an existing response level.




![](MachineAccounting_UserGuide_images/171.2.png)




i
The newest level is the next available number in the sequence.

The number of pager levels depends on how many escalations are desired. The
Time Out and Paged fields must be selected for each pager level.

4\. Enter the time in minutes until the next level is activated (escalation) in the Time Out
field.

5\. Select the check box next to the staff to be paged by this action in the Available field, or
click Page All to select all staff. Click Add. The staff are included in the pager event.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="171" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 12 Pager Workbook" -->




![](MachineAccounting_UserGuide_images/172.1.png)




Selecting Page All pages the selected staff every time a pager event occurs. If Page
All is not selected, the pager event rotates the page among the selected group.

6\. Select the staff in the Paged pane to remove from a pager event, or press and hold CTRL
to select multiple members, then click Remove. The staff are removed from the pager
event.

7\. Click Save. The changes save, and the Pager window reappears.


## 12.2 E-mail Notifications

Use the E-mail Notifications function to send e-mail notifications for a variety of machine
events.


### 12.2.1 Adding New Equipment Types

To add a new equipment type:

1\. Select IGT Spade > Floor > Equipment. The Equipment Information window appears.

2\. Click Edit Types. The Equipment Types window opens.

3\. Click Add in the Equipment Types window. The Equipment Type Update window opens.

4\. Select Email Device in the Description field.

5\. Select Email Paging from the drop-down list in the Type field.




![Figure 12-4 New Equipment Types](MachineAccounting_UserGuide_images/172.2.png)




6\. Click Save. The equipment type is saved.


### 12.2.2 Adding New E-Mail Addresses

To add a new e-mail address:

1\. Select IGT Spade > Floor > Equipment. The Equipment Information window appears.

2\. Click Add. The Equipment Update window appears.

<!-- PageNumber="172" -->
<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 12 Pager Workbook" -->




![Figure 12-5 New E-Mail Address](MachineAccounting_UserGuide_images/173.1.png)




3\. Select Email Device from the Equipment Type drop-down list.

4\. Type the e-mail address to send notifications in the Transmit ID field.

5\. Click Save. The new email address saves.

6\. Verify that Notification Only is selected on the Pager Trigger Update window.




![](MachineAccounting_UserGuide_images/173.2.png)




When Notification Only is selected: A single text notification is sent and does not
require the event to be cleared.


### 12.3 Paging Zone Setup

Access the Paging Zone Setup tab to do the following:

· Assign a floor location to a paging zone

· Add a new zone

· Add and remove locations from a zone

· Rename a zone

· Delete a zone


#### 12.3.1 Accessing the Paging Zone Setup Tab

To access the Pager Workbook:

1\. Click IGT Spade > Floor > Pagers. The Pager Workbook window opens.

2\. Click the Paging Zone Setup tab. The Paging Zone Setup tab appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="173" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 12 Pager Workbook" -->




![](MachineAccounting_UserGuide_images/174.1.png)




#### 12.3.2 Adding New Zones


##### To add a new paging zone:

1\. Click IGT Spade > Floor > Pagers. The Pager Workbook window opens.

2\. Click the Paging Zone Setup tab. The Paging Zone Setup tab appears.

3\. Select a zone from the Zone drop-down list.

4\. Click New.

5\. Enter an alphanumeric character for the new zone. The new zone is saved.


#### 12.3.3 Adding Pager Zone Locations

To add a pager zone location:

1\. Click IGT Spade > Floor > Pagers. The Pager Workbook window opens.

2\. Click the Paging Zone Setup tab. The Paging Zone Setup tab appears.

3\. Select a machine location in the left pane to add to the paging zone in the right pane.
OR
Press and hold CTRL to select multiple machine locations.

4\. Click Add. The selected machines are assigned to the zone (right pane).


### 12.3.4 Removing Pager Zone Locations

To remove a pager zone location:

1\. Click IGT Spade > Floor > Pagers. The Pager Workbook window opens.

2\. Click the Paging Zone Setup tab. The Paging Zone Setup tab appears.

3\. Select a machine location in the right pane to remove from the paging zone.
OR
Press and hold CTRL to select multiple machine locations.

4\. Click Remove. The pager zone locations are removed from the zone.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="174" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 12 Pager Workbook" -->


# 12.3.5 Renaming Paging Zones

To rename an existing paging zone:

1\. Click IGT Spade > Floor > Pagers. The Pager Workbook window opens.

2\. Click the Paging Zone Setup tab. The Paging Zone Setup tab appears.

3\. Select the zone to rename from the Zone drop-down list, then click Modify. The Modify
Paging Zone window appears.




![](MachineAccounting_UserGuide_images/175.1.png)




4\. Select Rename Zone.

5\. Select a zone from the Zones field.

6\. Enter the new zone name in the New Name field.

7\. Click OK. The paging zone is renamed.


# 12.3.6 Deleting Paging Zones

To delete an existing paging zone:

1\. Click IGT Spade > Floor > Pagers. The Pager Workbook window opens.

2\. Click the Paging Zone Setup tab. The Paging Zone Setup tab appears.

3\. Select the zone to delete from the Zone drop-down list, then click Modify. The Modify
Paging Zone window appears.

4\. Select Delete Zone.

5\. Select a zone from the Zones field.

6\. Click OK. The selected paging zone is deleted.


# 12.4 Hot Players

Configure hot players in the Hot Players tab of the Pager Workbook window. When a player
reaches the thresholds configured in this tab, the host receives a hot-player message. For
example, a hot player might be a player who plays $100 (Hot Player $) within 30 minutes
(Hot Player Time) playing a minimum of 10 games (Hot Player Games). This configuration
varies by property.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="175" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 12 Pager Workbook" -->




![Figure 12-6 Pager Workbook - Hot Players](MachineAccounting_UserGuide_images/176.1.png)




## To configure hot player thresholds:

1\. Click IGT Spade > Floor > Pagers. The Pager Workbook window opens.

2\. Click the Hot Players tab. The Hot Players tab opens.

3\. Enter a dollar amount to qualify a player as a hot player in the Hot Player $ field.

4\. Enter the amount of time (in minutes) indicating a hot player in the Hot Player Time
field.

5\. Enter the number of games indicating a hot player in the Hot Player Games field.

6\. Click Apply. The settings save.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="176" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/177.1.png)




