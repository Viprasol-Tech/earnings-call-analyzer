---
name: earnings-call-analyzer
description: Analyze an earnings call transcript or shareholder letter — extract KPIs vs guidance, guidance changes, management tone & candor, segment performance, and Q&A red flags. Outputs a structured briefing with watch-items. Use to digest an earnings call, prep for a position, or screen management credibility.
version: 1.0.0
---

# Earnings Call Analyzer

A structured methodology for reading an **earnings call transcript**, a
**shareholder letter**, or an **MD&A** section the way a buy-side analyst does:
pull the KPIs and compare them to guidance and consensus, classify the guidance
change, read management's **tone and candor**, dissect the **Q&A** for dodged
questions, run a **red-flag scan**, and produce a structured briefing with a
**tone score** and **watch-items** for next quarter — grounded in the actual
words and numbers in the document.

> **Not investment advice.** This is an educational analytical framework. It
> reads what management *said* and how they said it; it cannot verify the
> figures, model the business, or account for your risk tolerance. Always verify
> every number against the primary filing (8-K/10-Q/10-K) and consult a licensed
> professional before acting.

---

## When to Activate

Activate this skill when the user:

- Shares an **earnings call transcript** (prepared remarks + Q&A), a
  **shareholder/CEO letter**, or a **10-K / 10-Q MD&A** section and asks what to
  make of it.
- Asks to "analyze this earnings call", "summarize the quarter", "did they beat
  or miss?", "what changed in guidance?", "how candid was management?", or "what
  are the red flags here?".
- Wants to **prep for a position** ahead of or after a print, or to **screen
  management credibility** across quarters.
- Pastes prepared remarks and an analyst Q&A and asks which questions were
  answered straight and which were dodged.

If only a headline is given (e.g. just "they beat EPS"), ask for the transcript
or the relevant section before scoring tone or guidance. Do not invent quotes,
figures, or guidance — work only from the supplied text, and mark anything you
infer as `(inferred)`.

---

## Step 1: Scope & Context

Before reading for signal, establish and restate the context so the briefing is
anchored:

| Field | Why it matters |
|---|---|
| **Company / ticker** | Identifies the entity and the peer set. |
| **Period / quarter** | Which fiscal quarter or year (e.g. FY24 Q3); calendar vs fiscal. |
| **Document type** | Transcript (remarks + Q&A), shareholder letter, or MD&A — Q&A only exists for a live call. |
| **vs prior period** | QoQ and YoY comparisons reveal acceleration/deceleration, not just level. |
| **vs consensus** | A "beat" only means something against the Street estimate — note it **only if the user provided it**; never fabricate consensus. |
| **Speakers** | CEO / CFO / IR / which sell-side analysts asked questions — tone differs by speaker. |
| **One-offs in the period** | M&A, divestiture, restructuring, FX, a recent IPO/SPAC, a guidance reset — these distort the read. |

State each explicitly in the briefing header. If the period, document type, or
comparison basis is unclear, ask — a "beat" or a "cut" is meaningless without
the baseline.

---

## Step 2: KPI & Results Extraction

Pull the hard numbers management reported, and line them up against guidance and
(if supplied) consensus. Flag anything missing, derived, or non-GAAP.

**Headline financials:**
- **Revenue** (total and growth % YoY/QoQ).
- **EPS — GAAP and non-GAAP/adjusted**, stated separately. Never merge the two.
- **Margins** — gross, operating, and net; GAAP and adjusted where both are
  given.
- **Segment / product-line revenue** and growth, plus segment operating income
  if disclosed.
- **Key operating metrics** — the ones that actually drive the business and that
  management leads with or that analysts press on, e.g.:
  - SaaS: ARR/NRR (net revenue retention), customer count, RPO/billings, churn.
  - Retail/consumer: comparable-store ("comps") sales, traffic vs ticket,
    inventory, gross margin rate.
  - Ads/internet: DAU/MAU, ARPU, ad load, take rate.
  - Hardware/industrial: units, ASP, backlog, book-to-bill.

For each metric, capture **actual vs guidance vs consensus** where available, and
the surprise (beat / in-line / miss) with magnitude.

Rules:
- **State GAAP and non-GAAP side by side.** If management leads with adjusted
  figures, surface the GAAP number next to it.
