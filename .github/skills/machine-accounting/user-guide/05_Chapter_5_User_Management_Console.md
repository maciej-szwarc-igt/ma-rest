# Chapter 5 User Management Console

Use the User Management Console to configure users, groups, jobs, departments, and
divisions.




![](MachineAccounting_UserGuide_images/55.2.png)




If UMS integration is enabled, use UMS to configure users, groups, jobs,
departments, and divisions instead. For more information, refer to the UMS User
Guide for the version of UMS in use.

These items must be configured in a specific order due to dependencies among the configured
items. For example, a job must be created prior to an employee being assigned to that job.


## Configuration Order

1\. Divisions

2\. Departments

3\. Jobs

4\. Groups

5\. Users




![](MachineAccounting_UserGuide_images/55.3.png)




i
Users are grouped by departments and jobs within a department but also by job
titles across departmental lines.


# To access the User Management Console:

Click User Management Console in the Quick Access Toolbar OR select IGT Spade >
Configuration > User Management. The User Management Console screen appears.




![Figure 5-1 User Management Console](MachineAccounting_UserGuide_images/55.4.png)




<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="55" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->


## 5.1 Divisions

Divisions are the property's main operating units, such as food and beverage, hotel, and casino.

To access the Divisions pane:

Navigate to IGT Spade > Configuration > User Management > Divisions. The
Divisions pane opens.




![Figure 5-2 User Management Console-Divisions](MachineAccounting_UserGuide_images/56.1.png)




### 5.1.1 Adding Divisions


#### To add a division:

1\. Click Add in the Divisions pane. The New Division window appears.




![Figure 5-3 New Division](MachineAccounting_UserGuide_images/56.2.png)




2\. Enter a name for the division in the Division field.

3\. Enter a code number for the division in the Code field.

i
The code number is a required alphanumeric field and is most often used for a
general ledger (GL) or expense code.

4\. Click Save. The New Division window closes, and the Divisions pane displays the new
division.

<!-- PageNumber="56" -->
<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->


### 5.1.2 Modifying Divisions

To modify an existing division:

1\. Select a division to modify in the Divisions pane.

2\. Click Modify. The Modify Division window appears.

3\. Modify the Division or Code as needed.

4\. Click Save. The Divisions pane updates with the changes.


### 5.1.3 Deactivating Divisions

To deactivate a division:

1\. Select a division to deactivate in the Divisions window.

2\. Click Deactivate. A confirmation prompt appears.

3\. Click Yes. The division becomes inactive.


### 5.1.4 Reactivating Divisions

To reactivate an inactive division:

1\. Select Include Inactive in the Divisions pane. The Divisions pane displays inactive
divisions.




![](MachineAccounting_UserGuide_images/57.1.png)




2\. Select a division to reactivate in the Divisions pane.

3\. Click Reactivate. The Reactivate Divisions window appears.

4\. Update the information as needed.

5\. Click Save. The division becomes active.


## 5.2 Departments

Departments are the areas in which users are assigned to work, such as Slots or Accounting.
To access the Departments pane:

Navigate to IGT Spade > Configuration > User Management > Departments. The
Departments pane appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="57" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->




![Figure 5-4 User Management Console-Departments](MachineAccounting_UserGuide_images/58.1.png)




### 5.2.1 Adding Departments


#### To add a department:

1\. Click Add in the Departments pane. The New Department window opens.




![](MachineAccounting_UserGuide_images/58.2.png)




2\. Enter a name for the new department in the Department field.

3\. Select a division to associate the department with from the Division drop-down list.




![](MachineAccounting_UserGuide_images/58.3.png)




Ť
The Card Layout field is linked to the Patron Management System and indicates the
layout used for Patron Management users' staff cards. The field is inactive (gray)
in Machine Accounting.

4\. Enter a department number in the Code field.




![](MachineAccounting_UserGuide_images/58.4.png)




This is a required alphanumeric field and is most often used for a general ledger
(GL) or expense code.

5\. Click Save. The department appears on the Departments pane.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="58" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->


### 5.2.2 Modifying Departments

To modify an existing department:

1\. Select a department to modify in the Departments window.

2\. Click Modify. The Modify Department window opens.

3\. Modify the information as needed.

4\. Click Save. The changes save.


### 5.2.3 Deactivating Departments




![](MachineAccounting_UserGuide_images/59.1.png)




A department must be disassociated from all jobs, groups, and users BEFORE
deactivation.


#### To deactivate a department:

1\. Select a department to deactivate in the Departments window. The Deactivate
Department window opens.

2\. Click Deactivate. A confirmation prompt appears.

3\. Click Yes. The department is deactivated.


### 5.2.4 Reactivating Departments

To reactivate an inactive department:

1\. Select Include Inactive in the Departments pane. Inactive departments appear on the
Departments pane.




