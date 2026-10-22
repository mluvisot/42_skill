# Antisèche : `gdb`

Vérifiée avec GNU gdb 15.1 sur un petit programme C, le 2026-10-22. Compile d'abord avec **`cc -g -O0`** : sans `-g`, gdb ne voit ni les lignes ni les noms de variables.

### Lancer
| Syntaxe | Effet | Exemple |
|---|---|---|
| `gdb ./prog` | ouvre le programme dans gdb, sans le lancer | |
| `gdb --args ./prog a b` | ouvre le programme avec ses arguments | `gdb --args ./push_swap 3 1 2` |
| `run` (`r`) | lance le programme | `run arg1 arg2`, `run < input.txt` |
| `start` | lance et s'arrête au début de `main` | |
| `kill` / `quit` (`q`) | arrête le programme / quitte gdb | |

### S'arrêter
| Syntaxe | Effet | Exemple |
|---|---|---|
| `break <fonction>` (`b`) | point d'arrêt (*breakpoint*) à l'entrée d'une fonction | `b ft_split` |
| `break <fichier>:<ligne>` | point d'arrêt sur une ligne | `b main.c:42` |
| `break … if <condition>` | ne s'arrête que si la condition est vraie | `b sum if i == 3` |
| `tbreak <lieu>` | point d'arrêt à usage unique | `tbreak main` |
| `watch <variable>` | s'arrête quand la variable change ; affiche l'ancienne et la nouvelle valeur | `watch s` |
| `info breakpoints` (`i b`) | liste les points d'arrêt | |
| `delete <n>` / `disable <n>` | supprime / désactive le point numéro `n` | `delete 2` |

### Avancer
| Syntaxe | Effet |
|---|---|
| `next` (`n`) | ligne suivante, **sans entrer** dans les fonctions appelées |
| `step` (`s`) | ligne suivante, **en entrant** dans les fonctions |
| `continue` (`c`) | reprend jusqu'au prochain arrêt |
| `finish` | termine la fonction en cours et affiche sa valeur de retour (`Value returned is $5 = 10`) |
| `until <ligne>` | reprend jusqu'à cette ligne : pratique pour sortir d'une boucle |
| *Entrée* (touche) | répète la dernière commande |

### Inspecter
| Syntaxe | Effet | Exemple → résultat |
|---|---|---|
| `print <expr>` (`p`) | affiche une valeur ou évalue une expression C | `p t[1] * 10` → `20` |
| `p *ptr` / `p ptr->champ` | contenu d'une structure pointée | `p *a.next` → `{v = 2, next = 0x0}` |
| `p *tab@n` | `n` éléments à partir d'un pointeur | `p *t@4` → `{1, 2, 3, 4}` |
| `p/x <expr>` | affiche en hexadécimal (aussi `/d`, `/c`, `/t` binaire) | `p/x 255` → `0xff` |
| `x/4dw <adresse>` | lit la mémoire brute : 4 entiers (`d`) de 4 octets (`w`) | `x/4dw t` → `1 2 3 4` |
| `display <expr>` | réaffiche l'expression à chaque arrêt | `display i` |
| `info locals` / `info args` | toutes les variables locales / les arguments | |
| `ptype <var>` | type complet d'une variable | `ptype a` → `struct s_node {…}` |
| `set var <x> = <v>` | modifie une variable pendant l'exécution | `set var i = 0` |

### Pile d'appels (après un crash)
| Syntaxe | Effet |
|---|---|
| `backtrace` (`bt`) | qui a appelé qui jusqu'au crash. Sur un segfault, la ligne `#0` est l'endroit exact : `#0 main (…) at p.c:21` |
| `frame <n>` (`f`) | se place dans le niveau `n` de la pile pour y lire les variables |
| `up` / `down` | remonte vers l'appelant / redescend |

### Affichage
| Syntaxe | Effet |
|---|---|
| `list` (`l`) | affiche le code autour de la ligne courante |
| `layout src` (ou *Ctrl-x a*) | code source en haut de l'écran pendant qu'on avance ; *Ctrl-x a* pour en sortir |

**Pièges**
- Une variable affichée « `<optimized out>` » ou des lignes qui sautent dans le désordre : tu as compilé avec `-O2`. Recompile en `-g -O0`.
- `print i` donne `No symbol "i" in current context` quand tu n'es pas dans la fonction qui contient `i`. Utilise `frame` ou `up` / `down` pour t'y placer.
- Un `watch` interrompt aussi les `finish` et `continue` à chaque changement de la variable. Supprime-le (`delete <n>`) quand tu n'en as plus besoin.
