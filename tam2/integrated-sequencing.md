# TAM 2.0 — Integrated (platforms) segment sequencing

Sources: Integrated workbook (NA, RoW; Sell/Support-Maintain/EOL interim
framing; summarized dependencies col K) + 2026-07-02 workshop transcript
(1h34m; see `meetings/2026-07-02-integrated-sequencing-workshop.md`).
JR called this workbook "the most thorough" of the segment packs.

## NA

- **Single-in**: current = Payrix API, ProPay API, Assist widgets, hWP stack
  (TriPOS+Express, RAFT/Core, iQ+Launchpad), TAPI (Meet-in-the-Cloud +
  Payfields), hGP legacy (Merchantware, Edge/OpenEdge), Mercury Pay, direct
  gateway integrations.
  Now: **TAPI over TriPOS + Express** (the first mover; unlocks Canada);
  Assist widgets → Global API 2.0 (least-risk product to take international —
  "own guinea pig"); ProPay → support/maintain by Jan '27 (largest partners
  reintegrate to Payrix; split-funding gaps to close); Payrix Payfields
  migration/decom plan; Innovo migrate+decomm (~end '27); MercuryPay shim to
  Express; OAuth for Global API; Global API for Express. ~90–95% of new
  integrations in the last 5 years went to TAPI. OpenEdge Host Pay (~30k
  merchants) + XCharge/RCM route through TAPI by EOY.
  Target: Global API on GG (federated to published spec, linting/validation),
  common portal + MCP server, target plug-in set, decomm duplicate front
  doors.
  Dependencies (col K): GCP↔Azure dedicated connection (hops, latency,
  five-nines); MitC vs triPOS messaging (recert risk — Curtis: MitC is
  protocol-agnostic websocket + matchmaking, likely no recert); boarding/
  servicing readiness so partners can board+service on the new path;
  UCM/FICO unwind; UBA/USI interim; MDM plumbing; MID migration strategy;
  token-vault migration; OAuth pass-through.
- **PayApps**: TAM payapp = triPOS/Nucleus hybrid; TAM cloud integration =
  triPOS cloud/MitC hybrid; merged SDK (triPOS SDK + GPSDK); UPA SI → TAM
  payapp. Cayan terminal app gap vs triPOS = on-device store-and-forward
  (triPOS Direct needs local Windows/Linux install).
- **Boarding**: GPI SF.com → hCorp/USI cutover Sep 21 (surcharging +
  auto-boarding); StoreBuilder/EdgeBuilder replaced by UBA at cutover;
  Lindsay's guidance: USI+UBA ~3 years, iNASA beyond H2 '27; Launchpad
  seamless self-enrolment (low-code embed); single onboarding API needed
  (Payfac, IP referral, Payrix); **boarding API fast-follows transaction API
  (Q4 '26/Q1 '27)** — biggest partners were sold the boarding API; FICO exit;
  Ignition + hWP party model target. Helix/UBA convergence option: refactor
  existing GMAS/GSAP boarding (GPI portfolio) into future state, hWP hooks in
  (Matthew Reily).
- **Processing**: **pan-segment ACH/eCheck gap** — options: VAP as ACH-only
  platform behind Core/Express vs mirror w/ Fifth Third ODFI behind Core
  (~$1.4M) vs ODFI microservices writing back to Core; VAP is NA-only and
  this gates retirement + Payrix gateway stop-sell. Push-to-Account parity
  with Dynamic Payouts → single global payouts. Decouple Payrix as gateway
  (CNP), funnel through Express. Proxy/shim pattern (TXP/TC → TransIT
  precedent) for partners who won't reintegrate. Migration decisioning:
  front+back-end together (hWP tradition, 1 disruption) vs separate (2×).
  Target: GG + PowerZac + RAFT (NA auth) + CORE (NA clearing) + NAP (RoW) +
  GPPaaS (RoW APMs); GG to support Platforms→RAFT by H1 '28 with same API
  implementation (hybrid GG) for RoW.
- **Sales & servicing**: iNASA at launch; target under CRM 2/3 analysis
  (pending). iNASA = NA/CAN/UK; ISI = RoW. l-GP CAN sales flows for iNASA;
  IPCRM migrate/decomm; USI/GPI→iNASA to sunset USI; Payrix/Assist sunset
  pulls partner+merchant records in (sequencing TBD).
- **VAS**: EFE, Fee Assist (some logic depends on Core routing — state-level
  MCC restrictions), CX Suite, Payrix VAS set sell-forward; RTR
  support/maintain (RTR UI+microservice on PRIME backend); gifts: Engage
  decision confirmed (Charlie Southgate) — commercialization to platforms
  ecosystem is the gate for exiting xGift/Merchantware processors; ProPay
  debit-card issuing for fund accounts — capability coverage decision needed;
  tokens: shared tokenization/replication service; RB 2.0; DCC/3DS/Fraud/FX
  per shared target stack.
- **Single-out**: portals converge → MyAccount++ (must cover MX, PX, gateway
  reporting + VT use cases; Curtis: <18mo or duplicate portals persist);
  Payrix/EFE portals align to common single-out; OEV+MSH+MW Portal →
  MyAccount; disputes → WDP north star (DMS interim hGP; Merlin+VAP disputes
  → WDP yrs 1–3; DMS→WDP yrs 2–5); PFaaS converged; reporting target
  selection in progress (enhanced reporting intelligence layer per Pazien;
  automated merchant-migration tooling for processor-to-processor moves);
  residuals: OpenEdge Commissions sunset by '27 ("needs to die"), EPPE
  covers?; hWP platforms use Marketo (Danielle Esma) — confirm EPPE serves
  partners (David Pritchett + Raji); payouts: Payrix flexible split funding
  unlocks ProPay partner migration; Payrix → WPAP P2X integration; Funding:
  hybrid, hWPAP for payout experiences.
- **Data**: MDM Reltio; real-time first-mover; semantic layer; data-centre
  consolidation overlay — reconcile app retirement dates with DC decomm
  timelines (infra preliminary view requested); design system WP DS + Vega.

## RoW

- Oceania: **IntegraPay = front-book** (forward decision); Ezidebit
  support/maintain (deal-review exceptions while CP gap persists — pipeline
  is CP-first and IntegraPay's Verifone-based CP is insufficient; gap
  analysis by product underway). Expand Verifone CP integration for Oceania;
  reconciliation transformation for IntegraPay CP; decomm TakePayments ISV;
  wrap international payments with API 2.0; EZDebit→WPG/NAP funnel assess.
- **Least-cost routing wave case resuming** (was L3/on-hold): route via WPG,
  off Cuscal — ~$1.7M/yr processing-fee savings; aligns Ezidebit/eWay/
  IntegraPay on one WPG path to networks; enables LCR for hGP.
- TAPI already connects to Ezidebit (AU instance live, UK connection built
  never launched) → Global API deployment path in-region; TakePayments ISV
  book → TAPI via IntegraPay → WPG/SAS/NAP.
- IntegraPay halfway in Azure; TakePayments in Azure → convergence assessment
  (CP, HPP, portals, hosting); Curtis in Australia from Jul 13.
- eWay direct business: stays eWay near-term; peel Cuscal (auth) and assess
  Highlander delta (settlement + finance functions); eWay TAM 1.0 plans exist
  (Alan Irwin mapping to resurface) — "paint by numbers" replacement.
  Boarding: UK partner boarding → Ignition/party model; Oceania boarding
  capabilities build. CRM: eWay/Ezidebit Salesforce deeply coupled (source of
  truth, boarding, downstream) — first mover: assess CRM convergence to ISI;
  Sugar → ISI too. CPQ: RCA for RoW Salesforce (eWay & Ezidebit).
- Switch: Olympus → WPG → NAP (decision needed now on WPG connection).
- Portals: align Payrix/Assist/IntegraPay partner/PFaaS capabilities into
  MyAccount++; billing Highlander/Netsuite → target; payouts/funding →
  WPAP + NAP (sell), Highlander support/maintain.
- Genius international: BOIPA/HK Genius S near-term rides GSAP/GMAS; NAP path
  blocked by IPP gap + acquiring licenses; define first-mover market and make
  localization reusable rails for subsequent markets; UK: don't change horses
  mid-launch — target H2 '27 to swap proprietary Verifone + IntegraPay HPP
  for HPP Premium + triPOS. CP/CNP for RoW: needs local currency + local
  payment methods + HPP parity before dropping in.
- Infra: migrate IntegraPay to cloud; design system consolidation as NA.
