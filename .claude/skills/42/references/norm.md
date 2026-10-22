# La Norme de 42 — v4.1 (fiche)

Source : Norme v4.1, dépôt officiel https://github.com/42School/norminette, dossier `pdf/` (récupérée le 22.10.2026). Texte original : `references/kb/sources/norme_v4.1_fr.txt` ; chaque section ci-dessous indique sa page, à relire en cas de doute ou de contestation.

## Essentiel
- `norminette` fait foi sur ce qu'elle contrôle (sauf règle locale du campus). Si elle est disponible, lance-la ; cette fiche sert à expliquer les erreurs et à vérifier le reste.
- Les règles marquées **(\*)** ne sont **pas** vérifiées par norminette mais peuvent valoir un **flag Norme** si le correcteur les voit : `review` et `defense` doivent les contrôler à la main.
- Interdits : `for`, `do…while`, `switch`, `case`, `goto`, **tout ternaire** (`? :`), VLA, type implicite.
- Fonction : 25 lignes, 4 paramètres, 5 variables. Fichier : 5 fonctions. Ligne : 80 colonnes.
- Un fichier qui ne compile pas n'est pas censé passer la Norme.

## Nommage (p. 5)
- Préfixes : `s_` structure, `t_` typedef, `u_` union, `e_` enum, `g_` globale.
- Identifiants, fichiers et dossiers : minuscules, chiffres et `_` uniquement (snake_case).
- Caractères hors ASCII standard interdits, sauf dans les chaînes et caractères littéraux.
- (\*) Noms explicites ou mnémoniques, lisibles en anglais (y compris macros, fichiers, dossiers).
- Variables globales non `const` ni `static` interdites, sauf si le sujet les autorise.

## Mise en forme (p. 6–7)
- 25 lignes max par fonction (accolades de la fonction non comptées).
- 80 colonnes max, commentaires compris ; une tabulation compte pour sa largeur.
- Une ligne vide entre deux fonctions.
- Indentation : vraies tabulations de largeur 4 (ASCII 9), jamais des espaces.
- Blocs entre accolades indentés ; accolades seules sur leur ligne, sauf dans la déclaration d'un `struct`, `enum`, `union`.
- Ligne vide vraiment vide ; aucun espace ou tabulation en fin de ligne.
- Jamais deux lignes vides d'affilée, jamais deux espaces d'affilée.
- Déclarations en début de fonction, une par ligne, noms de variables alignés sur la même colonne dans leur portée.
- `*` collé au nom de la variable.
- Pas de déclaration + initialisation sur la même ligne, sauf globales (si autorisées), `static` et constantes.
- Une ligne vide entre les déclarations et le reste de la fonction ; aucune autre ligne vide dans la fonction.
- Une instruction ou structure de contrôle par ligne : pas d'affectation dans une condition, pas d'affectations multiples.
- Une instruction coupée sur plusieurs lignes : lignes suivantes indentées, opérateur en début de nouvelle ligne.
- Espace après chaque virgule et point-virgule (sauf en fin de ligne) ; un seul espace autour de chaque opérateur.
- Espace après chaque mot-clé C, sauf les types (`int`, `char`…) et `sizeof`.
- Accolades obligatoires sur `if`, `while`…, sauf instruction unique sur une seule ligne.

## Fonctions (p. 8)
- 4 paramètres nommés max ; paramètres nommés dans les prototypes.
- Sans argument : prototype explicite avec `void`.
- 5 variables max par fonction.
- `return (valeur);` entre parenthèses ; `return ;` si la fonction ne renvoie rien.
- Une seule tabulation entre le type de retour et le nom de la fonction.

## typedef, struct, enum, union (p. 9)
- Espace entre `struct` / `enum` / `union` / `typedef` et le nom ; indentation habituelle pour les noms.
- Noms de structures alignés sur la même colonne dans leur portée.
- **Pas de déclaration de structure dans un `.c`.**

## Headers (p. 10)
- (\*) Un `.h` ne contient que : inclusions, déclarations, defines, prototypes, macros.
- Tous les `#include` en début de fichier ; jamais d'inclusion d'un `.c`.
- Protection contre la double inclusion : pour `ft_foo.h`, la macro est `FT_FOO_H` (`#ifndef FT_FOO_H` / `# define FT_FOO_H`).
- (\*) Inclure un header inutilisé est interdit.

## Header 42 (p. 11)
- Chaque `.c` et `.h` commence par le header standard 42.
- (\*) Il doit être à jour : créateur (login et e-mail étudiant), date de création, login et date de dernière modification.

## Macros et préprocesseur (p. 12)
- (\*) `#define` seulement pour des valeurs littérales et constantes ; (\*) aucun `#define` pour contourner la Norme ou obscurcir le code.
- (\*) Macros de la bibliothèque standard seulement si elles sont autorisées par le sujet.
- Pas de macro multiligne ; noms de macros en MAJUSCULES.
- Directives indentées à l'intérieur des blocs `#if` / `#ifdef` / `#ifndef`.
- Préprocesseur interdit hors de la portée globale.

## Interdits (p. 13)
`for`, `do…while`, `switch`, `case`, `goto`, opérateurs ternaires, VLA, type implicite dans une déclaration.

## Commentaires (p. 14)
- Pas de commentaire dans le corps d'une fonction ; commentaire en fin de ligne ou sur sa propre ligne.
- (\*) En anglais et utiles.
- (\*) Un commentaire ne justifie pas une fonction fourre-tout (`f1`, `a`, `b`…) ni une fonction créée seulement pour contourner la Norme.

## Fichiers (p. 15)
- Pas d'inclusion d'un `.c` dans un `.c`.
- 5 définitions de fonctions max par `.c`.

## Makefile (p. 16)
Non vérifié par norminette ; contrôlé pendant l'évaluation. Sauf instruction du sujet :
- Règles obligatoires : `$(NAME)`, `all`, `clean`, `fclean`, `re` ; `all` est la règle par défaut (`make` seul).
- **Relink inutile = projet considéré comme non fonctionnel.**
- Projet à plusieurs binaires : une règle par binaire, et `all` les compile tous.
- Bibliothèque non système fournie avec le code (ex. libft) : le Makefile doit la compiler automatiquement.
- Tous les fichiers sources nommés explicitement : pas de `*.c`, `*.o` ni autre wildcard.
