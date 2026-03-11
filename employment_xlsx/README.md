<div align="center">
<div style="background:linear-gradient(135deg,#1B2838 0%,#0d1b2a 50%,#162435 100%);border-radius:16px;padding:0;overflow:hidden;border:2px solid #0099CC;box-shadow:0 8px 32px rgba(0,153,204,0.12),0 4px 16px rgba(245,166,35,0.08);">
<div style="height:4px;background:linear-gradient(90deg,#0099CC,#00BFFF 20%,#F5A623 40%,#E08A00 60%,#0099CC 80%,#00BFFF);"></div>
<div style="height:2px;background:linear-gradient(90deg,#F5A623,#0099CC 50%,#F5A623);"></div>
<div style="padding:24px 36px 18px;">
<div style="display:inline-block;background:linear-gradient(135deg,#0099CC,#00BFFF);border-radius:12px;padding:10px 14px;margin-bottom:8px;"><span style="font-size:1.8em;">📊</span></div>
<h1 style="margin:6px 0 0;font-size:1.7em;background:linear-gradient(90deg,#0099CC,#F5A623);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Employment Documents</h1>
<h2 style="margin:6px 0 12px;font-size:1.05em;color:#0099CC;font-weight:500;">Excel (.xlsx) & Google Sheets — 15 Branded Files</h2>
<p>
<img src="https://img.shields.io/badge/Files-15%20Excel-0099CC?style=for-the-badge&labelColor=1B2838" alt="15 Excel" />
<img src="https://img.shields.io/badge/HR-Employment%20Docs-F5A623?style=for-the-badge&labelColor=1B2838" alt="HR Docs" />
</p>
<p><img src="https://img.shields.io/badge/Lagos%2C%20Nigeria-pechgroupholdings.tech-0099CC?style=flat-square" alt="Location" /></p>
<div style="height:2px;background:linear-gradient(90deg,#F5A623,#0099CC 50%,#F5A623);margin:10px -36px 0;"></div>
<div style="height:4px;background:linear-gradient(90deg,#0099CC,#00BFFF 20%,#F5A623 40%,#E08A00 60%,#0099CC 80%,#00BFFF);margin:0 -36px -18px;"></div>
</div>
</div>
</div>

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
