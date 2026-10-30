# /42 vs — comparer pour choisir

> Mode déjà rapide : `--work` est sans objet. Options communes : voir `SKILL.md`.

But : l'étudiant hésite entre deux notions (ou trois, quatre au plus) et veut savoir laquelle prendre, maintenant : `/42 vs list tuple`, `/42 vs malloc calloc`, `/42 vs read fgets`, `/42 vs "liste chaînée" tableau`.

## Entrée

Les notions à comparer sont les mots du sujet. Une notion de plusieurs mots est entre guillemets, ou séparée des autres par `/` ou `,`. S'il n'y a qu'une notion, compare-la à son alternative la plus courante et dis-le en une ligne. Si le langage est ambigu, prends le plus probable d'après la conversation et indique-le dans le titre.

## Format

```
## <a> vs <b>

| | `a` | `b` |
|---|---|---|
| Ce que c'est | | |
| Syntaxe | | |
| … | | |
| Quand le choisir | | |

**Pièges** : 1–3 lignes.
**Verdict** : `a` si …, `b` si … (une ligne).
```

Choisis 4 à 8 lignes de tableau parmi celles qui départagent vraiment : syntaxe, retour et erreurs, coût (temps, mémoire), mutabilité, initialisation, sécurité, portabilité, autorisée ou non dans les projets 42. N'ajoute pas une ligne où les deux colonnes disent la même chose.

Si un exemple court montre la différence mieux que le tableau (le contenu de la mémoire après `malloc` et après `calloc`), ajoute-le sous le tableau, en quelques lignes, avec sa sortie réelle.

## Règles

- **Vérifie** ce qui peut l'être : exécute les exemples, lis les pages `man` locales. Une différence de comportement annoncée doit être constatée.
- Pas d'intro, pas de conclusion en dehors du verdict.
- Si le choix dépend d'une contrainte du sujet (fonction non autorisée, structure imposée), le verdict le dit.