![](MachineAccounting_UserGuide_images/59.2.png)




2\. Select a department to reactivate in the Departments window.

3\. Click Reactivate. The Reactivate Department window opens.

4\. Update any information, as needed.

5\. Click Save. The department is reactivated.


### 5.3 Jobs

Jobs are the positions that employees hold. Example jobs include Slot Tech, Controller, and
Regulator.




![](MachineAccounting_UserGuide_images/59.3.png)




!
Machine Accounting disables the options to add, modify, deactivate, and reactivate
jobs if UMS integration is enabled. Manage jobs in UMS instead.

To access the Jobs pane:

Navigate to IGT Spade > Configuration > User Management > Jobs. The Jobs
pane appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="59" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->




![Figure 5-5 User Management Console-Jobs](MachineAccounting_UserGuide_images/60.1.png)




#### 5.3.1 Adding Jobs

To add a job:

1\. Click Add in the Jobs pane. The New Job Type window appears.




![](MachineAccounting_UserGuide_images/60.2.png)




2\. Enter a name for the job in the Job field.

3\. Select the department to associate the job with from the Department drop-down list.

4\. Enter a job number in the Code field (a required alphanumeric field that is most often
used for a general ledger (GL) or expense code).

İ
The Host, Commissioned Rep, and Trip Authorizer fields are not applicable to
Machine Accounting.




![](MachineAccounting_UserGuide_images/60.3.png)




5\. Click Save. The new job type is saved.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="60" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->


#### 5.3.2 Modifying Jobs




![](MachineAccounting_UserGuide_images/61.1.png)




If UMS integration is enabled, the Update Job Type screen appears for
informational purposes but cannot be modified.

To modify an existing job:

1\. Select a job to modify in the Jobs pane.

2\. Click Modify. The Update Job Type window appears.

3\. Modify the information as needed.

4\. Click Save. The changes save.


#### 5.3.3 Deactivating Jobs




![](MachineAccounting_UserGuide_images/61.2.png)




A job must be disassociated from all groups and users BEFORE deactivation.

To deactivate a job:

1\. Select a job to deactivate in the Jobs pane.

2\. Click Deactivate. A confirmation prompt appears.

3\. Click Yes. The job is deactivated.


#### 5.3.4 Reactivating Jobs

To reactivate an inactive job:

1\. Select the Include Inactive check box in the Jobs pane. The Jobs pane displays inactive
jobs.




![](MachineAccounting_UserGuide_images/61.3.png)




2\. Select a job to reactivate in the Jobs pane.

3\. Click Reactivate. The Reactivate Job Type window appears.

4\. Update the information as needed.

5\. Click Save. The job is reactivated.


### 5.4 Groups

Use the Groups pane to assign employees to specific user groups and designate each group's
rights and permissions.

To access the Groups pane:

Navigate to IGT Spade > Configuration > User Management > Groups. The
Groups pane appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="61" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->




![Figure 5-6 User Management Console-Groups](MachineAccounting_UserGuide_images/62.1.png)




#### 5.4.1 Adding Groups


##### To add a group:

1\. Click Add in the Groups pane. The New Group window appears.




![](MachineAccounting_UserGuide_images/62.2.png)




2\. Enter a name for the group in the Group field.

3\. Click Save. The Group Definition window appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="62" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->




![](MachineAccounting_UserGuide_images/63.1.png)




4\. Select Permissions. Permission groups display in the left pane.

a. Select a group on the left pane. The right pane populates with the group's permissions.

b. On the right pane, select the permissions necessary for the group to complete their job
tasks.

5\. Select Reports. The left pane shows the report groups.

a. Select a group on the left pane. The right pane populates with the reports available to
the group.

b. On the right pane, select the reports necessary for the group to complete their job
tasks.

6\. Click OK. The group is added, and the updated Groups pane appears.


#### 5.4.2 Modifying Groups

To modify an existing group:

1\. Select a group to modify in the Groups pane.

2\. Click Modify. The Modify Group window appears.

3\. Modify the information as needed.

4\. Click Save. The changes save.


#### 5.4.3 Deactivating Groups




![](MachineAccounting_UserGuide_images/63.2.png)




A group must be disassociated from all users BEFORE deactivation.

To deactivate a group:

1\. Select a group to deactivate in the Groups pane.

2\. Click Deactivate. A confirmation prompt appears.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="63" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->

3\. Click Yes. The group is deactivated.


#### 5.4.4 Reactivating Groups


##### To reactivate an existing group:

1\. Select the Include Inactive check box in the Groups pane. The Groups pane displays
inactive groups.




![](MachineAccounting_UserGuide_images/64.1.png)




2\. Select a group to reactivate in the Groups pane.

3\. Click Reactivate. The Reactivate Group window appears.

4\. Update the information as needed.

5\. Click Save. The group is reactivated.


