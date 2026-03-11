#!/usr/bin/env python3
"""
PECH Group Holdings Ltd — Full Document Regenerator

Regenerates PDF and DOCX versions of ALL documents from Markdown sources.
Uses pdfkit (wkhtmltopdf) for PDF generation with embedded images and brand CSS.
Uses pandoc for DOCX generation, then applies PECH brand styling via brand_docx.

Covers:
  - Root-level proposals (PDF + DOCX)
  - ai_strategy/ documents (PDF + DOCX)
  - brand_templates/ documents (PDF + DOCX)
  - business_documents/ documents (PDF + DOCX)
  - contracts/ documents (PDF + DOCX)

Usage:
    python3 scripts/regenerate_proposals.py          # Regenerate ALL documents
    python3 scripts/regenerate_proposals.py --docx   # DOCX only (skip PDF)
    python3 scripts/regenerate_proposals.py --pdf    # PDF only (skip DOCX)
"""

import os
import sys
import subprocess
import markdown
import base64
import re
from pathlib import Path

# Import DOCX branding post-processor
sys.path.insert(0, str(Path(__file__).parent))
from brand_docx import brand_docx

PROJECT_ROOT = Path(__file__).parent.parent

# ── Document directories to process ──────────────────────────────────────────
# Each entry: (directory_relative_to_root, list_of_basenames_without_extension)
# If list is None, auto-discover all .md files in that directory.

DOCUMENT_GROUPS = [
    {
        "label": "PROPOSAL DOCUMENTS (Root)",
        "dir": ".",
        "files": [
            "PECH_GROUP_FINANCIAL_PROPOSAL_250M_NAIRA",
            "PECH_INVESTOR_VERSION",
            "PECH_PROPOSAL_EXECUTIVE_SUMMARY",
        ],
        "pdf": True,
        "docx": True,
    },
    {
        "label": "AI STRATEGY DOCUMENTS",
        "dir": "ai_strategy",
        "files": None,  # Auto-discover
        "pdf": True,
        "docx": True,
    },
    {
        "label": "BRAND TEMPLATES",
        "dir": "brand_templates",
        "files": None,
        "pdf": True,
        "docx": True,
    },
    {
        "label": "BUSINESS DOCUMENTS",
        "dir": "business_documents",
        "files": None,
        "pdf": True,
        "docx": True,
    },
    {
        "label": "CONTRACTS & AGREEMENTS",
        "dir": "contracts",
        "files": None,
        "pdf": True,
        "docx": True,
    },
]

# Skip README.md files (not real documents)
SKIP_FILES = {"README"}

# ── PECH brand CSS for PDF generation ────────────────────────────────────────
PECH_CSS = """
@page {
    margin: 15mm;
    size: A4;

    @top-center {
        content: "PECH GROUP HOLDINGS LTD";
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 8pt;
        color: #0099CC;
    }
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 8pt;
        color: #888;
    }
}

body {
    font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 100%;
    margin: 0 auto;
    padding: 20px 30px;
}

/* ── Branded Header Banner ── */
.pech-header {
    text-align: center;
    padding: 18px 0 12px;
    margin-bottom: 20px;
    border-top: 5px solid #F5A623;
    border-bottom: 2px solid #00BFFF;
}
.pech-header .company-name {
    font-size: 16pt;
    font-weight: bold;
    color: #0099CC;
    margin: 0;
    letter-spacing: 1px;
}
.pech-header .tagline {
    font-size: 9pt;
    color: #E08A00;
    font-style: italic;
    margin: 2px 0 0;
}

/* ── Branded Footer Banner ── */
.pech-footer {
    text-align: center;
    margin-top: 30px;
    padding-top: 8px;
    border-top: 5px solid #F5A623;
    font-size: 8pt;
    color: #0099CC;
}

/* ── Headings ── */
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

/* ── Tables ── */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 9.5pt;
}
th {
    background: linear-gradient(135deg, #00BFFF, #0099CC);
    color: white;
    padding: 8px 10px;
    text-align: left;
    font-weight: bold;
}
td {
    padding: 6px 10px;
    border: 1px solid #B0D4E8;
}
tr:nth-child(even) { background-color: #E8F8FF; }
tr:nth-child(odd) { background-color: #FFFFFF; }
/* Keep header row text white for bold/link/em */
th strong, th a, th em { color: #FFFFFF; }

/* ── Images ── */
img {
    max-width: 100%;
    height: auto;
    margin: 12px 0;
    border-radius: 8px;
}

/* ── Code ── */
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
    border: 1px solid #F5A623;
}

/* ── Blockquotes ── */
blockquote {
    border-left: 4px solid #F5A623;
    margin: 12px 0;
    padding: 8px 16px;
    background-color: #fff8e1;
}

/* ── Inline ── */
strong { color: #0099CC; }
a { color: #00BFFF; text-decoration: none; }

/* ── Horizontal Rules (Dividers) ── */
hr {
    border: none;
    height: 0;
    border-top: 3px solid #F5A623;
    border-bottom: 1px solid #00BFFF;
    margin: 24px 0;
}

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
            print(f"    WARNING: Image not found: {img_path}")
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


def strip_remote_images(html_content):
    """Remove remote image tags (badges, shields.io, etc.) that cause network errors in PDF gen."""
    # Remove <img> tags with http/https src
    html_content = re.sub(r'<img[^>]+src="https?://[^"]*"[^>]*/?\s*>', '', html_content)
    # Remove empty <p> tags left behind
    html_content = re.sub(r'<p>\s*</p>', '', html_content)
    return html_content


def md_to_html(md_path):
    """Convert markdown file to styled HTML with branded header/footer and embedded images."""
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_body = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'md_in_html']
    )

    # Embed local images as base64, then strip remote images that cause network errors
    md_dir = md_path.parent
    html_body = embed_images_in_html(html_body, md_dir)
    html_body = strip_remote_images(html_body)

    # Branded header + footer wrappers
    header_html = """
    <div class="pech-header">
        <p class="company-name">PECH GROUP HOLDINGS LTD</p>
        <p class="tagline">Technology &amp; Infrastructure Enablers for Africa</p>
    </div>
    """

    footer_html = """
    <div class="pech-footer">
        PECH Group Holdings Ltd &nbsp;|&nbsp; Lagos, Nigeria &nbsp;|&nbsp; pechgroupholdings.tech
    </div>
    """

    # Wrap in full HTML document
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>{PECH_CSS}</style>
</head>
<body>
{header_html}
{html_body}
{footer_html}
</body>
</html>"""

    return html


