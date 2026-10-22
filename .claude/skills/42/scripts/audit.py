#!/usr/bin/env python3
"""Audit mécanique du skill 42 : structure, liens entre fichiers, cohérence des listes,
fraîcheur de la base, tests. Usage : python3 scripts/audit.py [dossier_du_skill]
Sortie : un rapport texte, une ligne par constat, préfixée par son niveau."""
import datetime
import os
import re
import sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), ".."))
TODAY = datetime.date.today()
findings = []


def add(level, msg):
    findings.append((level, msg))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def exists(rel):
    return os.path.exists(os.path.join(ROOT, rel))


skill = read("SKILL.md")
m = re.match(r"---\n(.*?)\n---\n", skill, re.S)
front = m.group(1) if m else ""
desc_m = re.search(r'^description:\s*"(.*)"\s*$', front, re.M)
desc = desc_m.group(1) if desc_m else ""

# 1. Frontmatter
if not m:
    add("BLOQUANT", "SKILL.md : frontmatter absent")
if not desc:
    add("BLOQUANT", "SKILL.md : description absente ou mal formée")
else:
    if len(desc) > 1024:
        add("BLOQUANT", f"description : {len(desc)} caractères (max 1024)")
    elif len(desc) > 900:
        add("ATTENTION", f"description : {len(desc)} caractères, proche de la limite de 1024")
    if "<" in desc or ">" in desc:
        add("BLOQUANT", "description : contient < ou >, refusé à l'empaquetage")
add("INFO", f"description : {len(desc)} caractères")

lines = skill.count("\n")
if lines > 500:
    add("ATTENTION", f"SKILL.md : {lines} lignes (idéal < 500)")
add("INFO", f"SKILL.md : {lines} lignes")

# 2. Modes : table de SKILL.md, fichiers de référence, description, help
table_modes = re.findall(r"^\| `/42 (\w+)`", skill, re.M)
add("INFO", "modes de la table : " + ", ".join(table_modes))
for mode in table_modes:
    if mode == "help":
        pass
    elif not exists(f"references/{mode}.md"):
        add("BLOQUANT", f"mode {mode} : references/{mode}.md introuvable")
    if mode not in desc:
        add("ATTENTION", f"mode {mode} : absent de la description (il risque de ne pas déclencher le skill)")
ref_modes = sorted(f[:-3] for f in os.listdir(os.path.join(ROOT, "references"))
                   if f.endswith(".md") and f not in ("norm.md", "doc-work.md"))
for mode in ref_modes:
    if mode not in table_modes:
        add("ATTENTION", f"references/{mode}.md : aucun mode correspondant dans la table de SKILL.md")

# 3. Chemins cités : tout `references/...`, `scripts/...` mentionné doit exister
cited = {}
for dirpath, _, files in os.walk(ROOT):
    if "/evals" in dirpath or "/sources" in dirpath:
        continue
    for f in files:
        if not f.endswith(".md"):
            continue
        rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
        for p in re.findall(r"`((?:references|scripts)/[\w./-]+?)`", read(rel)):
            cited.setdefault(p, set()).add(rel)
for p, where in sorted(cited.items()):
    if "<" in p or p.endswith("/"):
        if not exists(p.rstrip("/")):
            add("INFO", f"dossier cité encore vide ou absent : {p} (dans {', '.join(sorted(where))})")
        continue
    if not exists(p):
        add("BLOQUANT", f"chemin cité introuvable : {p} (dans {', '.join(sorted(where))})")

# 4. Options : chaque mode du tableau --work doit exister
work_rows = re.findall(r"^\| `([\w`, ]+)` \| ", skill.split("**`--web`")[0].split("Avec `--work`")[-1], re.M)
for row in work_rows:
    for mode in re.findall(r"\w+", row):
        if mode not in table_modes:
            add("ATTENTION", f"tableau --work : mode inconnu {mode}")
for mode in table_modes:
    if mode != "help" and not any(mode in r for r in work_rows):
        add("ATTENTION", f"tableau --work : le mode {mode} n'y figure pas")

# 5. Base de connaissances : index, fiches, fraîcheur
if exists("references/kb/INDEX.md"):
    index = read("references/kb/INDEX.md")
    for row in re.findall(r"^\| `([^`]+)` \|.*\| (\d{4}-\d{2}-\d{2}) \|\s*$", index, re.M):
        path, date = row
        if not exists(path):
            add("BLOQUANT", f"INDEX.md : fiche introuvable {path}")
        age = (TODAY - datetime.date.fromisoformat(date)).days
        if age > 182:
            add("ATTENTION", f"INDEX.md : {path} récupérée il y a {age} jours (> 6 mois), à revérifier")
    if exists("references/kb/projets"):
        for f in os.listdir(os.path.join(ROOT, "references/kb/projets")):
            if f.endswith(".md") and f"projets/{f}" not in index:
                add("ATTENTION", f"fiche projet absente de l'index : projets/{f}")
        for f in os.listdir(os.path.join(ROOT, "references/kb/projets")):
            if f.endswith(".md"):
                size = os.path.getsize(os.path.join(ROOT, "references/kb/projets", f))
                if size > 4000:
                    add("SUGGESTION", f"fiche projets/{f} : {size} octets, viser 1–2 Ko")
else:
    add("ATTENTION", "references/kb/INDEX.md absent")

# 6. Tests
evals = os.path.join(ROOT, "evals")
covered = set()
if os.path.isdir(evals):
    for case in sorted(os.listdir(evals)):
        d = os.path.join(evals, case)
        if not os.path.isdir(d):
            continue
        for need in ("prompt.md", "case.yaml"):
            if not os.path.exists(os.path.join(d, need)):
                add("ATTENTION", f"test {case} : {need} manquant")
        if not os.path.isdir(os.path.join(d, "graders")) or not os.listdir(os.path.join(d, "graders")):
            add("ATTENTION", f"test {case} : aucun grader")
        if os.path.exists(os.path.join(d, "prompt.md")):
            pm = re.search(r"/42 (\w+)", open(os.path.join(d, "prompt.md"), encoding="utf-8").read())
            if pm:
                covered.add(pm.group(1) if pm.group(1) in table_modes else "doc (mode deviné)")
    add("INFO", "modes couverts par les tests : " + (", ".join(sorted(covered)) or "aucun"))
    for mode in table_modes:
        if mode not in covered:
            add("SUGGESTION", f"aucun test pour le mode {mode}")
else:
    add("SUGGESTION", "aucun dossier evals/ : le skill n'a pas de tests")

# 7. Taille des fichiers de référence
for f in sorted(os.listdir(os.path.join(ROOT, "references"))):
    if f.endswith(".md"):
        n = read(f"references/{f}").count("\n")
        if n > 300:
            add("SUGGESTION", f"references/{f} : {n} lignes, envisager une table des matières ou un découpage")

order = {"BLOQUANT": 0, "ATTENTION": 1, "SUGGESTION": 2, "INFO": 3}
print(f"Audit mécanique de {ROOT} ({TODAY})")
for level, msg in sorted(findings, key=lambda x: order[x[0]]):
    print(f"[{level}] {msg}")
counts = {k: sum(1 for l, _ in findings if l == k) for k in order}
print(f"Total : {counts['BLOQUANT']} bloquant(s), {counts['ATTENTION']} attention, {counts['SUGGESTION']} suggestion(s)")
