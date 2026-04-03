---
name: machine-accounting
description: "Machine Accounting (MA) domain knowledge for IGT gaming EGM audit workflows. Use when: working with periods (open/close/reopen), meter variances, drops (soft/hard), EFT imports, machine status transitions, user tasks, events, cabinet-level meters, MGA paytables, vouchers, zero drops, Correct Meter Variance (CMV), stored procedures, system configuration, maintenance console/workbook, EGM enable/disable, lease machines, flash reports, audit checklists, handpays/fills/jackpots, voucher/IVS drops, EZ Pay/WAT cashless drops, coupon/CEP/NCEP promotion audits, progressive workbooks, report generation, or reprinting work orders. Includes a user-guide chapter index for targeted reading."
---

# Machine Accounting (MA) Domain Skill

## Overview

Machine Accounting is an IGT system for auditing Electronic Gaming Machines (EGMs). It tracks meter readings, drops, events, and variances across accounting periods. This skill covers the core domain concepts, database procedures, and operational workflows.

## When to Use

- Managing accounting periods (open, close, reopen, start-over)
- Inserting or querying meter readings from floor systems
- Investigating or resolving meter variances (CMV)
- Working with machine status transitions (Pending Add → Active → Retire)
- Simulating events, drops, or EFT imports for testing
- Understanding drop types (soft, hard, zero drop, manual entry)
- Working with MGA paytable-level meters
- Managing user tasks during the audit process
- Debugging meter increment or denomination issues

## Core Concepts

### Accounting Periods
See [periods reference](./references/periods.md) for full rules on opening, closing, and reopening periods.

### Machine Status Transitions
See [machine-status reference](./references/machine-status.md) for the complete state machine diagram and required meter types per transition.

### Meter Types and Insertion
See the **ma-meters** skill for meter type codes, stored procedures, cabinet-level meter rules, event insertion, and MGA meter generation.

### Correct Meter Variance (CMV)
See [variances reference](./references/variances.md) for variance types, detection logic, and resolution workflow.

### User Tasks
See [user-tasks reference](./references/user-tasks.md) for how user tasks interact with period closure.

### Drops and EFT Imports
See [drops reference](./references/drops.md) for drop simulation, EFT import procedures, zero drops, vouchers, and audit meter workflows.

### MGA Paytable Meters
See the **ma-meters** skill for MGA meter generation, paytable queries, and the MGAMeter job pipeline.

## User Guide

The user guide provides detailed operational procedures organized by chapter. **Read only the chapters relevant to your current task** — do not load all chapters at once.

