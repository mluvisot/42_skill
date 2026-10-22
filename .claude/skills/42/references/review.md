# /42 review — revue de projet + tests unitaires

> Avec `--work` : garde les vérifications et les tests, mais le rapport se limite au verdict, aux problèmes et au tableau des tests ; pas de section « Questions qu'un correcteur te poserait ». Options communes : voir `SKILL.md`.

But : faire ce que ferait un correcteur exigeant, avant la vraie évaluation, pour que l'étudiant découvre ses erreurs lui-même plutôt qu'en soutenance.

## Déroulé

1. **Rassembler le contexte.** Le code (fichiers joints, dossier, ou collé), et si possible le sujet PDF : il donne les fonctions autorisées, les fichiers à rendre, le comportement attendu. Sans sujet, base-toi sur ce que tu connais du projet et dis-le.

2. **Vérifications automatiques** (si un shell est disponible). Le script `scripts/review.sh <dossier_du_projet>` fait la base en une fois :
   - norminette (installée via `pip install norminette` si absente),
   - `make`, puis second `make` pour détecter le relink, puis `make fclean`,
   - symboles externes (`nm -u`) à comparer aux fonctions autorisées du sujet.
   Lis sa sortie, ne la recopie pas brute : traduis chaque erreur en explication.

3. **Revue manuelle.** Avec `references/norm.md` en tête (Norme v4.1 ; contrôle à la main les règles marquées (\*), que norminette ne vérifie pas) et la fiche du projet si elle existe dans `references/kb/` : ce que norminette ne voit pas (fuites, cas limites, robustesse, lisibilité, découpage des fonctions, noms).

4. **Tests unitaires.** Écris les tests dans un dossier `tests/` **à côté du projet** (jamais au milieu des sources à rendre) : `tests/test_<projet>.c`, plus un `tests/run.sh` qui compile et lance tout. Ils doivent :
   - comparent au comportement de la libc quand il existe un équivalent (`ft_strlen` vs `strlen`, `ft_printf` vs `printf` en comparant la valeur de retour et la sortie),
   - couvrent les cas limites : `NULL` (quand le sujet en parle), chaîne vide, un seul caractère, très grandes entrées, `INT_MIN`/`INT_MAX`, `0`, négatifs, bases invalides…,
   - pour get_next_line : plusieurs `BUFFER_SIZE` (1, 42, 10000000), fichier vide, sans `\n` final, fd invalide,
   - tournent sous `valgrind --leak-check=full --show-leak-kinds=all --error-exitcode=42` (l'étudiant est sous Linux).
   Compile et exécute-les. Rapporte les résultats réels (✅/❌), pas des suppositions.
   Le dossier `tests/` reste à l'étudiant : écris-le à côté de son projet (directement dans son dossier s'il est accessible depuis son ordinateur, sinon envoie les fichiers). Ce ne sont pas des solutions, il peut les garder et les relancer après chaque modification avec `bash tests/run.sh`. Rappelle-lui de ne pas mettre `tests/` dans le dépôt de rendu (ou de l'ajouter au `.gitignore`), car les fichiers en trop peuvent coûter l'évaluation.

5. **Rapport.** Format ci-dessous.

## Ce que tu donnes (et ce que tu ne donnes pas)

Sans `/easter-egg` : pour chaque problème, dis **où** (fichier:ligne ou fonction), **quoi** (la règle ou le type de bug) et **pourquoi** c'est un problème, puis un **indice** pour corriger. N'écris pas la version corrigée de sa fonction. Pour une erreur purement de forme (espace, tabulation, nom), tu peux montrer la forme correcte d'une ligne : ce n'est pas la solution du problème.

Avec `/easter-egg` : tu peux fournir les corrections complètes, chacune expliquée.

## Format du rapport

```
## Revue — <nom du projet>

**Verdict** : prêt pour l'évaluation / presque / pas encore
<une phrase de synthèse>

### 🔴 Bloquant (note 0 en évaluation)
Norm, compilation, relink, fuite mémoire, segfault, fonction interdite, fichier manquant.
- `fichier.c:42` — <problème> → <pourquoi> · 💡 <indice>

### 🟠 À corriger
Cas limites ratés, comportement différent de la libc, robustesse.

### 🟢 Suggestions
Lisibilité, découpage, noms, simplifications.

### 🧪 Tests unitaires
| Test | Attendu | Obtenu | |
|---|---|---|---|
| ft_strlen("") | 0 | 0 | ✅ |

### ❓ Questions qu'un correcteur te poserait
2–3 questions sur des choix du code (« Pourquoi ce malloc de len + 1 ? »).
```

Classe correctement : une erreur de Norm est bloquante à 42 même si elle paraît cosmétique — dis-le, c'est une information utile pour l'étudiant.
