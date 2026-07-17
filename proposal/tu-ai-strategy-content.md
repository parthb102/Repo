# TU AI Strategy proposal — content pack

Wording only, keyed to the current vDraft (7/16). Everything under **Use:** is paste-ready.
Fit notes are from test-fitting this text in the actual deck shapes.

---

## Slide 2 — Background

**Use (3 bullets, bold spans marked):**

1. During the AI immersion, **TransUnion's leadership shared a set of in-flight and planned AI use cases** spanning internal operations, AI-in-product, and new business models
2. The next step is to **cluster these into end-to-end domains** — the right unit of transformation — then **prioritize and sequence them** into an enterprise AI roadmap
3. In today's discussion, **we will highlight the methodology** to identify enterprise big bets, prioritize them, and sequence actions into a pragmatic execution roadmap

Change vs. current: bullet 2 drops the trailing "…leading with the domains highest in value, readiness, and feasibility" — the triad is introduced properly on pages 4/7, and VG asked for fewer words here.

---

## Slide 3 — Three-part approach

**Lead (keep current):** A three-part approach to AI transformation: prioritize the value, prove it, then scale it

Alternates if VG wants punchier:
- There is a method to the madness: prioritize where the value is, prove it in 2–3 domains, then scale what works *(echoes his own phrase from the call)*
- A three-part playbook: build the value roadmap, prove the value in 2–3 domains, scale what works

Column 2, strategy row (already in draft — keep): "Pick 2–3 domains, conduct proof of value and launch to production" / "Reimagine next priority domains, scale to 3–4 domains"

---

## Slide 4 — Six building blocks

**Lead (keep current):** Six building blocks translate scattered AI ideas into a value-backed roadmap of priority domains

Alternate: Six building blocks take TU from scattered AI ideas to a value-backed roadmap of priority domains

**Blocks (title + 2-line description):**

| # | Title | Description |
|---|-------|-------------|
| 1 | Identify high-value domains | Full set of domains where material value is at stake, anchored in strategic priorities and value pools |
| 2 | Establish a detailed baseline | Current state of each domain including process flow, personnel, performance (e.g., FTE utilization, unit cost) |
| 3 | Develop prioritization framework | Aligned set of criteria and weightings to score domains on value, readiness, and feasibility |
| 4 | Assess impact | Each domain scored on AI impact potential (e.g., revenue growth, cost reduction), strategic readiness, and feasibility |
| 5 | Develop a heatmap scorecard | Single view of all domains scored on each criterion, rolled up into a ranked shortlist for the prioritization workshop |
| 6 | Build execution roadmap | Sequenced path through the priority domains, with owners, milestones, and enabling investments |

Changes vs. current: box 3 now names all three dimensions (was "value and feasibility" only); box 4 fixes the typo ("risk),and") and the wrong example mapping — readiness examples are talent/data, not "risk". Fit note: box 4 caps at ~120 chars before it wraps to a 5th line and spills the card; the version above fits. VG's full impact list (revenue growth, cost reduction, cost avoidance, risk reduction) doesn't fit in the box — it lives on slide 7 (see below).

Box 5 rewritten — the old line ("Rank-ordering of domains across the three dimensions, surfacing the big bets and no-regret moves") was substantively off in two ways: scoring domains on the dimensions is block 4's job (block 5's distinct job is consolidating those scores into one comparable view and an aggregate ranking), and "big bets / no-regret moves" is the vocabulary of the 2x2 quadrants on the framework page, not what a scorecard outputs. Alt if you want continuity with the quadrant language: "Single view of all domains scored on each criterion, rolled up into a ranked shortlist of big bets and no-regret moves."

Footer bar (keep): Every building block is backed by proven tools and methodologies – details follow

---

## Slide 5 — Deep dive 1: Identify high-value domains

**Lead (keep current):** Identify high-value domains: End-to-end workflows with clear potential to demonstrate impact

**"What is a domain?" (left column — tightened, ~25% shorter):**
- **One unit of transformation** — an end-to-end journey, workflow, or function reimagined as a whole, not use case by use case
- **A meaningful value pool** — material upside in revenue, cost, risk, or customer experience
- **Big enough to matter, specific enough to own** — one accountable owner, a measurable baseline, a sequenceable roadmap

**Goldilocks headers (keep):** Entire enterprise – Too big / E2E domain – Just right / Use case – Too small

**Too big — examples (replace all three):**
1. All customer operations
2. Marketing + sales + service at once
3. Enterprise "AI everywhere" program

**Too small — examples (replace all):**
1. Call summarization for one queue
2. Auto-drafting marketing emails
3. OCR for one onboarding document

