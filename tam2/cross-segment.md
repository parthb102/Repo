# TAM 2.0 — cross-segment view

## Shared target platforms (~2029) — recur across all three segments

| Capability | Target |
|---|---|
| Single-in API | Global API / API 2.0 (federated build to published spec; OAuth pass-through auth) |
| Payment apps | PayApp 2.0 "Nucleus" (+ triPOS hybrid), Yazara softPOS, Scalefusion+Sightstream TMS/DaaS |
| Developer portal | nGP (net-new experience; hWP+hGP portals decommissioned) |
| Gateway | Global Gateway (locally retained: C2.0, APF LATAM, EDPS Greece tail) |
| Switch | Supercheckout; PowerZac (RoW auth) |
| Acquiring | RAFT (NA auth) / CORE (NA clearing); NAP + PowerZac (RoW); GNAP→GSAP; GMAS/TMAS/Sierra exits |
| Boarding | HUB: Boarding Gateway, Workstream Manager, Party model, Actor/PIL, Kafka, MuleSoft; experience = Ignition (Launchpad+Horizon/Kirby converged); CPQ = RCA; underwriting = UCM (FICO exits) |
| CRM / servicing | iNASA (NA/CAN/UK), ISI "RoW Salesforce" (RoW); enterprise = hWP Enterprise Salesforce |
| VAS | Dynamic Routing 2.0; Engage (gift; decision confirmed over Valutec); COMO (loyalty); Revenue Boost 2.0; FraudSight (Ravelin); 3DS Flex; hWP FX; target DCC (FX + BIN lookup); unified credential vault |
| Single-out | MyAccount 2.0/++ (portal); hGP SMB/partner reporting platform + SFG; CORE+ / NAP B&F (billing); WDP→"GDS" (disputes); WPAP P2X (payouts); EPI/EPPE (residuals) |
| Data | Reltio MDM; resilient real-time ingestion (Iceberg/Flink/Snowflake); semantic layer; NDP/TIDAL (CDP & Caspian retire) |
| Infra | Global Design System (Worldpay foundation + Vega/Index assets) |

## First-mover decisions (cross-segment, from July 2 workshops)

1. **API 2.0 / Global API standards** — publish specs (Alex Dewison/Chris
   Gaseltine); every front door (GPAPI, Access, TAPI, GPECom) conforms; OAuth
   pass-through removes boarding credential debt.
2. **TAPI → TriPOS → Express** (Integrated NA; echoes in SMB) — the single
   integration unlock; every net-new MID routes to Express ASAP; requires
   GCP↔Azure dedicated connection (five-nines NFR, hop count — Andre
   Dubreuil), Meet-in-the-Cloud vs triPOS messaging resolution.
3. **Merchant/MID migration strategy** ("the critical decision point showing up
   everywhere"): Option A migrate merchants to target host with manageable
   attrition vs Option B duplicative throwaway boarding integrations to
   legacy hosts. Gates CP unlock, boarding, servicing, single-out. Matt Downs
   (ELT) wants the book shape to decide trade/migrate/build per portfolio.
4. **Credential/token migration** — all gateways (Edge, Merchantware, Express)
   onto the credential management system; shared tokenization/replication
   service; unified credential vault. Gates every e-com migration.
5. **Boarding API fast-follow** — API 2.0 first release is transactions only;
   boarding + reporting + disputes + merchant-management APIs must land
   Q4 '26/Q1 '27 or partners can't move merchants (biggest partners were sold
   the boarding API).
6. **MDM / master data** — product catalog, pricing catalog, merchant &
   partner hierarchy mastered outside Salesforce (Helix architecture),
   Salesforce reads it. Named first mover in Integrated + SMB sessions.
7. **Sales commission via iNASA** (SMB NA Direct) — gating build for any
   net-new direct merchant on hWP rails; "the $6M question"; needs sizing now.
8. **UCM everywhere / FICO exit** — budget submitted (~$2.6M/2.5yr, ISO tab);
   new scope discovered: Launchpad + iNASA integration, sales AND servicing →
   budget/LOE rework (Jennifer Gebhart).
