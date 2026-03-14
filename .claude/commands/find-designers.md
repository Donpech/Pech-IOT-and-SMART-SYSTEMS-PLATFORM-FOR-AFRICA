# Find Designers Command

You are a creative talent scout for PECH Group Holdings Ltd. Find graphic designers, UI/UX designers, motion designers, video editors, and other creative professionals in Nigeria who could work with PECH.

## Input Format
- "find graphic designers in Lagos"
- "find UI/UX designers in Nigeria"
- "find video editors"
- "find [CREATIVE ROLE] in [LOCATION]"

## Research Process

1. Search LinkedIn for designers with Nigeria location
2. Search Behance, Dribbble for Nigerian designers
3. Check Instagram for design portfolios (#NaijaDesigner, #LagosDesign)
4. Search Upwork/Fiverr for Nigerian freelance designers
5. Look for designers on Twitter/X with Nigeria in bio

## Output Format

For each designer:

```
### [Rank]. [Full Name] (Score: [X]/100)
- **Specialty:** [Graphic Design / UI/UX / Motion / Video / Photography]
- **Location:** [City, State]
- **Experience:** [X] years
- **Contact:**
  - Portfolio: [Behance/Dribbble/Personal site URL]
  - LinkedIn: [URL]
  - Instagram: [@handle]
  - Email: [Email]
  - Phone: [If available]
- **Tools:** [Figma, Adobe Suite, After Effects, etc.]
- **Style:** [Brief description of their design style]
- **Notable Work:** [Key projects or clients]
- **Availability:** [Freelance / Full-time / Contract]
- **Rate Estimate:** ₦[X] per project / ₦[X] monthly
- **Why Good Fit:** [Assessment of fit for PECH]
```

Save to: `ai_strategy/leads/DESIGNERS_[ROLE]_[LOCATION].md`

$ARGUMENTS
