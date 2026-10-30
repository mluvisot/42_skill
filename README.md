# Skill 42

Skill Claude Code d'assistance pédagogique pour l'École 42 (`/42 <mode> [options] <sujet>`) : leçons, revue Norm et tests, simulation de soutenance, entraînement aux examens, debug, antisèches… Il explique et fait comprendre plutôt que de donner des solutions toutes faites.

📂 **Le skill est ici : [`skills/42/`](skills/42/)** — point d'entrée [`SKILL.md`](skills/42/SKILL.md), modes dans [`references/`](skills/42/references/), antisèches dans [`cheats/`](skills/42/cheats/).

Exemples : `/42 doc --work malloc`, `/42 doc --work --from c dictionnaire python`, `/42 err "<message>"`, `/42 vs list tuple`, `/42 cheat gdb`, `/42 test ft_atoi`, `/42 q quel header pour write`, `/42 review ./libft`, `/42 summary --exercice ex03`, `/42 summary --project minishell`, `/42 exam`, `/42 help`.

## Installation

### Dans le chat claude.ai (le plus simple)

1. Télécharge **[42-skill.zip](https://github.com/mluvisot/42_skill/releases/latest/download/42-skill.zip)**.
2. Sur claude.ai : **Paramètres → Capacités**, active **Exécution de code / création de fichiers**.
3. Dans **Skills**, clique **Importer un skill** et choisis le ZIP.

Écris ensuite `/42 help`, ou parle simplement de la Norm, de libft, d'un examen… Dans le chat, `/42 review` n'a pas `norminette` ni accès à ta machine : colle ton code ou joins les fichiers. Pour mettre à jour, retélécharge le ZIP et réimporte-le.

### Dans Claude Code, en une commande

```sh
mkdir -p ~/.claude/skills && curl -fsSL https://github.com/mluvisot/42_skill/releases/latest/download/42-skill.zip -o /tmp/42-skill.zip && unzip -oq /tmp/42-skill.zip -d ~/.claude/skills
```

La commande `/42` est alors disponible dans tous tes projets. Relance la même commande pour mettre à jour.

### Comme plugin (recommandé : mises à jour en une commande)

Dans une session Claude Code :

```
/plugin marketplace add mluvisot/42_skill
/plugin install 42@mluvisot-42
```

Le skill s'appelle alors `/42:42 <mode> …` (préfixe du plugin), et Claude le déclenche aussi tout seul dès que tu parles de 42, de la Norm ou d'un projet.

**Mettre à jour** : `/plugin marketplace update mluvisot-42`, ou une fois pour toutes `/plugin` → **Marketplaces** → `mluvisot-42` → **Enable auto-update**.

Sans clé SSH GitHub sur ta machine, lance Claude Code avec `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1`.

### Comme skill personnel, avec git (commande `/42` sans préfixe)

```sh
git clone https://github.com/mluvisot/42_skill.git ~/.claude/42_skill
mkdir -p ~/.claude/skills
ln -s ~/.claude/42_skill/skills/42 ~/.claude/skills/42
```

**Mettre à jour** : `git -C ~/.claude/42_skill pull`.

Dans ce dépôt lui-même, le skill est chargé automatiquement depuis `.claude/skills/42/` (lien vers `skills/42/`).

## Documents de 42

Le dépôt ne contient aucun document de 42 : ni le texte de la Norme, ni les sujets de l'intra. `references/norm.md` résume la Norme v4.1 avec les numéros de page ; le PDF officiel est dans le dossier `pdf/` de [42School/norminette](https://github.com/42School/norminette). Les fiches projet que tu crées à partir de tes sujets (`references/kb/projets/`) et les sources que tu y déposes (`references/kb/sources/`) sont ignorées par git et restent sur ta machine.

## Licence

[MIT](LICENSE).
