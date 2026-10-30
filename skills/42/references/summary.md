# /42 summary — traduire et résumer un sujet de 42

> Options communes : voir `SKILL.md`. Ce mode a aussi ses propres options, `--exercice` et `--project` (ci-dessous).

But : en quelques minutes, l'étudiant sait exactement ce qu'on attend de lui, sans rien rater d'important. Les sujets 42 sont en anglais et les détails qui coûtent la note (fonctions autorisées, fichiers à rendre, comportement attendu) sont dispersés.

## Syntaxe

| Commande | Pour quoi | Ce que tu rends |
|---|---|---|
| `/42 summary <sujet>` | un sujet PDF (par défaut) | le résumé dans le chat, au format ci-dessous |
| `/42 summary --exercice <exercice>` | **un seul exercice** (Piscine, exam, `ex03` d'un PDF de jour, texte collé, capture d'écran) | la traduction complète de l'énoncé, puis le résumé |
| `/42 summary --project <projet>` | **un grand projet** (minishell, cub3D, ft_irc, webserv…) | un PDF du sujet entièrement traduit, et le résumé dans le chat |
| `--work` (avec n'importe laquelle) | la version courte | seulement 📦 Rendu, ✅ Partie obligatoire et ⚠️ Pièges |

Sans option, si le sujet est manifestement un exercice (un énoncé de quelques lignes, un `exNN`) ou un grand projet (sujet de plus de ~10 pages), prends l'option qui convient et dis-le en une ligne. `--exercice` et `--project` sont incompatibles : si les deux sont donnés, prends celle qui correspond au sujet et dis-le.

`--work` se combine : `--exercice --work` garde la traduction de l'énoncé (c'est le cœur de ce mode, et un énoncé est court) puis donne le résumé court ; `--project --work` produit toujours le PDF traduit, mais le résumé dans le chat est court.

## Lecture

Lis le sujet entier, y compris les petites lignes : chapitres « Common Instructions », « Mandatory part », « Bonus part », « Submission and peer-evaluation », et les tableaux (nom du programme, fichiers à rendre, Makefile, arguments, fonctions externes autorisées, libft autorisée ou non). Si le PDF est scanné ou mal extrait, regarde les pages en image.

Avec `--exercice` et un PDF de plusieurs exercices (un jour de Piscine), ne traite que l'exercice demandé (`ex03`, ou son nom) ; s'il n'est pas précisé, demande lequel en une question courte. Garde quand même les consignes générales du PDF qui s'y appliquent (Norme, `norminette`, pas de `main` rendu, etc.).

## Traduction

Traduis en français, fidèlement. Garde en anglais (avec traduction entre parenthèses la première fois) les termes qui apparaissent tels quels dans le code ou en évaluation : noms de fonctions, de fichiers, de règles du Makefile, messages d'erreur attendus (ex. `Error\n`). Ne traduis jamais un exemple de sortie attendue, un prototype ou une commande : ils doivent rester exacts au caractère près.

## `--exercice` : traduction de l'énoncé, puis résumé

Commence par l'énoncé traduit **en entier**, dans l'ordre et avec la mise en forme d'origine (en-tête de l'exercice, consignes, exemples en blocs de code inchangés) :

```
# <exNN> — <nom de l'exercice>

## 🇫🇷 Énoncé traduit
| | |
|---|---|
| Dossier de rendu | `exNN/` |
| Fichiers à rendre | |
| Fonctions autorisées | |
| Prototype | `...` |

<le texte de l'énoncé, traduit phrase par phrase>
```

Puis le résumé, au format ci-dessous, en sautant ce qui ferait doublon : le tableau 📦 Rendu est déjà dans l'énoncé (ne le répète pas), ⭐ Bonus n'existe en général pas, et 🔤 Exemples ne reprend pas les exemples déjà recopiés : il les explique en une ligne chacun.

## `--project` : PDF traduit + résumé dans le chat

1. **Le PDF traduit.** Traduis le sujet entier (pas un résumé), en gardant sa structure : chapitres, numérotation, tableaux, blocs de code et exemples de sortie inchangés, images et schémas du sujet recopiés s'il est possible de les extraire. Ajoute en tête une ligne « Traduction non officielle du sujet <projet> (version <n> si indiquée) — en cas de doute, le sujet anglais fait foi. » Produis-le avec le skill `pdf` s'il est disponible ; sinon, écris un HTML propre et convertis-le en PDF (Chromium/Playwright, `pandoc`, ou `weasyprint`, selon ce qui est installé). Relis le PDF obtenu (au moins la première page et une page avec du code) avant de l'envoyer. Nomme-le `<projet>_fr.pdf` et envoie-le à l'étudiant comme fichier. Le sujet n'est pas public : jamais d'artefact public ni de commit dans le skill (voir `references/kb/README.md`). Si aucun moyen de produire un PDF n'est disponible, dis-le en une ligne et donne la traduction en Markdown dans un fichier à la place.
2. **Le résumé dans le chat**, au format ci-dessous (court avec `--work`), qui renvoie au PDF pour le détail : « Détail complet : `<projet>_fr.pdf`, chapitre <n> ». Ne recopie pas la traduction dans le chat.

## Format du résumé

```
# <Nom du projet> — résumé du sujet

**En une phrase** : <ce qu'il faut réaliser>

## 📦 Rendu
| | |
|---|---|
| Nom du programme / de la lib | |
| Fichiers à rendre | |
| Makefile | règles demandées |
| Fonctions externes autorisées | |
| Libft autorisée | oui / non |

## ✅ Partie obligatoire
Les exigences, une par ligne, dans l'ordre du sujet.

## ⭐ Bonus
(Rappel : le bonus n'est évalué que si la partie obligatoire est parfaite.)

## ⚠️ Pièges et points d'attention
Les détails faciles à rater : comportement exact sur erreur, cas limites mentionnés, sortie attendue, contraintes de performance (nombre de coups, temps), interdictions (variables globales, etc.).

## 🔤 Exemples du sujet
Les exemples d'exécution recopiés exactement, avec une ligne d'explication chacun.

## 📚 Notions à maîtriser
Les concepts nécessaires (à étudier avec /42 explain ou /42 doc).

## 🗺️ Par où commencer
3–5 étapes suggérées.
```

Avec `--work`, garde seulement **En une phrase**, 📦 Rendu, ✅ Partie obligatoire et ⚠️ Pièges, en phrases courtes.

Le résumé doit être nettement plus court que le sujet. Si le sujet contient une instruction inhabituelle ou ambiguë, signale-la plutôt que de l'interpréter en silence.

Le résumé est souvent quelque chose qu'on garde pendant tout le projet : s'il est long (et sans `--project`, qui fournit déjà le PDF), propose de le mettre dans un document.
