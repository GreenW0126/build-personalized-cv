# Fixed-Format Chinese Word Export

Read this reference only when preparing, changing, or troubleshooting a Chinese Word export.

## Stable visual grammar

The validated format is intentionally conservative:

- A4 portrait with compact 0.5–0.58 inch margins;
- centered name and one-line contact block;
- black section rules, no color blocks, icons, columns, or sidebars;
- Microsoft YaHei for Chinese body text, compact Arial-compatible Latin text;
- bold role/date row, smaller organization line, dense justified bullets;
- default 9.25 pt body copy and 11 pt section headings;
- accepted bullets remain verbatim during layout work.

Do not redesign this visual system during ordinary export. Layout repair may adjust spacing by small amounts but must not silently shorten or rewrite accepted text.

## Lightweight routing

### Education

Use `before_experience` when any of these apply:

- the user is a new graduate or has no substantial full-time experience;
- education is unusually strong or directly relevant enough to be a deliberate lead signal;
- the user explicitly requests it.

Use `after_experience` when the candidate has multiple substantial roles and the hiring argument is primarily experience-led.

This is a ranking decision, not a rigid seniority formula. A strategically strong degree may remain near the top for an experienced candidate. Explicit user choice wins.

### Independent projects

Use `before_experience` when the project is independent, highly relevant to the target role, and supplies proof that the employment history does not show.

Use `after_experience` when the project is supportive evidence but professional experience should lead.

Use `integrated` when the project is part of a continuous career narrative or separating it would distort the timeline. Integrated records are sorted with experience by their supplied `sort_date`.

If the trade-off is ambiguous and materially affects interpretation, show the resolved order and ask for one confirmation. Do not ask when the user has already chosen.

## Export payload

The exporter accepts UTF-8 JSON:

```json
{
  "name": "string",
  "contact": "string",
  "summary": "string",
  "profile": {
    "graduation_year": 2024,
    "substantive_work_roles": 0,
    "education_is_lead_signal": false,
    "projects_are_primary_target_evidence": true
  },
  "layout": {
    "education_position": "auto|before_experience|after_experience",
    "projects_position": "auto|before_experience|after_experience|integrated"
  },
  "education": [{"title": "string", "date": "string"}],
  "experience": [{"title": "string", "organization": "string", "date": "string", "sort_date": "YYYY-MM", "bullets": ["string"]}],
  "projects": [{"title": "string", "organization": "string", "date": "string", "sort_date": "YYYY-MM", "bullets": ["string"]}],
  "internships": [{"title": "string", "organization": "string", "date": "string", "bullets": ["string"]}],
  "skills": [{"label": "string", "text": "string"}]
}
```

The Dashboard publisher or Master produces this payload from accepted canonical state. Dashboard HTML and local UI state are not the long-term source of truth.

## Command

```bash
python scripts/export_chinese_cv.py --input accepted-cv.json --output candidate.docx
```

Use a `.docm` output path when the user explicitly requests a macro-enabled container. The exporter does not add VBA code; it changes the package content type only.

## Verification

After export, use the document render-and-verify workflow:

1. Render every page to PNG.
2. Inspect clipping, broken role/date rows, orphan headings, inconsistent section rules, and sparse accidental pages.
3. Repair spacing or routing; do not rewrite accepted claims.
4. Deliver only the requested language and file type.
