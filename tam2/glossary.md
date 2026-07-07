# TAM 2.0 — glossary (platforms & acronyms)

Definitions come from context in the absorbed materials; entries marked (?)
are inferred and unconfirmed. hGP = heritage Global Payments; hWP = heritage
Worldpay.

## Programme terms

| Term | Meaning |
|---|---|
| TAM / TAM 2.0 | Target architecture model — the post-merger target-state platform map (expansion never spelled out in materials; spoken as "target architecture model/module") |
| Boulder / Rock | Capability family / sub-capability rows in the sequencing grids |
| Now / Next | Build-migrate-decomm horizons: now → interim (~H2 '27) → next → target (~2029) |
| Front book / back book | New sales vs existing merchant portfolio |
| First mover | A decision/build that unlocks dependent decisions (JR's framing) |
| KTLO | Keep the lights on — JR wants precision about what it means per platform |
| Single-in / Single-out | One integration front door / one merchant-partner experience |
| WAVE | hGP investment/initiative intake system (wave cases, L1–L3 stages) |
| TSA | Transition services agreement (FIS-related exits) |
| Project Carbon | UK data-centre closure programme (Evo/e-service exit supports it) |
| Project Frank | ERSTE JV: bring Croatia onto the GPE technology stack (1 Nov '26) |
| BFS data programme | Homogenised data/statements workstream referenced in back-book principles |
| Wave 180243 | Initiative whose resources now target Edge & Merchantware → Express paths (Belfast teams) |
| Wave 143029 | AP automated-onboarding initiative (Salesforce Experience Cloud → MBS) |
| CRM 2/3 decision | Pending decision on hGP CRM consolidation target beyond iNASA-at-launch |

## APIs / single-in

| Term | Meaning |
|---|---|
| Global API / API 2.0 | Target unified API standard across all front doors; OAuth pass-through |
| GPAPI / GP-API | hGP API (SMB/enterprise front door) |
| Access (Worldpay) | hWP modern eCom API/gateway; "Access→WPG→RAFT" pilot path |
| TAPI | hGP integrated/platforms API (incl. Meet-in-the-Cloud, Payfields) |
| MitC | Meet-in-the-Cloud — cloud terminal-messaging infrastructure (websocket + matchmaking) |
| Payfields | hGP hosted-fields product (single-use token service + iframes + JS) |
| HPP / OEHP / TUI / HPV3 | Hosted payment pages (hWP HPP; OpenEdge Host Pay; Transaction UI; legacy HPP) |
| PBL | Pay-by-link engine |
| GPECom | hGP eCommerce gateway (RoW) |
| GPE WebPay | GPE gateway used by ERSTE JVs (cheaper per-feature invoicing than GPECom) |
| eProtect | hWP eCom tokenization/hosted capture (Vantiv heritage) |
| nGP Developer Portal | Net-new target developer portal |

## Gateways / processing

| Term | Meaning |
|---|---|
| Global Gateway (GG) | Target gateway; decomposes into shared services behind a payment-request API; "hybrid GG" = WPG-backed interim |
| WPG | Worldpay Gateway (hWP eCom gateway; being thinned) |
| VAP | hWP NA platform (eCheck/ACH, 18 currencies, dynamic payouts, FX, disputes); NA-only; being thinned to gateway |
| RAFT / Core | hWP NA auth switch / clearing-settlement (target NA rails; assembler/COBOL "intermediary target") |
| Express | hWP integrated gateway + boarding (MMS) — NA interim consolidation point |
| TriPOS | hWP CP integration middleware/SDK |
| Portico, TransIT, Merchantware, Edge (OpenEdge), Sterling, SNAP, TXP, Innovo, Mercury Pay | hGP/hWP legacy gateways (TXP/Sterling/SNAP/Innovo decomm now; Portico/TransIT persist pending GG) |
| XiPay | Third-party enterprise gateway in Enterprise NA current state |
| GSAP / GMAS | hGP auth host / merchant accounting-settlement (incl. EU & AP instances; exits via CORE migration) |
| Sierra / TMAS | legacy-TSYS front-end host / merchant accounting system ("L-TSYS" rails) |
| GNAP | hGP NA auth platform instance → GSAP NA (ACI consolidation) |
| Exchange / NWS / Passport | hGP acquiring/funding & settlement systems (Passport same-day batch close must be preserved) |
| HCSDB | Heartland core system/database ("mousetrap"/"ball of yarn" of comp, fee rules) |
| NAP | hWP RoW acquiring platform (New Acquiring Platform (?)); target RoW back end |
| SAS | hWP RoW auth switch (paired with NAP) |
| PowerZac | Target RoW auth switch/host (ACI Base24/Postilion exits onto it) |
| Supercheckout | Switch/protocol-conversion layer (legacy protocol mapping, D2H unwind) |
| Base24 / Postilion | ACI switch products being consolidated (exit by 2029 corporate priority) |
| EDPS | Greek 100%-GP-owned technical provider + multi-acquiring PSP hub (auth for Greek networks; retained tail) |
| GAPS | Greek host connecting GP Tom/GPECom to PowerZac |
| Highlander | hGP Oceania settlement/back office (eWay stack) |
| Cuscal | AU third-party processor for eWay auth (exit ⇒ ~$1.7M/yr savings) |
| Olympus | Oceania switch to schemes (→ WPG → NAP assess) |
| MPGS / CYbs | Mastercard Payment Gateway Services / CyberSource (third-party gateways being exited) |
| Secure Acceptance | CyberSource hosted checkout (EOL Jun '27; Visa extension to Jun '28 sought) |
| RS2, FEVO/BEVO | LATAM processing platforms (Enterprise current state) |
| APF | LATAM auth platform retained for local requirements |
| C2.0 | Platform retained for local requirements (RoW) |
| Transxpay / WPT | hWP RoW CP gateway / Worldpay Total UK CP stack (WPT decomm) |
| EMBOSS | UK CP gateway under Genius (DCC source today) |
| IPP | Installment payment plans (AP; ~30% of HK revenue; NAP gap) |
| LCR | Least-cost routing |
| D2H | Direct-to-host integration (to be unwound) |

## Boarding / CRM

| Term | Meaning |
|---|---|
| HUB | Target boarding architecture: Boarding Gateway, Workstream Manager, Product/Party model, Actor & PIL, Kafka, MuleSoft |
| PIL | Platform integration layer (fulfillment connectors to hosts, e.g. Edge GW, GSAP, GMAS) (?) |
| UBA | Unified boarding application (hWP; interim orchestration; opens Sierra/TMAS pipe) |
| USI | US Salesforce instance aka H-Corp (GPI consolidates into it Sep 21 '26) |
| GPI | hGP Salesforce instance being consolidated into USI |
| iNASA | Target Salesforce CRM+servicing for NA/CAN/UK (integrated N.A. Salesforce (?)) |
| ISI | International (RoW) Salesforce instance — "RoW Salesforce" |
| iSI/hPOS/Atlas/OMS | Other hGP CRM/order systems converging into iNASA |
| Launchpad / Horizon / Kirby / Tuza / Takepayments / Agent Hub | Boarding/partner experiences converging into Ignition |
| Ignition | Target boarding experience (Launchpad + Horizon/Kirby convergence) |
| Helix | hWP boarding modernization programme (MVP = CNP Access EMEA); Helix architecture = master data outside Salesforce |
| MBS / OmniTracker | RoW boarding activation & orchestration layer (AP, Greece) |
| MOS AP | Legacy AP boarding intake (decom path needed; self-serve exits early '27) |
| ECBD / CBD | e-service boarding/back-office (Poland & Greece; same platform) |
| ARC Mercury / Hermes | RoW servicing/onboarding systems (Poland/Greece) |
| OnTrak / MAP / Central Station / MEA / Base / ELAPP / MerchantFlo / DES / Genesis / SEAT / Client Manager / WebTops / Onboard / Instant Boarding / Flex | hGP NA boarding/servicing/CRM estate to converge (MAP orchestrates Central Station; OnTrak orchestrates ELAPP/Base) |
| ID Gen | MID-generation service (Base team) — pick one vs comparable |
| CPQ → RCA | Oracle/Salesforce CPQ estates → RCA (Revenue Cloud Advanced (?)) |
| UCM | Target credit/underwriting case management (FICO replacement; ~$2.6M/2.5yr budget) |
| FICO | Legacy underwriting rules engine being exited |
| pKYC | Perpetual KYC |
| CDD | Customer due diligence |
| Thermos / Fast Track | Automated boarding exceptions (NAP / VAP) |
| StoreBuilder / EdgeBuilder | OpenEdge boarding tools (EOL at Sep cutover) |
| CBOS / eConnections / TransLink / Jarvis / PPM | Indirect/ISO partner back-office, portals, pricing (CBOS Risk 3.0, PPM licensable) |

## VAS / single-out

| Term | Meaning |
|---|---|
| EFE | Embedded finance engine (hWP) |
| Fee Assist | Surcharging VAS (state-level MCC logic partly on Core) |
| RTR / PRIME | hGP routing microservice / hWP dynamic-debit-routing ML — converge into Dynamic Routing 2.0 |
| Revenue Boost (RB 2.0) | hWP managed optimization microservice → single orchestration API |
| Engage / Valutec / Premier / OptiCard / xGift | Gift platforms — Engage confirmed target (Valutec interim), Premier migrates, xGift/OptiCard exit |
| COMO | Loyalty target (pilots: ERSTE ~Aug '26; Greece w/ Sklavenitis planned) |
| FraudSight / FraudSwitch / Ravelin | Fraud target (Ravelin-powered) / integration microservice |
| 3DS Flex | hWP 3DS service (Cardinal + Ravelin MPI) |
| DCC | Dynamic currency conversion (target = FX + BIN lookup; Planet third-party today in AP; GPE DCC in PL/Greece) |
| Planet | Third-party DCC provider (global agreement — Marcus Lang) |
| BLIK | Polish APM (contracted; quick win) |
| IRIS | Greek mandatory APM (instant payments) |
| GPPaaS / GPADS | hGP APM services (GPADS sits behind GPECom) |
| NTRS / TaaS | hGP token provisioning services integrating to Credential API |
| Credential API / unified credential vault | hWP credential management target (token vault consolidation) |
| OmniToken / PASS Token | hGP token schemes (support/maintain) |
| iQ | hWP portal (enterprise one-stop; SMB variant) |
| MyAccount / MyAccount++ / 2.0 | hGP portal → unified target portal/shell (must cover MX/PX/gateway reporting + VT) |
| WP Dashboard | hWP SMB portal (MFE into MyAccount) |
| InfoCentral | Heartland reporting portal (converges w/ iQ) |
| EMAF | hGP report file feed (SFG replacement assess) |
| SFG | Secure file gateway (target file delivery) |
| Pazien | Reporting/reconciliation intelligence direction (Integrated) |
| WDP / DiMS / Merlin / CB911 / GDS | Disputes: Worldpay Disputes Platform (north star, rename → Global Dispute System); hGP DiMS interim; Merlin→DiMS; chargebacks911 sunsetting; GDS cannot process non-acquired traffic |
| Chargeback Help | Acquired asset (Ethoca/Verifi alerts incl. non-acquired); overlaps Ravelin — assessment owed |
| WPAP / P2X / DPO / FAF | hWP payouts platform / push-to-anything target / Dynamic Payouts + Fast Access Funding (end-of-sale) |
| EPPE / EPI | Enterprise Partner Payments Engine (hWP residuals target; "EPI" used interchangeably) |
| Marketo | Used for hWP platforms residuals today (Danielle Esma) — to confirm EPPE coverage |
| Aperia | Oceania residuals (support/maintain) |
| NAP B&F | NAP billing & funding (target billing; NA PoC) |
| CORE+ | Core billing supporting back book until NAP B&F ready |
| ZSFK | e-service billing system (UK&I/PL current state) |
| SURF | Fee-data standard for transaction-level billing (?) |
| MCA | Merchant cash advance |
| VT / MX / PX | Virtual terminal / merchant experience / partner experience |
| EPPE gaps | Base / Central Station / MEA residuals to absorb |

## Payment apps / devices

| Term | Meaning |
|---|---|
| Nucleus / PayApp 2.0 | Target payment application (triPOS hybrid); replaces UPA, e-service, NerPay, EDPS app, GPE Pay, PayTen/Printec, P2C etc. |
| UPA | hGP universal payment app (freeze + stabilize; migrate to Nucleus) |
| GP Tom / GP Mobile Pay / Genius Mobile | GPE softPOS app (rename blocked — asset still ERSTE's); Yazara-based target |
| Yazara | SoftPOS provider in target stack |
| Genius S / N / R | Genius POS proposition variants (S≈standalone/smart; N/R per-market/native/retail variants; value drops 1.0–5) |
| GP1 / Moby 5500 / GC26 | Devices in Genius value drops |
| Scalefusion / Sightstream | Target TMS/DaaS (deployment-as-a-service) |
| TMS / MDM (devices) | Terminal management system / mobile device management (OTA updates avoid re-terminaling) |
| RCM / XCharge / Cayan terminal app / UCI | hGP deployed apps routing through TAPI; Cayan gap = on-device store-and-forward |
| WP360 | Omnichannel hospitality proposition (Ireland GA Q3 '26) |
| OCPI | EV-charger protocol opportunity (Greece) |

## Data / infra

| Term | Meaning |
|---|---|
| Reltio / Informatica | Target MDM / legacy MDM (retire) |
| Party model | hWP customer/merchant hierarchy master (target ops data) |
| NDP / CDP / TIDAL / Caspian | Data platforms: hWP CDP→NDP; hGP Caspian→TIDAL |
| EDIA | hWP Kafka estate (event data) (?) |
| Databolt | Tokenization platform (interim data stack) |
| dbt Cloud / GLOBAL_PROD / WORLDPAY_PROD | Transform tooling / split Snowflake databases |
| Iceberg / Flink | Lakehouse materialization / stream-transform standard |
| Alation | Data catalog (↔ Informatica migration prep) |
| GSI + Azure B2C | Unified identity for portals (SSO) |
| Vega / Index | Design systems being folded into the Worldpay-based Global Design System |
| Genesys | Target telephony (servicing) |

## People (as referenced in these materials)

JR = Jonathan Rigaud (TAM 2.0 sequencing lead). Named leads/owners: Chris
Gaseltine (gateways/GG/acquiring taxonomy), Alex Dewison (single-in/API),
Alan Johnson (single-out), Soltan Nayabkhil + Curtis Landry (Integrated
platforms), Matt Downs (ELT platforms), Lindsay/Lindsey (CRM), Maegan
Cardillo (boarding/Salesforce consolidation), Matthew Reily (UBA/Helix
boarding), Vivek Pujeri (RoW Salesforce/MBS), David Pritchett (Launchpad/
partner boarding + EPI w/ Raji), Raji Sitaram (billing/residuals EPI),
Jennifer Gebhart (UCM/FICO), Khali White (servicing), Jake Bruley (partner
experience), Mark Hagan (SMB NA business), Jerry Roberts (product), John
Winstel (VAS/disputes), Marcus Lang (FX/DCC/Planet), Michael de Jacquier
(architecture/terminals), Nana Yaa Mensah (target-state/EDPS), Stuart Taylor
(payment apps/UPA), Scott Moser (UPA dev review), Lucy Anderson (RoW SMB/AP),
Karel Jára (Nucleus/TMS), Jaemi Bremner (portals/SSO), Milan Bednár (ERSTE),
Marek (Poland), Dimitris Charaklias (Greece/NBG), Eyal Mor (COMO), James Fry
(AP enterprise/APM), Gilbert (Genius AP), Gregor/Greg Liset (Genius CZ/
Greece), Rob Ward (UK CyberSource exit), Gemma Hammer (schemes/Visa), Ryan
Heaton + Himanshu (data platform), Mario Gonzalez Madrid + Parth Bahl +
Christina + Dejan Cusic (programme/consulting team), Melissa Perreira
(legal), Lori Sheehan (ACH lead; also CBOS/eConnections context), Mike Clark
(ACH sponsor), Tim Held (KTLO/vulnerabilities), Kenny Garrison + Philip
(Core resourcing), Michelle Young (servicing requirements), Julie (Heartland
direct Genius analysis), Danielle Esma (platforms residuals/Marketo), Charlie
Southgate (gift decision), Vikrant Gupta (RoW reporting), Alan Irwin (eWay
TAM 1.0 mapping), Amy/Ami Mehta (Germany), Luis Palomero (Spain/Comercia),
Vaclav Kerka (CSOB), Nick Collins (AP commercialization), Pat Bateman
(hierarchy/MDM), Jamie/Jaemi + Maegan (InfoCentral migration), Sunny Tucker
(chargebacks 911), Kim (chargeback product), Steve Stidhem, Karin Woodard,
Andre Dubreuil (WP architecture), Joanne Lee, Daniel McDowell, Anushree
Kolhe, Nick Corrigan (MBR/CRM), Matt L., Sean M., Max B. (design), Snjezana/
Milton (WAVE governance), Jamie Bremner started SMB RoW #1 transcription.
