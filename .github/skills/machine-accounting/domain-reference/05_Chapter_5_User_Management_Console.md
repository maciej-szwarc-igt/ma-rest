# Chapter 5 User Management

Use User Management to configure users, groups, jobs, departments, and divisions.

> If UMS (User Management System) integration is enabled, use UMS to configure these items instead.

These items must be configured in a specific order due to dependencies:

1. Divisions
2. Departments
3. Jobs
4. Groups
5. Users

> Users are grouped by departments and jobs within a department, but also by job titles across departmental lines.

## 5.1 Divisions

Divisions are the property's main operating units (e.g., Food and Beverage, Hotel, Casino).

### Adding a Division

The following information is required to create a division:

- **Division** — Name of the division
- **Code** — A required alphanumeric code, most often used for a general ledger (GL) or expense code

### Modifying a Division

The Division name and Code can be updated for existing divisions.

### Deactivating a Division

A division can be deactivated. Deactivated divisions are hidden from default views but can be made visible.

### Reactivating a Division

An inactive division can be reactivated and its information updated as part of reactivation.

## 5.2 Departments

Departments are the areas in which users are assigned to work (e.g., Slots, Accounting).

### Adding a Department

The following information is required:

- **Department** — Name of the department
- **Division** — The division to associate the department with
- **Code** — A required alphanumeric code (GL or expense code)

### Modifying a Department

Department information can be updated for existing departments.

### Deactivating a Department

> A department must be disassociated from all jobs, groups, and users BEFORE deactivation.

### Reactivating a Department

An inactive department can be reactivated and its information updated.

## 5.3 Jobs

Jobs are the positions that employees hold (e.g., Slot Tech, Controller, Regulator).

> Machine Accounting disables job management if UMS integration is enabled. Manage jobs in UMS instead.

### Adding a Job

The following information is required:

- **Job** — Name of the job
- **Department** — The department to associate the job with
- **Code** — A required alphanumeric code (GL or expense code)

### Modifying a Job

> If UMS integration is enabled, job information is read-only.

### Deactivating a Job

> A job must be disassociated from all groups and users BEFORE deactivation.

### Reactivating a Job

An inactive job can be reactivated and its information updated.

## 5.4 Groups

Groups define user permission sets. Employees are assigned to groups that determine their rights and access within the system.

### Adding a Group

The following information is required:

- **Group** — Name of the group

After creation, the Group Definition must be configured with specific permissions.

### Group Permissions

Permissions control access to specific features and functions. Each group has a set of permissions that can be individually enabled or disabled.

### Modifying Groups

Group permissions and settings can be updated.

### Deactivating Groups

Groups can be deactivated when no longer needed.

### Reactivating Groups

Inactive groups can be reactivated.

## 5.5 Users

Users are the individuals who access Machine Accounting.

### Adding a User

The following information is required:

- **User Name** — Login identifier
- **First Name** and **Last Name**
- **Employee Number**
- **Job** — The job position assigned to the user
- **Group** — The permission group assigned to the user
- **Password** — Initial password

### Modifying Users

User information, job assignments, and group assignments can be updated.

### Deactivating Users

Users can be deactivated to revoke system access.

### Reactivating Users

Inactive users can be reactivated.