- **Flag the "adjusted-vs-GAAP wedge."** If **non-GAAP is emphasized while GAAP
  is deteriorating** — adjusted EPS up but GAAP EPS down, or a widening list of
  add-backs (stock-based comp, "one-time" restructuring, amortization of
  intangibles) — call it out explicitly. A growing wedge is an earnings-quality
  warning.
- **Mark estimates.** If a figure is derived or inferred from text rather than
  stated, mark it `(inferred)`.
- **Watch units and basis.** Reported vs constant-currency, organic vs total,
  before/after a divestiture — restate the basis with every number.

---

## Step 3: Guidance Analysis

Guidance moves the stock more than the printed quarter. Extract it and classify
the change precisely.

**Extract:**
- **Next-period guidance** (revenue, EPS, key metric) — range and midpoint.
- **Full-year guidance** — new range and midpoint, and whether it was reaffirmed
  or revised.
- Any **segment-level** or **metric-level** guidance (e.g. margin target, capex,
  NRR, comps).

**Classify the change** vs the prior outlook into exactly one of:

| Class | Meaning |
|---|---|
| **Raised** | New range/midpoint above the prior outlook. |
| **Maintained** | Reaffirmed; range essentially unchanged. |
| **Cut / Lowered** | New range/midpoint below the prior outlook. |
| **Withdrawn** | Guidance pulled / suspended (often a serious signal). |
| **Initiated** | First-time guidance (no prior baseline). |

**Read the framing, not just the number:**
- Note when a **cut is buried** — disclosed late in prepared remarks, only in the
  appendix, or surfaced only under analyst questioning rather than stated up
  front.
- Flag **euphemistic framing** of a cut: "recalibrating", "prudent", "de-risking
  the outlook", "reflecting a more conservative posture", "updated to reflect the
  current macro" — name the euphemism and translate it to plain English (this is
  a guidance cut).
- Distinguish a **lowered top line with a held bottom line** (cost-cutting to
  protect EPS) from a clean reaffirm.

---

## Step 4: Tone & Candor Assessment

How management talks is signal. Read the **prepared remarks** and especially the
**Q&A** for confidence, directness, and candor.

### 4a. Language: confident/direct vs hedged/evasive

