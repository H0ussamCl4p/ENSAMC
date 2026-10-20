"""Build Vault, the static site of this repo, into _site/.

Plain HTML with the Flow design system: no framework, one CSS file, a few lines
of JS for search and mobile navigation. Every page is pre-rendered.

    python scripts/build_site.py

Pages:
- Markdown (.md)              -> same path, .html (README.md -> index.html)
- Notebooks (.ipynb)          -> same path, .html
- Code (.c .py .m .R .sql ...) -> file name + .html, raw file kept for download
- Folders                     -> index.html (README content if any, then the folder listing)
"""
import html
import json
import os
import re
import shutil
import sys
import urllib.request
from datetime import date

import markdown
import yaml
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import TextLexer, get_lexer_by_name

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_site")
ASSETS = os.path.join(ROOT, "site")
SECTIONS = ["API", "CI", "Master"]
EXTRA_PAGES = ["CONTRIBUTING.md"]
SITE_URL = "https://vault.hclap.tech"
REPO_URL = "https://github.com/H0ussamCl4p/ENSAMC"
LINKEDIN = "https://www.linkedin.com/company/ensamien-parrainage/posts/"
FLOW_URL = "https://flow.hclap.tech/"
ORIENTATION = "CI/orientation-filieres.html"
DRIVES_PAGE = "drives.html"

# Sidebar labels for the cycles, and the names shown on the level boxes of folder pages.
CYCLES = {"API": "Integrated prep cycle", "CI": "Engineering cycle", "Master": "Master's"}
LEVELS = {"avant-api1": "Get ready for prépa", "api1": "Prep year 1", "api2": "Prep year 2",
          "tronc-commun": "Modules communs à toutes les filières", "cs2c": "Cybersécurité et Cloud Computing",
          "iagi": "Intelligence Artificielle et Génie Informatique", "gsi": "Génie des Systèmes Industriels",
          "gsmi": "Génie des Systèmes Mécaniques Industriels", "gem": "Génie Électromécanique",
          "gm2a": "Génie Mécatronique pour l'Automobile et l'Aéronautique",
          "msei": "Management des Systèmes Électriques Intelligents"}
DRIVES = [("API1", "2026-2027", "1agpbin9asgD10WXHt4Agk_-0C27z8CY-"),
          ("API2", "2026-2027", "13TV1AZulLeBDfWJQB11-BYGQg9lmQzL9"),
          ("GSI", "2025-2026", "186BMD4eDyG8JPjyYd6-sNqbF8_W_XPgL"),
          ("GM2A", "2026-2027", "16gkD6kp0codf8mjscpTy4R54hoFfGbHf"),
          ("MSEI", "2025-2026", "1-APZVKuBcKRbjmePPZj6OHiQq5TOmYAY")]

CODE = {".c": "c", ".h": "c", ".py": "python", ".m": "matlab", ".r": "r", ".sql": "sql", ".algo": "text"}
KIND = {".pdf": ("PDF", "red"), ".png": ("Image", "blue"), ".jpg": ("Image", "blue"), ".txt": ("Data", "gray")}
IGNORE = {"__pycache__", ".ipynb_checkpoints"}
ACRONYMS = {"api": "API", "api1": "API1", "api2": "API2", "ci": "CI", "cs2c": "CS2C", "iagi": "IAGI", "gsi": "GSI",
            "gsmi": "GSMI", "gem": "GEM", "gmaa": "GM2A", "msei": "MSEI", "ti": "TI", "bdio": "BDIO", "idms": "IDMS",
            "s1": "S1", "s2": "S2", "s3": "S3", "s4": "S4", "s5": "S5", "gm2a": "GM2A", "td": "TD", "tp": "TP", "tdp": "TDP", "sql": "SQL", "dsa": "DSA", "c": "C",
            "matlab": "MATLAB", "leetcode": "LeetCode"}
NAMES = {"avant-api1": "Before API1", "tronc-commun": "Tronc commun", "programmation-c": "Programmation C",
         "algorithmique": "Algorithmique", "analyse-numerique": "Analyse numérique",
         "cryptographie": "Cryptographie", "problem-solving": "Problem solving", "hassan-el-bahi": "Hassan El Bahi",
         "chaines-fichiers": "Strings and files", "exercices": "Exercises", "examens": "Exams", "exam-tp": "Lab exam",
         "cours": "Lessons", "projet": "Project", "bases": "Basics", "tableaux": "Arrays", "structures": "Structures",
         "maths": "Maths", "notes-cours": "Notes", "basic-programming": "Basic programming", "input-output": "Input / output",
         "linked-list": "Linked list", "trees": "Trees", "array": "Array", "orientation-filieres": "Choosing a program",
         "fiche-r": "R cheat sheet", "examen-blanc": "Mock exam", "resume-linux": "Linux summary",
         "fiche-scripts-shell": "Shell scripts cheat sheet"}