9. **ACH / eCheck decision** (gates VAP retirement, Payrix gateway stop-sell):
   keep VAP as ACH-only platform vs mirror with Fifth Third ODFI behind Core
   (~$1.4M) vs microservices to ODFI writing back to Core (Gaseltine's
   variant). Workstream led by Lori Sheehan; Soltan/Curtis/Andre + Parth/
   Mario/Christina to help kick off.
10. **Global Gateway decomposition** — dual path: low-volume non-strategic
    gateways (Sterling, SNAP, TXP…) move volume to Express interim now; big
    gateways (Portico, TransIT, Merchantware) do NOT two-hop — decompose into
    shared services (decryption, tokenization) co-evolving NA + RoW into GG.
    Chris Gaseltine owns the decomposition + switch/gateway/host/auth-platform
    taxonomy (Mario to circulate).
11. **Direct-to-host unwind** — terminate D2H integrations (via Supercheckout
    /PowerZac patterns) as predecessor for GG everywhere.
12. **CP migration pattern** — configure merchant in target (data, sales
    profile, boarding) → then OTA terminal/firmware upgrade (no re-terminal,
    no re-papering, no funding-window change). To be formalized 20th/21st;
    applies NA Genius upsell (≈50% of Heartland direct book addressable) and
    AP/EU terminal swaps (MDM OTA assess — de Jacquier).
13. **CRM convergence** — hGP CRM 2/3 decision pending (target beyond
    iNASA-at-launch); RoW: Sugar→ISI, Ezidebit/eWay→ISI; USI+UBA interim ~3
    yrs then iNASA (Lindsay's guidance).

## Recurring themes of asks

- **Cross-company access** (hGP↔hWP contractor onboarding) is blocking staffed
  work *now* (ProPay dev portal team queued 2+ weeks; Belfast teams Q3). JR
  took the action to facilitate a fix.
- **Resourcing/funding**: boarding PM resources (~3–5 people) bottleneck; PIL
  engineering shortfall (payouts, APMs, disputes); Helix/UBA contractor funding
  ends EOY '26 (Endava to Jun '28 with ramp-down); Core team capacity is the
  named constraint for multi-currency and billing work ("one big team" idea
  needs leadership buy-in). Board ask (Jul 24): fund TAM outside feature work;
  investment split by tier (boarding vs API vs gateway vs single-out).
- **Freeze/constrain non-target dev**: UPA feature freeze (formalize Scott
  Moser's informal review), Merlin stop, DiMS minimize, GPE WebPay constrain,
  eWay/Ezidebit critical-maintenance only, KTLO precision (JR: define what
  KTLO means per platform; Tim Held conversation — low/med vulnerabilities
  likely not addressed).
- **Throwaway-work tension**: accept *some* deliberately (Launchpad→Sierra/
  TMAS via UBA while migration runs in parallel; NPC demise precedent = ~3yr)
  but refuse it elsewhere (no target-disputes integrations into non-target
  processors — merchants get WDP "for free" when processing moves; no GPAPI→
  Portico investment if omni requires single back end).
- **Trailing activity / duality**: finite, well-communicated dual-tool periods
  are acceptable (iQ vs InfoCentral, old disputes login for chargeback tail;
  add-location duality needs a focused session).
- **Gateway-level reporting + virtual terminal** must be in the target portal
  (MyAccount++) — <18mo, or duplicate portals persist (Curtis).
- **Partner representation**: partner portals, residuals (EPPE/EPI covering
  platforms + wholesale/indirect reverse rev-share), PFaaS in target designs.

## Open decisions / follow-ups (cross-segment)

- CRM 2/3 decision (hGP consolidation target).
- Reporting target selection (single-out) — in progress.
- VT + gateway reporting placement in new taxonomy.
- Chargeback Help vs Ravelin overlap assessment (GDS can never process
  non-acquired traffic per scheme rules).
- Multi-currency auth/settle/clear on Core — "just an idea in TAM", unowned;
  FX service + DCC (BIN-lookup-only) design depends on it (Marcus Lang ↔
  Gaseltine).
- Residuals: confirm EPPE serves platforms/partners too (David Pritchett +
  Raji); hWP platforms currently on Marketo (Danielle Esma).
- Access readiness for NA SMB e-com: hybrid GG (WPG-backed, sooner, more ops
  complexity) vs wait ~1yr for clean GG→Core.
