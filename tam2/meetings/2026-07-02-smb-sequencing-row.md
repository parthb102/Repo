# SMB sequencing (RoW) — 2026-07-02

Two recordings exist for this session:

1. **11:10AM, 2h01m, "Meeting Transcript"** (`TAM_2.0_SMB_Sequencing_RoW_2.docx`)
   — the substantive session, distilled below. JR led until ~1:23, then Parth
   Bahl + Mario Gonzalez Madrid facilitated Greece + wrap.
2. **1:38PM, 51m, "Meeting Recording"** (`TAM_2.0_SMB_Sequencing_RoW.docx`,
   also re-uploaded as `_1`) — transcription captured almost nothing usable
   (a handful of lines; Jaemi Bremner started transcription). Treat as empty.

Present (speaking, session 1): JR, Lucy Anderson (RoW SMB product), Vivek
Pujeri, Matthew Reily, Michael de Jacquier, Karel Jára, Marcus Lang, Khali
White, Jerry Roberts, Jennifer Gebhart, Alexander Dewison, Jaemi Bremner,
Milan Bednár (ERSTE), Marek (Poland), Dimitris Charaklias (Greece), Eyal Mor
(COMO), Nana Yaa Mensah, Mario Gonzalez Madrid, Parth Bahl, Daniel McDowell,
Joanne Lee, Anushree Kolhe.

## Asia-Pacific (Lucy Anderson)

- Strategy: exit third parties across the value chain (reseller model: 7
  device software stacks via PAX/Ingenico; MPGS + CyberSource gateways;
  third-party installments ≈35% of Asia revenue — concentration risk;
  GSAP/GMAS back end; GPAPI front). Fix foundations ~12mo (to mid-'27) →
  localize Genius S. Markets: HK (65–70% revenue), Philippines (JV/BOIPA),
  Macau, Singapore, Malaysia; Taiwan separate (onshoring).
- Onboarding: **wave 143029** — Salesforce Experience Cloud → MBS/OmniTracker
  (self-serve): 12–14 days → 2–3 days; MOS AP out of self-serve architecture
  early next year; **sales-assisted path off MOS = "plan for the plan"**
  (Matthew Reily, beginning; assess under onboarding — priority now). MBS
  integrations already MuleSoft/UBA-conformant (Reily: "we're aligned").
  UCM prioritized (Jennifer). Micro vision: app-store download → first
  softPOS transaction in 20 minutes; sales channel: straight-through, 14d→2–3d.
- **Data hierarchy cleanup pre-migration**: AP minted a MID per product per
  merchant (installments) — expensive, must map old→new model (de Jacquier +
  Pat Bateman + Reily + Vivek huddle); "review and determine go-forward
  product/pricing/merchant hierarchy" noted under migrate-assess.
- Genius Mobile (GP Mobile Pay/Yazara): **Philippines 2026-10-30 launch on
  PowerZac**; fast-follow HK + Macau. Nucleus + TMS (Karel) for Genius S in
  flight; HK/Macau Nucleus Q1 '27 (workbook). Genius S AP = triPOS + Nucleus
  (nucleus shim) — converge Karel's TMS with hWP-side plans.
- Migration (next): James Fry segmenting AP enterprise vs SMB; first movers =
  e-com enterprise merchants w/o IPP → hWP stack; **IPP on NAP is the gap**
  (HK IPP ≈30% revenue); NAP acquiring licenses needed (HK first, then PH/
  Macau/Malaysia); PH JV rules complicate (WP has no PH footprint).
  **Secure Acceptance EOL Jun '27** — Gemma Hammer pushing Visa (via GP
  global CyberSource lead) for 12-month extension to Jun '28. Connect with
  Rob Ward (UK CyberSource→target-rails pattern) / global CyberSource
  relationship owner. Terminals: assess **MDM OTA update instead of
  re-terminaling** (de Jacquier w/ terminal team). iNASA boarding amendments
  (pricing config, merchant hierarchy) to prep migrations; portal
  localization (language/servicing — Nick Collins commercialization);
  Salesforce Service Cloud live in AP.
- DCC: Planet today; localizing into EU DCC solution; **may need backward
  compatibility to Planet** if support runs longer — scope increase; Marcus
  Lang owns global Planet agreement negotiation.
- VAS: protect installments (35% revenue), land Genius S, then demand-based
  business cases; DCC continues.

## Poland (Marek)

- Priorities (next ~12–18mo): e-comm enhancements (consistency + verticals,
  e.g. public sector); VAS consistency — Amex two models (Fiserv local +
  direct) → Amex's European **PayFac model**; "**service pipe**" combined
  platform for mid-enterprise differentiation; **all-in-one commerce
  device** — fiscal app + POS app + terminal app on one device ("single
  provider of commerce solutions", no "payments" in the words — Cameron
  strategy).
- GP Tom in market on e-service payment-app rails → **e-service → Nucleus
  convergence incl. TMS consolidation** (2–3 TMSes in PL).
- **BLIK APM = quickest win**: contract + gateway integration exist on GPE
  stack; leverage for Worldpay gateway with modest work (James Fry follow-up).
- **Sugar CRM → Salesforce International** within 12–18mo (Vivek) — unlocks
  MBS connectivity (Salesforce already connected to MBS).
- **Bilats / least-cost routing**: EU regulation separates scheme from
  routing; PL bilats route down cheaper networks → price competitiveness;
  map holistically for Europe incl. on-us JV routing — preserve in target
  (Lucy flagged as strategic, all LOBs).

