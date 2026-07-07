# Integrated sequencing workshop — 2026-07-02, 9:07PM ET (1h34m)

Present (speaking): Soltan Nayabkhil (led), Curtis Landry, Jonathan Rigaud
(JR), Andre Dubreuil, Matthew Reily, Mario Gonzalez Madrid, Parth Bahl,
Ryan Heaton (data), Steve Stidhem, Karin Woodard. JR: this pack was "the most
thorough" of the segments.

## Decisions / alignments

- **TAPI → TriPOS → Express is the first mover** for Integrated NA; goal:
  every net-new MID routes to Express ASAP (~6–9mo); then selective
  aggressive back-book migration once natural shift is visible (10% churn/
  backfill heuristic). ~90–95% of new integrations over 5 yrs already TAPI.
- **Assist widgets → Global API 2.0** — the "own guinea pig" product to take
  international (lowest customer debt).
- **ProPay → KTLO by Jan '27** (8 dev teams vs Edge's 1; reallocation to
  Assist in flight); large partners reintegrate to Payrix (CareStream from
  Edge already moving); split-funding gaps on Payrix to close first. Show
  the dwindling tail so ELT can decide when to pull the plug.
- **Innovo decomm by end '27.**
- **Wave 180243 resources** (were Edge→Merchantware) now target Edge &
  Merchantware → Express paths; 2 dev teams spinning up Belfast, Q3.
- **Token/credential first mover**: all three gateways (Edge, Merchantware,
  Express) use credential-management tokens; shared tokenization/replication
  service; critical for every e-com migration (Sterling/SNAP/Innovo →
  Express too).
- **CP critical decision** (recurring across segments): Option A migrate MIDs
  to target host w/ manageable attrition vs Option B duplicative throwaway
  boarding integrations. Merchantware merchants boarded on Sierra are sticky
  until GSAP→Express/RAFT and Sierra→RAFT MID-migration paths exist (no
  re-papering, no pricing/funding-window changes). JR kicked off core
  acquiring analysis of every host → with Chris Gaseltine.
