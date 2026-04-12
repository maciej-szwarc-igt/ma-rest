# Chapter 13 Floor Staff Workbook

The Floor Staff feature tracks personnel and equipment assigned to the casino floor. Each employee and piece of equipment is entered into the system and assigned a unique identification number. Employees receive specific rights within the system, and equipment usage is tracked based on equipment rights.

## 13.1 Floor Staff Functions

The following operations are available:

- Activate and deactivate floor staff
- Promote and demote individuals or groups of floor staff
- Change shift status (ON or OFF shift)
- Set pager options (Always On Shift or Clear Always On Shift)
- Check equipment IN and OUT
- Print barcode labels for equipment

## 13.2 Filtering Floor Staff

The floor staff list can be filtered by the following criteria:

- **Active** — Only active staff
- **Promoted** — Only promoted staff
- **On Shift** — Only staff currently on shift
- **Paging - Always On Shift** — Only staff with Always On Shift enabled
- **Promote Eligible** — Only staff eligible for promotion
- **Demote Eligible** — Only staff promoted during the current shift

Staff status is indicated by color:

| Color | Status |
|-------|--------|
| Green | Currently ON SHIFT |
| Red | ON SHIFT longer than eight hours |
| Yellow | Not activated |

## 13.3 Activating Floor Staff

Users must be added to the system (via UMS or the Maintenance Console) and activated before they can be placed ON Shift or issued equipment.

One or more staff members can be activated at once.

## 13.4 Deactivating Floor Staff

A user may be deactivated regardless of current status. For example, a user shown as on-shift may be deactivated.

## 13.5 Promoting Floor Staff

An employee or group of employees may be temporarily promoted up one level for the duration of a shift. At the end of the shift, employees automatically revert to their regular title.

Promotion requires selecting the target permission group. The promotion grants the permissions defined for that group.

## 13.6 Demoting Floor Staff

Promoted employees can be demoted back to their previous level. One or more staff members can be demoted at once.

## 13.7 On-Shift Status Change

Staff members can be placed on shift. The shift change date and time are recorded.

> Employee shifts are normally changed at the Attendant Workstation.

## 13.8 Off-Shift Status Change

Staff members can be taken off shift. The equipment custody status should be confirmed before completing the off-shift transition.

> Employee shifts are normally changed at the Attendant Workstation.

## 13.9 Paging - Always On Shift

The Always On Shift option is used for employees who need to receive pages or email notifications at any time, regardless of shift status. The setting takes effect immediately.

## 13.10 Clearing Paging - Always On Shift

The Always On Shift option can be removed for an employee, stopping off-hours notifications.

## 13.11 Checking Out Equipment

Equipment can be issued to on-shift staff members. The system tracks which equipment is checked out to which employee.

> Equipment is normally issued at the Attendant Workstation.

To check out equipment:

1. Select an on-shift staff member.
2. Select the equipment to issue from the available equipment list.
3. Confirm the checkout.

## 13.12 Checking In Equipment

Equipment can be returned by staff members. The system updates the custody record.

## 13.13 Equipment Management

Equipment records can be created, modified, and deleted. Each equipment item is assigned:

- **Equipment Number** — Unique identifier
- **Equipment Type** — Category of the equipment
- **Description** — Description of the item

## 13.14 Equipment Types

Equipment types categorize the equipment used on the casino floor. Each type has:

- **Description** — Name of the equipment type
- **Type** — Classification (e.g., Standard, Email Paging)
