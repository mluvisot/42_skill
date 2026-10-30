# /42 dev — audit et amélioration du skill lui-même

But : garder le skill 42 cohérent à mesure qu'il grandit. Ce mode ne s'adresse pas à l'apprentissage de 42 : il audite **les fichiers du skill** (SKILL.md, `references/`, `scripts/`, `evals/`), repère les incohérences et propose des améliorations. Il ne modifie rien sans l'accord de l'étudiant.

Le dossier du skill est le « base directory » donné au chargement du skill.

## Syntaxe

- `/42 dev` ou `/42 dev audit` : audit complet.
- `/42 dev <mode ou fichier>` (`/42 dev exam`, `/42 dev norm.md`) : audit centré sur ce mode ou ce fichier, et sur tout ce qui s'y réfère.
- `--work` : seulement la liste des problèmes, sans les propositions détaillées.
- `--web` : vérifie aussi que les sources de `references/kb/` sont toujours à jour (comme la vérification semestrielle).

## Étape 1 — vérifications mécaniques

Si un shell est disponible, lance `python3 scripts/audit.py <dossier_du_skill>`. Il contrôle :
- la description (longueur, caractères interdits) et la taille de SKILL.md ;
- que chaque mode de la table a son fichier de référence, figure dans la description et dans le tableau `--work` ;
- que chaque chemin cité (`references/…`, `scripts/…`) existe ;
- l'index de la base : fiches présentes, âge de plus de 6 mois, fiches non indexées, taille ;
- les tests : format des cas, modes non couverts.

Ses constats sont des faits : reprends-les tels quels dans le rapport, sans les reformuler en suppositions.

## Étape 2 — relecture

Lis SKILL.md et les fichiers concernés (tout, pour un audit complet). Cherche ce que le script ne voit pas :

- **Contradictions** : deux fichiers qui disent l'inverse (une règle de la Norme différente entre `norm.md` et un mode, un comportement par défaut annoncé différemment dans SKILL.md et dans le fichier du mode, la règle de l'easter-egg appliquée différemment).
- **Options** : chaque option commune (niveau, `--work`, `--web`) est-elle prise en compte dans chaque mode, ou explicitement déclarée sans objet ?
- **Règles 42 périmées** : une affirmation sur 42 (Norme, cursus, projets, examens) qui contredit `references/kb/` ou qui n'a pas de source.
- **Instructions mortes ou floues** : une consigne qu'aucun cas réel ne déclenche, une consigne ambiguë qu'on peut lire de deux façons, un format de sortie qui n'est pas défini.
- **Doublons** : la même consigne répétée dans plusieurs fichiers (risque de divergence) ; propose de la garder à un seul endroit.
- **Coût** : un fichier lu à chaque appel alors qu'il ne sert qu'à un mode ; une section longue qui pourrait passer en fiche ou en script.
- **Ton et forme** : consignes en majuscules impératives sans explication, au lieu d'expliquer pourquoi.

## Étape 3 — rapport

```
## Audit du skill 42 — <date>

**État** : sain / à corriger / bloquant
<une phrase>

### 🔴 Bloquant
Ce qui casse le skill ou l'empaquetage (chemin introuvable, description refusée…).
- `fichier` — problème → conséquence

### 🟠 Incohérences
- `fichier A` dit … ; `fichier B` dit … → laquelle garder et pourquoi

### 🟢 Améliorations proposées
Classées par utilité. Pour chacune : le problème, la modification proposée (texte exact à remplacer et texte nouveau, ou nouveau fichier), et ce que ça change à l'usage.

### 🧪 Tests
Modes ou comportements non couverts, et 1–2 cas de test proposés.
```

Garde le rapport lisible : au plus une dizaine d'améliorations, les plus utiles d'abord.

## Étape 4 — appliquer (seulement si l'étudiant le demande)

L'étudiant choisit les améliorations à appliquer (« applique 1, 3 et 4 »). Alors :
1. copie le skill dans un dossier modifiable (le dossier installé peut être en lecture seule) ;
2. applique seulement les modifications choisies ;
3. relance `scripts/audit.py` sur la copie : aucun nouveau constat bloquant ne doit apparaître ;
4. empaquette avec le skill-creator s'il est disponible (`python -m scripts.package_skill <copie>` depuis son dossier) et envoie le fichier `.skill` à l'étudiant, qui l'installe lui-même ;
5. résume en quelques lignes ce qui a changé.

Ne change pas le nom du skill ; ne touche pas aux fiches de `references/kb/` sans nouvelle source.