| # | Chapter | When to read |
|---|---------|-------------|
| 00 | [Preamble](./user-guide/00_preamble.md) | Document metadata, warranty info, and full table of contents. Rarely needed. |
| 01 | [System Overview](./user-guide/01_Chapter_1_System_Overview.md) | Understanding overall MA architecture, accounting periods, bonusing systems, voucher/EZ Pay integration, system components (workstations, FJP, drop utilities), and how different components interconnect. |
| 02 | [Starting Machine Accounting](./user-guide/02_Chapter_2_Starting_Machine_Accounting.md) | Initial setup, user logon, audit date selection, accounting calendar configuration, fiscal period definition, and password management. |
| 03 | [Navigating Machine Accounting](./user-guide/03_Chapter_3_Navigating_Machine_Accounting.md) | UI navigation, IGT Spade menu structure, Quick Access toolbar customization, and task group configuration. |
| 04 | [Configuration Options](./user-guide/04_Chapter_4_ConfigurationOptions.md) | System-wide configuration: general period settings, variance tolerances, voucher/WAT systems, casino info, tax rates/W2G forms, barcode printers, FJP station options, banned players, handpay limits, slip sequences, and display preferences. |
| 05 | [User Management Console](./user-guide/05_Chapter_5_User_Management_Console.md) | Organizational hierarchy, divisions, departments, jobs, user groups, individual user creation, permissions, and access rights. |
| 06 | [Maintenance Console](./user-guide/06_Chapter_6_Maintenance_Console.md) | Casino floor master data: cabinet types, sections, game types, display types, manufacturers, denominations, denomination ranges, and machine types. |
| 07 | [Maintenance Workbook](./user-guide/07_Chapter_7_Maintenance_Workbook.md) | Machine lifecycle: adding, updating, converting, and retiring machines; viewing machine details; machine verification tasks during audits. |
| 08 | [Enabling and Disabling EGMs](./user-guide/08_Chapter_8_Enabling_and_Disabling_EGMs.md) | Enabling/disabling individual machines or groups, creating EGM groups, and setting up automated enable/disable schedules. |
| 09 | [Player ID Locales](./user-guide/09_Chapter_9_Player_ID_Locales.md) | Configuring country and state codes for player identification and locale-specific requirements. |
| 10 | [Configuring Flash Reports](./user-guide/10_Chapter_10_Configuring_Flash_Reports.md) | Automated email report delivery: report categories (Audit, Bonus, Cashless, Dashboard), recipients, delivery schedules, and mandatory task options. |
| 11 | [Configuring Lease Machines](./user-guide/11_Chapter_11_Configuring_Lease_Machines.md) | Lease fee structures: formulas based on machine meters, rules with percentages/fixed amounts, daily lease amounts, and machine lease assignment. |
| 12 | [Pager Workbook](./user-guide/12_Chapter_12_Pager_Workbook.md) | Pager/email alerts for machine events: paging triggers, actions, email configuration, paging zones, and hot player thresholds. |
| 13 | [Floor Staff Workbook](./user-guide/13_Chapter_13_Floor_Staff_Workbook.md) | Floor staff management: activation/deactivation, promotional status, shift management, equipment check-out/check-in, and barcode tracking. |
| 14 | [Audit Checklist](./user-guide/14_Chapter_14_Audit_Checklist.md) | Complete 25-step daily audit workflow from period opening through closing, including all checkpoint validations. Essential for understanding the end-to-end audit process. |
| 15 | [Opening the Audit Day](./user-guide/15_Chapter_15_Opening_the_Audit_Day.md) | Period opening: starting the period, initializing handpay entries, retrieving period meters, User Tasks list, and Period Timeline Ribbon. |
| 16 | [Machine Meter Variances](./user-guide/16_Chapter_16_Machine_Meter_Variances.md) | Investigating and correcting meter variances: runaway meters, rollover, over-tolerance, RAM clears, misapplied voucher meters, meter adjustments, coin-in editing, tolerance management, and paytable reconciliation. |
| 17 | [Manual Meters](./user-guide/17_Chapter_17_Manual_Meters.md) | Entering and adjusting manual meter entries for non-communicating machines that require manual meter reads. |
| 18 | [Fills, Jackpots, and Hand Pays](./user-guide/18_Chapter_18_Fills_Jackpots_and_Hand_Pays.md) | Verifying and balancing hand pays (fills, jackpots, progressives, cancel credits, bonus jackpots) between system and cage, manual handpay entry, slip editing/voiding, aux fills, and jackpot variance acceptance. |
| 19 | [Voucher Drop — IVS Tasks](./user-guide/19_Chapter_19_Voucher_Drop_-_IVS_Tasks.md) | Auditing voucher-in/voucher-out variances from IVS soft-count vouchers and EZ Pay end-of-day issuance, importing voucher data, adjusting meters, and accepting variances. |
| 20 | [EZ Pay Cashless Drop](./user-guide/20_Chapter_20_EZ_Pay_Cashless_Drop.md) | Auditing WAT-in/WAT-out (Wager Account Transfer) variances for EZ Pay Smart Card and Mag Card transactions, importing cashless drop data, and documenting adjustments. |
| 21 | [Coupon Promotion Audit](./user-guide/21_Chapter_21_Coupon_Promotion_Audit.md) | Auditing coupon-in/coupon-out promotion drops, importing coupon data, adjusting meter variances, and accepting variances. |
| 22 | [Non-Cashable Electronic Promotion (NCEP) Audit](./user-guide/22_Chapter_22_Non-Cashable_Electronic_Promotion_NCEP_Audit.md) | Auditing non-cashable electronic promotion credits (Xtra Credit transfers) between player-tracking and EGM meters, importing NCEP data, and adjusting variances. |
| 23 | [Cashable Electronic Promotion (CEP)](./user-guide/23_Chapter_23_Cashable_Electronic_Promotion_CEP.md) | Auditing cashable electronic promotion (Xtra Credit, PointPlay, Bonus) against machine meter movement, importing CEP data, and adjusting variances. |
| 24 | [Soft Drop Tasks](./user-guide/24_Chapter_24_Soft_Drop_Tasks.md) | Soft drop audit: retrieving actual soft drops, assigning orphan cans, accepting/swapping/unaccepting variances within tolerances, and adjusting soft drop amounts and meters. |
| 25 | [Argentina Bill Tax-Out](./user-guide/25_Chapter_25_Argentina_Bill_Tax-Out.md) | Argentina-specific bill tax-out audit: importing bill tax-out data, verifying tax calculations, identifying variances, and adjusting amounts. |
| 26 | [Closing the Audit Period](./user-guide/26_Chapter_26_Closing_the_Audit_Period.md) | Final period closure: verifying machine retirements after drops are complete and closing the period to freeze audit information once all user tasks are done. |
| 27 | [Hard Drop Tasks](./user-guide/27_Chapter_27_Hard_Drop_Tasks.md) | Hard drop audit: retrieving actual hard drops, assigning orphan buckets, accepting/swapping/unaccepting variances, and adjusting hard drop amounts and meters. |
| 28 | [Audit Workbook](./user-guide/28_Chapter_28_Audit_Workbook.md) | EGM meter auditing: viewing electronic/physical meters, creating audit groups, reading floor meters with drop scanners, adjusting machine meters, and requesting immediate meter readings. |
| 29 | [Reprinting Work Orders](./user-guide/29_Chapter_29_Reprinting_Work_Orders.md) | Reprinting work orders for machines pending retirement or relocation, with filters for date, user, type, and machine number. |
| 30 | [Reports](./user-guide/30_Chapter_30_Reports.md) | Report generation: selecting reports, applying filters (machines, date ranges), exporting to various formats, and printing from the supervisor reporting interface. |
| 31 | [Progressive Workbook Tasks](./user-guide/31_Chapter_31_Progressive_Workbook_Tasks.md) | Progressive jackpot tracking (in development): configuring progressive workbooks, managing progressives, selecting participating machines, and adjusting values/reset amounts/contribution percentages for stand-alone and linked pools. |
