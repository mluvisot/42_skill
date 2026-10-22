# /42 summary — traduire et résumer un sujet PDF de 42

> Avec `--work` : seulement le tableau 📦 Rendu, la partie obligatoire et les pièges. Options communes : voir `SKILL.md`.

But : en quelques minutes, l'étudiant sait exactement ce qu'on attend de lui, sans rien rater d'important. Les sujets 42 sont en anglais et les détails qui coûtent la note (fonctions autorisées, fichiers à rendre, comportement attendu) sont dispersés.

## Lecture

Lis le PDF entier, y compris les petites lignes : chapitres « Common Instructions », « Mandatory part », « Bonus part », « Submission and peer-evaluation », et les tableaux (nom du programme, fichiers à rendre, Makefile, arguments, fonctions externes autorisées, libft autorisée ou non). Si le PDF est scanné ou mal extrait, regarde les pages en image.

## Traduction

Traduis en français, fidèlement. Garde en anglais (avec traduction entre parenthèses la première fois) les termes qui apparaissent tels quels dans le code ou en évaluation : noms de fonctions, de fichiers, de règles du Makefile, messages d'erreur attendus (ex. `Error\n`). Ne traduis jamais un exemple de sortie attendue : il doit rester exact au caractère près.

## Format de sortie

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

Le résumé doit être nettement plus court que le sujet. Si le sujet contient une instruction inhabituelle ou ambiguë, signale-la plutôt que de l'interpréter en silence.

Le résumé est souvent quelque chose qu'on garde pendant tout le projet : s'il est long, propose de le mettre dans un document.