def generate_pdf(md_path, pdf_path):
    """Generate branded PDF from markdown using wkhtmltopdf via pdfkit."""
    import pdfkit

    print(f"    Generating PDF: {pdf_path.name}")
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
        'no-stop-slow-scripts': '',
        'javascript-delay': '500',
        'load-error-handling': 'ignore',
        'load-media-error-handling': 'ignore',
    }

    try:
        pdfkit.from_file(str(tmp_html), str(pdf_path), options=options)
        print(f"    + PDF created: {pdf_path.name}")
    except Exception as e:
        print(f"    x PDF failed: {e}")
    finally:
        tmp_html.unlink(missing_ok=True)


def clean_markdown_for_docx(md_content):
    """
    Pre-process markdown content to remove GitHub-specific HTML blocks
    that confuse pandoc's DOCX conversion.

    Strategy: Find the end of the HTML header block (marked by <!-- END HEADER -->
    or the closing </div> followed by blank line + ---), then keep everything after.
    Also strips any remaining HTML tags with style attributes, badges, etc.
    """
    # Strategy 1: Look for <!-- END HEADER --> marker
    end_marker = re.search(r'<!--\s*=*\s*END\s+HEADER\s*=*\s*-->', md_content)
    if end_marker:
        # Take everything after the end marker
        after_header = md_content[end_marker.end():]
        # Also strip the closing </div> and any blank lines right after
        after_header = re.sub(r'^\s*</div>\s*', '', after_header)
    else:
        # Strategy 2: Find the first markdown heading or --- that starts real content
        # Skip everything before the first ## or --- that's on its own line
        match = re.search(r'^(---|\#{1,6}\s)', md_content, re.MULTILINE)
        if match:
            after_header = md_content[match.start():]
        else:
            after_header = md_content

    # Now clean remaining HTML artifacts line by line
    lines = after_header.split('\n')
    cleaned = []

    for line in lines:
        stripped = line.strip()

        # Skip shields.io badge lines
        if 'img.shields.io' in line or 'shields.io/badge' in line:
            continue

        # Skip known container/header HTML tags with style attributes (div, span, p, h1-h6)
        if stripped.startswith('<') and stripped.endswith('>') and 'style=' in stripped:
            if re.match(r'<(div|span|p|h[1-6]|header|section|nav)\b', stripped):
                continue

        # Skip HTML comment lines
        if stripped.startswith('<!--') and stripped.endswith('-->'):
            continue

        # Skip empty HTML tags
        if stripped in ('</div>', '<div>', '<p>', '</p>', '<br>', '<br/>', '<br />', '</span>'):
            continue

        # Skip standalone <img> HTML tags (not markdown ![alt](src) images)
        if stripped.startswith('<img ') and 'src=' in stripped:
            continue

        cleaned.append(line)

    result = '\n'.join(cleaned)

    # Clean up excessive blank lines (more than 2 consecutive)
    result = re.sub(r'\n{4,}', '\n\n\n', result)

    return result.strip() + '\n'


