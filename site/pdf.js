// Vault PDF reader. Loaded only on PDF pages. Pages are drawn when they come
// near the screen, and PDF.js fetches only the byte ranges it needs, so a
// 350 page file opens as fast as a short one.
const PDFJS = "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.10.38/build/";
let pdfjs = null;

const box = document.querySelector(".pdf");
const pagesEl = box.querySelector(".pdf-pages");
const countEl = box.querySelector(".pdf-count");
const zoomEl = box.querySelector("[data-zoom-level]");
const ratio = Math.min(window.devicePixelRatio || 1, 2);
let doc = null;
let zoom = 1; // 1 = fit to width
let observer = null;
let farObserver = null;
const drawn = new Map();

function widthFor() {
  return Math.min(pagesEl.clientWidth, 1100) * zoom;
}

async function draw(slot) {
  const n = Number(slot.dataset.page);
  if (drawn.get(n) === zoom) return;
  drawn.set(n, zoom);
  const page = await doc.getPage(n);
  const base = page.getViewport({ scale: 1 });
  const scale = widthFor() / base.width;
  const view = page.getViewport({ scale: scale * ratio });
  const canvas = document.createElement("canvas");
  canvas.width = Math.floor(view.width);
  canvas.height = Math.floor(view.height);
  canvas.style.width = Math.floor(view.width / ratio) + "px";
  canvas.setAttribute("aria-label", "Page " + n);
  await page.render({ canvasContext: canvas.getContext("2d"), viewport: view }).promise;
  if (drawn.get(n) !== zoom) return; // zoom changed while drawing
  slot.style.aspectRatio = view.width + " / " + view.height;
  slot.replaceChildren(canvas);
}

function layout(firstPage) {
  const base = firstPage.getViewport({ scale: 1 });
  const w = widthFor();
  pagesEl.style.setProperty("--page-w", w + "px");
  drawn.clear();
  observer?.disconnect();
  observer = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) draw(e.target);
  }, { rootMargin: "800px 0px" });
  // Free the canvases of pages far from the screen, so a long PDF stays light on a phone.
  farObserver?.disconnect();
  farObserver = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) continue;
      const n = Number(e.target.dataset.page);
      if (drawn.has(n)) { drawn.delete(n); e.target.replaceChildren(); }
    }
  }, { rootMargin: "4000px 0px" });
  const frag = document.createDocumentFragment();
  for (let i = 1; i <= doc.numPages; i++) {
    const slot = pagesEl.children[i - 1] || document.createElement("div");
    slot.className = "pdf-page";
    slot.dataset.page = i;
    slot.style.aspectRatio = base.width + " / " + base.height;
    if (!slot.parentNode) frag.appendChild(slot);
  }
  pagesEl.appendChild(frag);
  for (const slot of pagesEl.children) {
    slot.replaceChildren();
    observer.observe(slot);
    farObserver.observe(slot);
  }
  zoomEl.textContent = Math.round(zoom * 100) + "%";
}

function currentPage() {
  const mid = window.innerHeight / 2;
  for (const slot of pagesEl.children) {
    const r = slot.getBoundingClientRect();
    if (r.bottom > mid) return Number(slot.dataset.page);
  }
  return doc.numPages;
}

async function open() {
  try {
    // PDF.js (350 KB) is fetched once the page itself is ready, so the page
    // head and the download button are usable straight away.
    pdfjs = await import(PDFJS + "pdf.min.mjs");
    pdfjs.GlobalWorkerOptions.workerSrc = PDFJS + "pdf.worker.min.mjs";
    doc = await pdfjs.getDocument({ url: box.dataset.pdf, disableAutoFetch: true, isEvalSupported: false }).promise;
  } catch (err) {
    countEl.textContent = "Could not display this PDF here.";
    box.querySelector(".pdf-fallback").hidden = false;
    return;
  }
  const first = await doc.getPage(1);
  layout(first);
  const update = () => { countEl.textContent = "Page " + currentPage() + " / " + doc.numPages; };
  update();
  window.addEventListener("scroll", () => requestAnimationFrame(update), { passive: true });

  box.addEventListener("click", (e) => {
    const b = e.target.closest("[data-zoom]");
    if (!b) return;
    const keep = currentPage();
    const step = b.dataset.zoom;
    zoom = step === "fit" ? 1 : Math.min(3, Math.max(0.5, zoom + (step === "+" ? 0.25 : -0.25)));
    layout(first);
    pagesEl.children[keep - 1]?.scrollIntoView({ block: "start" });
  });

  let resizeTimer;
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => layout(first), 200);
  });
}

if (document.readyState === "complete") open();
else window.addEventListener("load", open, { once: true });
