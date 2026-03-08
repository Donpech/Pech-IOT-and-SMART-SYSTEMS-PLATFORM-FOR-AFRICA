#!/bin/bash
# ============================================================================
# PECH Group Holdings Ltd — HR Document Export Script
#
# Converts HR Markdown documents to PDF and Word (.docx) formats using pandoc.
#
# Requirements:
#   - pandoc (https://pandoc.org/installing.html)
#   - For PDF: LaTeX distribution (texlive-xetex recommended)
#     Ubuntu/Debian: sudo apt install pandoc texlive-xetex texlive-fonts-recommended
#     macOS: brew install pandoc && brew install --cask mactex
#
# Usage:
#   chmod +x scripts/export_hr_docs.sh
#   ./scripts/export_hr_docs.sh          # Export all HR documents
#   ./scripts/export_hr_docs.sh --docx   # Export Word only (no PDF)
#   ./scripts/export_hr_docs.sh --pdf    # Export PDF only (no Word)
# ============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Project root (parent of scripts/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="$PROJECT_ROOT/exports"

# Documents to export
declare -a DOCS=(
    "business_documents/PECH_JOB_REQUIREMENTS_HANDBOOK.md"
    "business_documents/PECH_CANDIDATE_APPLICATION_FORM.md"
    "business_documents/PECH_INTERVIEW_PROCESS_AND_CHECKLIST.md"
    "contracts/PECH_SCHEDULE_B_TEMPLATES.md"
)

# Parse arguments
EXPORT_PDF=true
EXPORT_DOCX=true

if [ "$1" == "--docx" ]; then
    EXPORT_PDF=false
elif [ "$1" == "--pdf" ]; then
    EXPORT_DOCX=false
fi

# Check dependencies
echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}  PECH HR Document Export${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

if ! command -v pandoc &> /dev/null; then
    echo -e "${RED}ERROR: pandoc is not installed.${NC}"
    echo ""
    echo "Install pandoc:"
    echo "  Ubuntu/Debian: sudo apt install pandoc"
    echo "  macOS:         brew install pandoc"
    echo "  Windows:       choco install pandoc"
    echo ""
    echo "For PDF export, also install LaTeX:"
    echo "  Ubuntu/Debian: sudo apt install texlive-xetex texlive-fonts-recommended"
    echo "  macOS:         brew install --cask mactex"
    exit 1
fi

echo -e "${GREEN}pandoc found: $(pandoc --version | head -1)${NC}"

# Create output directory
mkdir -p "$OUTPUT_DIR"
echo -e "${GREEN}Output directory: $OUTPUT_DIR${NC}"
echo ""

# Export each document
SUCCESS=0
FAILED=0

for doc in "${DOCS[@]}"; do
    filepath="$PROJECT_ROOT/$doc"
    basename=$(basename "$doc" .md)

    if [ ! -f "$filepath" ]; then
        echo -e "${YELLOW}SKIP: $doc (file not found)${NC}"
        continue
    fi

    echo -e "${BLUE}Processing: $doc${NC}"

    # Export to Word (.docx)
    if [ "$EXPORT_DOCX" = true ]; then
        output_docx="$OUTPUT_DIR/${basename}.docx"
        if pandoc "$filepath" \
            -f markdown \
            -t docx \
            --reference-doc="$SCRIPT_DIR/reference.docx" 2>/dev/null \
            -o "$output_docx" 2>/dev/null || \
           pandoc "$filepath" \
            -f markdown \
            -t docx \
            -o "$output_docx" 2>/dev/null; then
            echo -e "  ${GREEN}Word: $output_docx${NC}"
            SUCCESS=$((SUCCESS + 1))
        else
            echo -e "  ${RED}Word: FAILED${NC}"
            FAILED=$((FAILED + 1))
        fi
    fi

    # Export to PDF
    if [ "$EXPORT_PDF" = true ]; then
        output_pdf="$OUTPUT_DIR/${basename}.pdf"
        if pandoc "$filepath" \
            -f markdown \
            -t pdf \
            --pdf-engine=xelatex \
            -V geometry:margin=1in \
            -V fontsize=10pt \
            -V mainfont="DejaVu Sans" \
            -o "$output_pdf" 2>/dev/null; then
            echo -e "  ${GREEN}PDF:  $output_pdf${NC}"
            SUCCESS=$((SUCCESS + 1))
        else
            echo -e "  ${YELLOW}PDF:  Skipped (LaTeX not available — install texlive-xetex)${NC}"
        fi
    fi

    echo ""
done

# Also generate Excel/Word application form via Python script
echo -e "${BLUE}Generating Excel/Word Application Form...${NC}"
if command -v python3 &> /dev/null; then
    if python3 "$SCRIPT_DIR/generate_application_form.py" 2>/dev/null; then
        echo -e "${GREEN}Application form generated (Excel + Word)${NC}"
        # Move to exports
        [ -f "$PROJECT_ROOT/PECH_CANDIDATE_APPLICATION_FORM.xlsx" ] && \
            mv "$PROJECT_ROOT/PECH_CANDIDATE_APPLICATION_FORM.xlsx" "$OUTPUT_DIR/" && \
            echo -e "  ${GREEN}Excel: $OUTPUT_DIR/PECH_CANDIDATE_APPLICATION_FORM.xlsx${NC}"
        [ -f "$PROJECT_ROOT/PECH_CANDIDATE_APPLICATION_FORM.docx" ] && \
            mv "$PROJECT_ROOT/PECH_CANDIDATE_APPLICATION_FORM.docx" "$OUTPUT_DIR/" && \
            echo -e "  ${GREEN}Word:  $OUTPUT_DIR/PECH_CANDIDATE_APPLICATION_FORM.docx${NC}"
        SUCCESS=$((SUCCESS + 2))
    else
        echo -e "${YELLOW}Python generation failed. Install dependencies:${NC}"
        echo "  pip install openpyxl python-docx"
        FAILED=$((FAILED + 1))
    fi
else
    echo -e "${YELLOW}Python3 not found. Skipping Excel/Word generation.${NC}"
fi

# Summary
echo ""
echo -e "${BLUE}============================================${NC}"
echo -e "${GREEN}Export complete: $SUCCESS successful${NC}"
if [ $FAILED -gt 0 ]; then
    echo -e "${RED}Failed: $FAILED${NC}"
fi
echo -e "${BLUE}Output: $OUTPUT_DIR/${NC}"
echo -e "${BLUE}============================================${NC}"
