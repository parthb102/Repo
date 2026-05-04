(function () {
    const el = document.getElementById("range-slider");
    if (!el) return;

    const minTs = parseInt(el.dataset.min, 10);
    const maxTs = parseInt(el.dataset.max, 10);
    const initAfter = parseInt(el.dataset.after, 10);
    const initBefore = parseInt(el.dataset.before, 10);
    const labelAfter = document.getElementById("label-after");
    const labelBefore = document.getElementById("label-before");
    const limitSel = document.getElementById("limit-select");
    const results = document.getElementById("results");

    const fmtMonth = (ts) => {
        const d = new Date(ts * 1000);
        return d.toLocaleString("en-US", { month: "short", year: "numeric", timeZone: "UTC" });
    };

    noUiSlider.create(el, {
        start: [initAfter, initBefore],
        connect: true,
        step: 86400,
        range: { min: minTs, max: maxTs },
        behaviour: "drag-tap",
    });

    const updateLabels = (vals) => {
        labelAfter.textContent = fmtMonth(parseInt(vals[0], 10));
        labelBefore.textContent = fmtMonth(parseInt(vals[1], 10));
    };

    const fetchResults = (vals) => {
        const after = parseInt(vals[0], 10);
        const before = parseInt(vals[1], 10);
        const limit = limitSel.value;
        const url = `/api/top?after=${after}&before=${before}&limit=${limit}`;
        htmx.ajax("GET", url, { target: "#results", swap: "innerHTML" });
    };

    el.noUiSlider.on("update", updateLabels);
    el.noUiSlider.on("change", fetchResults);
    limitSel.addEventListener("change", () => fetchResults(el.noUiSlider.get()));

    const tsOf = (y, m, d) => Math.floor(Date.UTC(y, m - 1, d) / 1000);
    const presets = {
        "last-year": () => [Math.max(minTs, maxTs - 365 * 86400), maxTs],
        "halloween-2014": () => [tsOf(2014, 10, 1), tsOf(2014, 11, 15)],
        "golden": () => [Math.max(minTs, tsOf(2012, 1, 1)), Math.min(maxTs, tsOf(2018, 12, 31))],
        "all": () => [minTs, maxTs],
    };

    document.querySelectorAll(".presets button[data-preset]").forEach((btn) => {
        btn.addEventListener("click", () => {
            const fn = presets[btn.dataset.preset];
            if (!fn) return;
            const [a, b] = fn();
            el.noUiSlider.set([a, b]);
            fetchResults([a, b]);
        });
    });
})();
