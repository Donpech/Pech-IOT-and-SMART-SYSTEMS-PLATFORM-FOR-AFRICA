#!/usr/bin/env python3
"""
PECH Group Holdings Ltd — Proposal Document Regenerator

Regenerates PDF and DOCX versions of proposal documents from updated Markdown sources.
Uses pdfkit (wkhtmltopdf) for PDF generation with embedded images.
Uses pandoc for DOCX generation.

Usage:
    python3 scripts/regenerate_proposals.py
"""

import os
import sys
import subprocess
import markdown
import base64
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

# Documents to regenerate (markdown source → output base name)
PROPOSAL_DOCS = [
    {
        "md": "PECH_GROUP_FINANCIAL_PROPOSAL_250M_NAIRA.md",
        "pdf": "PECH_GROUP_FINANCIAL_PROPOSAL_250M_NAIRA.pdf",
        "docx": "PECH_GROUP_FINANCIAL_PROPOSAL_250M_NAIRA.docx",
    },
    {
        "md": "PECH_INVESTOR_VERSION.md",
        "pdf": "PECH_INVESTOR_VERSION.pdf",
        "docx": "PECH_INVESTOR_VERSION.docx",
    },
    {
        "md": "PECH_PROPOSAL_EXECUTIVE_SUMMARY.md",
        "pdf": "PECH_PROPOSAL_EXECUTIVE_SUMMARY.pdf",
        "docx": "PECH_PROPOSAL_EXECUTIVE_SUMMARY.docx",
    },
]

AI_STRATEGY_DOCS = [
    "ai_strategy/PECH_AI_ARCHITECTURE_GUIDE",
    "ai_strategy/PECH_AI_HARDWARE_AND_SETUP_GUIDE",
    "ai_strategy/PECH_AI_MODEL_CATALOG",
    "ai_strategy/PECH_OPEN_SOURCE_PLATFORM_STACK",
    "ai_strategy/PECH_ECOSYSTEM_COMPREHENSIVE_GUIDE",
    "ai_strategy/NIGERIA_AFRICA_AUTOMATION_SMART_SYSTEMS_INDUSTRY_RESEARCH",
    "ai_strategy/CRM_ERP_INTEGRATION_RESEARCH",
]

# PECH brand CSS for PDF generation
PECH_CSS = """
body {
    font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 100%;
    margin: 0 auto;
    padding: 20px 30px;
}
h1 {
    color: #0099CC;
    border-bottom: 3px solid #F5A623;
    padding-bottom: 8px;
    font-size: 22pt;
}
h2 {
    color: #0099CC;
    border-bottom: 1px solid #00BFFF;
    padding-bottom: 4px;
    font-size: 16pt;
    margin-top: 24px;
}
h3 {
    color: #E08A00;
    font-size: 13pt;
    margin-top: 18px;
}
h4 { color: #0099CC; font-size: 11pt; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 9.5pt;
}
th {
    background-color: #0099CC;
    color: white;
    padding: 8px 10px;
    text-align: left;
    font-weight: bold;
}
td {
    padding: 6px 10px;
    border: 1px solid #ddd;
}
tr:nth-child(even) { background-color: #f8f9fa; }
tr:hover { background-color: #e8f4f8; }
img {
    max-width: 100%;
    height: auto;
    margin: 12px 0;
    border-radius: 8px;
}
code {
    background-color: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 9.5pt;
}
pre {
    background-color: #1B2838;
    color: #00BFFF;
    padding: 12px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 9pt;
}
blockquote {
    border-left: 4px solid #F5A623;
    margin: 12px 0;
    padding: 8px 16px;
    background-color: #fff8e1;
}
strong { color: #0099CC; }
a { color: #00BFFF; text-decoration: none; }
hr { border: 1px solid #F5A623; margin: 20px 0; }
.page-break { page-break-before: always; }
"""


