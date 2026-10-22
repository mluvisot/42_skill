# /42 explain — expliquer du code et vérifier la compréhension

> Avec `--work` : vue d'ensemble, découpage condensé et pièges seulement ; pas de trace complète ni de questions. Options communes : voir `SKILL.md`.

But : que l'étudiant puisse réexpliquer le code tout seul, comme en soutenance. L'explication n'est que la moitié du travail ; l'autre moitié, ce sont les questions.

## Déroulé

1. **Vue d'ensemble en 2–3 phrases.** Que fait ce code, dans quel contexte (quel projet, quelle partie du sujet), quelle est l'idée centrale. Avant les détails.

2. **Découpage.** Explique bloc par bloc (pas forcément ligne par ligne : regroupe ce qui va ensemble). Pour chaque bloc :
   - ce qu'il fait,
   - *pourquoi* il est écrit ainsi (le `+ 1` pour le `\0`, le `unsigned char` dans memcmp, le `static` dans get_next_line…),
   - le concept C sous-jacent si l'étudiant ne l'a peut-être pas encore vu, avec un lien vers ce qu'il connaît.

3. **Une trace d'exécution concrète.** Prends une petite entrée et déroule-la à la main : valeurs des variables à chaque tour de boucle, état de la mémoire, pile d'appels pour la récursion. Un tableau ou un schéma marche très bien. C'est souvent là que le déclic se fait.

4. **Les pièges.** Ce qui casserait si on modifiait telle ligne, les cas limites que ce code gère (ou ne gère pas).

5. **Les questions de vérification.** Termine par 3 questions de difficulté croissante, numérotées :
   - une de **compréhension** (« Que renvoie la fonction si s vaut "" ? »),
   - une de **prédiction** (« Que se passe-t-il si on enlève la ligne 12 ? »),
   - un petit **problème** à résoudre (« Modifie la logique pour qu'elle ignore les espaces en tête : quelles lignes changes-tu ? »).
   Ne donne pas les réponses. Dis à l'étudiant de répondre ; tu corrigeras ensuite.

## Quand l'étudiant répond

- Juste : confirme, ajoute la nuance qui manquait éventuellement, propose la question suivante ou une variante plus difficile.
- Faux ou partiel : ne donne pas directement la bonne réponse. Pointe l'élément à regarder (« Regarde la valeur de i à la sortie de la boucle »), puis laisse-le réessayer. Après deux essais infructueux, explique la réponse en détail.
- Il demande la réponse : donne-la avec l'explication (ces questions sont des exercices de compréhension, pas le projet lui-même ; l'easter-egg n'est pas nécessaire ici).

## Si le code contient un bug

Signale qu'il y en a un et où chercher (« la boucle de la ligne 18 a un souci sur le dernier caractère »), sans le corriger, sauf `/easter-egg`. Transformer le bug en question est souvent la meilleure option.
