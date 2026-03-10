# PECH Employment Documents — Excel (.xlsx) & Google Sheets

**PECH Group Holdings Ltd** | Lagos, Nigeria | pechgroupholdings.tech

---

## Overview

This directory contains **15 branded Excel (.xlsx) files** covering all PECH employment documents — contracts, HR forms, and tracking spreadsheets. Each file features:

- **Full PECH branding** (Sky Blue #00BFFF, Orange #F5A623, Dark Navy #1B2838)
- **Colorful header blocks** with company name, document title, and accent bars
- **Dropdown validations** for status fields, departments, employment types, etc.
- **Alternating row colors** for easy reading
- **Multiple sheets**: Tracker view (list/register) + Fillable form view
- **Print-ready** landscape layout with auto-fit

---

## Files

### Contracts (9 files)

| File | Description | Sheets |
|------|-------------|--------|
| `PECH_FULL_TIME_EMPLOYMENT_CONTRACT.xlsx` | FT employee contract tracker + fillable form | 2 |
| `PECH_CONTRACT_WORKER_AGREEMENT.xlsx` | Independent contractor register | 1 |
| `PECH_INTERNSHIP_AGREEMENT.xlsx` | Intern engagement tracker | 1 |
| `PECH_OFFICE_MARKETER_AGREEMENT.xlsx` | Office marketer contracts + sales tracking | 1 |
| `PECH_COMMISSION_MARKETER_AGREEMENT.xlsx` | Commission-based marketer register | 1 |
| `PECH_INSTALLER_AGREEMENT.xlsx` | Certified installer contractor tracker | 1 |
| `PECH_GUARANTOR_FORM.xlsx` | Guarantor/surety register + fillable form | 2 |
| `PECH_NON_DISCLOSURE_AGREEMENT.xlsx` | NDA register | 1 |
| `PECH_API_DEVELOPER_AGREEMENT.xlsx` | External API developer register | 1 |

### HR Forms (5 files)

| File | Description | Sheets |
|------|-------------|--------|
| `PECH_CANDIDATE_APPLICATION_FORM.xlsx` | Application tracker + fillable form | 2 |
| `PECH_INTERVIEW_PROCESS_AND_CHECKLIST.xlsx` | Interview pipeline + scoring rubric | 2 |
| `PECH_LEAVE_REQUEST_FORM.xlsx` | Leave tracker + fillable request form | 2 |
| `PECH_STAFF_ID_CARD_REQUEST.xlsx` | ID card request tracker + fillable form | 2 |
| `PECH_JOB_REQUIREMENTS_HANDBOOK.xlsx` | All 37 roles pre-filled with details | 1 |

### Dashboard (1 file)

| File | Description |
|------|-------------|
| `PECH_HR_MASTER_DASHBOARD.xlsx` | Master overview of all documents + Google Sheets setup instructions |

---

## Google Sheets Instructions

All `.xlsx` files are **100% compatible with Google Sheets**. To use:

1. Open **Google Drive** (drive.google.com)
2. Click **+ New** > **File upload** > Select the `.xlsx` file
3. Double-click the uploaded file to open in Google Sheets
4. Click **File** > **Save as Google Sheets** to create a native version
5. Click **Share** (top-right) to share with team members
6. Set permissions: **Editor** for HR team, **Viewer** for managers

All dropdown validations, colors, and formatting are preserved in Google Sheets.

---

## Regenerating Files

To regenerate all Excel files (e.g., after updating the templates):

```bash
python3 scripts/generate_employment_xlsx.py
```

Requires: `openpyxl` (`pip install openpyxl`)

---

*PECH Group Holdings Ltd | Confidential | Technology & Infrastructure Enablers for People*
