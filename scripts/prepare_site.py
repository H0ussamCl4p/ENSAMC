"""Copy the repo content into _vault_src, the docs_dir used by mkdocs.yml.

- every code file gets a readable page next to it (foo.c -> foo_c.md), the raw file is kept for download
- links to code files in Markdown pages are pointed to those pages
- every folder without a README gets an index page listing its content
- site/ (home page, assets, CNAME) is copied on top
"""
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_vault_src")
CONTENT = ["API", "CI", "Master", "CONTRIBUTING.md"]

CODE = {".c": "c", ".h": "c", ".py": "python", ".m": "matlab", ".r": "r", ".sql": "sql", ".algo": "text"}
LABELS = {".pdf": "PDF", ".ipynb": "notebook", ".png": "image", ".txt": "texte"}
LINK = re.compile(r"(\]\()([^)#\s]+?)\.(c|h|py|m|R|sql|algo)(\)|#)")


def code_lang(name):
    return CODE.get(os.path.splitext(name)[1].lower())


def page_of(name):
    stem, ext = os.path.splitext(name)
    return f"{stem}_{ext[1:]}.md"


def is_code_page(folder, name):
    return name.endswith(".md") and any(page_of(f) == name for f in os.listdir(folder) if code_lang(f))


def copy_content():
    shutil.rmtree(SRC, ignore_errors=True)
    os.makedirs(SRC)
    for item in CONTENT:
        src = os.path.join(ROOT, item)
        dst = os.path.join(SRC, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".ipynb_checkpoints"))
        else:
            shutil.copy(src, dst)


def code_pages():
    for folder, _, files in os.walk(SRC):
        for name in files:
            lang = code_lang(name)
            if not lang:
                continue
            path = os.path.join(folder, name)
            with open(path, encoding="utf-8", errors="replace") as f:
                code = f.read().rstrip("\n")
            fence = "````" if "```" in code else "```"
            page = (f"---\ntitle: {name}\n---\n\n# {name}\n\n"
                    f"[Télécharger le fichier]({name}){{ download }}\n\n"
                    f"{fence}{lang}\n{code}\n{fence}\n")
            with open(os.path.join(folder, page_of(name)), "w", encoding="utf-8") as f:
                f.write(page)


def rewrite_links():
    for folder, _, files in os.walk(SRC):
        for name in files:
            if not name.endswith(".md") or is_code_page(folder, name):
                continue
            path = os.path.join(folder, name)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            new = LINK.sub(lambda m: f"{m.group(1)}{m.group(2)}_{m.group(3)}.md{m.group(4)}", text)
            if new != text:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new)


def folder_indexes():
    for folder, dirs, files in os.walk(SRC):
        if folder == SRC or "README.md" in files or "index.md" in files:
            continue
        title = os.path.basename(folder)
        lines = [f"# {title}", ""]
        for d in sorted(dirs):
            lines.append(f"- [{d}/]({d}/)")
        for name in sorted(files):
            if is_code_page(folder, name):
                continue  # generated code page, listed through its source file
            if code_lang(name):
                lines.append(f"- [{name}]({page_of(name)})")
            elif name.endswith(".md"):
                lines.append(f"- [{name[:-3]}]({name})")
            else:
                label = LABELS.get(os.path.splitext(name)[1].lower(), "fichier")
                lines.append(f"- [{name}]({name}) ({label})")
        with open(os.path.join(folder, "index.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


def copy_site():
    shutil.copytree(os.path.join(ROOT, "site"), SRC, dirs_exist_ok=True)


if __name__ == "__main__":
    copy_content()
    code_pages()
    rewrite_links()
    folder_indexes()
    copy_site()
    print("prepared", SRC)
