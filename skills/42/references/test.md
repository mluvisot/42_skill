# /42 test — les cas à tester

> Mode déjà rapide : `--work` est sans objet. Options communes : voir `SKILL.md`.

But : l'étudiant veut savoir **quoi tester** sur une fonction ou un programme, sans revue complète : `/42 test ft_atoi`, `/42 test get_next_line`, `/42 test ./push_swap`, `/42 test ma fonction python parse_args`. `review` fait tout (Norme, Makefile, tests, rapport) ; `test` ne donne que les cas.

## Les cas

Classe-les par catégorie, dans cet ordre :
1. **Nominal** : 2–3 cas simples qui doivent marcher.
2. **Limites** : vide, un seul élément, `0`, négatifs, `INT_MIN` / `INT_MAX`, très grandes entrées, espaces et signes multiples, chaîne sans `\n` final…
3. **Erreurs** : mauvaise entrée, mauvais nombre d'arguments, `NULL` (seulement si le sujet en parle), fd invalide, fichier absent.
4. **Mémoire et ressources** : à lancer sous `valgrind --leak-check=full` ; fd fermés ; pour get_next_line, plusieurs `BUFFER_SIZE` (1, 42, 10000000).

Vise 8 à 15 cas. Chaque cas a un **attendu exact**, qui vient :
- de la fonction d'origine quand elle existe (`atoi`, `strlen`, `printf`) : **exécute-la** pour obtenir l'attendu, ne le devine pas ;
- sinon du sujet (cite la page si une fiche existe dans `references/kb/`) ;
- sinon marque-le « à vérifier dans le sujet ».

## Format

```
## Cas de test : <fonction ou programme>

| # | Entrée | Attendu | Pourquoi ce cas |
|---|---|---|---|
| 1 | `ft_atoi("42")` | `42` | nominal |
| 2 | `ft_atoi("  -+42")` | `0` | deux signes : atoi s'arrête |
```

Les sorties de programme s'écrivent au caractère près, avec `| cat -e` quand les fins de ligne comptent.

## Avec le code de l'étudiant

Si son code est accessible et qu'un shell est disponible, lance les cas et ajoute une colonne **Obtenu** (✅ / ❌). Ne corrige pas : un ❌ dit quel cas échoue, pas comment réparer (règle de l'easter-egg).

À la fin, propose en une ligne d'écrire ces cas dans un `tests/run.sh` qu'il pourra relancer, placé **à côté** du dossier du projet, pas dedans (même règle que `references/review.md`).
