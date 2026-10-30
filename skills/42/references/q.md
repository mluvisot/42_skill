# /42 q — question rapide

> Mode déjà rapide : `--work` est sans objet. Options communes : voir `SKILL.md`.

But : une question factuelle, une réponse immédiate : `/42 q quel header pour write`, `/42 q que renvoie pop() sur une liste vide`, `/42 q norminette compte-t-elle les accolades`.

## Format

1 à 3 lignes, sans titre ni introduction :
- la réponse, d'abord ;
- si utile, la précision qui évite l'erreur classique ;
- la référence entre parenthèses : `man 2 write`, `help(list.pop)`, `references/norm.md` p. 6, ou un lien officiel dont tu es sûr.

Exemple :

> `#include <unistd.h>`. Prototype : `ssize_t write(int fd, const void *buf, size_t count);` (`man 2 write`)

## Règles

- **Vérifie** quand c'est rapide (`man`, `python3 -c`, une compilation de deux lignes) : une réponse courte et fausse coûte plus cher qu'une réponse longue.
- Si la question demande plus que quelques lignes, donne quand même la réponse courte, puis propose en une ligne la bonne commande (`/42 doc --work …`, `/42 vs …`).
- Une question sur une règle de 42 passe par la base de connaissances (`references/kb/INDEX.md`), comme dans les autres modes.
- Si la question revient à demander la solution d'un exercice ou d'un projet 42, applique la règle de l'easter-egg : indique la notion ou la piste, pas le code.
