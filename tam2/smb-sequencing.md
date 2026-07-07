# TAM 2.0 — SMB segment sequencing

Sources: SMB workbook (UK&I ×3 tabs, NA ×4 channel tabs + `NA>>` rollup, RoW +
`RoW>>` rollup) + 2026-07-02 NA session (1h56m) + 2026-07-02 RoW session
(2h01m). See `meetings/` for distilled minutes.

## UK&I

- **Front-book priorities (L col)**: 1) Genius S UK — confirmed, built on NAP
  target-state rails, Q1 '27 pilot; 2) eCommerce expansion (WP eComm
  Essentials targeting POS back-book, Shopify Onsite plugin, payment links &
  invoicing); 3) VAS growth — Everyday Settlement H2 '26 (NAP-acquired), DCC
  back-book opt-out, MCA in-house (rev ~$35m '27–28), terminal leasing for hGP
  terminals; 4) bank channels — BOI, Virgin Money/Nationwide, HSBC (Tuza,
  eComm, Genius Mobile, Dashboard hooks); 5) WP360 GA into Ireland Q3 '26.
- **Corporate (M col)**: Business Gateway migration (audit deadline extended to
  Jul '27; automated migration scripting blocked on infra DB capacity); NerPay
  Ingenico app sunset; ACI/Postilion back-office exit by 2029; fragmented
  hGP/hWP sales tooling & portals.
- **Back-book priority exits**: Evo/e-service (ACI-based, ~60% CP volume; exit
  enables ACI exit + Project Carbon data-centre closure), GMAS Europe (FIS
  dependency, TSA close), Greenhouse (converge all UK&I SMB to one stack),
  Take Payments (own CRM+dialer island; TP Plus app → Genius).
- **Key trade-offs**: e-comm integration — bridge GP API to Access vs require
  reintegration (recommended; depends on Global API standard first; WP eComm
  back book already on Access so GG move is seamless). CP swap — route
  terminal→Nucleus→host vs keep legacy direct-to-host; terminal heartbeats
  allow remote push. BIN/ICA — migrate small/mid first onto new BIN/ICA,
  large enterprises (own BINs) later vs whole book at once.
- Genius resold under Worldpay UK Ltd; hGP back-book (Evo, TP, GPUK) repapered
  to WP entities. Combined SDK needs PCI MPOC/INBOX certification; rationalise
  6 POS test/cert labs. DCC required to sell Genius UK&I (GA target Q2).
  UCM awaiting budget approval. Boarding: OMS → Boarding Gateway/Workstream
  Manager transition in flight; UK SMB back-book migrate + OMS decom in Next.

## NA — channel structure

Direct = Heartland (lion's share) + EVO direct + legacy-TSYS direct.
Wholesale/Indirect/ISO decompose hWP's "partner" notion. ISO spans two hGP
rails (GSAP/GMAS **and** Sierra/TMAS); Indirect is TSYS rails (Express/MMS).
Rails: interim destination confirmed = **RAFT + Core** ("intermediary target"
— assembler/COBOL, long-term TBD).

### Direct

- **Gating first mover: sales commission via iNASA** (+ OMS/USI gap closure)
  before any net-new direct merchant boards on hWP rails. "The $6M question"
  — sizing is the immediate ask. Confirmed by CRM (Lindsey via Pritchett),
  servicing (Khali White).
- Migration bias: EVO + TSYS-direct merchants move first; Heartland later
  (Passport same-day batch close; HCSDB "ball of yarn"; Core won't reach
  Passport parity near-term).
- **Add-location duality**: existing merchants adding locations may live in
  two tools (iQ vs InfoCentral, two IVRs); acceptable only if the transition
  window is finite and defined → focused session needed.
- **Gateways**: Sterling/SNAP/TXP decomm — move volume to Express/Portico now
  regardless of feature gaps; Portico/TransIT persist, decision "late next";
  no two-hop for the big gateways (decompose toward GG instead).
- **Genius upsell pattern**: today Genius→Portico; tomorrow Genius→TriPOS→
  Express. ~50% of Heartland direct book (target MCCs) addressable (Julie's
  analysis). Non-Genius back-book CP → become Genius customers on target
  rails via OTA terminal/firmware upgrade once configured in target
  (de Jacquier/Hagan). Pattern to formalize on 20th/21st.
- **CNP/e-com**: GPAPI→Portico interim vs hybrid GG (WPG-backed, earlier) vs
  wait ~1yr for clean GG→Core. Omni-channel requirement (single back end,
  one data feed) may rule out GPAPI→Portico. Need e-com/omni/Genius-only
  persona requirements doc for 20th/21st. Access is live for Enterprise NA
  but not ready for SMB NA; Access→RAFT in test.

### Wholesale

- Genius S TriPOS/Express pilot = wholesale is the pilot channel.
- **Boarding**: Launchpad ≈ apples-to-apples vs Base except boarding onto
  Sierra/TMAS. Preferred: **Launchpad + UBA opens the Sierra/TMAS pipe**
  (not tactical point-to-point) while merchant migration runs in parallel —
  accepted as partially throwaway; NPC demise precedent ≈ 3 years. Kill list:
  MAP, Central Station, MEA, MerchantFlo, OnTrak, StoreBuilder/EdgeBuilder;
  ID Gen (MID generation) — find comparable service, pick one.
- **Residuals/pricing**: EPI (=EPPE) is target; close gaps vs Base, MEA,
  Central Station; billing platforms must feed EPI; reverse rev-share for
  indirect has funding/billing nuances — Raji workshops before Jul 20.
- **UCM**: done for Base/Cayan; NOT yet in Genius S wholesale path; new scope
  = Launchpad + iNASA integration, sales AND servicing → budget/LOE rework.
- **Servicing**: target iNASA; Base servicing work paused (~1yr to bridge,
  mid-'27 to complete) — decide resume-as-bridge vs converge direct;
  perspective needed by end of July. Capability assessment (10-things list)
  for Central Station/OnTrak/MAP → iNASA; requirements exist from Base
  servicing effort (Jason Ohlson/Nicole/Drew Chamberlain). Servicing must
  either touch Sierra/TMAS or merchants migrate first — chicken-and-egg with
  Michelle Young's requirements ask. Approach persona-based, not
  portfolio-based (Jake Bruley).

### Indirect / ISO

- Last movers. Express+CBOS stack is stable and partners like it (CBOS,
  eConnections; TransLink for direct book) — defer, assess in next phase.
  Heavy Sierra/TMAS coupling: if that goes, whole stack + pricing changes.
  Broomfield data warehouse content already in hGP data lake.
- ISO: GMAS→CORE first, then TMAS (separation project); GNAP→GSAP NA (ACI
  consolidation). FICO→UCM: $2.6M/2.5yr budget submitted (gap build, data
  migration, FICO decom).
- Wholesale vs ISO split rationale (for Raji/billing): ISO = two rails
  (GSAP/GMAS + Sierra/TMAS), Indirect = TSYS rails only.

### NA VAS / single-out notes

- **Disputes 4→2→1**: VAP disputes → WDP ~Q4 '26; Merlin→DiMS wave continues;
  DiMS→WDP/"GDS" in the 2–5yr window as processing moves (merchants get the
  target disputes platform "for free"); principle: no bespoke integrations of
  target disputes into non-target processors; trailing chargebacks = temporary
  dual login. Chargeback Help (declining revenue, fire-drill): overlaps
  Ravelin (Ethoca/Verifi, acquired + non-acquired; GDS can never do
  non-acquired) → go-forward assessment owed (John Winstel; ping Kim).
- **VAP thinning**: service enablement + interchange calc onto Core in
  flight; billing/funding onto Core = end-state dependent on transaction-level
  accounting + daily net settlement; VAP → gateway-only within 5yrs (not
  removed); dynamic payouts assumed solved by payouts workstream.
- **Multi-currency on Core**: auth/settle/clear "just an idea in TAM" —
  unowned; FX service should feed Core rates; DCC (Planet today) becomes BIN
  lookup once multi-currency exists; connect Core ↔ FX/DCC workstreams
  (Marcus Lang ↔ Gaseltine); Core resourcing is the constraint (Philip/Kenny
  Garrison; "one big team" needs leadership buy-in + constraint elsewhere).

## RoW (excl. UK&I)

### Asia-Pacific (Lucy Anderson)

- Strategy: exit third parties across the value chain (reseller model today:
  PAX/Ingenico + 7 device software stacks, MPGS+CyberSource gateways,
  third-party installments = ~35% of Asia revenue concentration risk,
  GSAP/GMAS back end, GPAPI front). Fix software foundations over ~12mo
  (to mid-'27), then localize Genius S.
- Onboarding: wave 143029 — Salesforce Experience Cloud → MBS/OmniTracker
  (self-serve), 12–14 days → 2–3 days; MOS AP decom for self-serve early '27;
  sales-assisted path off MOS = "plan for the plan" (Matthew Reily, just
  starting); MBS integrations use MuleSoft/UBA-conformant patterns (rip-and-
  replace safe). UCM prioritized. Micro-merchant vision: download app →
  first softPOS transaction in 20 minutes.
- Markets: Hong Kong (65–70% of AP revenue; third-party solution today,
  blocks Genius), Philippines (JV; BOIPA; JV rules span Ent+Int+SMB; NAP has
  no WP footprint), Macau, Singapore, Malaysia; Taiwan separate (onshoring).
- Genius Mobile (GP Mobile Pay / Yazara softPOS): Philippines launch
  2026-10-30 on PowerZac architecture; fast-follow HK + Macau.
- Payment app: Nucleus + TMS (Karel Jára) for Genius S — in flight; HK/Macau
  Nucleus Q1 '27. Genius S AP = **triPOS + Nucleus** (nucleus shim) — must
  converge Karel's TMS work with hWP stack before back-book migration.
- Data hierarchy cleanup is a pre-migration must: AP created one MID per
  product per merchant (installments) — map old→new model (de Jacquier, Pat
  Bateman, Reily, Vivek huddle).
- Migration path: James Fry segmenting enterprise vs SMB; first movers =
  e-com enterprise merchants without IPP → hWP stack; **IPP on NAP is the
  blocker** (HK IPP ≈30% of revenue); NAP acquiring licenses needed for the 5
  markets (HK first). Secure Acceptance (CyberSource HPP) EOL Jun 2027 —
  Gemma Hammer working Visa extension to Jun 2028. Reuse Rob Ward's UK
  CyberSource-exit pattern. Terminal transition: assess MDM OTA update
  instead of re-terminaling. iNASA boarding amendments (pricing, hierarchy)
  prep. DCC: Planet today; localize into EU DCC solution; may need backward
  compatibility to Planet (scope increase) — Marcus Lang owns global Planet
  agreement. VAS: protect installments revenue, land Genius S, then
  demand-based; DCC continues.

### Poland (Marek)

- E-comm enhancements (consistency, verticals e.g. public sector); VAS
  consistency (Amex dual model → Amex PayFac model; "service pipe" for
  mid-enterprise); all-in-one commerce device (fiscal + POS + terminal app in
  one) per "single provider of commerce solutions" strategy.
- GP Tom in market on e-service payment app rails → converge e-service →
  Nucleus incl. TMS consolidation (2–3 TMSes today).
- **APM quick win: BLIK** — contract + gateway integration already exist on
  GPE stack; leverage for Worldpay gateway with modest work (James Fry).
- Sugar CRM → Salesforce International in 12–18mo (unlocks MBS connectivity).
- **Bilats/least-cost routing**: EU regulation separates scheme from routing;
  Polish bilats route down cheaper networks (win on price); map holistically
  for Europe incl. on-us JV routing — must be preserved in target.

### ERSTE JV (Milan Bednár)

- #1 **Project Frank** — Croatia onto GPE stack; 1 Nov '26 all face-to-face
  clients board the new stack.
- #2 Genius for Czech Republic by Oct '26 — new fiscalization law makes
  fiscalization mandatory; product at par with competition (Gregor Liset).
- #3 Nucleus as the only payment app: today 50/50 Nucleus vs GPE Pay (PayTen);
  gaps block Nucleus for new clients in Slovakia, Austria, Romania. GP Tom
  asset still owned by ERSTE (sale contract unsigned — GP Mobile Pay rename
  blocked).
- Processing: Nucleus→PowerZac→Base24 today; ACI host consolidation = stand
  up PowerZac as auth host; back end MMS→NAP (disputes, multicash etc. hang
  off MMS). Mix: ~8% e-com, 18% VAS, rest in-person.
- E-com: GPE WebPay serves all ERSTE JVs (even some competitors). WebPay vs
  GPECom: APM feature-parity gap + cost model (GPE invoices JVs per feature;
  WebPay cheaper) → enhancements paused. GPECom has no enterprise-grade
  solution — losing large merchants to Adyen, can't compete in RFPs. Fix =
  bring hWP eCom proposition + APM service (GPADS behind GPECom) as the
  migration "carrot" for ACI consolidation. Follow up: Richard J/Keering,
  Mark Hopkins, Rob Wingfield.
- VAS: COMO pilot ~Aug '26 (CZ/HU/SK via P2C terminals; Nucleus integration
  starting; long-term bundled with Genius); spread existing VAS across
  countries.
- Portals: GPE merchant portal + Marketplace today; **SSO for 8 EU regions by
  Oct '26** (Jaemi Bremner). Beyond SSO: do NOT invest in GPE merchant
  portal/reporting — enhance WP Dashboard within MyAccount++ framework;
  portal closure follows NAP back-end migration (NAP ⇒ WP Dashboard by
  default). Exception: public assets (help centers, marketplaces/app stores)
  migrate right after SSO.

### Greece (Dimitris Charaklias — NBG Pay JV)

- GP Tom → Genius Mobile ~Sep/Oct '26 for ~7,000 merchants. Genius
  fiscalization decision pending (Greg Liset call); Greece all-in-one
  fiscalization market is competitive (top-5 POS all-in-one, top-50 softPOS).
- E-com: MPGS + GPECom; GPECom gaps = IRIS (mandatory Greek APM), Greek
  installments, recurring; enterprise gap (two biggest Greek airlines —
  considering Worldpay). Decision needed: continue GPECom feature-parity work
  vs pivot to target payment orchestration (Access payments API) — Dewison/
  Mensah: do parity for named gaps, then pause and converge to GG.
- Estate: Mellon legacy vendor ~200k POSs (direct to e-service); EDPS (100%
  GP-owned) = NBG technical provider + multi-acquiring PSP hub (switching,
  loyalty, crypto, APMs for top retailers); EDPS PayApp → Nucleus is hard
  (custom/localized, fiscalization) — Karel discussions started. GAPS Greek
  host connects to PowerZac (GP Tom + GPECom). Postilion migration (3-yr,
  e-service) just completing. Target: thin EDPS long-term, retain
  hard-to-replace loyalty/in-region capability — little in 18mo (Mensah).
- Boarding: ECBD (e-service boarding; same platform as Poland) ↔ MBS gap =
  manual adds for GPECom; 18-mo roadmap: ECBD → MBS → GPECom → RealControl
  fully automated. Salesforce Greece = lead management only; need full
  pipeline + product + pricing (then MBS connect — mirrors Poland pattern).
  Servicing runs through NBG branches (my NBG → ECBD, ARC Mercury).
- VAS: DCC from Poland's GPE DCC service (via Supercheckout); e-service DCC
  also exists → consolidate on GPE DCC now, combined hGP/hWP DCC later; MCA
  (no dates); COMO with Sklavenitis (largest retailer) not started.

### Coverage gaps / follow-ups (RoW)

- Germany (Commerz Global Pay) — no product lead in seat (Amy recruiting);
  Spain Comercia (Luis Palomero); CSOB JV CZ/HU (white-label GPAPI+GPECom
  resale; Vaclav Kerka). Sessions to be arranged (possibly one combined).
- Australia/NZ: direct SMB book was segmented into Integrated international,
  but needs differ (half of ANZ P&L is SMB direct); ~$10M capex/yr exposure
  staying on current platforms; front-book call = IntegraPay (ISV), back-book
  direct plan TBD (eWay). Lucy ↔ JR to reconcile with Integrated coverage.
- Japan: no hGP SMB presence (James Fry / Simmons if anything).
- India + other geos: check nothing missed (de Jacquier).
