# /42 cheat — antisèche d'un thème

> Mode déjà rapide : `--work` est sans objet. Options communes : voir `SKILL.md`.

But : `doc --work` couvre une fonction ou une commande ; `cheat` couvre **toute une famille** sur un ou deux écrans, pour l'avoir sous les yeux pendant qu'on code : `/42 cheat méthodes str python`, `/42 cheat gdb`, `/42 cheat options valgrind`, `/42 cheat formats printf`, `/42 cheat git`.

## D'abord : l'antisèche existe-t-elle déjà ?

Les antisèches déjà faites sont dans le dossier `cheats/` du skill, listées dans `cheats/INDEX.md`. Lis l'index avant de rédiger quoi que ce soit, et compare le thème demandé aux colonnes « Thème » et « Aussi demandée comme ».

- **Elle existe** : affiche-la telle quelle, sans revérifier les exemples (ils l'ont été à sa création). Ajoute seulement une ligne en tête : « Antisèche enregistrée du <date> ; `/42 cheat --web <thème>` ou « mets-la à jour » pour la refaire. »
- **Elle a plus de 6 mois**, ou l'outil installé a une version majeure différente de celle de l'index (`gdb --version`, `python3 --version`) : affiche-la, et propose en une ligne de la mettre à jour.
- **L'étudiant demande une mise à jour**, ou ajoute `--web` : refais-la (section suivante) et remplace le fichier.
- **Elle n'existe pas** : fais-la, puis enregistre-la (dernière section).

## Contenu

- Les éléments les plus utilisés d'abord ; laisse de côté ce qui sert rarement (une ligne « Aussi : … » peut les citer en fin de groupe).
- Regroupe par usage (« chercher », « découper », « transformer » pour les chaînes ; « lancer », « s'arrêter », « inspecter » pour `gdb`).
- Un tableau par groupe : `syntaxe` | effet | exemple court (avec son résultat si utile).
- Termine par **Pièges** : 1–3 lignes.

Vise 15 à 40 lignes de tableau en tout. Si le thème est trop large (`cheat python`), propose 2–3 thèmes plus étroits en une ligne et fais le plus probable.

## Format

```
# Antisèche : <thème>

### <groupe 1>
| Syntaxe | Effet | Exemple |
|---|---|---|

### <groupe 2>
…

**Pièges** : …
```

## Règles

- **Vérifie** : exécute les exemples, consulte `man` ou `help()` pour les options et les signatures. Une ligne fausse dans une antisèche est recopiée des dizaines de fois.
- Pour un thème lié à un projet 42 (`cheat push_swap`), l'antisèche liste les règles, les opérations et les commandes de test, jamais l'algorithme de la solution (règle de l'easter-egg).

## Enregistrer

Après une nouvelle antisèche ou une mise à jour, si le dossier du skill est modifiable :
1. écris-la dans `cheats/<thème>.md`. Le nom du fichier est en minuscules, sans accents ni mots vides, avec des tirets : `méthodes str python` → `str-python.md`, `options valgrind` → `valgrind.md` ;
2. commence le fichier par une ligne « Vérifiée avec <outil et version>, le <date> » ;
3. ajoute ou mets à jour sa ligne dans `cheats/INDEX.md`, avec 2–3 autres façons de la demander ;
4. si le skill est dans un dépôt git, dis-le en une ligne et propose de commiter et pousser : sinon, la fiche disparaît avec la session.

Si le dossier n'est pas modifiable (skill installé dans un compte), propose plutôt d'envoyer l'antisèche comme fichier `<thème>.md` à l'étudiant.
