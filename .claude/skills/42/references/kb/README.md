# Base de connaissances — règles d'usage

But : répondre juste en lisant le moins possible. Usage personnel de l'étudiant uniquement : ne jamais publier ni partager ce contenu (pas d'artefact public).

## Lire
1. Lis `INDEX.md` (court), puis **seulement** la fiche utile à la demande. Pour une question précise, cherche la section (Grep) au lieu de lire toute la fiche.
2. Chaque fiche commence par une section **Essentiel** : lis-la d'abord ; ne descends dans le détail que si la réponse en dépend.
3. **Point critique ou ambigu** (ce qui peut coûter la note : fichiers à rendre, fonctions autorisées, sortie exacte, limites chiffrées, règle de la Norme contestée) : relis la page indiquée dans la source originale (`sources/`, ou le PDF si l'étudiant l'a fourni) avant d'affirmer.
4. **L'outil prime sur la fiche** : `norminette` prime sur `norm.md`, une compilation ou un test réel prime sur ce qu'une fiche annonce.
5. **Fiche manquante** : dis-le en une ligne, réponds avec ce que tu sais en le signalant comme non vérifié, et propose d'ajouter la source.

## Fraîcheur
- Si la date de récupération d'une fiche utilisée a plus de **6 mois**, signale-le en une ligne (« fiche du … : la source a peut-être changé ») et propose de la mettre à jour. Une vérification semestrielle automatique existe aussi (1er février et 1er septembre).
- Si l'étudiant indique une version de sujet plus récente que celle de la fiche, la fiche est périmée : dis-le et demande le nouveau PDF.

## Ajouter une fiche projet (`projets/<projet>.md`)
À partir d'un sujet PDF fourni par l'étudiant. Format :

```
# <projet> — fiche
Source : sujet <version>, intra 42, récupéré le <date>.

## Essentiel
| | |
|---|---|
| Rendu | nom du programme / de la lib |
| Fichiers à rendre | … (exact) |
| Fonctions autorisées | … (exact) |
| Makefile | règles demandées |
| Libft autorisée | oui / non |
| Langage / normes | C + Norme, ou Python + linter… |

## Partie obligatoire (p. …)
## Bonus (p. …)
## Pièges (p. …)
## Exemples exacts (p. …)
```

- **Recopie tel quel** ce qui est vérifié au caractère près : noms de fichiers, fonctions autorisées, messages d'erreur, exemples de sortie, limites chiffrées. Le reste se reformule de façon concise.
- Indique la page de chaque section.
- Garde la fiche courte (1–2 Ko si possible). Le PDF original reste chez l'étudiant ; ne le mets pas dans le skill.
- Ajoute la ligne correspondante dans `INDEX.md` (mots-clés, version, date).
