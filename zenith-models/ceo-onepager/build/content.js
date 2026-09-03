// Single source of copy for the one-pager (slide + page). No figures on the page. ~420 words.
module.exports = {
  eyebrow: "AI program  ·  Investment requirements  ·  Emerging themes",
  headline: "Delivering the AI program needs dedicated teams and incremental funding in the tens of millions — and some of the savings will arrive through different routes than expected.",
  subtitle: "Cross-workstream view for discussion  ·  investment cases in build with Finance",

  themes_title: "What we are seeing across workstreams",
  themes: [
    { lead: "Dedicated resourcing is required.",
      text: "None of this can be absorbed by existing teams. Each initiative needs a standing team to build it and a small team to run it. The ask is people as much as money." },
    { lead: "Incremental funding is needed — tens of millions, not single digits.",
      text: "Run costs recur and scale with usage, so the annual bill rises as adoption succeeds; build spend comes on top." },
    { lead: "Spend is front-loaded; value ramps behind it.",
      text: "Build spend lands ahead of benefits, so early periods show cost before savings even for cases with strong steady-state economics. Ramp profiles are being set per initiative with Finance." },
    { lead: "Some savings will not come from the areas expected.",
      text: "Servicing: much of the cost base is outsourced, so savings come through vendor contracts, not in-house headcount. Engineering and Sales: value arrives largely as capacity and acceleration, which count as savings only once Finance agrees how it is captured." },
  ],

  shape_title: "What the investment looks like",
  layers: [
    { name: "Build", tag: "one-time",
      text: "a dedicated delivery team per initiative; platform, integration and data set-up; vendor builds where buying beats building." },
    { name: "Run", tag: "recurring",
      text: "model usage that grows with adoption; subscriptions and vendor support; a small standing team with monitoring and controls." },
    { name: "Enable", tag: "people",
      text: "training and change in the business; adoption champions in engineering; tracking of benefits and of service, quality and loss guardrails." },
  ],

  deps_title: "Dependencies and decisions in flight",
  dependencies: [
    { lead: "Accounting treatment",
      text: "Jamie and Tom are working the capitalization question (build labour and platforms as CapEx vs expensed). It changes P&L phasing, not the underlying economics." },
    { lead: "Funding mechanism",
      text: "Central transformation pool vs business-unit budgets is still open; it decides who carries the build cost and who carries the run cost as it grows." },
    { lead: "Finance engagement",
      text: "Finance is embedded in every case, validating baselines, vendor rates and the approval package. Run-cost inputs (usage, vendor, platform rates) are planning assumptions until usage data and rates land — the inputs most likely to move." },
  ],

  snapshot_title: "Workstream snapshot",
  snapshot: {
    rows: ["Scope", "Where value lands", "Case readiness"],
    cols: [
      { name: "Servicing", cells: [
        "Six — contact avoidance, self-serve, AI-assisted agents, workforce management, back-office automation, non-people cost flow-through",
        "Front- and back-office servicing cost, including outsourced vendor and non-people cost pools",
        "First full case drafted; Finance validating baselines and rates; decision gate this week" ] },
      { name: "Engineering (SDLC)", cells: [
        "Two — AI-driven development (agentic loop engineering), product-lifecycle redesign",
        "Engineering and product capacity",
        "Structured; baselines landing; gate alongside" ] },
      { name: "Sales", cells: [
        "Two — underwriting and pricing for the front book, small-business long tail via partners",
        "Revenue quality and seller capacity",
        "Drivers set; baselines and vendor quotes landing; gate alongside" ] },
      { name: "Risk & Compliance", cells: [
        "Portfolio being consolidated — existing Helix program plus fraud, financial-crime, compliance, credit and collections",
        "Operating cost, third-party spend and transaction loss",
        "Portfolio being refreshed; gate the following week" ] },
    ],
  },

  footer: "Draft for discussion — themes only. Investment cases are being built per initiative with Finance; figures follow once sponsors, Finance and Jamie are aligned.",
};