### 5.5 Users

Users are the personnel who use IGT Advantage Machine Accounting while performing their
job. The system administrator enters necessary user information and assigns user access and
rights.

To access the Users pane:

Navigate to IGT Spade > Configuration > User Management > Users. The Users
pane appears.

User Management Console

×
☒




![](MachineAccounting_UserGuide_images/64.2.png)




<table>
<tr>
<th>Login</th>
<th>First Name</th>
<th>Last Name</th>
<th>Middle Initial</th>
<th>License</th>
<th>Description</th>
<th>A</th>
</tr>
<tr>
<td>AANDRADE</td>
<td>Anthony</td>
<td>Andrade</td>
<td></td>
<td></td>
<td>TTSS Admin</td>
<td></td>
</tr>
<tr>
<td>ABSREDEMPTION</td>
<td>ABSREDEMPTION</td>
<td>GAMING</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>ADI</td>
<td>ADI</td>
<td>Systems</td>
<td>Z</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>ATTSTAT</td>
<td>ATTSTAT</td>
<td>GAMING</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>AUDITOR1</td>
<td>Slot</td>
<td>Auditor</td>
<td></td>
<td></td>
<td>Auditor</td>
<td></td>
</tr>
<tr>
<td>BORINGC</td>
<td>Christy</td>
<td>Boring</td>
<td></td>
<td></td>
<td>TTSS Admin</td>
<td></td>
</tr>
<tr>
<td>BSAECK</td>
<td>Brandon</td>
<td>Saeck</td>
<td></td>
<td></td>
<td>TTSS Admin</td>
<td></td>
</tr>
<tr>
<td>CAGE1</td>
<td>cage</td>
<td>one</td>
<td></td>
<td></td>
<td>Audit Manager</td>
<td></td>
</tr>
<tr>
<td>CAGE2</td>
<td>cage</td>
<td>two</td>
<td></td>
<td></td>
<td>Audit Manager</td>
<td></td>
</tr>
<tr>
<td>CAGE3</td>
<td>cage</td>
<td>three</td>
<td></td>
<td></td>
<td>Audit Manager</td>
<td></td>
</tr>
<tr>
<td>CAGE4</td>
<td>Cage</td>
<td>Four</td>
<td></td>
<td></td>
<td>Audit Manager</td>
<td></td>
</tr>
<tr>
<td>CAGE5</td>
<td>Cage</td>
<td>Five</td>
<td></td>
<td></td>
<td>Audit Manager</td>
<td></td>
</tr>
<tr>
<td>CAGE6</td>
<td>Cage</td>
<td>Six</td>
<td></td>
<td></td>
<td>Audit Manager</td>
<td></td>
</tr>
<tr>
<td>CBORING</td>
<td>Christy</td>
<td>Boring</td>
<td></td>
<td></td>
<td>TTSS Admin</td>
<td></td>
</tr>
<tr>
<td>CCS</td>
<td>CCS</td>
<td>Systems</td>
<td>Z</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>CISUSER</td>
<td>CIS</td>
<td>USER</td>
<td></td>
<td></td>
<td>TTSS Admin</td>
<td></td>
</tr>
<tr>
<td>CSLATER</td>
<td>Chris</td>
<td>Slater</td>
<td></td>
<td></td>
<td>TTSS Admin</td>
<td></td>
</tr>
<tr>
<td>CTA</td>
<td>CTA</td>
<td>Systems</td>
<td>Z</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>CustomRating</td>
<td>CustomRating</td>
<td>Systems</td>
<td>Z</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>GREENM</td>
<td>Marcos</td>
<td>Green</td>
<td></td>
<td></td>
<td>TTSS Admin</td>
<td></td>
</tr>
<tr>
<td>HNELSON</td>
<td>Heather</td>
<td>Nelson</td>
<td></td>
<td></td>
<td>TTSS Admin</td>
<td></td>
</tr>
<tr>
<td>IB</td>
<td>IB</td>
<td>Systems</td>
<td>Z</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>IGTSYSTEMS</td>
<td>IGT</td>
<td>SYSTEMS</td>
<td></td>
<td></td>
<td>TTSS Admin</td>
<td>V</td>
</tr>
</table>


Figure 5-7 User Management Console-Users

<!-- PageNumber="64" -->
<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->


#### 5.5.1 Adding Users

To add a user:

1\. Navigate to IGT Spade > Configuration > User Management > Users. The Users
pane opens.

2\. Click Add ... in the Users pane. The New User window appears.




![](MachineAccounting_UserGuide_images/65.1.png)




3\. Use the following table as a reference for completing the New User window:


