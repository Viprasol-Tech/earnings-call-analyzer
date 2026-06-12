# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-06-12

### Added
- Initial release of the **earnings-call-analyzer** Agent Skill.
- `skill.md` methodology with a 6-step workflow: scope & context, KPI & results
  extraction, guidance analysis, tone & candor assessment, red-flags scan, and a
  structured briefing output format.
- **KPI extraction** — revenue, GAAP vs non-GAAP EPS, margins, segment revenue,
  and sector-specific operating metrics — as actual vs guidance vs consensus,
  with a GAAP/non-GAAP wedge flag.
- **Guidance classifier** — Raised / Maintained / Cut / Withdrawn / Initiated,
  with buried- and euphemistic-cut detection.
- **Tone & candor scoring** — hedge-word and macro-deflection counting, Q&A
  dodge tracking, and a Candid / Measured / Evasive rating backed by evidence
  quotes.
- **Red-flag scan** — buried cuts, non-GAAP cover, macro deflection, exec
  departures, channel-stuffing hints, going-concern/covenant mentions.
- Structured briefing output: TL;DR, KPI table, guidance summary, tone score,
  takeaways, red flags, and next-quarter watch-items.
- Two worked example briefings: a SaaS beat-and-raise (decelerating NRR) and a
  retailer guidance cut (evasive tone, multiple red flags).
- "Not investment advice" disclaimer in both `skill.md` and `README.md`.
- Cross-link to the Viprasol **financial-statement-analysis** skill.
- CI validator (`scripts/validate_skill.py`) and GitHub Actions workflow
  (`.github/workflows/validate.yml`).

[1.0.0]: https://github.com/Viprasol-Tech/earnings-call-analyzer/releases/tag/v1.0.0