- **Global Gateway dual path**: low-volume non-strategic gateways → migrate
  volume to Express now; Portico/TransIT/Merchantware do NOT two-hop —
  decompose GG into shared services (common decryption connected to HSMs,
  common tokenization) co-evolving RoW + NA (Curtis's "no 2M-merchant event
  in 4 years"). Gaseltine decomposes what GG means.
- **Payfields/hosted convergence**: keep partner-facing JS (CDN-hosted, ~$20/
  mo) — converge single-use token service + hosted iframes behind the scenes
  across Portico/Payrix/TAPI/GPE versions; partners never recode.
- **Boarding**: Sep 21 GPI SF.com → hCorp/USI cutover confirmed (unless
  catastrophic); StoreBuilder/EdgeBuilder replaced by UBA then; Lindsay:
  USI+UBA for ~3 years, iNASA convergence beyond H2 '27. **Boarding API must
  fast-follow the transaction API (Q4 '26/Q1 '27)** — biggest partners were
  sold the boarding API; single onboarding API across Payfac/IP-referral/
  Payrix. Helix/UBA convergence option: refactor GMAS/GSAP boarding for GPI
  into future state; hWP hooks in (Reily).
- **MDM named a first mover** (Reily): product, pricing, merchant/partner
  hierarchy mastered outside Salesforce (Helix architecture), SF reads it.
- **ACH workstream to kick off**: Lori Sheehan leads ACH (per Mike Clark);
  options: VAP as ACH-only platform vs mirror w/ Fifth Third ODFI behind
  Core (~$1.4M) vs Gaseltine's ODFI microservices + Core reporting
  write-back. Parth/Mario/Christina support the kickoff. Gates VAP
  retirement + Payrix gateway stop-sell.
- **Gift = Engage** (not Valutec) — decision documented by Charlie Southgate;
  commercialization into platforms ecosystem is what matters; xGift
  migrate+decomm.
- **Routing**: leverage RTR microservice + UI on the PRIME backend.
- **Residuals**: hWP platforms use Marketo today (Danielle Esma); EPPE
  (Enterprise Partner Payments Engine) is the direction — confirm with David
  Pritchett + Raji that it serves partner/platform needs, not just SMB.
  OpenEdge commission portal sunset by '27.
- **Portals**: gateway-level reporting + virtual terminal must be in target
  portal (MyAccount) or duplicates persist — solve <18mo; partner portals
  need "appropriate love" (assist/Payrix/commission portals).
- **Data** (Ryan Heaton): target platforms must adopt data target patterns;
  analytical data from target platforms accessible in target data solution —
  don't wait; MDM customer master/hierarchy/product master feeds apps; Ryan
  takes to Himanshu team.
- **Oceania**: IntegraPay forward-book (Ezidebit deal-review exceptions; CP
  gap analysis by product — pipeline is CP-first, Maas's concern); LCR wave
  case resuming: off Cuscal → WPG ≈ $1.7M/yr savings, aligns Ezidebit/eWay/
  IntegraPay; TAPI has AU instance (Ezidebit) + dormant UK connection →
  Global API in-region path; TakePayments ISV → TAPI via IntegraPay →
  WPG/SAS/NAP; IntegraPay+TakePayments both Azure — convergence assessment;
  eWay direct: peel Cuscal, assess Highlander delta; eWay TAM 1.0 map (Alan
  Irwin) to resurface; RoW target CRM = ISI (not iNASA); Ezidebit/eWay SF
  deeply coupled — CRM convergence assess is a first mover (Nick Corrigan's
  MBR emphasized).
- **Genius international**: HK/BOIPA near-term = GSAP/GMAS integration; NAP
  blocked by IPP (~30% HK revenue) + acquiring licenses; define first-mover
  market; build localization as reusable rails; UK — don't change horses
  mid-launch; H2 '27: assess swapping proprietary Verifone + IntegraPay HPP
  for HPP Premium + triPOS.

## Actions / follow-ups

| Action | Owner |
|---|---|
| Cross-company access fix (contractors both ways; ProPay dev-portal team blocked 2wks, July starters) | JR to facilitate targeted conversation |
| ProPay/ProPay-gateway cross-company access follow-up | JR ("JR to have follow-up convo") |
| Core acquiring analysis of every host | Chris Gaseltine (JR handed over) |
| Decompose "Global Gateway" into service definitions | Chris Gaseltine + platforms |
| Switch vs gateway vs host vs auth-platform taxonomy — circulate | Mario (Chris authored) |
| ACH workstream kickoff | Parth/Mario/Christina + Lori Sheehan, Soltan, Curtis, Andre |
| Confirm EPPE covers platforms residuals (Marketo exit) | David Pritchett + Raji (Parth/Mario chase) |
| Boarding deep-dive w/ Maegan Cardillo team, Utah, early Aug | Soltan (fwd invite to Curtis) |
| Level-of-effort assess: single onboarding API | Soltan team |
| Australia convergence mapping (from Jul 13) | Curtis |
| Lucy follow-up: remap APTM/TAM 1.0 for Australia (~2 wks, in person) | JR |
| Virtual terminal + gateway reporting placement in taxonomy; ensure planned in 0–18mo | JR + teams |
| Salesforce Commerce Cloud extension (PGA et al) → Express integration | platforms |
| Engage commercialization to platforms ecosystem | platforms + gift team |

## Next steps (JR)

Synthesize transcripts + workbooks into now/next plans; investment-request
percentages by tier (boarding vs API vs gateway vs single-out); **board
presentation Jul 24** (funding guidance outside feature work; incremental
funding ahead of '27 budget cycle); **Jul 20–21 focused cross-segment
sessions** (CRM, boarding+servicing, single-in/gateway, payment apps) —
segment-agnostic interdependency mapping; prep summary circulated in days.
