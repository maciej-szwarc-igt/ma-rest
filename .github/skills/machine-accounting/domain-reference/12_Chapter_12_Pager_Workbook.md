# Chapter 12 Pager Workbook

The Pager Workbook feature alerts specified floor staff to machine events using pagers and/or email notifications. It also manages zoning information for the paging server.

## 12.1 Paging Triggers

Paging triggers define which machine events cause a page to be sent and to whom.

### Adding a Pager Trigger

The following information is required:

- **Event Code** — One or more event codes that trigger the page (see Event Codes reference)
- **Bonus** — The bonus dollar amount triggering a page
- **Minimum Amount ($)** and **Maximum Amount ($)** — Dollar range for initiating the trigger
- **Description** — Description of the paging trigger
- **Clear Event** — An event code that clears the page trigger
- **Escalation Mode** — One of:
  - No Escalation — Sends only one page
  - Active — Activates escalation levels
  - Notification Only — Sends a single email notification

### Modifying Pager Triggers

Existing trigger settings can be updated.

### Deleting Paging Triggers

Triggers can be removed. Deletion requires confirmation.

### Pager Actions

Pager actions specify which staff members are paged at each escalation level when a trigger activates.

To configure a pager action:

- **Pager Level** — The escalation level (sequential numbering)
- **Time Out** — Minutes until the next escalation level activates
- **Staff Selection** — Select individual staff members or all staff for the level

> If "Page All" is selected, all selected staff are paged every time. If not selected, the pager event rotates among the selected group.

Staff can be added to or removed from a pager level.

## 12.2 Email Notifications

Email notifications can be sent for machine events instead of or in addition to pager alerts.

### Setup Requirements

1. An **Email Device** equipment type must be created in the Equipment Types configuration.
2. An email address must be added as equipment with the Email Device type, using the email address as the Transmit ID.
3. The trigger must be set to **Notification Only** mode.

> When Notification Only is selected, a single text notification is sent and does not require the event to be cleared.

## 12.3 Paging Zone Setup

Paging zones assign floor locations to specific zones for targeted staff alerting.

### Managing Zones

- **Add Zone** — Create a new zone with an alphanumeric identifier.
- **Add Locations** — Assign machine locations to a zone. Multiple locations can be assigned at once.
- **Remove Locations** — Remove machine locations from a zone.
- **Rename Zone** — Change a zone's name.
- **Delete Zone** — Remove a zone entirely.

## 12.4 Hot Players

Hot player configuration defines thresholds for identifying high-activity players. When a player reaches the configured thresholds, the host receives a hot-player notification.

The following thresholds are configurable:

- **Hot Player $** — Dollar amount qualifying a player as a hot player
- **Hot Player Time** — Time window in minutes
- **Hot Player Games** — Minimum number of games played within the time window

Example: A hot player might be defined as a player who plays $100 within 30 minutes with a minimum of 10 games. Configuration varies by property.
