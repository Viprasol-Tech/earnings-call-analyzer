# Earnings Call Analyzer — Agent Skill

> Read an earnings call transcript or shareholder letter like a buy-side analyst:
> KPIs vs guidance, guidance changes, tone & candor scoring, Q&A red flags, and a
> watch-list for next quarter.

[![GitHub stars](https://img.shields.io/github/stars/Viprasol-Tech/earnings-call-analyzer?style=social)](https://github.com/Viprasol-Tech/earnings-call-analyzer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-blueviolet)](https://github.com/Viprasol-Tech/earnings-call-analyzer)
[![Steps](https://img.shields.io/badge/Workflow-6%20steps-green)](skill.md)
[![Output](https://img.shields.io/badge/TL%3BDR%20%2B%20KPI%20table%20%2B%20tone%20score-blue)](skill.md)
[![Version](https://img.shields.io/badge/version-1.0.0-informational)](CHANGELOG.md)

**Works with:** Claude Code · OpenAI Codex · Cursor · GitHub Copilot · Gemini CLI · 26+ tools
that support portable agent skills.

---

## Quick Install

Clone the skill into your agent's skills directory:

```bash
# Claude Code
git clone https://github.com/Viprasol-Tech/earnings-call-analyzer \
  ~/.claude/skills/earnings-call-analyzer

# Cursor / Codex / other tools — clone anywhere your tool loads skills from, e.g.
git clone https://github.com/Viprasol-Tech/earnings-call-analyzer \
  ~/.config/skills/earnings-call-analyzer
```

The skill is a single self-contained `skill.md` (plus examples) — no
dependencies, no install step, nothing to build.

## Try It

Paste an earnings call transcript (or a shareholder letter / MD&A) and ask:

```
Analyze this earnings call — did they beat, what changed in guidance, and how candid was management?
```

The skill will scope the company and quarter, pull the KPIs vs guidance and
consensus, classify the guidance change, score management's tone and candor with
evidence quotes, dissect the Q&A for dodged questions, scan for red flags, and
return a structured briefing with watch-items for next quarter.

---

## Why This Exists

An earnings call is two things at once: a set of numbers and a performance. The
numbers are easy to skim; the performance is where the signal hides — a guidance
cut buried in the last paragraph, an adjusted-EPS beat that papers over a GAAP
decline, a key metric that management mentions only when an analyst forces it,
"macro headwinds" doing the work of an explanation. Good analysts run the *same*
read every time: KPIs vs guidance, classify the guidance change, score the tone,
dissect the Q&A, scan for red flags. This skill encodes that read so your agent
runs it consistently, quotes the evidence, separates GAAP from non-GAAP, and
never lets euphemism pass for disclosure.

## What It Does

1. **Scopes** the company, ticker, quarter, document type, and comparison basis
   (vs prior period; vs consensus only if you provide it).
2. **Extracts KPIs** — revenue, GAAP *and* non-GAAP EPS, margins, segment
   revenue, and the operating metrics that drive the business — actual vs
   guidance vs consensus.
3. **Flags the GAAP/non-GAAP wedge** when adjusted figures are emphasized while
   GAAP deteriorates.
4. **Classifies the guidance change** — Raised / Maintained / Cut / Withdrawn /
   Initiated — and flags buried or euphemistic cuts.
5. **Scores tone & candor** — counts hedge words and macro deflection, dissects
   which Q&A questions were answered vs dodged, and rates **Candid / Measured /
   Evasive** with evidence quotes.
6. **Scans for red flags** and produces a **TL;DR, KPI table, guidance summary,
   tone score, takeaways, red flags, and watch-items** for next quarter.

## Features

- **KPI extraction** — revenue, GAAP vs non-GAAP EPS, gross/operating/net
  margins, segment revenue, and sector-specific operating metrics (NRR, comps,
  ARPU, backlog…), each as actual vs guidance vs consensus.
- **Guidance classifier** — Raised / Maintained / Cut / Withdrawn / Initiated,
  with framing analysis that catches buried and euphemized cuts.
- **Tone & candor scoring** — hedge-word and macro-deflection counting, Q&A
  dodge tracking, over-promise detection, and a Candid / Measured / Evasive
  rating backed by verbatim quotes.
- **Q&A dissection** — answered directly vs partially vs dodged, with the
  repeatedly side-stepped metrics surfaced.
- **Red-flag scan** — buried guidance cuts, non-GAAP cover, macro deflection,
  CFO/exec departures, channel-stuffing hints, going-concern/covenant mentions.
- **Structured briefing** — TL;DR, KPI table, guidance summary, tone score,
  takeaways, red flags, and next-quarter watch-items/catalysts.

### Tone & candor scale

| Score | Signature |
|---|---|
| **Candid** | Names problems plainly, gives specifics even when bad, answers Q&A directly, GAAP-forward. |
| **Measured** | Mostly straight but selectively vague on weak spots; some hedging; a few dodged questions. |
| **Evasive** | Heavy hedge-word/macro deflection, buried or euphemistic bad news, multiple non-answers, GAAP obscured. |

*Tone scoring is a qualitative heuristic, always backed by evidence quotes.*

See full worked briefings in **[examples/](examples/)**:
- [SaaS beat-and-raise](examples/saas-beat-and-raise.md) — beat with raised
  guidance, but decelerating net-revenue-retention surfaced only in Q&A →
  Measured tone, watch-items.
- [Retailer guidance cut](examples/retailer-guidance-cut.md) — a miss, a
  euphemized guidance cut, heavy macro deflection, evasive Q&A → Evasive tone,
  multiple red flags.

---

## Not Investment Advice

This skill provides **educational analysis of management communication only** —
not investment, legal, or accounting advice. It reads the words and self-reported
numbers in a transcript or letter; it does not audit the figures, model the
business, or capture everything that moves a stock. Tone scores are subjective,
and "beats", "misses", and guidance changes depend entirely on the baseline you
supply. Always verify every figure and guidance change against the **primary
filing** (the 8-K earnings release, 10-Q/10-K, and the company's investor
materials) and consult a licensed professional before making any investment
decision. **Not affiliated with or endorsed by Anthropic.**

---

## Contact — Viprasol Tech Private Limited
- 🌐 Website: [viprasol.com](https://viprasol.com)
- ✉️ Email: [support@viprasol.com](mailto:support@viprasol.com)
- 💬 Telegram: [t.me/viprasol_help](https://t.me/viprasol_help) · 📱 WhatsApp: +91 96336 52112
- 🐙 GitHub: [@Viprasol-Tech](https://github.com/Viprasol-Tech) · 💼 [LinkedIn](https://www.linkedin.com/in/viprasol/) · 𝕏 [@viprasol](https://twitter.com/viprasol)

> *Viprasol Tech — fintech software, AI agents, algorithmic trading systems, and B2B SaaS.*

## License
[MIT](LICENSE) © 2025 Viprasol Tech Private Limited