def embed_images_in_html(html_content, md_dir):
    """Replace image src paths with base64-encoded data URIs for PDF embedding."""
    def replace_img(match):
        full_match = match.group(0)
        src = match.group(1)

        # Resolve the image path relative to the markdown file
        if src.startswith(('http://', 'https://', 'data:')):
            return full_match

        img_path = (md_dir / src).resolve()
        if not img_path.exists():
            print(f"  WARNING: Image not found: {img_path}")
            return full_match

        # Determine MIME type
        suffix = img_path.suffix.lower()
        mime_map = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
                    '.svg': 'image/svg+xml', '.gif': 'image/gif'}
        mime = mime_map.get(suffix, 'image/png')

        # Read and encode
        with open(img_path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')

        return full_match.replace(src, f"data:{mime};base64,{b64}")

    return re.sub(r'<img[^>]+src="([^"]+)"', replace_img, html_content)


def md_to_html(md_path):
    """Convert markdown file to styled HTML with embedded images."""
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_body = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'md_in_html']
    )

    # Embed images as base64
    md_dir = md_path.parent
    html_body = embed_images_in_html(html_body, md_dir)

    # Wrap in full HTML document
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>{PECH_CSS}</style>
</head>
<body>
{html_body}
</body>
</html>"""

    return html


def generate_pdf(md_path, pdf_path):
    """Generate PDF from markdown using wkhtmltopdf via pdfkit."""
    import pdfkit

    print(f"  Generating PDF: {pdf_path.name}")
    html = md_to_html(md_path)

    # Write temp HTML
    tmp_html = pdf_path.with_suffix('.tmp.html')
    with open(tmp_html, 'w', encoding='utf-8') as f:
        f.write(html)

    options = {
        'page-size': 'A4',
        'margin-top': '15mm',
        'margin-right': '15mm',
        'margin-bottom': '15mm',
        'margin-left': '15mm',
        'encoding': 'UTF-8',
        'enable-local-file-access': '',
        'print-media-type': '',
        'no-stop-slow-scripts': '',
        'javascript-delay': '1000',
    }

    try:
        pdfkit.from_file(str(tmp_html), str(pdf_path), options=options)
        print(f"  ✓ PDF created: {pdf_path.name}")
    except Exception as e:
        print(f"  ✗ PDF failed: {e}")
    finally:
        tmp_html.unlink(missing_ok=True)


def generate_docx(md_path, docx_path):
    """Generate DOCX from markdown using pandoc."""
    print(f"  Generating DOCX: {docx_path.name}")

    cmd = [
        'pandoc', str(md_path),
        '-f', 'markdown',
        '-t', 'docx',
        '--resource-path', str(md_path.parent),
        '-o', str(docx_path)
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(md_path.parent))
        if result.returncode == 0:
            print(f"  ✓ DOCX created: {docx_path.name}")
        else:
            print(f"  ✗ DOCX failed: {result.stderr}")
    except Exception as e:
        print(f"  ✗ DOCX failed: {e}")


def main():
    print("=" * 60)
    print("  PECH Document Regenerator")
    print("  Rebuilding PDFs and DOCX from updated Markdown sources")
    print("=" * 60)
    print()

    # Regenerate proposal documents (PDF + DOCX)
    print("--- PROPOSAL DOCUMENTS ---")
    for doc in PROPOSAL_DOCS:
        md_path = PROJECT_ROOT / doc["md"]
        pdf_path = PROJECT_ROOT / doc["pdf"]
        docx_path = PROJECT_ROOT / doc["docx"]

        if not md_path.exists():
            print(f"SKIP: {doc['md']} not found")
            continue

        print(f"\nSource: {doc['md']}")
        generate_pdf(md_path, pdf_path)
        generate_docx(md_path, docx_path)

    # Regenerate ai_strategy DOCX files
    print("\n--- AI STRATEGY DOCUMENTS ---")
    for doc_base in AI_STRATEGY_DOCS:
        md_path = PROJECT_ROOT / f"{doc_base}.md"
        docx_path = PROJECT_ROOT / f"{doc_base}.docx"

        if not md_path.exists():
            print(f"SKIP: {doc_base}.md not found")
            continue

        print(f"\nSource: {doc_base}.md")
        generate_docx(md_path, docx_path)

    print("\n" + "=" * 60)
    print("  Regeneration complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