FORMATTER = HtmlFormatter(nowrap=False, cssclass="hl-code", wrapcode=True)
MD = markdown.Markdown(extensions=["fenced_code", "codehilite", "tables", "toc", "attr_list", "admonition", "sane_lists"],
                       extension_configs={"codehilite": {"css_class": "hl-code", "guess_lang": False},
                                          "toc": {"permalink": False}})


# ----------------------------------------------------------------------------- helpers

def esc(s):
    return html.escape(str(s), quote=True)


def nice(slug):
    if slug in NAMES:
        return NAMES[slug]
    if slug.lower() in ACRONYMS:
        return ACRONYMS[slug.lower()]
    m = re.fullmatch(r"(tp|td|tdp)(\d+)", slug)
    if m:
        return f"{m.group(1).upper()}{m.group(2)}"
    return slug.replace("-", " ").replace("_", " ").capitalize()


def url_of(src_rel):
    """Output path (relative to site root, with forward slashes) of a source file."""
    rel = src_rel.replace(os.sep, "/")
    folder, name = os.path.split(rel)
    stem, ext = os.path.splitext(name)
    if name.lower() == "readme.md":
        out = "index.html"
    elif ext == ".md":
        out = stem + ".html"
    elif ext == ".ipynb":
        out = stem + ".html"
    elif ext.lower() in CODE or ext.lower() == ".pdf":
        out = name + ".html"
    else:
        out = name
    return f"{folder}/{out}" if folder else out


def rel_link(from_url, to_url):
    """Relative link between two output URLs."""
    base = os.path.dirname(from_url)
    r = os.path.relpath(to_url, base or ".").replace(os.sep, "/")
    return r


