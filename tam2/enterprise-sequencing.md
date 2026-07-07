# TAM 2.0 — Enterprise segment sequencing

Source: Enterprise workbook (NA; RoW excl. LATAM). No transcript absorbed for
this segment yet. Consolidated dependencies live in NA col P.

## NA highlights

- **Single-in**: current VAP cnpAPI, RAFT native/ISO, GPAPI, Portico, WPG XML,
  Access WP → Global API on GG hybrid (Access-WPG-VAP) interim → Global API
  target. Build OAuth, publish standards, v2.0 APIs, SDK/plugin adherence.
  Confirm Access→WPG→RAFT pilot before scaling; payouts gaps tied to win/loss
  (gaming); proprietary-protocol unwind aligns with switch/GG roadmap.
  CP: 25% of CP volume on VAP; large merchants (Disney) = high migration
  risk; TriPOS/Nucleus target. CNP: API 2.0 + GG US instance of Access
  (24+ mo); close Access→WPG→RAFT; multi-currency, dynamic payouts, net
  settlement, ACH/e-check, FX all sit under VAP today.
- **Boarding**: manual today (Thermos/NAP, Fast Track/VAP exceptions). Build
  Actor+PIL on UBA w/ GPI as proof point; Helix MVP (CNP Access EMEA); UBA
  OpenEdge MVP; party model/product catalog alignment; HUB target. Resourcing
  is the risk: PM ~3–5 FTE gap; PIL engineering shortfall (payouts, APMs,
  disputes); Helix/UBA contractor funding ends EOY '26. <10% of new business
  uses automated boarding (iNASA); focus so far EMEA, NA must start.
  Experience: Launchpad/Horizon → Ignition (requirements not begun).
  Underwriting: UCM gap-build, FICO decom (limited enterprise upside).
- **Processing**: terminate D2H terminal connections (facilitates GG);
  Enterprise likely stays WPG-VAP through "next" while target rails focus
  RAFT/Core. Acquiring: RAFT↔GIMS for Interac; thin VAP (services, clearing
  → Core under "Helixx"); daily scheme-fee calc + centralized rules engine;
  event-driven scheme cost/fee data; RAFT currency gap (US/CAD only vs VAP
  18) — TBD build of 16 currencies on RAFT/Core; GNAP→GSAP next; Kafka AVRO
  upgrade. Follow-up: Chris/Degiorgio/John (WP) — what must be true to close
  VAP.
- **Sales & servicing**: iNASA ~1% traffic → migrate into hWP Enterprise
  Salesforce; MuleSoft for downstream boarding flows; common SF module for
  HUB integration.
- **VAS**: routing RTR↔PRIME interop explore → Dynamic Routing 2.0; gifts
  Engage+Valutec (RAFT/Core integration capacity is the constraint); Revenue
  Boost 2.0; 3DS Flex integration of hGP MPI; FraudSwitch → FraudSight;
  FX on Core to support VAP thinning (TBD reqs); credential API integrations
  (NTRS, TaaS) + unified credential vault explore.
- **Single-out**: iQ is the enterprise one-stop today (needs UI uplift) →
  MVP Enterprise Portal EOY, MyAccount++ 2027; maintain iQ continuity for
  TJ Maxx/Kroger during uplift; single worldwide Enterprise-portal owner
  (not regional). Reporting: Core→datalake export, hGP reporting layer, MFE
  into portal, SFG replacing EMAF (assess). Billing: Core Billing build
  (transaction-level fees/SURF, EDA events, daily net settlement for TSA
  exit + VAP); consume VAS events from WPG (duplicated in VAP today — noted);
  NAP B&F PoC for NA billing; GMAS/TMAS migration strategies; CORE+ supports
  back book until NAP B&F ready. Payouts: DPO+FAF end-of-sale; front book via
  Access P2X; close US gaps (gaming push-to-card); WPAP parity then target
  WPAP/P2X; Helix Payout Consolidate + Super Ledger back in scope. Disputes:
  WDP. Residuals: gap analysis underway → EPI.
- **Data (shared across segments; copied into Integrated workbook too)**:
  MDM → Reltio (Informatica retire; D&B Marketplace interim); real-time
  ingestion target build (Iceberg, Flink SQL, schema mgmt, NRT + SLOs, ODS
  MVP); data foundational build (11 of 26 domains, dbt Cloud split
  GLOBAL_PROD/WORLDPAY_PROD, CDP→NDP, Caspian→TIDAL); reporting semantic
  layer (retire MicroStrategy, SSRS; use cases: auth exec dashboard,
  Reporting 2.0, Customer 360); data risk/trust (stewardship, lineage,
  Alation↔Informatica); AI (sandbox, AI Gateway MVP, golden path; possible
  Azure retirement).

## RoW (excl. LATAM) highlights

- Single-in current Access/WPG/WPAP/GPAPI → Global API (Access codebase) on
  WPG interim → Global API. Unified prop: EMBOSS feed into Access query DB;
  POS data in Enterprise Portal; phase 2 terminal concentrator → WPG, PayApp
  2.0 → Global API → WPG, WPT back-book migrate/decomm (UK&I corporate
  priority).
- CP: direct-to-SAS, Transxpay, WPT, partners (FreedomPay) → Genius N /
  partners interim → TriPOS/Nucleus + API access point + Supercheckout;
  Tesco/Walmart possible direct-to-acquirer exceptions.
- CNP: slow-develop WPG, move customers to Access; corporate: get off
  Cybersource + MPGS; GMAS EU/AP exit explorations (replicate AP exercise for
  GMAS EU enterprise customers over 18mo; Taiwan needs focused conversation;
  IPP feature gaps; JV single-out work prioritization).
- Boarding = same HUB story as NA (same resourcing risks). CPQ → RCA paced to
  Oracle contract exit. Experience: Launchpad/Horizon/Tuza/Takepayments →
  Ignition (Tuza-vs-Horizon gap analysis needed). Underwriting: manual today;
  UCM fit assessment incl. pKYC (~3mo, underway).
- Processing: GG routing build; thin WPG (behind Access) to 5–0%; converge
  WPT into GG; retain C2.0, APF (LATAM auth), EDPS (Greek networks) for local
  requirements. Switch: SAS/NAP + hGP ACI consolidation, GMAS EU+AP migration
  planning; Base24 MMS → PowerZac; Postillion → PowerZac/NAP next; legal/
  risk/compliance/tax engagement model + acquiring-licensing working group
  (Melissa Perreira legal POC); Helix support = Endava contractors funded to
  Jun '28 (ramp-down question — may retain to accelerate).
- Sales & servicing: Enterprise SF + Siebel(NAP)/VAP servicing → Enterprise
  SF; decouple servicing DBs behind APIs; amendments orchestrated via HUB.
- Payouts: WPAP (AWP front) — decomm APMs out of WPAP, cloud migration
  (elasticity), stop-sell dynamic payouts on VAP, thin reporting/billing/FX
  out of WPAP; confirm payouts as the single banking integration; include
  Marketplaces assets; treasury-management operational support needed.
- Single-out: Enterprise portal for Access (like WPG) + Helix roadmap → MyAccount
  2.0 (MFE = Enterprise Experience Portal). Reporting: follow up w/ Vikrant
  Gupta. Billing: NAP Billing. Disputes: WDP.
- Data: RT events for 18 event types from NAP into lakehouse; EU datalake
  approach explore. Infra: design system consolidation (Worldpay foundation;
  decomm Vega/Index; TSA/access constraints; design-driven migration with
  gates + standards council).