Design intent: each extreme is one of the six "just right" domains either blown up or shrunk down (all customer operations ↔ contact center; commercial engine ↔ marketing / sales enablement; call summarization ↔ contact center; marketing emails ↔ marketing; onboarding OCR ↔ client onboarding), so the Goldilocks logic reads without explanation. Spares: "Enterprise-wide risk & compliance" (too big); "Triage bot for one dispute type," "Password-reset chatbot" (too small). Fit note: keep entries ≤ ~35 chars — these columns hold two lines max; the current layout has 3 too-big slots and 2 too-small slots, so drop one too-small item or add a slot.

**"Examples of typical domains" (the six from the call — resolves the "Change examples" sticky):**
1. PDLC / SDLC
2. Client onboarding
3. Sales enablement
4. Fraud risk and compliance
5. Contact center / servicing
6. Marketing

Fit note: "Contact center / servicing" and "Fraud risk and compliance" wrap to two lines — put them in the taller slots (positions 4/5 in the current grid); "Marketing" takes the single-line bottom-right slot, otherwise it collides with the blue footer bar.

Per VG: no HR / F&A / corporate functions — too small for TU. Contact center and Marketing can be broken into sub-journeys later (à la JPM credit-card marketing); don't split them on this page.

---

## Slide 6 — Deep dive 2: Establish a detailed baseline

**Lead:** Establish a detailed baseline: Map each domain's current state end-to-end
*(current says "detailed…baseline" twice: "Create a detailed current-state baseline across each domain")*

**Header over the blueprint previews:** Example: Onboarding service blueprint

**Optional caption under previews:** Sanitized example from a global bank; full pages in appendix

