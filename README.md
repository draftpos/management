# Business Operations Management (Management)

[![Odoo Version](https://img.shields.io/badge/Odoo-19.0-714B67?logo=odoo&logoColor=white)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.en.html)
[![Maintained by](https://img.shields.io/badge/Maintained%20by-DraftPOS%20%2F%20Havano-22c55e.svg)](https://github.com/draftpos)

A comprehensive business operations and customer lifecycle management application built for Odoo 19. The **Management** app unifies sales performance, field jobs, marketing attribution, customer support tickets, and post-service client follow-ups into a single operational workspace.

---

## Table of Contents

- [Overview](#overview)
- [Application Modules & Features](#application-modules--features)
  - [1. Jobs Management](#1-jobs-management)
  - [2. Marketing & Campaign Tracking](#2-marketing--campaign-tracking)
  - [3. Sales Performance](#3-sales-performance)
  - [4. Activity & Field Performance](#4-activity--field-performance)
  - [5. Help Desk & Support Ticketing](#5-help-desk--support-ticketing)
  - [6. Client Follow-Up](#6-client-follow-up)
  - [7. Product Catalog](#7-product-catalog)
  - [8. Configuration & Settings](#8-configuration--settings)
- [Data Model Reference](#data-model-reference)
- [Access Rights & Security](#access-rights--security)
- [Installation & Deployment](#installation--deployment)
- [Technical Notes](#technical-notes)

---

## Overview

Modern field service, B2B sales, and client management teams require tightly coupled tracking across all customer touchpoints. The **Management** application eliminates silos between field workers, support technicians, and sales reps by providing:

1. **Clear Service Job Pipelines**: Transition jobs from initial quotation through demonstration to completion.
2. **Marketing Lead Attribution**: Connect campaigns directly to leads, reps, and associated costs.
3. **Support SLA & Duration Tracking**: Automatically calculate resolution duration with precise timestamps.
4. **Customer Post-Delivery Adoption**: Verify if clients are actively using delivered systems or experiencing onboarding hurdles.

---

## Application Modules & Features

```
Management App (Root)
 ├── Jobs (management.job)
 ├── Marketing (management.marketing)
 ├── Sales Performance (management.sales.performance)
 ├── Activity Performance (management.activity.performance)
 ├── Help Desk (management.helpdesk)
 ├── Client Follow Up (management.client.followup)
 └── Configuration
      ├── Settings (res.config.settings)
      ├── Products (management.product)
      └── Activity Types (management.activity.type)
```

---

### 1. Jobs Management

*Model:* `management.job` | *Menu:* **Management → Jobs**

The Jobs module manages on-site and technical jobs from assignment to completion.

- **Workflow Stages**:
  - `To Be Done` (New / pending assignment)
  - `In Progress` (Actively being worked on by assigned reps/technicians)
  - `Demo Scheduled` (Product or service demo is booked)
  - `Done` (Completed)
- **Assignments**:
  - **Sales Reps** (`sales_rep_ids`): Multiple sales team members can be assigned.
  - **Technicians** (`technician_ids`): Field or service technicians executing the job.
- **Financial Details**:
  - Amount invoiced/quoted (`amount_quoted`) with automatic currency symbol formatting.
- **Customer & Location**:
  - Organization (`res.partner`), Address Line, City, and Country.
  - Next Contact Date (`next_contact_date`) with deadline tracking.
- **Chatter & Activities**: Full messaging, audit log, follower management, and scheduled activities (`mail.thread`, `mail.activity.mixin`).

---

### 2. Marketing & Campaign Tracking

*Model:* `management.marketing` | *Menu:* **Management → Marketing**

Tracks return on investment (ROI) and performance across marketing initiatives and advertising campaigns.

- **Campaign Details**: Campaign title, ad name, linked product, and assigned sales rep.
- **Lead Metrics**:
  - **Expected Leads**: Target number of leads expected from the campaign (defaults to global setting).
  - **Actual Leads**: Real leads generated.
  - **Lost Leads**: Leads that dropped off or were disqualified.
- **Cost Metrics**: Cost per lead (`cost_per_lead`) in company currency.
- **Temporal Analysis**: Auto-calculates the **Day of the Week** from the campaign date to highlight top-performing advertising days.

---

### 3. Sales Performance

*Model:* `management.sales.performance` | *Menu:* **Management → Sales Performance**

Logs closed deals and individual sales contributions.

- **Product & Customer**: Directly links the customer (`res.partner`) and the management product (`management.product`).
- **Revenue Value**: Closed transaction amount with multi-currency handling.
- **Sales Rep Attribution**: Credited sales representative (`res.users`).
- **Multi-Company Aware**: Records transactions per company for consolidated reporting.

---

### 4. Activity & Field Performance

*Models:* `management.activity.performance`, `management.activity.type` | *Menu:* **Management → Activity Performance**

Tracks day-to-day rep prospecting actions, call volume, and door-to-door outreach.

- **Activity Types**:
  - `Cold Calls`
  - `Calls Done`
  - `Door to Door`
  - `Other`
- **Dynamic Field Display**: Form inputs automatically adapt based on the selected activity type:
  - *Cold Calls*: Prompts for **Leads Generated** and **Unanswered Calls**.
  - *Calls Done*: Prompts for **Unanswered Calls**.
  - *Door to Door*: Prompts for **Leads Done**.
- **Target vs. Actuals**: Compares **Qty Done** against **Expected Qty**.

---

### 5. Help Desk & Support Ticketing

*Model:* `management.helpdesk` | *Menu:* **Management → Help Desk**

A structured incident management and support ticketing system.

- **Automated Sequence**: Tickets are assigned auto-incrementing references (e.g., `HD-0001`).
- **Team Coordination**: Captures both the reporting sales rep and the assigned resolving technician.
- **Status Lifecycle**:
  - `Not Assigned` → `In Progress` → `Done` / `Overdue`
- **Time Tracking & Duration Computation**:
  - **Time to be Taken**: Estimated SLA hours.
  - **Start Time & End Time**: Datetime timestamps.
  - **Time Taken to Resolve**: Computed automatically in decimal hours (`(end_time - start_time) / 3600.0`).

---

### 6. Client Follow-Up

*Model:* `management.client.followup` | *Menu:* **Management → Client Follow Up**

Ensures high retention and client satisfaction after system onboarding or job delivery.

- **Job Audit**: Logs the completion date, customer, sales rep, and technician.
- **Adoption Verification**:
  - **Using System**: `Not Yet`, `Yes`, `No`.
  - **Sales Invoices Done Now**: Boolean checklist verifying if client is actively processing transactions.
- **Issue Tracking**: Free-text notes for unresolved client feedback or scheduled training visits.

---

### 7. Product Catalog

*Model:* `management.product` | *Menu:* **Management → Configuration → Products**

A lightweight internal catalog designed specifically for operational workflows, ticketing, and marketing attribution.

- **Auto Item Code**: Generates sequential identifiers via sequence `management.product` (e.g., `PRD0001`).
- **Formatted Display**: Automatically formats record names as `[ITEM_CODE] Name` across all Many2one selection fields.

---

### 8. Configuration & Settings

*Model:* `res.config.settings` | *Menu:* **Management → Configuration → Settings**

Integrates into standard Odoo Settings under the **Management App** section.

- **Default Expected Leads**: Global setting (`management_app.default_expected_leads`) applied as default target for new marketing records.

---

## Data Model Reference

| Model Technical Name | Friendly Name | Key Inherits | Key Fields |
| :--- | :--- | :--- | :--- |
| `management.job` | Management Job | `mail.thread`, `mail.activity.mixin` | `name`, `status`, `organization_id`, `sales_rep_ids`, `technician_ids`, `amount_quoted`, `product_id` |
| `management.marketing` | Management Marketing | - | `name`, `campaign`, `expected_leads`, `actual_leads`, `lost_leads`, `cost_per_lead`, `date`, `day_of_week` |
| `management.sales.performance` | Sales Performance | - | `product_id`, `customer_id`, `sales_rep_id`, `value`, `company_id` |
| `management.activity.type` | Activity Type | - | `name`, `code` |
| `management.activity.performance` | Activity Performance | - | `activity_type_id`, `qty_done`, `expected_qty`, `leads_generated`, `unanswered_calls`, `leads_done` |
| `management.helpdesk` | Help Desk | - | `name` (sequence), `customer_id`, `issue_type`, `technician_id`, `start_time`, `end_time`, `time_taken_to_resolve`, `status` |
| `management.client.followup` | Client Follow Up | - | `customer_id`, `using_system_status`, `sales_invoices_done_now`, `scheduled_issues`, `date_job_done` |
| `management.product` | Management Product | - | `item_code` (sequence), `name`, `display_name` |

---

## Access Rights & Security

Configured in `security/ir.model.access.csv`:

- All internal users (`base.group_user`) are granted full Read, Write, Create, and Unlink permissions across all management models.
- System administrators (`base.group_system`) hold exclusive access to global configuration settings and sequence configuration.

---

## Installation & Deployment

### Dependencies
- Odoo 17.0+ / 18.0+ / 19.0+
- Required base modules: `base`, `mail`

### CLI Installation / Upgrade
```bash
# Upgrade on container or server:
odoo -u management -c /etc/odoo/odoo.conf -d <database_name> --stop-after-init
```

### Git Repository
```bash
git clone git@github.com:draftpos/management.git
```

---

## Technical Notes

- **Odoo 19 Compatibility**: All tree views use the modern `<list>` tag with color decorations (`decoration-info`, `decoration-warning`, `decoration-success`).
- **Static Assets**: Backend assets are registered under `management/static/src/css/form_highlight.css`.
- **Display Name Computation**: Utilizes `@api.depends('item_code', 'name')` to compute `display_name` efficiently in batch.