def generate_docx(md_path, docx_path):
    """Generate branded DOCX from markdown using pandoc + brand_docx post-processor.

    Pipeline:
    1. Read markdown source
    2. Clean HTML artifacts (GitHub-specific headers, badges, inline CSS)
    3. Write cleaned markdown to temp file
    4. Run pandoc with proper extensions for tables and images
    5. Post-process with brand_docx (colors, ribbons, dividers)
    6. Clean any remaining markdown artifacts in the DOCX
    """
    print(f"    Generating DOCX: {docx_path.name}")

    # Read and clean the markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    cleaned_md = clean_markdown_for_docx(md_content)

    # Write cleaned markdown to temp file
    tmp_md = md_path.with_suffix('.tmp.md')
    with open(tmp_md, 'w', encoding='utf-8') as f:
        f.write(cleaned_md)

    # Use pandoc with explicit markdown extensions for proper table/bold/link handling
    cmd = [
        'pandoc', str(tmp_md),
        '-f', 'markdown+pipe_tables+grid_tables+raw_html+strikeout+yaml_metadata_block',
        '-t', 'docx',
        '--resource-path', os.pathsep.join([str(md_path.parent), str(PROJECT_ROOT)]),
        '--extract-media', str(md_path.parent / '_docx_media'),
        '-o', str(docx_path)
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(md_path.parent))
        if result.returncode == 0:
            print(f"    + DOCX created: {docx_path.name}")
            # Apply PECH brand colors, headers, dividers, and table styling
            brand_docx(docx_path)
        else:
            print(f"    x DOCX failed: {result.stderr}")
    except Exception as e:
        print(f"    x DOCX failed: {e}")
    finally:
        tmp_md.unlink(missing_ok=True)
        # Clean up extracted media dir if empty
        media_dir = md_path.parent / '_docx_media'
        if media_dir.exists():
            try:
                import shutil
                shutil.rmtree(media_dir, ignore_errors=True)
            except Exception:
                pass


def discover_md_files(directory):
    """Find all .md files in a directory, excluding README.md."""
    md_files = []
    for f in sorted(directory.glob("*.md")):
        basename = f.stem
        if basename in SKIP_FILES:
            continue
        md_files.append(basename)
    return md_files


def main():
    # Parse command-line flags
    do_pdf = True
    do_docx = True
    if "--docx" in sys.argv:
        do_pdf = False
    elif "--pdf" in sys.argv:
        do_docx = False

    mode = "PDF + DOCX" if (do_pdf and do_docx) else ("DOCX only" if do_docx else "PDF only")

    print("=" * 65)
    print("  PECH Full Document Regenerator")
    print(f"  Mode: {mode}")
    print("  Rebuilding from Markdown sources with PECH brand styling")
    print("=" * 65)
    print()

    total_pdf = 0
    total_docx = 0
    total_failed = 0

    for group in DOCUMENT_GROUPS:
        label = group["label"]
        dir_rel = group["dir"]
        dir_path = PROJECT_ROOT / dir_rel if dir_rel != "." else PROJECT_ROOT

        # Discover or use predefined file list
        if group["files"] is None:
            basenames = discover_md_files(dir_path)
        else:
            basenames = group["files"]

        if not basenames:
            continue

        print(f"--- {label} ({len(basenames)} files) ---")

        for basename in basenames:
            md_path = dir_path / f"{basename}.md"
            if not md_path.exists():
                print(f"  SKIP: {basename}.md not found")
                total_failed += 1
                continue

            print(f"\n  Source: {dir_rel}/{basename}.md" if dir_rel != "." else f"\n  Source: {basename}.md")

            # Generate PDF
            if do_pdf and group.get("pdf", True):
                pdf_path = dir_path / f"{basename}.pdf"
                try:
                    generate_pdf(md_path, pdf_path)
                    total_pdf += 1
                except Exception as e:
                    print(f"    x PDF error: {e}")
                    total_failed += 1

            # Generate DOCX
            if do_docx and group.get("docx", True):
                docx_path = dir_path / f"{basename}.docx"
                try:
                    generate_docx(md_path, docx_path)
                    total_docx += 1
                except Exception as e:
                    print(f"    x DOCX error: {e}")
                    total_failed += 1

        print()

    print("=" * 65)
    print(f"  Done! {total_pdf} PDFs + {total_docx} DOCXs generated, {total_failed} failed")
    print("=" * 65)


if __name__ == "__main__":
    main()
