# Review Codebase Command

You are a software architect and documentation specialist for PECH Group Holdings Ltd (Lagos, Nigeria). Analyze the current repository structure, identify changes since the last summary, and produce an updated codebase review report.

## Input Format
The user will say something like:
- "review codebase"
- "review codebase and update summary"
- "codebase review focusing on [AREA]"
- Just "/review-codebase"

If no specific area is mentioned, perform a full repository review.

## Analysis Steps

### 1. Repository Structure Scan
- List all top-level directories with file counts
- Identify new directories or files added since `CODEBASE_SUMMARY.md` was last updated
- Identify deleted or moved files
- Count files by extension (.md, .docx, .pdf, .xlsx, .svg, .png, .py, .sh, etc.)

### 2. Directory Breakdown
For each major directory (`ai_strategy/`, `business_documents/`, `contracts/`, `brand_templates/`, `employment_xlsx/`, `design_assets/`, `design_system/`, `conversations/`, `proposal_images/`, `scripts/`, `.claude/commands/`):
- Count total files
- Note any new additions since last review
- Verify descriptions in CODEBASE_SUMMARY.md are still accurate

### 3. Slash Commands Audit
- List all files in `.claude/commands/`
- Verify each command file has proper structure (heading, input format, output)
- Note any new or removed commands
- Confirm count matches CODEBASE_SUMMARY.md

### 4. Business Verticals Check
- Cross-reference verticals listed in CODEBASE_SUMMARY.md against `ai_strategy/` docs
- Verify count matches (currently 11 verticals)
- Note any new verticals or changes

### 5. Technology Stack Verification
- Confirm AI model list matches `CLAUDE.md` and `PECH_AI_MODEL_CATALOG.md`
- Verify platform stack entries are current
- Check for any new technology additions or removals

### 6. File Statistics
- Generate accurate file counts by type using filesystem commands
- Compare against CODEBASE_SUMMARY.md statistics table
- Calculate total repository size

### 7. Change Summary
- List all material changes found
- Categorize as: additions, removals, corrections, updates
- Provide specific line references in CODEBASE_SUMMARY.md that need updating

## Output

Produce two outputs:

### 1. Change Report (always)
A markdown summary of findings with:
- Date of review
- Total files scanned
- Discrepancies found (table format)
- Recommended updates

### 2. Updated CODEBASE_SUMMARY.md (if user requests)
Apply all corrections directly to `CODEBASE_SUMMARY.md`:
- Update the date badge to current date
- Fix all file counts
- Add/remove directory entries as needed
- Update the statistics table
- Ensure business verticals list is complete

## Quality Requirements
- All file counts MUST be verified by actual filesystem scan — do NOT estimate
- Flag any discrepancies between `CLAUDE.md` and `CODEBASE_SUMMARY.md`
- Ensure brand color references match `CLAUDE.md` specifications
- Use PECH brand colors in any generated visuals: Sky Blue `#00BFFF`, Orange `#F5A623`

$ARGUMENTS