Characterize the prepared remarks on a spectrum from **direct** ("revenue grew
22%, ahead of our guidance, driven by enterprise") to **hedged/evasive**
("we're navigating a dynamic environment and remain focused on execution").

**Count and characterize hedge words / deflection phrases**, and note where they
cluster (a spike around a specific topic — e.g. a weak segment — is more telling
than the overall count):

- Macro deflection: "macro headwinds", "challenging environment", "choppy",
  "uncertain", "elongated sales cycles", "budget scrutiny".
- Minimizers: "transitory", "temporary", "timing", "one-off", "noise", "modest".
- Reassurance-without-substance: "prudent", "disciplined", "focused on
  execution", "well-positioned", "confident in the long term".
- Vagueness: "a number of factors", "certain headwinds", "some softness".

### 4b. Q&A dissection

The Q&A is where candor is tested — analysts push on the weak spots. For each
notable exchange, classify the answer:

- **Answered directly** — gave the number/the reason the analyst asked for.
- **Partially answered** — addressed it but withheld the specific metric.
- **Dodged / non-answer** — pivoted to a different topic, gave a "we don't break
  that out", repeated talking points, or deflected to "macro".

Track **which topics get dodged** — a repeatedly side-stepped metric (e.g. NRR,
churn, comps by month, a segment's profitability) is itself a red flag. Note any
**over-promising** ("we expect to reaccelerate next quarter", "back-half
weighted", "second-half recovery") and whether it's substantiated or just
asserted — and whether prior such promises were kept.

### 4c. Candor score

Synthesize Step 4 into one rating:

| Score | Signature |
|---|---|
| **Candid** | Names problems plainly, gives specifics even when bad, answers Q&A directly, GAAP-forward. |
| **Measured** | Mostly straight but selectively vague on the weak spots; some hedging; a few dodged questions. |
| **Evasive** | Heavy hedge-word/macro deflection, buried or euphemistic bad news, multiple non-answers, GAAP obscured by adjusted figures. |

Always cite **evidence quotes** (verbatim short excerpts) supporting the score.

---

## Step 5: Red-Flags Quick Scan

Scan for these signals. Each is a prompt to dig deeper, not an automatic
condemnation:

- **Guidance cut buried late** — the lowered outlook appears at the end of
  remarks or only in Q&A, not up front.
- **Repeated macro deflection** — "macro/headwinds" invoked to explain
  company-specific underperformance, especially when peers aren't blaming macro.
- **Heavy non-GAAP emphasis hiding GAAP** — adjusted figures lead while GAAP
  deteriorates; growing add-back list; "one-time" charges that recur every
  quarter.
- **Evasive / non-answer Q&A** — analysts repeatedly pressing the same point;
  "we don't disclose that"; pivot-and-deflect on a key metric.
- **Blaming externalities** — weather, FX, "the consumer", a single large
  customer, the calendar — as the whole story rather than part of it.
- **CFO / senior-exec departure** — a CFO, CEO, or chief accounting officer exit
  mentioned (especially abrupt, "to pursue other interests", or right before/with
  a guidance reset).
- **Channel stuffing / pull-forward hints** — "pulled forward demand", "pre-buy",
  "sell-in vs sell-through" gap, rising receivables/DSO referenced, distributor
  inventory build.
- **Going-concern / covenant / liquidity mentions** — "going concern",
  "covenant", "waiver", "amendment to our credit facility", "refinancing",
  "liquidity" framed defensively.
- **Buyback/dividend as distraction** — a fresh buyback announced alongside a
  miss or cut, used to steer the narrative.
- **NRR / churn / comps deceleration disclosed quietly** — a key health metric
  decelerating but mentioned only in passing or under questioning.

---

## Step 6: Output Format

Produce the briefing in this order:

### 1. Header
Company · ticker · period/quarter · document type · comparison basis (vs prior
period; vs consensus only if provided) · notable one-offs in the period.

### 2. TL;DR (3–5 bullets)
The punchline first: beat/miss, guidance direction, tone, and the single most
important takeaway or red flag.

### 3. KPI table
One row per key metric:

| Metric | Actual | Guide / Consensus | Δ | Beat/Miss |
|---|---|---|---|---|
| Revenue | $1.42B (+22% YoY) | $1.38B guide | +$40M | Beat |
| Non-GAAP EPS | $0.71 | $0.66 cons. | +$0.05 | Beat |
| GAAP EPS | $0.12 | — | — | — |
| Operating margin | 18% | — | — | — |
| Net revenue retention | 109% | ~114% prior qtr | −5 pts | Miss/decel |

(Use "—" where no guide/consensus was supplied; never fabricate one.)

### 4. Guidance-change summary
Next-period and full-year guidance, the classification (**Raised / Maintained /
Cut / Withdrawn / Initiated**), and a note on framing (was a cut buried or
euphemized?).

### 5. Tone & candor score
**Candid / Measured / Evasive**, with **2–4 evidence quotes** (verbatim short
excerpts) and the hedge-word/deflection read, plus the Q&A dodge list.

### 6. Top takeaways
The 3–6 things that actually matter from the quarter — what's working, what's
breaking, what management is steering toward.

### 7. Red flags
Prioritized, most material first, each with the supporting evidence (the quote
or the number behind it).

### 8. Watch-items / catalysts for next quarter
The specific things to verify or watch into the next print: a decelerating metric
to track, an over-promised reacceleration to hold management to, a guidance
midpoint they'll be measured against, a departing exec's replacement, a covenant
test date.

---

## Disclaimer

This skill provides **educational analysis of management communication, not
investment, legal, or accounting advice.** It reads the words and the
self-reported numbers in a transcript or letter — it does **not** audit the
figures, model the business, or capture everything that moves a stock. Tone and
candor scores are subjective heuristics; "beats", "misses", and guidance changes
depend entirely on the baseline you feed in. Always verify every figure and every
guidance change against the **primary filing** (the 8-K earnings release,
10-Q/10-K, and the company's own investor materials), consider the qualitative
and forward-looking context the transcript can't settle, and consult a licensed
financial professional before making any investment decision. This skill is
**not affiliated with or endorsed by Anthropic** or any data provider.

---

## Related Viprasol Skills

- **[financial-statement-analysis](https://github.com/Viprasol-Tech/financial-statement-analysis)**
  — once you've read the call, run the actual financials: liquidity, solvency,
  profitability and efficiency ratios, DuPont, Altman Z-score, Beneish M-score,
  and an earnings-quality check. The two pair naturally: this skill reads what
  management *says*, that one checks whether the *numbers* back it up.
