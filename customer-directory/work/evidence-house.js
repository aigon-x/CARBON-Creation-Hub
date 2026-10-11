(() => {
  "use strict";

  const config = {
    "EVID-COMMERCIAL-001": {
      category: "commercial",
      label: "Commercial",
      title: "Commercial leadership and strategic accounts",
      sourceNote: "Public-safe claim record. Primary source material remains controlled."
    },
    "EVID-CARBON-001": {
      category: "commercial",
      label: "Commercial",
      title: "Creative production and controlled delivery",
      sourceNote: "Controlled sample access is recorded; this does not prove buyer acceptance, conversion or payment."
    },
    "EVID-BUILD-DELIVERY-001": {
      category: "build",
      label: "Build delivery",
      title: "Evidence-governed product delivery",
      sourceNote: "The build record is bounded; it does not establish buyer acceptance or payment.",
      links: [
        { label: "Search first-cycle record", href: "https://github.com/amillimatrix-eng/CARBON-Creation-Hub/issues/16" },
        { label: "Public-safe proof stack", href: "../../public-evidence/AMX_PROOF_STACK_20261011.svg" }
      ]
    },
    "EVID-DEMONSTRATOR-001": {
      category: "systems",
      label: "Systems / AI",
      title: "Bounded execution-state and safety tests",
      sourceNote: "Results apply to the declared fixtures and retained events only; not a universal reliability score.",
      links: [
        { label: "Public-safe proof stack", href: "../../public-evidence/AMX_PROOF_STACK_20261011.svg" }
      ]
    },
    "EVID-OVERDRIVE-001": {
      category: "systems",
      label: "Systems / AI",
      title: "Evidence-led commercial workflow",
      sourceNote: "Historical execution provenance; this card does not claim current scheduled autonomy or current revenue."
    },
    "EVID-T10-001": {
      category: "governance",
      label: "Governance",
      title: "Outcome-truth controls",
      sourceNote: "The artifact defines the control; propagation across every producer and consumer remains unproven."
    },
    "EVID-IRIS-001": {
      category: "systems",
      label: "Systems / AI",
      title: "IRIS / MiCase presentation surface",
      sourceNote: "Current deployment and source/hash verification remain on HOLD; no current implementation claim is made."
    }
  };

  const form = document.getElementById("evidence-search-form");
  const queryInput = document.getElementById("evidence-query");
  const categoryInput = document.getElementById("evidence-category");
  const status = document.getElementById("evidence-status");
  const results = document.getElementById("evidence-results");
  const indexUrl = "../../evidence/index.json";
  let records = [];

  if (!form || !queryInput || !categoryInput || !status || !results) return;

  const text = (value) => typeof value === "string" ? value : "";
  const normalize = (value) => text(value).toLocaleLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
  const categoryPriority = (category) => ({ commercial: 0, build: 1, systems: 2, governance: 3 }[category] ?? 4);

  function recordSearchText(record, meta) {
    const translation = record.market_translation || {};
    return normalize([
      record.evidence_id, record.capability, record.artifact, record.date_version,
      record.status_freshness, record.acceptance_test, record.interview_safe_explanation,
      record.T10_REMAINING_GAP, meta.title, meta.label, meta.category,
      translation.recruiter_safe, translation.buyer_safe, ...(record.tags || [])
    ].join(" "));
  }

  function make(tag, className, value) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (value !== undefined) node.textContent = value;
    return node;
  }

  function addLinkList(card, meta) {
    const links = Array.isArray(meta.links) ? meta.links : [];
    const source = make("div", "evidence-source");
    source.appendChild(make("strong", "", "Evidence pointer: "));
    source.appendChild(make("span", "", text(card.dataset.evidenceId)));
    if (meta.sourceNote) source.appendChild(make("p", "evidence-source-note", meta.sourceNote));
    if (links.length) {
      const list = make("ul", "evidence-source-links");
      links.forEach((item) => {
        const li = make("li");
        const a = make("a", "", item.label);
        a.href = item.href;
        a.rel = "noopener noreferrer";
        if (/^https?:/.test(item.href)) a.target = "_blank";
        li.appendChild(a);
        list.appendChild(li);
      });
      source.appendChild(list);
    }
    return source;
  }

  function renderCard(record, meta) {
    const card = make("article", "evidence-result-card");
    card.dataset.evidenceId = text(record.evidence_id);
    const heading = make("h3", "", meta.title);
    const badge = make("span", "evidence-category", meta.label);
    const top = make("div", "evidence-result-top");
    top.appendChild(heading);
    top.appendChild(badge);
    card.appendChild(top);

    const freshness = text(record.status_freshness) || "UNKNOWN";
    const pass = text(record.T10_PASS).toUpperCase();
    const hold = pass !== "PASS" || /HOLD|REMEDIATE|UNKNOWN/i.test(freshness);
    const statusLine = make("p", "evidence-status-line");
    statusLine.appendChild(make("strong", "", "Status: "));
    statusLine.appendChild(make("span", hold ? "evidence-pill hold" : "evidence-pill pass", hold ? "HOLD" : "PASS"));
    statusLine.appendChild(make("span", "evidence-freshness", "Freshness: " + (text(record.date_version) || "Not dated") + " · " + freshness));
    card.appendChild(statusLine);

    card.appendChild(make("p", "evidence-result-summary", text(record.interview_safe_explanation) || "No public-safe summary is available for this record."));
    card.appendChild(make("h4", "", "What was checked"));
    card.appendChild(make("p", "evidence-test", text(record.acceptance_test) || "Acceptance/test detail is not available in the current index."));
    card.appendChild(make("h4", "", "Remaining gap"));
    card.appendChild(make("p", "evidence-gap", text(record.T10_REMAINING_GAP) || "No remaining-gap statement is available in the current index."));
    card.appendChild(addLinkList(card, meta));
    return card;
  }

  function render() {
    const query = normalize(queryInput.value);
    const category = categoryInput.value;
    const words = query ? query.split(" ").filter(Boolean) : [];
    const matched = records.filter((record) => {
      const meta = config[record.evidence_id];
      if (!meta) return false;
      if (category !== "all" && meta.category !== category) return false;
      if (!words.length) return true;
      const haystack = recordSearchText(record, meta);
      return words.every((word) => haystack.includes(word));
    });

    matched.sort((a, b) => {
      const ca = categoryPriority(config[a.evidence_id].category);
      const cb = categoryPriority(config[b.evidence_id].category);
      if (ca !== cb) return ca - cb;
      return text(a.evidence_id).localeCompare(text(b.evidence_id));
    });

    results.replaceChildren();
    if (!matched.length) {
      results.appendChild(make("p", "evidence-empty", "No matching public-safe evidence record. Try another keyword or category."));
      status.textContent = "0 records matched. No result was inferred from missing evidence.";
      return;
    }

    matched.forEach((record) => results.appendChild(renderCard(record, config[record.evidence_id])));
    status.textContent = matched.length + " public-safe record" + (matched.length === 1 ? "" : "s") + " shown from the current evidence index. D04 is not part of this public view.";
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    render();
  });
  categoryInput.addEventListener("change", render);

  status.textContent = "Loading current evidence index…";
  fetch(indexUrl, { cache: "no-store", headers: { Accept: "application/json" } })
    .then((response) => {
      if (!response.ok) throw new Error("Evidence index request failed with status " + response.status);
      return response.json();
    })
    .then((data) => {
      if (!data || !Array.isArray(data.records)) throw new Error("Evidence index schema is not recognized");
      records = data.records.filter((record) => Object.prototype.hasOwnProperty.call(config, record.evidence_id));
      if (!records.length) throw new Error("No allowlisted public-safe records were found");
      render();
    })
    .catch(() => {
      records = [];
      results.replaceChildren(make("p", "evidence-error", "The current evidence index could not be verified. No cached PASS or stale result is shown. Try again later or request a controlled review."));
      status.textContent = "Evidence unavailable — no result inferred.";
    });
})();
