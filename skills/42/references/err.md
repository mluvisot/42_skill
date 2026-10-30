# /42 err — traduire un message d'erreur

> Mode déjà rapide : `--work` est sans objet. Options communes : voir `SKILL.md`.

But : l'étudiant colle une erreur (`cc`, `make`, `norminette`, `valgrind`, `gdb`, traceback Python, message du shell) et veut savoir en un message ce qu'elle veut dire et où regarder. `debug` est un parcours guidé en plusieurs étapes ; `err` est une réponse unique.

## Entrée

Le `<sujet>` est le message d'erreur, collé tel quel. S'il manque, demande-le en une ligne. Le code et la commande lancée sont utiles mais pas obligatoires : sans eux, réponds avec la cause la plus probable et dis ce qui permettrait de trancher.

Si un shell est disponible et que le code est accessible, reproduis l'erreur avant d'affirmer sa cause.

## Lire la bonne ligne

- **`cc`** : `fichier.c:ligne:colonne: error:`. Traite la **première** erreur : les suivantes en découlent souvent (un `;` oublié en provoque dix).
- **`valgrind`** : la première ligne de la pile (`at …` / `by …`) qui pointe vers un fichier de l'étudiant, pas vers la libc. Pour une fuite, la ligne du `malloc` d'origine.
- **Traceback Python** : la dernière ligne donne le type d'erreur ; la dernière frame qui pointe vers le code de l'étudiant donne l'endroit.
- **`norminette`** : le code de l'erreur (`TOO_MANY_LINES`, `SPACE_BEFORE_FUNC`…) et sa position ; relie-le à la règle de `references/norm.md`, avec sa page.
- Plusieurs erreurs du même type : regroupe-les en une seule entrée.

## Format

```
## <outil> : <message abrégé>

**Ce que ça veut dire** : 1–2 phrases, en français simple.
**Cause probable** : 1–3 causes, de la plus probable à la moins probable.
**Où regarder** : fichier:ligne, fonction ou zone.
**Pour confirmer** : la commande ou la vérification qui tranche (`cc -g -fsanitize=address`, `valgrind --track-origins=yes`, `print(type(x))`…).
```

Si l'erreur ne se localise pas sans enquête (crash sans trace, mauvaise sortie), termine par une ligne qui propose `/42 debug`.

## Règle de l'easter-egg

Pour une erreur de forme ou de syntaxe (point-virgule, indentation, espace exigé par la Norme, import manquant), tu peux montrer la ligne corrigée : ce n'est pas la solution du problème. Pour une erreur de logique dans un projet ou un exercice 42, dis où et de quel type est le bug, pas le code corrigé, sauf `/easter-egg`.
