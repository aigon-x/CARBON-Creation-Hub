(() => {
  const root = document.querySelector("[data-live-proof]");
  if (!root) return;

  const queryInput = root.querySelector("[data-proof-query]");
  const statusSelect = root.querySelector("[data-proof-status]");
  const statusLine = root.querySelector("[data-proof-status-line]");
  const results = root.querySelector("[data-proof-results]");
  const sourceUrl = "https://github.com/amillimatrix-eng/CARBON-Creation-Hub/blob/main/evidence/index.json";
  let records = [];

  const addText = (parent, tag, text, className) => {
    const node = document.createElement(tag);
    node.textContent = text == null || text === "" ? "Not recorded" : String(text);
    if (className) node.className = className;
    parent.appendChild(node);
    return node;
  };

  function render() {
    const q = (queryInput.value || "").trim().toLowerCase();
    const selected = statusSelect.value;
    const filtered = records.filter((r) => {
      const state = String(r.T10_PASS || r.status_freshness || "UNKNOWN").toUpperCase();
      const searchable = [
        r.evidence_id, r.capability, r.interview_safe_explanation,
        r.T10_ACTUAL, r.T10_REMAINING_GAP, ...(Array.isArray(r.tags) ? r.tags : [])
      ].filter(Boolean).join(" ").toLowerCase();
      const statusMatch = selected === "ALL" || state.includes(selected);
      return statusMatch && (!q || searchable.includes(q));
    });

    results.replaceChildren();
    if (!filtered.length) {
      addText(results, "p", "No public-safe evidence record matches this query and status filter.");
      return;
    }

    filtered.forEach((r) => {
      const card = document.createElement("article");
      card.className = "detail-card";
      addText(card, "p", r.evidence_id, "kicker");
      addText(card, "h3", r.capability);
      addText(card, "p", "Result: " + (r.T10_PASS || "STATUS NOT RECORDED") + " · Freshness: " + (r.status_freshness || "UNKNOWN") + " · Evidence date: " + (r.date_version || "Not recorded"));
      addText(card, "p", r.interview_safe_explanation);
      if (r.T10_ACTUAL) {
        addText(card, "h4", "What the evidence shows");
        addText(card, "p", r.T10_ACTUAL);
      }
      if (r.T10_REMAINING_GAP) {
        addText(card, "h4", "Boundary / remaining gap");
        addText(card, "p", r.T10_REMAINING_GAP);
      }
      const link = document.createElement("a");
      link.href = sourceUrl;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.textContent = "Inspect public-safe evidence index";
      card.appendChild(link);
      results.appendChild(card);
    });
  }

  queryInput.addEventListener("input", render);
  statusSelect.addEventListener("change", render);
  statusLine.textContent = "Loading the published evidence index…";

  fetch(root.dataset.source || "../../evidence/index.json", { cache: "no-store" })
    .then((response) => {
      if (!response.ok) throw new Error("Evidence index request failed");
      return response.json();
    })
    .then((payload) => {
      records = (Array.isArray(payload.records) ? payload.records : []).filter((r) =>
        r && r.visibility === "HOUSE" && r.evidence_id && r.capability && r.interview_safe_explanation
      );
      statusLine.textContent = records.length
        ? "Evidence index loaded. " + records.length + " explicitly public-safe records are available; per-record dates and limits remain visible. This is not a live CRM, payment-rail or buyer-response connection."
        : "The evidence index loaded, but no records explicitly marked HOUSE were available. No fallback data was substituted.";
      render();
    })
    .catch(() => {
      records = [];
      statusLine.textContent = "Live-proof mode is unavailable because the published evidence index could not be read. No cached or fallback records are being presented.";
      results.replaceChildren();
    });
})();