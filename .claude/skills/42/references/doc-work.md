# /42 doc --work — fiche de travail rapide

But : l'étudiant est **en train de coder** et veut une réponse utilisable tout de suite (« /42 doc --work malloc », « /42 doc --work print python », « /42 doc --work git rebase »). Il ne cherche pas à apprendre le sujet en profondeur : il veut savoir comment l'utiliser correctement, maintenant. Pense à une bonne page de référence, ou à un collègue qui répond sans faire de cours.

Ce mode remplace la leçon : pas d'intro, pas de partie Explications, pas de questions de vérification, pas d'invitation à `/42 resume`. Les niveaux (`--beginner`, `--expert`…) ne s'appliquent pas ici ; s'il y en a un, ignore-le.

Le sujet peut être n'importe quoi d'utile au travail : une fonction C ou de la libc, un appel système, une fonction Python ou JavaScript, une commande shell, une option de `cc`, un outil (`valgrind`, `git`, `make`), une notion courte. Si le langage est ambigu (`print`), prends le plus probable vu la demande ou la conversation et indique-le dans le titre.

## Format

Titre : le nom du sujet, puis une ligne « Mode : work » (avec « · web » si `--web`).

### Description
1–2 phrases : ce que ça fait et quand on s'en sert.

### Syntaxe
Le prototype ou la signature dans un bloc de code, avec ce qu'il faut pour l'utiliser (header à inclure, import, paquet). Puis, en liste courte : les paramètres, la valeur de retour, les erreurs (valeur renvoyée, `errno`, exception). Pour une commande, les options les plus utilisées.

**Liens** : 1–3 liens vers la documentation officielle (man7.org, docs.python.org, cppreference, MDN, documentation de l'outil). Sans `--web`, ne donne que des liens officiels dont tu es sûr de l'adresse ; dans le doute, donne la référence à la place (`man 3 malloc`, `help(print)`). Ne fabrique jamais d'URL.

### Exemple
Le cas le plus simple, en quelques lignes, avec sa sortie si elle aide.

### Exemple concret
Un usage réaliste, comme on l'écrit dans du vrai code : gestion d'erreur, nettoyage, bonne pratique. 5–25 lignes.

### À savoir (facultatif)
1–3 pièges ou détails qui font perdre du temps : un comportement surprenant, une erreur classique, une différence entre plateformes ou versions. Une ligne chacun.

### Avec `--from <langage>`
Sous la Syntaxe, une ligne « En <langage> : … » donne l'équivalent (ou dit qu'il n'y en a pas). Dans À savoir, au moins un piège de traduction : ce qui se ressemble dans les deux langages mais ne se comporte pas pareil. Exemple pour `--from c` sur les listes Python : « En C : un tableau de taille fixe (ou `malloc` + `realloc`) ; ici la taille s'adapte toute seule, et `b = a` ne copie pas ».

Tu peux t'écarter de ce format quand le sujet s'y prête mal : une commande peut demander un tableau d'options, une notion peut se passer de prototype. Le but reste une réponse qu'on lit en moins d'une minute et qu'on peut recopier ou adapter directement.

## Règles

- **Court.** Pas de phrase d'introduction, pas de conclusion, pas d'analogie. Une fiche qui tient sur un écran ou deux.
- **Juste.** Quand un shell est disponible, compile ou exécute les exemples avant de les donner (pour du C : `cc -Wall -Wextra -Werror`). Ça reste rapide, et un exemple qui ne compile pas fait perdre plus de temps qu'il n'en fait gagner. Les pages `man` locales font foi pour les prototypes et les retours.
- **Recherche web seulement avec `--web`.** Avec `--web`, une ou deux recherches suffisent, ciblées sur la documentation officielle : pour vérifier une signature, une version, un comportement récent, et donner des liens confirmés.
- **La règle de l'easter-egg s'applique.** L'exemple concret montre l'outil, pas la solution d'un projet 42 : si le sujet est une fonction que l'étudiant doit recoder (`ft_split`, `get_next_line`), donne la fiche de la fonction d'origine ou de la notion, pas une implémentation, sauf `/easter-egg`.
- **Suite.** Si l'étudiant pose une question après la fiche, réponds dans le même esprit : direct et court.