<table>
<tr>
<th>Field</th>
<th>Description/Action</th>
</tr>
<tr>
<td>Logon Name</td>
<td>Enter a login name for the new user (an alphanumeric combination of one to 15 characters).</td>
</tr>
<tr>
<td>First Name</td>
<td>Enter the user's first name.</td>
</tr>
<tr>
<td>M.I.</td>
<td>Enter the user's middle initial.</td>
</tr>
<tr>
<td>Last name</td>
<td>Enter the user's last name.</td>
</tr>
<tr>
<td>Display Name</td>
<td>Enter the user's name as displayed in a mail merge when creating letters for printing in the Contact Workbook.</td>
</tr>
<tr>
<td>Job Description</td>
<td>Select the user's job role.</td>
</tr>
<tr>
<td>Job Title</td>
<td>Enter the user's job title (can be helpful if the job has several applicable titles).</td>
</tr>
<tr>
<td>License</td>
<td>Enter the user's gaming license number or a specific user number.</td>
</tr>
<tr>
<td>Password</td>
<td>Enter a unique password (an alphanumeric combination of six to 10 characters). O 1 Assign a generic password and instruct the user to change the password after they first log on.</td>
</tr>
<tr>
<td>Confirm Password</td>
<td>Re-enter unique password entered in the Password field.</td>
</tr>
<tr>
<td>External Ref.</td>
<td>Enter the third-party software interface .</td>
</tr>
<tr>
<td>Commission</td>
<td>Commission earned by this user (populated from Patron Management).</td>
</tr>
<tr>
<td>Lock Account</td>
<td>Select to prevent user from accessing account.</td>
</tr>
<tr>
<td>Change Password on next login</td>
<td>Select to require a user to change the password.</td>
</tr>
<tr>
<td colspan="2">Floor Staff Only</td>
</tr>
<tr>
<td>PIN</td>
<td>Enter a unique PIN.</td>
</tr>
<tr>
<td>Confirm PIN</td>
<td>Re-enter the PIN entered in the PIN field.</td>
</tr>
<tr>
<td>PIN Locked</td>
<td>Select to prevent the user from resetting the PIN if locked out.</td>
</tr>
<tr>
<td colspan="2">i All field descriptions listed in blue text are required.</td>
</tr>
</table>


4\. Click Save. The user is added, and the updated Users pane displays.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="65" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->


#### 5.5.2 Defining Users

Once a user has been created, the system administrator must assign the user to at least one
group in order to associate user rights to the user.

To define a user's groups:

1\. Navigate to IGT Spade > Configuration > User Management > Users. The Users
pane opens.

2\. Select a user to define in the Users pane.

3\. Click Define. The Group Assignment window opens.




![](MachineAccounting_UserGuide_images/66.1.png)




4\. Select a site from the Site drop-down list.

5\. To assign the user to a group listed in the Not a Member of pane:

a. Select a group to assign the user from the Not a Member of pane.

b. Click Add to assign the group to the Member of pane, OR
Click Add All to assign the user to all groups listed in the Not a Member of pane.

6\. To remove the user from in the Member of pane:

a. Select a group to assign the user from the Member of pane. (Press and hold Ctrl to
select multiple groups.)

b. Click Remove, OR
Click Removal All to remove the user from all groups listed in the Member of pane.

7\. Click Done. The user is assigned to the selected groups, and the updated Users pane
appears.


#### 5.5.3 Modifying Users

To modify an existing user:

1\. Navigate to IGT Spade > Configuration > User Management > Users. The Users
pane opens.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="66" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->

2\. Select a user to modify in the Users pane.

3\. Click Modify. The Update User window appears.

4\. Modify the information as needed.

5\. Click Save. The changes save, and the Users window updates.


#### 5.5.4 Deactivating Users




![](MachineAccounting_UserGuide_images/67.1.png)




A user must be disassociated from all divisions, departments, jobs, and groups
BEFORE deactivation.


#### To deactivate a user:

1\. Navigate to IGT Spade > Configuration > User Management > Users. The Users
pane opens.

2\. Select a user to deactivate in the Users pane.

3\. Click Deactivate. A confirmation prompt appears.

4\. Click Yes to deactivate the user.


## 5.5.5 Reactivating Users

To reactivate an inactive user:

1\. Navigate to IGT Spade > Configuration > User Management > Users. The Users
pane opens.

2\. Select the Include Inactive check box in the Users pane to display inactive users.




![](MachineAccounting_UserGuide_images/67.2.png)




3\. Select a user to reactivate in the Users pane.

4\. Click Reactivate. The Update Users window opens.

5\. Update the information as necessary.

6\. Click Save. The user is reactivated.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="67" -->
<!-- PageBreak -->

<!-- PageHeader="Chapter 5 User Management Console" -->

This page is intentionally left blank.

<!-- PageFooter="Machine Accounting 9.7.5" -->
<!-- PageNumber="68" -->
<!-- PageBreak -->




![](MachineAccounting_UserGuide_images/69.1.png)