## ERSTE JV (Milan Bednár)

- #1 **Project Frank**: Croatia → GPE stack; 1 Nov '26 face-to-face clients
  onboard new stack. #2 **Genius CZ by Oct '26** (fiscalization law; par with
  competition; Gregor Liset). #3 **Nucleus as only payment app**: 50/50 today
  vs GPE Pay (PayTen); gaps in SK/AT/RO block 100% for new clients. GP Tom
  asset still ERSTE-owned (sale unsigned → GP Mobile Pay rename blocked).
- Processing: Nucleus→PowerZac→Base24; ACI consolidation = PowerZac as auth
  host (upstream unchanged for merchants); back end MMS→NAP with downstream
  deps (disputes, multicash etc.). Mix: 8% e-com / 18% VAS / rest CP.
- E-com: **GPE WebPay** for all ERSTE JVs (+ some competitors resell);
  WebPay↔GPECom gap = APM parity + cost model (GPE invoices JVs per feature;
  WebPay cheaper) → enhancements paused (Dewison; full gap sheet exists);
  may need to build parity at own expense. **GPECom can't serve enterprise**
  — losing large merchants to Adyen, can't compete in RFPs. Fix: bring hWP
  eCom proposition + APM service (**GPADS** behind GPECom) as the migration
  "carrot" for ACI consolidation — **follow up Richard (Keering), Mark
  Hopkins, Rob Wingfield on ACI consolidation plan** (footnote: Mario/Parth).
- VAS: **COMO pilot in ~1 month** (CZ/Budapest/SK via P2C terminals; Nucleus
  integration starting — Eyal Mor; long-term bundled with Genius); spread
  existing VAS across countries.
- Portals: GPE merchant portal + Marketplace; **SSO for 8 EU regions, target
  Oct** (Jaemi Bremner). JR guidance: beyond SSO, don't invest in GPE
  merchant portal/reporting — enhance **WP Dashboard within MyAccount++**
  and let portal closure follow the NAP back-end migration (NAP ⇒ WP
  Dashboard/iQ by default). Jaemi caveat: public assets (help centers,
  marketplaces/app stores) migrate right after SSO — not gated on rails;
  sequence rest-of-EU after WP Dashboard converges into MyAccount++ unified
  shell (UK&I first).

## Greece (Dimitris Charaklias — NBG Pay)

- GP Tom → **Genius Mobile ~Sep/Oct for ~7,000 merchants**. Genius
  fiscalization decision pending (Greg Liset call Monday); Greece all-in-one
  market is fiscalization-driven (top-5 POS all-in-one, top-50 softPOS
  competitive position); OCPI/EV-charger + unattended PAX opportunities.
- E-com: MPGS + GPECom; GPECom gaps = **IRIS (mandatory APM), Greek
  installments, recurring**; enterprise gap — two biggest Greek airlines
  (talking to Worldpay). Dewison/Mensah: continue GPECom feature-parity for
  named gaps then pause → converge to GG; assess pivot to target payment
  orchestration (Access payments API).
- Estate: Mellon legacy vendor ~200k POSs; **EDPS** = 100% GP-owned technical
  provider + multi-acquiring PSP hub (switching, loyalty, crypto, APMs for
  top retailers e.g. Sklavenitis); EDPS PayApp → Nucleus is hard
  (localization, fiscalization) — Karel discussions started; **GAPS** host →
  PowerZac (GP Tom + GPECom); Postilion migration (3yr) just completing.
  Target (Mensah): thin EDPS long-term, retain hard-to-replace loyalty/
  in-region capability; little movement inside 18mo.
- Boarding: **ECBD ↔ MBS gap = manual adds** for GPECom (ECBD same platform
  as Poland); 18-mo roadmap: ECBD → MBS → GPECom → RealControl automated.
  Salesforce Greece = leads only; needs full pipeline + product + pricing
  (mirrors Poland; then MBS connects). Servicing via NBG branches (my NBG →
  ECBD, ARC Mercury) — same architecture as Poland (Vivek/Khali).
- VAS: DCC from Poland's GPE DCC (via Supercheckout); e-service DCC also
  exists → consolidate on GPE DCC now, combined hGP/hWP DCC service later
  (Marcus/Dewison); MCA (no dates); COMO w/ Sklavenitis not started.

## Coverage gaps & wrap (Parth/Mario facilitating)

- **Germany** (Commerz Global Pay): no product lead in seat — Amy (Mehta)
  recruiting; **Spain** Comercia — Luis Palomero (e-com roadmap Friday mtg);
  **CSOB JV** (CZ/HU) — white-label GPAPI+GPECom resale (Dewison to name
  contact; workbook: Vaclav Kerka). Possibly one combined follow-up session.
- **Australia/NZ**: direct SMB book segmented into Integrated international
  but needs differ (half of ANZ P&L = SMB direct; Lucy wearing the hat until
  hire); ~**$10M capex/yr exposure** staying on current platforms; front-book
  = IntegraPay (ISV-specific); back-book direct plan TBD; Lucy pings JR;
  integrated session output shared back, targeted follow-up if gaps.
  de Jacquier: don't let org/revenue segmentation (Conway's law) deny SMB
  customers the right SMB experience.
- Japan: no hGP SMB. Check India/other geos (de Jacquier).
- JR dropped ~1:23 (GMT hard stop); will listen back + syndicate the now-work
  for remaining markets, as done for AP/PL/ERSTE.
