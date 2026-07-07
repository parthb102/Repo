# SMB sequencing (NA) workshop — 2026-07-02, 1:42PM (1h56m)

Present (speaking): Jonathan Rigaud (led), Chris Gaseltine, Mark Hagan, Jerry
Roberts, Jake Bruley, David Pritchett, Raji Sitaram, Jennifer Gebhart, Khali
White, Matthew Reily, Vivek Pujeri, John Winstel, Marcus Lang, Michael de
Jacquier, Nana Yaa Mensah, Stuart Taylor, Parth Bahl, Dejan Cusic.

Context: JR walked ELT through TAM 2.0 on ~Jun 30; ELT wants now/next/later.
Anything not on the sequencing page → start/stop/continue challenge. Channels
covered: Direct (Heartland + EVO + legacy-TSYS), Wholesale, ISO, Indirect.

## Direct

- **Sales commission via iNASA is the gating first mover** for net-new direct
  merchants on hWP rails (+ OMS/USI gap closure). Confirmed by CRM/servicing
  (Pritchett synced Lindsey; Khali). Sizing = "the immediate thing"; Chris:
  "the $6M question". Wholesale Genius-TriPOS work provides the rails; direct
  is blocked only on comp.
- Migration bias: EVO + TSYS-direct first; Heartland later (Passport
  same-day batch close; HCSDB complexity; Core ≠ Passport parity near-term).
- **Add-location duality** (Jerry/Jake/Hagan): manual push of location adds to
  hWP rails means two reporting tools (iQ + InfoCentral), two IVRs — OK only
  if the window is finite and defined → focused session on "what does
  add-location mean". Jaemi/Maegan systematically migrating InfoCentral users.
- **Gateways**: Sterling/SNAP/TXP → decomm; move ALL their volume to Express
  (regardless of feature gaps) / TXP already underway. Portico/TransIT
  persist; "late next" decision. Genius team must know: new integration =
  TriPOS→Express (or interim-interim GG). Chris: need the interim or wait
  two years.
- **Genius reboarding pattern**: Portico-upsold Genius merchants = migration
  campaign via reintegration later (2yr+, Chris). Julie's analysis: ~50% of
  Heartland direct book (target MCCs) addressable for Genius. Hagan: enable
  "Genius for the masses" — every customer becomes a Genius customer from day
  one w/ upgrade path (phone → line-buster → countertop). de Jacquier: once
  on correct acquiring rails, everything after is upsell — no reboarding;
  OTA terminal upgrade ("reboot → upgrade to Genius"). Pattern = configure
  data/sales profile in target first, then upgrade device. To be principled
  at Jul 20–21 as THE card-present migration pattern.
- **CNP/e-com**: today GPAPI (front book) + Portico/third-party. Choices
  (Chris): (a) early Global API via **hybrid GG** (WPG-backed; more boarding/
  ops complexity), (b) wait ~1yr → clean GG direct to Core, (c) interim GPAPI
  →Portico then switch. Omni requirement (one back end, one data feed,
  mix-and-match channels) likely rules out GPAPI→Portico. **Ask for Jul
  20–21: requirements doc for hGP direct customers — e-com-only vs omni vs
  Genius-only personas** (we know Genius; e-com/omni gaps unknown). Access:
  live for Enterprise NA, not SMB-ready; Access→RAFT in test (Nana Yaa).
- Khali: ignore VAP for SMB servicing purposes (Chris), payfac stack (MPM)
  out of scope here.

## Wholesale

- Genius S TriPOS/Express integration underway = the pilot channel; R+N
  piggyback. **UPA**: freeze features (formalize Scott Moser's informal
  review — Stuart Taylor), stabilize only, shift resources to Nucleus.
- **Boarding**: Launchpad ≈ parity with Base except Sierra/TMAS rails.
  Decision: **Launchpad + UBA opens the Sierra/TMAS pipe** (Pritchett prefers
  Helix/UBA over tactical point-to-point) while merchant migration runs in
  parallel (migration >1yr anyway; NPC demise precedent ≈ 3yr across iNASA/
  servicing/pricing/portals). Get everyone on Launchpad even if partially
  throwaway. Kill: MAP, Central Station (CPA?), MEA, MerchantFlo, OnTrak;
  Base elements assessed; ID Gen → pick a comparable service.
- **Residuals/pricing** (Raji + Pritchett): EPI/EPPE = target; Base, Central
  Station (+ MEA?) run own residual calc/statements → EPI parity + absorb;
  underlying billing must feed EPI (billing produces bills even for
  indirect); reverse rev-share nuances (funding, invoicing) — **Raji
  workshops before Jul 20**.
