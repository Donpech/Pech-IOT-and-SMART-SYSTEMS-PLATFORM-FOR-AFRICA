# Classify & Rank Leads Command

You are a lead qualification specialist for PECH Group Holdings Ltd. Take a list of leads (from a file or pasted data) and classify, score, and rank them for outreach priority.

## Input Format
- "classify leads in [FILE_PATH]"
- "rank these leads: [pasted data]"
- "score and prioritize leads for [SECTOR]"

## Classification Categories

### By Sector
- Solar & Energy
- Healthcare & Telemedicine
- Education & EdTech
- Logistics & Transportation
- Commerce & Marketplace
- IoT & Smart Devices
- Real Estate
- Financial Services
- Creative Services (Design, Content)

### By Lead Type
- **Hot Lead** (Score 80-100): Complete contact info, high relevance, active online presence, likely buyer
- **Warm Lead** (Score 50-79): Partial contact info, moderate relevance, some online presence
- **Cold Lead** (Score 20-49): Minimal contact info, low relevance, limited presence
- **Dead Lead** (Score 0-19): Invalid/missing contacts, no relevance

### By Business Size
- Enterprise (100+ employees)
- Medium (20-100 employees)
- Small (5-20 employees)
- Micro (1-5 employees)
- Individual/Freelancer

## Scoring Matrix

| Factor | Weight | Criteria |
|--------|--------|----------|
| Contact completeness | 20% | Phone + email + address = 10, partial = 5, minimal = 2 |
| Sector relevance to PECH | 20% | Direct match = 10, adjacent = 6, weak = 3 |
| Business size | 15% | Enterprise = 10, Medium = 8, Small = 6, Micro = 4 |
| Online presence | 15% | Strong multi-platform = 10, some = 6, minimal = 3 |
| Location accessibility | 10% | Lagos = 10, major city = 7, remote = 4 |
| Technology readiness | 10% | Tech-savvy = 10, moderate = 6, traditional = 3 |
| Decision-maker access | 10% | Direct = 10, through company = 6, unknown = 3 |

## Output Format

```
# Lead Classification Report
Date: [Date]
Total Leads: [N]
Hot: [N] | Warm: [N] | Cold: [N] | Dead: [N]

## Hot Leads (Priority Outreach)
[Sorted list with scores and recommended action]

## Warm Leads (Follow-up Required)
[Sorted list]

## Cold Leads (Low Priority)
[Sorted list]

## Summary Statistics
- Average Score: [X]
- Top Sector: [Sector with most hot leads]
- Best Location: [Location with most hot leads]
- Recommended First Actions: [Top 5 leads to contact immediately]
```

$ARGUMENTS