def strip_tags(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def tidy_headings(body):
    """The page title is the only h1: content headings start at h2 and never skip a level."""
    prev = 1

    def repl(m):
        nonlocal prev
        level = min(max(int(m.group(2)), 2), prev + 1)
        prev = level
        return f"<{m.group(1)}h{level}{m.group(3)}"

    return re.sub(r"<(/?)h([1-6])(\b[^>]*>)", lambda m: repl(m) if not m.group(1) else f"</h{prev}>", body)


def read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def front_matter(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, text[m.end():]


ANSI = re.compile(r"\x1b\[[0-9;]*m")


# ----------------------------------------------------------------------------- content tree

class Node:
    def __init__(self, rel, is_dir):
        self.rel = rel.replace(os.sep, "/")
        self.is_dir = is_dir
        self.children = []
        self.title = nice(os.path.basename(rel)) if rel else "Vault"
        self.url = (self.rel + "/index.html") if is_dir else url_of(rel)


TITLES = {}  # folder path -> shown name, for the breadcrumb


def scan(rel=""):
    node = Node(rel, True)
    full = os.path.join(ROOT, rel)
    # folders first; what comes before the levels ("avant-api1", the common first year) sorts first
    entries = sorted(os.listdir(full), key=lambda n: (not os.path.isdir(os.path.join(full, n)),
                                                      not n.startswith(("avant-", "tronc-commun")), n.lower()))
    for name in entries:
        if name in IGNORE or name.startswith("."):
            continue
        child_rel = os.path.join(rel, name) if rel else name
        if os.path.isdir(os.path.join(ROOT, child_rel)):
            child = scan(child_rel)
            # A module's README can give its official name: `title:` in its front matter.
            readme = os.path.join(ROOT, child_rel, "README.md")
            if os.path.exists(readme):
                child.title = front_matter(read(readme))[0].get("title") or child.title
            TITLES[child.rel] = child.title
            node.children.append(child)
        else:
            node.children.append(Node(child_rel, False))
    return node


def all_nodes(node):
    yield node
    for c in node.children:
        yield from all_nodes(c)


# ----------------------------------------------------------------------------- rendering of sources

def fix_links(body_html, page_url, src_dir):
    """Point relative links of rendered Markdown to the generated pages."""
    def repl(m):
        attr, q, href = m.group(1), m.group(2), m.group(3)
        if re.match(r"^(https?:|mailto:|#|data:|/)", href):
            return m.group(0)
        path, _, frag = href.partition("#")
        target_src = os.path.normpath(os.path.join(src_dir, path))
        full = os.path.join(ROOT, target_src)
        if os.path.isdir(full) or path.endswith("/"):
            target = target_src.replace(os.sep, "/").rstrip("/") + "/index.html"
        elif os.path.exists(full):
            target = url_of(target_src)
        else:
            return m.group(0)
        new = rel_link(page_url, target) + (f"#{frag}" if frag else "")
        return f'{attr}={q}{new}{q}'
    return re.sub(r'(href|src)=(["\'])([^"\']+)\2', repl, body_html)


def render_md(path):
    meta, text = front_matter(read(path))
    MD.reset()
    body = MD.convert(text)
    title = meta.get("title")
    m = re.match(r"\s*<h1[^>]*>(.*?)</h1>\s*", body, re.S)
    if m:
        title = title or strip_tags(m.group(1))
        body = body[m.end():]
    return title, meta, tidy_headings(body)


def render_code(path, lang):
    code = read(path).rstrip("\n")
    try:
        lexer = get_lexer_by_name(lang)
    except Exception:
        lexer = TextLexer()
    lines = code.count("\n") + 1
    return highlight(code, lexer, HtmlFormatter(cssclass="hl-code", wrapcode=True, linenos="table")), lines


def render_notebook(path, page_url, assets_dir):
    nb = json.loads(read(path))
    lang = (nb.get("metadata", {}).get("kernelspec", {}) or {}).get("language", "python")
    lexer = get_lexer_by_name(lang if lang else "python")
    parts, title, img_n = [], None, 0
    for cell in nb.get("cells", []):
        src = "".join(cell.get("source", "")) if isinstance(cell.get("source"), list) else cell.get("source", "")
        if cell.get("cell_type") == "markdown":
            src = re.sub(r"!\[[^\]]*\]\(attachment:[^)]*\)", "", src)
            src = re.sub(r"</?font[^>]*>", "", src)  # old <font color=...> markup from the course notebooks
            MD.reset()
            h = MD.convert(src)
            if title is None:
                m = re.search(r"<h[12][^>]*>(.*?)</h[12]>", h, re.S)
                if m and strip_tags(m.group(1)):
                    title = strip_tags(m.group(1))
                    h = h.replace(m.group(0), "", 1)  # it becomes the page title
            if strip_tags(h):
                parts.append(f'<div class="nb-md">{h}</div>')
        elif cell.get("cell_type") == "code":
            if not src.strip():
                continue
            # shell (!pip ...) and magic (%run ...) lines are not Python
            cell_lexer = TextLexer() if src.lstrip()[:1] in "!%" else lexer
            out = [f'<div class="nb-cell"><div class="nb-in">{highlight(src, cell_lexer, FORMATTER)}</div>']
            for o in cell.get("outputs", []):
                t = o.get("output_type")
                if t == "stream":
                    txt = "".join(o.get("text", ""))
                    out.append(f'<pre class="nb-out">{esc(ANSI.sub("", txt))}</pre>')
                elif t in ("execute_result", "display_data"):
                    data = o.get("data", {})
                    if "image/png" in data:
                        img_n += 1
                        name = f"img-{img_n}.png"
                        os.makedirs(assets_dir, exist_ok=True)
                        import base64
                        with open(os.path.join(assets_dir, name), "wb") as f:
                            f.write(base64.b64decode("".join(data["image/png"])))
                        rel = rel_link(page_url, os.path.relpath(os.path.join(assets_dir, name), OUT).replace(os.sep, "/"))
                        out.append(f'<img class="nb-img" src="{rel}" alt="" loading="lazy" decoding="async">')
                    elif "text/html" in data:
                        out.append(f'<div class="nb-html">{"".join(data["text/html"])}</div>')
                    elif "text/plain" in data:
                        out.append(f'<pre class="nb-out">{esc(ANSI.sub("", "".join(data["text/plain"])))}</pre>')
                elif t == "error":
                    tb = ANSI.sub("", "\n".join(o.get("traceback", [])))
                    out.append(f'<pre class="nb-out nb-err">{esc(tb)}</pre>')
            out.append("</div>")
            parts.append("".join(out))
    return title, tidy_headings("\n".join(parts))


# ----------------------------------------------------------------------------- layout

ICONS = {
    "home": '<path d="M3.5 10.2 12 3.5l8.5 6.7V20a1 1 0 0 1-1 1h-5v-6h-5v6h-5a1 1 0 0 1-1-1z"/>',
    "folder": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "drive": '<path d="M8 3h8l6 10-4 7H6l-4-7z"/><path d="M8 3 2 13M16 3l6 10M6 20l4-7h12"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "github": '<path d="M9 19c-4 1.5-4-2-6-2.5M15 21v-3.5a3 3 0 0 0-.9-2.4c3-.3 6-1.5 6-6.6a5 5 0 0 0-1.4-3.6 4.7 4.7 0 0 0-.1-3.5s-1.1-.3-3.6 1.4a12.4 12.4 0 0 0-6.6 0C5.9 1.1 4.8 1.4 4.8 1.4a4.7 4.7 0 0 0-.1 3.5A5 5 0 0 0 3.3 8.5c0 5.1 3 6.3 6 6.6a3 3 0 0 0-.9 2.4V21"/>',
    "doc": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    "code": '<path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 5l-4 14"/>',
    "nb": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 3v18M11 8h6M11 12h6"/>',
    "pdf": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M8.5 16v-4h1.2a1.2 1.2 0 0 1 0 2.4H8.5"/>',
    "download": '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/>',
    "star": '<path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.8l-5.2 2.8 1-5.8-4.3-4.1 5.9-.9z"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6"/>',
}


def icon(name, cls="icon"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


def kind_of(node):
    if node.is_dir:
        return "Folder", "gray", "folder"
    ext = os.path.splitext(node.rel)[1].lower()
    if ext == ".md":
        return "Note", "purple", "doc"
    if ext == ".ipynb":
        return "Notebook", "yellow", "nb"
    if ext in CODE:
        return ext[1:].upper() if ext != ".algo" else "Algo", "green", "code"
    label, color = KIND.get(ext, ("File", "gray"))
    return label, color, "pdf" if ext == ".pdf" else "doc"


def sidebar(tree, page_url, current_rel):
    home_active = " active" if page_url == "index.html" else ""
    links = []
    for sec in tree.children:
        if not sec.is_dir:
            continue
        active = " active" if current_rel == sec.rel or current_rel.startswith(sec.rel + "/") else ""
        links.append(f'<a class="side-link{active}" href="{rel_link(page_url, sec.url)}">{icon("folder")}'
                     f'<span>{esc(sec.title)}</span><small>{esc(CYCLES[sec.rel])}</small></a>')
    guide = " active" if page_url == ORIENTATION else ""
    groups = [f'<div class="side-label">Browse</div>{"".join(links)}',
              f'<div class="side-label">Guides</div><a class="side-link{guide}" href="{rel_link(page_url, ORIENTATION)}">'
              f'{icon("doc")}<span>Choosing a program</span></a>']
    contrib = rel_link(page_url, "CONTRIBUTING.html")
    return f"""<aside class="sidebar" id="sidebar" aria-label="Navigation">
<a class="brand" href="{rel_link(page_url, 'index.html')}">{BRAND_INNER}</a>
<button class="side-search" type="button" data-search>{icon('search')}<span>Search</span><kbd>Ctrl K</kbd></button>
<a class="side-link{home_active}" href="{rel_link(page_url, 'index.html')}">{icon('home')}<span>Home</span></a>
<a class="side-link{' active' if page_url == DRIVES_PAGE else ''}" href="{rel_link(page_url, DRIVES_PAGE)}">{icon('drive')}<span>Shared drives</span></a>
{''.join(groups)}
<div class="sidebar-foot">
<a class="side-link subtle" href="{contrib}">{icon('users')}<span>Contribute</span></a>
<a class="side-link subtle star-btn" href="{REPO_URL}" target="_blank" rel="noopener">{icon('star')}<span>Star on GitHub</span>{star_slot()}</a>
</div>
</aside>"""


# The brand mark drawn inline, as Flow does, so there is no icon file to fetch.
FAVICON = ("<link rel=\"icon\" href=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='8' fill='%23560261'/%3E%3Cpath d='M8 8h4.3l3.7 11 3.7-11H24l-6 17h-4z' "
           "fill='white'/%3E%3C/svg%3E\">")

BRAND_INNER = ('<span class="brand-mark" aria-hidden="true">V</span><span class="brand-name">'
               '<strong class="brand-word">Vault</strong><span class="brand-by">By ENSAMIENParrainage</span></span>')


STARS = None


def fetch_stars():
    """Star count at build time, so it shows before any script runs. The page refreshes it later."""
    global STARS
    try:
        req = urllib.request.Request(REPO_URL.replace("github.com", "api.github.com/repos"),
                                     headers={"Accept": "application/vnd.github+json", "User-Agent": "vault-build"})
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=8) as r:
            STARS = json.load(r)["stargazers_count"]
    except Exception:
        STARS = None


def star_slot():
    if STARS is None:
        return '<span class="star-count" data-stars hidden></span>'
    return f'<span class="star-count" data-stars>{STARS}</span>'


def crumbs(page_url, rel, title):
    parts = rel.split("/") if rel else []
    links = [f'<a href="{rel_link(page_url, "index.html")}">Vault</a>']
    acc = ""
    for i, p in enumerate(parts):
        acc = f"{acc}/{p}" if acc else p
        if i == len(parts) - 1:
            links.append(f"<span>{esc(title)}</span>")
        elif os.path.isdir(os.path.join(ROOT, acc)):
            links.append(f'<a href="{rel_link(page_url, acc + "/index.html")}">{esc(TITLES.get(acc, nice(p)))}</a>')
    return '<span class="sep">/</span>'.join(links)


def layout(tree, page_url, rel, title, body, description="", head_extra=""):
    js = rel_link(page_url, ASSET_PATHS["js"])
    root = rel_link(page_url, "index.html")[:-len("index.html")] or "./"
    desc = esc(description or "Course notes, exercises and solutions shared by students. By Ensamien Parrainage.")
    full_title = "Vault" if page_url == "index.html" else f"{title} · Vault"
    canonical = f"{SITE_URL}/{page_url}".replace("/index.html", "/")
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(full_title)}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#ffffff">
<link rel="canonical" href="{canonical}">
{FAVICON}
<link rel="preload" href="/assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<style>{ASSET_PATHS["css_text"]}</style>
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="Vault by Ensamien Parrainage">
{head_extra}
</head>
<body class="has-tabbar" data-root="{root}">
<a class="skip" href="#main">Skip to content</a>
<div class="app-layout">
{sidebar(tree, page_url, rel)}
<div class="main-shell">
<header class="topbar">
<a class="brand" href="{root}index.html">{BRAND_INNER}</a>
<nav class="crumb" aria-label="Breadcrumb">{crumbs(page_url, rel, title)}</nav>
<div class="topbar-right">
<button class="btn ghost icon-btn" type="button" data-search aria-label="Search">{icon('search')}</button>
<a class="btn star-btn" href="{REPO_URL}" target="_blank" rel="noopener" aria-label="Star Vault on GitHub">{icon('star')}<span>Star</span>{star_slot()}</a>
<a class="btn soft wide-only" href="{LINKEDIN}" rel="noopener">Ensamien Parrainage</a>
</div>
</header>
<main class="content" id="main">
{body}
</main>
</div>
</div>
<nav class="tabbar" aria-label="Tabs">
<a class="tab{' active' if page_url == 'index.html' else ''}" href="{root}index.html">{icon('home')}<span>Home</span></a>
<button class="tab{'' if page_url == 'index.html' else ' active'}" type="button" data-menu>{icon('folder')}<span>Browse</span></button>
<button class="tab" type="button" data-search>{icon('search')}<span>Search</span></button>
<a class="tab{' active' if page_url == DRIVES_PAGE else ''}" href="{root}{DRIVES_PAGE}">{icon('drive')}<span>Drives</span></a>
</nav>
<div class="scrim" data-close hidden></div>
<dialog class="search" id="search" aria-label="Search">
<div class="search-box">{icon('search')}<input type="search" placeholder="Search notes, TPs, code…" autocomplete="off" spellcheck="false" aria-label="Search"><kbd>Esc</kbd></div>
<ol class="results" role="listbox"></ol>
<p class="search-hint">Type at least 2 letters. <kbd>↑</kbd> <kbd>↓</kbd> to move, <kbd>Enter</kbd> to open.</p>
</dialog>
<script src="{js}" defer></script>
</body>
</html>
"""


def page_head(eyebrow_tags, title, sub="", actions=""):
    tags = "".join(f'<span class="tag {c}">{esc(t)}</span>' for t, c in eyebrow_tags)
    sub_html = f"<p>{sub}</p>" if sub else ""
    act = f'<div class="head-actions">{actions}</div>' if actions else ""
    return f'<div class="page-head"><div><div class="props">{tags}</div><h1>{esc(title)}</h1>{sub_html}</div>{act}</div>'


def listing(node, page_url):
    rows = []
    for c in node.children:
        if c.is_dir or os.path.basename(c.rel).lower() == "readme.md":
            continue
        size = os.path.getsize(os.path.join(ROOT, c.rel))
        meta = f"{size / 1024:.0f} KB" if size >= 1024 else f"{size} B"
        label, color, ic = kind_of(c)
        name = os.path.basename(c.rel)
        shown = c.title if c.is_dir else name
        rows.append(f'<a class="row" href="{rel_link(page_url, c.url)}">{icon(ic)}<span class="row-name">{esc(shown)}</span>'
                    f'<span class="tag {color}">{esc(label)}</span><span class="row-meta">{meta}</span></a>')
    if not rows:
        return ""
    return f'<section class="list"><div class="list-head"><span>Name</span><span>Type</span><span>Size</span></div>{"".join(rows)}</section>'


def file_count(node):
    return sum(1 for x in all_nodes(node) if not x.is_dir)


def plural(n, word="file"):
    return f"{n} {word}{'s' if n != 1 else ''}"


def folder_boxes(node, page_url):
    subs = [c for c in node.children if c.is_dir]
    if not subs:
        return ""
    cards = []
    for c in subs:
        slug = os.path.basename(c.rel)
        label = f"{esc(c.title)} · " if slug in LEVELS else ""
        cards.append(f'<a class="mod" href="{rel_link(page_url, c.url)}"><span class="tag purple">Folder</span>'
                     f'<b>{esc(LEVELS.get(slug, c.title))}</b><small>{label}{plural(file_count(c))}</small></a>')
    return f'<div class="mods">{"".join(cards)}</div>'


# ----------------------------------------------------------------------------- pages

SEARCH = []


def add_search(url, title, section, text):
    SEARCH.append({"u": url, "t": title, "s": section, "x": text[:1200]})


def section_of(rel):
    parts = rel.split("/")[:-1]
    return " / ".join(nice(p) for p in parts)


def write(url, content):
    path = os.path.join(OUT, url)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Compact the whitespace between tags, but never inside <pre>, where it is the code.
    parts = re.split(r"(<pre[\s>].*?</pre>)", content, flags=re.S)
    content = "".join(p if p.startswith("<pre") else re.sub(r">\s*\n\s*<", ">\n<", p) for p in parts)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def build_dir(tree, node):
    page_url = node.url
    readme = next((c for c in node.children if not c.is_dir and os.path.basename(c.rel).lower() == "readme.md"), None)
    title, intro = node.title, ""
    if readme:
        t, meta, body = render_md(os.path.join(ROOT, readme.rel))
        title = t or title
        intro = f'<article class="prose">{fix_links(body, page_url, node.rel)}</article>'
        add_search(page_url, title, section_of(node.rel + "/x"), strip_tags(body))
    else:
        add_search(page_url, title, section_of(node.rel + "/x"), "")
    n_files = sum(1 for x in all_nodes(node) if not x.is_dir)
    head = page_head([("Folder", "gray"), (f"{n_files} files", "purple")], title)
    lst = listing(node, page_url)
    boxes = folder_boxes(node, page_url)
    body = (head + intro + (f'<h2 class="list-title">Folders</h2>{boxes}' if boxes else "") +
            (f'<h2 class="list-title">Files</h2>{lst}' if lst else ""))
    write(page_url, layout(tree, page_url, node.rel, title, body))


def build_file(tree, node):
    src = os.path.join(ROOT, node.rel)
    ext = os.path.splitext(node.rel)[1].lower()
    page_url = node.url
    name = os.path.basename(node.rel)
    if os.path.basename(node.rel).lower() == "readme.md":
        return
    # raw copy of every non-Markdown source (downloads, PDFs, code)
    if ext != ".md":
        dst = os.path.join(OUT, node.rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    if ext == ".md":
        title, meta, body = render_md(src)
        title = title or nice(os.path.splitext(name)[0])
        tags = [("Note", "purple")]
        if meta.get("date"):
            tags.append((str(meta["date"]), "gray"))
        sub = esc(meta.get("author", "")) if meta.get("author") else ""
        html_body = page_head(tags, title, sub) + f'<article class="prose">{fix_links(body, page_url, os.path.dirname(node.rel))}</article>'
        add_search(page_url, title, section_of(node.rel), strip_tags(body))
    elif ext == ".ipynb":
        assets_dir = os.path.join(OUT, os.path.dirname(node.rel), "_img", os.path.splitext(name)[0])
        title, body = render_notebook(src, page_url, assets_dir)
        title = title or nice(os.path.splitext(name)[0])
        dl = f'<a class="btn soft" href="{esc(name)}" download>{icon("download")}Download .ipynb</a>'
        html_body = page_head([("Notebook", "yellow")], title, esc(name), dl) + f'<article class="prose nb">{fix_links(body, page_url, os.path.dirname(node.rel))}</article>'
        add_search(page_url, title, section_of(node.rel), strip_tags(body))
    elif ext in CODE:
        code_html, lines = render_code(src, CODE[ext])
        dl = f'<a class="btn soft" href="{esc(name)}" download>{icon("download")}Download</a>'
        lang = ext[1:].upper() if ext != ".algo" else "Algo"
        html_body = page_head([(lang, "green"), (f"{lines} lines", "gray")], name, "", dl) + f'<div class="code-card">{code_html}</div>'
        add_search(page_url, name, section_of(node.rel), read(src)[:600])
        title = name
    elif ext == ".pdf":
        title = name
        size = os.path.getsize(src)
        pages = pdf_pages(src)
        tags = [("PDF", "red")] + ([(f"{pages} pages", "gray")] if pages else []) + [(f"{size / 1048576:.1f} MB", "gray")]
        actions = (f'<a class="btn soft" href="{esc(name)}" download>{icon("download")}Download</a>'
                   f'<a class="btn outline" href="{esc(name)}" target="_blank" rel="noopener">Open original</a>')
        viewer = f"""<div class="pdf" data-pdf="{esc(name)}">
<div class="pdf-bar"><span class="pdf-count">Loading…</span>
<div class="pdf-zoom"><button type="button" class="btn ghost icon-btn" data-zoom="-" aria-label="Zoom out">−</button>
<span data-zoom-level>100%</span>
<button type="button" class="btn ghost icon-btn" data-zoom="+" aria-label="Zoom in">+</button>
<button type="button" class="btn ghost" data-zoom="fit">Fit</button></div></div>
<div class="pdf-pages"></div>
<p class="pdf-fallback" hidden><a class="btn" href="{esc(name)}">Open the PDF</a></p>
<noscript><p><a class="btn" href="{esc(name)}">Open the PDF</a></p></noscript>
</div>"""
        html_body = page_head(tags, name, "", actions) + viewer
        head = ('<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>'
                f'<script type="module" src="{rel_link(page_url, ASSET_PATHS["pdf"])}"></script>')
        add_search(page_url, name, section_of(node.rel), "PDF " + name.replace("-", " "))
        write(page_url, layout(tree, page_url, node.rel, title, html_body, head_extra=head))
        return
    else:
        return
    write(page_url, layout(tree, page_url, os.path.dirname(node.rel) + "/" + name if os.path.dirname(node.rel) else name,
                           title, html_body))


def pdf_pages(path):
    """Page count read from the PDF trailer (/Count of the page tree); 0 if unknown."""
    with open(path, "rb") as f:
        data = f.read()
    counts = [int(c) for c in re.findall(rb"/Count\s+(\d+)", data)]
    return max(counts) if counts else 0


def build_home(tree):
    page_url = "index.html"
    counts = {"files": 0, "notes": 0, "code": 0, "nb": 0}
    for n in all_nodes(tree):
        if n.is_dir or not n.rel.split("/")[0] in SECTIONS:
            continue
        counts["files"] += 1
        ext = os.path.splitext(n.rel)[1].lower()
        counts["notes"] += ext == ".md"
        counts["code"] += ext in CODE
        counts["nb"] += ext == ".ipynb"

    body = f"""
<section class="home-hero">
<span class="eyebrow">Ensamien Parrainage</span>
<h1>Every course, <span class="hl"><i aria-hidden="true"></i>kept</span> in one vault.</h1>
<p class="hero-lede">Notes, exercises and solutions, by students.</p>
<div class="hero-actions">
<button class="btn" type="button" data-search>{icon('search')}Search the vault</button>
<a class="btn star-btn hero-star" href="{REPO_URL}" target="_blank" rel="noopener">{icon('star')}<span>Star on GitHub</span>{star_slot()}</a>
</div>
</section>
<div class="stats">
<div class="stat"><span class="stat-label">Files</span><span class="stat-value num">{counts['files']}</span></div>
<div class="stat"><span class="stat-label">Code</span><span class="stat-value num">{counts['code']}</span></div>
<div class="stat"><span class="stat-label">Notes</span><span class="stat-value num">{counts['notes'] + counts['nb']}</span></div>
</div>
<p class="muted note-line">Student project, not official. Check solutions with your teachers.</p>
<div class="card about">
<h2>Ensamien Parrainage</h2>
<div class="about-actions">
<a class="btn" href="{LINKEDIN}" rel="noopener">{icon('linkedin')}Follow on LinkedIn</a>
<a class="btn soft" href="{FLOW_URL}" rel="noopener">Open Flow</a>
<a class="btn outline" href="CONTRIBUTING.html">Contribute</a>
</div>
</div>
"""
    add_search(page_url, "Home", "", "Vault course notes exercises solutions Ensamien Parrainage")
    write(page_url, layout(tree, page_url, "", "Home", body))


def build_drives(tree):
    page_url = DRIVES_PAGE
    links = "".join(f'<a class="mini-link" href="https://drive.google.com/drive/folders/{i}?usp=drive_link" rel="noopener">'
                    f'{icon("drive")}<span><b>{esc(n)}</b></span><span class="tag">{y}</span></a>' for n, y, i in DRIVES)
    body = page_head([("Google Drive", "blue")], "Shared drives", "Slides, past exams and scanned notes.") + \
        f'<div class="drives">{links}</div>'
    add_search(page_url, "Shared drives", "", "shared drives Google Drive " + " ".join(n for n, _, _ in DRIVES))
    write(page_url, layout(tree, page_url, "drives", "Shared drives", body))


def build_extra(tree):
    for name in EXTRA_PAGES:
        title, meta, body = render_md(os.path.join(ROOT, name))
        url = url_of(name)
        html_body = page_head([("Guide", "blue")], title or "Contribute") + f'<article class="prose">{fix_links(body, url, "")}</article>'
        add_search(url, title, "", strip_tags(body))
        write(url, layout(tree, url, name, title, html_body))


def build_404(tree):
    body = (page_head([("404", "red")], "Page not found", "This page does not exist or has moved.") +
            '<p><a class="btn" href="/index.html">Back to the vault</a></p>')
    html_doc = layout(tree, "404.html", "", "Not found", body)
    html_doc = re.sub(r'(href|src)="(?!https?:|/|#|data:)', lambda m: m.group(1) + '="/', html_doc)
    write("404.html", html_doc.replace('data-root="./"', 'data-root="/"'))


# ----------------------------------------------------------------------------- assets

ASSET_PATHS = {}


def build_assets():
    import hashlib
    css = read(os.path.join(ASSETS, "vault.css"))
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};:,>])\s*", r"\1", css).replace(";}", "}")
    os.makedirs(os.path.join(OUT, "assets", "fonts"), exist_ok=True)
    # CSS is inlined in every page (no render-blocking request); the script is
    # versioned by its hash so a deploy is never hidden behind a cached copy.
    ASSET_PATHS["css_text"] = css
    # vault.js runs on every page; pdf.js (the reader) only on PDF pages
    for key, name in (("js", "vault"), ("pdf", "pdf")):
        js = read(os.path.join(ASSETS, f"{name}.js"))
        js = re.sub(r"^\s*//.*$", "", js, flags=re.M)
        js = re.sub(r"\n\s*\n+", "\n", js)
        h = hashlib.sha1(js.encode()).hexdigest()[:10]
        ASSET_PATHS[key] = f"assets/{name}.{h}.js"
        with open(os.path.join(OUT, ASSET_PATHS[key]), "w", encoding="utf-8") as f:
            f.write(js)
    shutil.copy(os.path.join(ASSETS, "fonts", "inter.woff2"), os.path.join(OUT, "assets", "fonts", "inter.woff2"))
    shutil.copy(os.path.join(ASSETS, "fonts", "OFL-Inter.txt"), os.path.join(OUT, "assets", "fonts", "OFL-Inter.txt"))
    shutil.copy(os.path.join(ASSETS, "CNAME"), os.path.join(OUT, "CNAME"))
    with open(os.path.join(OUT, ".nojekyll"), "w") as f:
        f.write("")


def build_sitemap():
    urls = sorted({e["u"] for e in SEARCH})
    today = date.today().isoformat()
    items = "".join(f"<url><loc>{SITE_URL}/{u.replace('index.html', '')}</loc><lastmod>{today}</lastmod></url>" for u in urls)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{items}</urlset>')
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    with open(os.path.join(OUT, "search.json"), "w", encoding="utf-8") as f:
        json.dump(SEARCH, f, ensure_ascii=False, separators=(",", ":"))


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT, exist_ok=True)  # a preview server may keep the folder itself open
    build_assets()
    fetch_stars()
    tree = Node("", True)
    for sec in SECTIONS:
        tree.children.append(scan(sec))
    for node in all_nodes(tree):
        if node.rel == "":
            continue
        if node.is_dir:
            build_dir(tree, node)
        else:
            build_file(tree, node)
    build_home(tree)
    build_drives(tree)
    build_extra(tree)
    build_404(tree)
    build_sitemap()
    pages = sum(1 for _, _, fs in os.walk(OUT) for f in fs if f.endswith(".html"))
    print(f"built {pages} pages into {OUT}")


if __name__ == "__main__":
    sys.exit(main())
