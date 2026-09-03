# AI & Automation big bets — discussion document (Enrique / Jaime, Fri Sep 4; ELT, Tue Sep 8)

Working-draft deck built from the Sep 2 working-team conversation and the "Enrique Materials" sticky-note storyline.

## Files

| File | What it is |
|---|---|
| `Enrique_AI_Automation_Big_Bets.pptx` | The deck (14 main pages + 7 appendix pages). Speaker notes on every page carry Anshu's talk track and the numbers that are deliberately kept off the page. |
| `Enrique_AI_Automation_Big_Bets.pdf` | PDF export of the same deck for quick review (notes not included). |
| `build.js` | pptxgenjs generator. Edit content here and rebuild; do not hand-edit the .pptx. |
| `render.py` | Renders a .pptx to per-slide PNGs (LibreOffice → PDF → PyMuPDF) for visual QA. |

## Storyline (one storyline serves both sessions)

1. Objectives for today — level-set, no dollars yet
2. Executive summary
3. Where we are — stage gates S1–S5, who has been engaged
4. Pipeline snapshot — ~15 big bets across five areas, RYG in Anshu's words
5. Org change impacts (talk track)
6. How we are resourcing — current model and the build/run archetype (Srini's technology resourcing framework page to be inserted after it)
7. Proposed sequencing methodology — five criteria, tiered investment
8. Sequencing applied — three horizons (illustrative)
9. Investment requirements — themes and observations, no dollars on page
10. Finance engagement and accounting treatment
11. Follow-ups from the CEO/CFO readout — value profile and actions
12. Progress and proofs of concept (ELT page)
13. Next steps and what we need from you
14. Appendix: stage-gate definitions, cost-sizing method, servicing architecture and NPS approach, seller productivity journey, PDLC structure, agenda mapping, glossary

## Guardrails baked in

- No dollar figures or initiative-level investment on any page; they live in speaker notes marked as off-page talking points.
- Pages are written in Anshu's (client) voice, not McKinsey's.
- Every page is stamped "Preliminary — working draft for discussion" and carries a source line.

## Rebuild

```bash
npm install pptxgenjs@3.12.0
node build.js                                   # writes Enrique_AI_Automation_Big_Bets.pptx
python3 render.py Enrique_AI_Automation_Big_Bets.pptx render 100   # optional visual QA renders
```

## Applying the client template

The client PowerPoint template (slide master) was not attached to the request, so the deck uses a neutral consulting palette (deep navy, electric blue accent, Arial). To move it onto the client master: open the template, use Home → New Slide → Reuse Slides (or paste slides with "Use Destination Theme"), then check footers and the title-slide layout. Colours are set explicitly in `build.js` (`C` palette object) and can be swapped for the template's theme colours in one place.