**Key takeaways (right rail — keep current 4, with one addition in #1):**
- **Baseline the end-to-end process** across people, process, and technology — sub-journeys, manual steps, and decision points
- **Quantify effort, capacity, and performance** to establish a fact base
- **Identify the highest-impact bottlenecks and value levers**
- **Define the future-state opportunity** with quantified improvement potential

*(Addition covers VG's dictation: manual flows, data flows, decision points, utilization.)*

---

## Slide 7 — Deep dive 3: Develop prioritization framework

**Lead (keep current):** Develop prioritization framework: Focus first on domains where AI reimagination is high on feasibility and value

**Criteria descriptions (left column):**
- **Value potential** — keep current: "Magnitude of sustainable business value that can be realized at scale through AI-enabled transformation across functions, processes, and business units"
- **Strategic readiness** — replace with: "Readiness of the organization to execute and sustain the initiative — the right talent, data availability, and executive sponsorship to drive adoption" *(current is vague "maturity of the organization"; VG defined readiness as talent + data + ability to execute)*
- **Feasibility** — keep current: "Likelihood and expected timeline of successful implementation and value realization, considering the complexity and practicality of delivering the solution"

**Example tiles:** current six are fine. To cover VG's four value levers, optionally add two tiles to the value row:
- **Cost avoidance** — Future spend avoided, e.g., absorbing growth without added headcount or vendor cost
- **Risk reduction** — Lower expected losses from fraud, credit, compliance, and operational failures

---

## Slide 8 — Deep dives 4+5: Assess impact → heatmap scorecard

Leads are fine as drafted ("Assess impact by selected prioritization criteria… / …to develop a heatmap scorecard across domains").

**Substance fixes (the empty box + unlabeled grid read as decoration):**

1. **Right side — real scorecard, not an abstract grid.** Rows = the six domains, columns = the three criteria + rollup, ILLUSTRATIVE sticker. Legend: ● High ◐ Med ○ Low (not an impact gradient). Optional column: "Value at stake, $M — illustrative."

   | Domain | Value potential | Readiness | Feasibility | Priority |
   |---|---|---|---|---|
   | Contact center / servicing | High | High | High | Big bet |
   | Client onboarding | High | Med | High | Big bet |
   | Fraud risk & compliance | High | Med | Med | |
   | Sales enablement | Med | High | High | No-regret |
   | Marketing | Med | Med | High | No-regret |
   | PDLC / SDLC | Med | High | Med | |

2. **Left box** — drop a mini of slide 15 in (it is the value-potential assessment example), same move as the blueprint previews on page 6.

3. **Left caption (replace circular filler):** "For each domain, activities are mapped, the share of work AI can power is estimated against benchmarks, and the impact is priced in dollars — productivity gains plus revenue growth"

4. **Outputs (replace — also kills the proprietary-asset line VG flagged):** "Ranked heatmap of all candidate domains — value at stake, readiness, and feasibility on one page — pressure-tested bottom-up with SMEs; the draft shortlist for the CM1 prioritization workshop"

5. Optional: number the column headers as a pipeline — "1 — Size the value in each domain" / "2 — Compare domains on one scorecard" — so the chevron carries a story.

---

## Slide 9 — Deep dive 6: Build execution roadmap

**Lead (keep current):** Build execution roadmap: Synthesize findings into a value-backed roadmap, including use cases and enabling capabilities

Tighter alternate: Build execution roadmap: Sequence priority domains and enabling investments into a value-backed roadmap

---

## Slide 10 — Work plan

**Title:** How we could partner with you on this journey
*(current says "How we will partner…"; VG's words were "how we could partner with you on this journey")*

**Week headers (verb-start):** Week 1: Identify high-value domains · Week 2: Baseline domains and size the value · Week 3: Assess readiness and feasibility · Week 4: Run the CM1 prioritization workshop *(outcome-flavored alt: "Align on priorities at the CM1 workshop")*

**Grid (current draft content is aligned — canonical copy below):**

| | Objective | Activities | What you get |
|---|---|---|---|
| **W1** | Build a comprehensive view of AI initiatives across functions, and cluster them into end-to-end, high-value domains | • Run working sessions with CM1 teams in every function to capture and cluster initiatives into end-to-end domains • Launch baseline data collection (e.g., headcount, roles, time allocation, cost) | Long list of candidate domains, drawn from one consolidated view of AI initiatives across the enterprise |
| **W2** | Assess how each candidate domain operates today and size the AI value potential across priority domains | • Align on the prioritization framework and scoring criteria • Build each candidate domain's operating baseline with SMEs • Size each domain's AI impact potential across aligned criteria | Prioritization framework and the quantified value at stake in every candidate domain |
| **W3** | Score every candidate domain on readiness and feasibility, and draft stack ranking of all domains | • Assess strategic readiness (talent, data, ability to execute) and implementation feasibility for every candidate domain • Build the heatmap that rank-orders domains on value, readiness, and feasibility • Draft sequencing logic for the roadmap, reflecting dependencies and overlaps | Heatmap ranking every domain along with the draft roadmap and sequencing logic |
| **W4** | Align leadership on enterprise AI priorities, roadmap, owners, and next steps | • Facilitate the CM1 workshop on prioritization outputs and trade-offs • Confirm owners, decision rights, funding, and governance • Align on the near-term roadmap and leadership commitments | Aligned set of priority domains and execution roadmap, with named owners and leadership commitments |

---

## Slide 14 (appendix) — Framework example page

- **X-axis label:** Strategic differentiation → **Strategic readiness** *(explicit ask from VG)*
- **Banner over the chart:** "Balance near term returns and sustained advantage" → **"Focus where value, readiness, and feasibility align"** *("sustained advantage" was the differentiation framing; 51 chars fits the banner at current size)*
- **Criteria column** — sync to slide 7 but compact (these boxes are ~15% narrower; full slide-7 sentences overflow into the row below):
  - Value potential: "Magnitude of sustainable business value that can be realized at scale through AI-enabled transformation"
  - Strategic readiness: "Readiness of the organization to execute and sustain the initiative — the right talent, data, and sponsorship to drive adoption"
  - Feasibility: "Likelihood and expected timeline of implementation and value realization, considering solution complexity and practicality"
  *(also kills the PE-flavored "run-rate EBITDA … across assets, value chains" text, which doesn't fit TU)*

---

## Slide 15 (appendix) — Impact sizing example

**Lead:** Assess impact: Top-down sizing of the AI impact from productivity gains and growth in each domain
*(current "The potential AI impact from gained growth and productivity is sized roughly" reads awkwardly)*

---

## Where Yas's BMO frameworks slot

Example-output coverage per building block today: 1 → page 5 itself · 2 → pp. 12–13 (onboarding blueprints) · 3 → p. 14 (2x2) · 4 → p. 15 (marketing sizing) · **5 → nothing** · 6 → p. 9 (illustrative Gantt, in main flow).

So, by what actually arrives:
- **Scored domain heatmap (domains × criteria)** → the priority catch. Sanitized appendix page behind slide 8 with an EXAMPLE OUTPUT sticker. Fills block 5 — the only block with no example output today (slide 8's right panel is just a schematic).
- **Roadmap / sequencing page** → candidate to replace slide 9's body; VG said he doesn't like the current roadmap page.
- **Prioritization criteria or a 2x2** → don't add pages — duplicates slides 7/14. Harvest better wording, scoring scales, or weights into ours.
- **Value-sizing methodology** → appendix behind slide 15; also use it to firm up slide 8's Inputs list (could replace the "proprietary asset" line with something demonstrably real).
- **Engagement work plan** → mine for slide 10 activities / "what you get" language only; no new page.

Rule of thumb: the main flow (4–10) is already complete 1:1 against the six blocks, so BMO material lands as sanitized EXAMPLE OUTPUT appendix pages — one per block where we lack proof — not as new main-flow pages.

---

## Open items (not content)

1. **TU's "chicken scratch" initiatives page** — VG wanted it kept in the appendix; it's not in the current vDraft. Re-add from the immersion doc.
2. **BMO frameworks from Yas** — pending; slotting map above.
3. **Slide 8 proprietary-asset language** — confirm with VG before it goes out (see flag above).
4. Slides 12–13 (sanitized onboarding blueprints) are already embedded as previews on slide 6 — nothing needed unless the JPM version replaces them.
