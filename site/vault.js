"use strict";

// Vault: search, mobile drawer and link prefetch. Everything else is plain HTML.
const root = document.body.dataset.root || "./";
const dialog = document.getElementById("search");
const input = dialog.querySelector("input");
const list = dialog.querySelector(".results");
let index = null;
let loading = null;
let selected = 0;

// The index is only fetched the first time search opens, so pages stay light.
function loadIndex() {
  if (index) return Promise.resolve(index);
  if (!loading) {
    loading = fetch(root + "search.json")
      .then((r) => r.json())
      .then((data) => {
        index = data.map((e) => ({ ...e, nt: norm(e.t), ns: norm(e.s), nx: norm(e.x) }));
        return index;
      });
  }
  return loading;
}

function norm(s) {
  return (s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
}

function escapeHtml(s) {
  return s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
}

function mark(text, terms) {
  let out = escapeHtml(text);
  for (const t of terms) {
    if (t.length < 2) continue;
    const re = new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig");
    out = out.replace(re, "<mark>$1</mark>");
  }
  return out;
}

function snippet(entry, terms) {
  const i = entry.nx.indexOf(terms[0]);
  if (i < 0) return "";
  const start = Math.max(0, i - 40);
  return (start ? "…" : "") + entry.x.slice(start, start + 140);
}

function search(q) {
  const terms = norm(q).split(/\s+/).filter(Boolean);
  if (!terms.length || q.trim().length < 2) {
    list.innerHTML = "";
    return;
  }
  const scored = [];
  for (const e of index) {
    let score = 0;
    for (const t of terms) {
      if (e.nt.includes(t)) score += e.nt.startsWith(t) ? 12 : 8;
      else if (e.ns.includes(t)) score += 4;
      else if (e.nx.includes(t)) score += 2;
      else { score = 0; break; }
    }
    if (score) scored.push([score, e]);
  }
  scored.sort((a, b) => b[0] - a[0] || a[1].t.length - b[1].t.length);
  const top = scored.slice(0, 30);
  selected = 0;
  if (!top.length) {
    list.innerHTML = '<li class="empty">No result for “' + escapeHtml(q) + "”</li>";
    return;
  }
  list.innerHTML = top
    .map(([, e], i) =>
      '<li><a href="' + root + e.u + '"' + (i === 0 ? ' aria-selected="true"' : "") + "><b>" + mark(e.t, terms) +
      "</b><small>" + [e.s ? escapeHtml(e.s) : "", mark(snippet(e, terms), terms)].filter(Boolean).join(" · ") +
      "</small></a></li>")
    .join("");
}

function move(step) {
  const links = list.querySelectorAll("a");
  if (!links.length) return;
  links[selected]?.removeAttribute("aria-selected");
  selected = (selected + step + links.length) % links.length;
  links[selected].setAttribute("aria-selected", "true");
  links[selected].scrollIntoView({ block: "nearest" });
}

function openSearch() {
  closeMenu();
  if (!dialog.open) dialog.showModal();
  input.select();
  loadIndex().then(() => search(input.value));
}

input.addEventListener("input", () => loadIndex().then(() => search(input.value)));
input.addEventListener("keydown", (e) => {
  if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
  else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
  else if (e.key === "Enter") {
    const a = list.querySelectorAll("a")[selected];
    if (a) { e.preventDefault(); window.location.href = a.href; }
  }
});
// A click on the dimmed backdrop lands on the dialog itself.
dialog.addEventListener("click", (e) => { if (e.target === dialog) dialog.close(); });

// Drawer: the sidebar slides in on phones from the Browse tab.
const scrim = document.querySelector(".scrim");
function openMenu() { document.body.classList.add("menu-open"); scrim.hidden = false; }
function closeMenu() { document.body.classList.remove("menu-open"); scrim.hidden = true; }

document.addEventListener("click", (e) => {
  if (e.target.closest("[data-search]")) { e.preventDefault(); openSearch(); return; }
  if (e.target.closest("[data-menu]")) { document.body.classList.contains("menu-open") ? closeMenu() : openMenu(); return; }
  if (e.target.closest("[data-close]")) closeMenu();
});

document.addEventListener("keydown", (e) => {
  const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName || "");
  if ((e.key === "k" && (e.ctrlKey || e.metaKey)) || (e.key === "/" && !typing)) {
    e.preventDefault();
    openSearch();
  } else if (e.key === "Escape") closeMenu();
});

// Keep the current page visible in a long sidebar.
document.querySelector(".sidebar .side-tree .active")?.scrollIntoView({ block: "center" });

// Prefetch a page when the pointer rests on its link, so the click feels instant.
const prefetched = new Set();
function prefetch(a) {
  if (!a || a.origin !== location.origin || a.hasAttribute("download")) return;
  const url = a.href.split("#")[0];
  if (prefetched.has(url) || url === location.href.split("#")[0] || !/\.html$|\/$/.test(url)) return;
  prefetched.add(url);
  const link = document.createElement("link");
  link.rel = "prefetch";
  link.href = url;
  document.head.appendChild(link);
}
let hoverTimer;
document.addEventListener("pointerover", (e) => {
  const a = e.target.closest("a");
  clearTimeout(hoverTimer);
  if (a) hoverTimer = setTimeout(() => prefetch(a), 65);
}, { passive: true });
document.addEventListener("touchstart", (e) => prefetch(e.target.closest("a")), { passive: true });

// GitHub star count, cached an hour so browsing pages does not hit the API (60 calls/hour per visitor).
function stars() {
  const slots = document.querySelectorAll("[data-stars]");
  if (!slots.length) return;
  const show = (n) => slots.forEach((s) => { s.textContent = n >= 1000 ? (n / 1000).toFixed(1) + "k" : String(n); s.hidden = false; });
  let cached = null;
  try { cached = JSON.parse(localStorage.getItem("vault-stars") || "null"); } catch (_) {}
  if (cached && Date.now() - cached.t < 3600e3) { show(cached.n); return; }
  if (cached) show(cached.n);
  fetch("https://api.github.com/repos/H0ussamCl4p/ENSAMC", { headers: { Accept: "application/vnd.github+json" } })
    .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
    .then((d) => {
      show(d.stargazers_count);
      try { localStorage.setItem("vault-stars", JSON.stringify({ n: d.stargazers_count, t: Date.now() })); } catch (_) {}
    })
    .catch(() => {});
}
// After the page has loaded, when the browser is idle: never in the way of the first paint.
const idle = window.requestIdleCallback || ((f) => setTimeout(f, 200));
if (document.readyState === "complete") idle(stars);
else window.addEventListener("load", () => idle(stars), { once: true });