- **UCM** (Jennifer Gebhart): FICO→UCM budget submitted, top priority; UCM
  integrated for Base/Cayan today; NOT in Genius S wholesale path; new scope:
  Launchpad + iNASA, sales AND servicing → re-scope budget/LOE.
- **Servicing** (Khali/Pritchett): target = iNASA (already supports referral
  banks, ISO/bank partner management). Base servicing paused; resume = ~1yr
  bridge (mid-'27 full) — is it a bridge worth doing vs converge direct?
  **Perspective needed by end of July**; capability assessment ("the 10
  things") to map Base plans → iNASA gaps; requirements exist (Jason Ohlson,
  Nicole, Drew Chamberlain). Key decision: servicing touches Sierra/TMAS vs
  merchants migrate first (chicken-and-egg w/ Michelle Young's requirements
  ask). Jake: assess persona-based (partner/sales/merchant/ops experiences),
  not portfolio-based; Khali: end-to-end incl. telephony (→ Genesys).
- FY27 assess: Central Station / OnTrak / MAP servicing convergence to
  target-state servicing (OnTrak "does everything" incl. orchestration).

## Indirect / ISO

- Last movers. Express+MMS rails; CBOS + eConnections well-liked (Lori
  Sheehan emphasized), TransLink for direct book; no target alternative
  defined — defer, next-phase assessment ("keep it, plug it in elsewhere"
  hypothesis). Heavy Sierra/TMAS coupling: if rails change, stack + pricing
  change; Broomfield DW data already in hGP data lake — structures understood.
- ISO = two portfolios (GSAP/GMAS + Sierra/TMAS); Indirect = TSYS rails only
  (answering Raji's billing split question). All aligned: interim target =
  **RAFT + Core** (acknowledged assembler/COBOL "intermediary target").

## VAS / disputes / cross-cutting

- **Disputes 4→2→1** (John Winstel): platforms today WDP, DiMS, Merlin, VAP;
  VAP→WDP targeted ~Q4 '26; Merlin→DiMS wave continues (5→2 consolidation
  is right regardless); do NOT integrate target disputes into every
  processing path — merchants get WDP "for free" when processing lands on
  target rails (Chris confirms: new login + URL); trailing chargebacks =
  temporary dual login (acceptable); CB911 sunsetting into new disputes
  platform (Sunny Tucker to confirm; John pings Kim).
- **Chargeback Help**: revenue declining, pressure to integrate into Merlin
  (non-target — conflict); GDS supports RDR + Verifi (Ethoca in build) but
  can never process non-acquired traffic (scheme rules); Ravelin overlaps
  (Ethoca/Verifi alerts secondary to fraud) → **go-forward assessment: CB
  Help vs Ravelin** (John).
- **VAP thinning** (Chris): in-flight = service enablement + interchange calc
  onto Core (long burn; multi-currency clearing deps); billing/funding onto
  Core = horizon goal after transaction-level accounting + daily net
  settlement; VAP = gateway-only in 5yr proposal (not removed); dynamic
  payouts assumed solved by payouts workstream. JR: ensure every VAP-thinning
  value drop (auth/clearing, dynamic payouts, ACH/eCheck, FX, multi-currency)
  is mapped somewhere.
- **Multi-currency on Core** (Marcus Lang ↔ Chris): build MC auth/settle/
  clear on Core; Core calls FX service for rates; DCC service then = BIN
  lookup only (don't replicate); today Planet does DCC on Core; "just an
  idea in TAM — no one looking at it"; Core resourcing must be sorted first
  (Philip + Kenny Garrison; "one big team" needs leadership buy-in +
  constraining dev elsewhere).

## Wrap (JR)

First movers crystallizing: payment apps (cross-segment #1), API 2.0
standards, boarding in aggregate (Kirby self-serve plan, iNASA plumbing, UBA
interim, UCM everywhere, activation/fulfillment), GG dual path (low-volume →
Express now; big gateways 2yr+ decomposition), D2H unwind via Supercheckout
(predecessor for GG), merchant-migration prioritization precedes processing
convergence, boarding+servicing move together (CP/CNP/omni capability
mapping), CRM (integrated partners + iNASA sales comp), no-regrets 5→2
consolidations, billing/residuals decoupling (Raji). Next: summarize, first
movers + overlap across segments, key activities to start before Jul 20–21;
20–21 = interdependency sequencing on the meaty areas; then start/stop/
continue on everything else.
