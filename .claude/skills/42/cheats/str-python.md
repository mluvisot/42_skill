# Antisèche : méthodes `str` en Python

Vérifiée par exécution avec Python 3.13, le 2026-10-22. Une méthode ne modifie jamais la chaîne : elle **renvoie une nouvelle chaîne**.

### Nettoyer
| Syntaxe | Effet | Exemple |
|---|---|---|
| `s.strip()` | retire les espaces (et `\n`, `\t`) aux deux bouts | `"  Hello  ".strip()` → `'Hello'` |
| `s.lstrip()` / `s.rstrip()` | côté gauche / côté droit seulement | `"hi\n".rstrip("\n")` → `'hi'` |
| `s.strip(chars)` | retire les caractères de `chars` aux deux bouts | `"xxhixx".strip("x")` → `'hi'` |
| `s.removeprefix(p)` / `s.removesuffix(p)` | retire un préfixe ou un suffixe exact | `"data.txt".removesuffix(".txt")` → `'data'` |

### Découper et assembler
| Syntaxe | Effet | Exemple |
|---|---|---|
| `s.split()` | découpe sur les blancs et ignore les doublons | `"a b  c".split()` → `['a', 'b', 'c']` |
| `s.split(sep)` | découpe sur `sep` et garde les vides | `"a,b,,c".split(",")` → `['a', 'b', '', 'c']` |
| `s.split(sep, n)` | au plus `n` découpes | `"a,b,c".split(",", 1)` → `['a', 'b,c']` |
| `s.rsplit(sep, n)` | découpe en partant de la droite | `"a/b/c".rsplit("/", 1)` → `['a/b', 'c']` |
| `s.splitlines()` | découpe en lignes, sans les `\n` | `"l1\nl2\n".splitlines()` → `['l1', 'l2']` |
| `s.partition(sep)` | coupe au 1er `sep` : `(avant, sep, après)` | `"k=v=w".partition("=")` → `('k', '=', 'v=w')` |
| `sep.join(liste)` | colle les éléments avec `sep` entre eux | `"-".join(["a", "b", "c"])` → `'a-b-c'` |

### Chercher
| Syntaxe | Effet | Exemple |
|---|---|---|
| `x in s` | présence d'une sous-chaîne | `"an" in "banana"` → `True` |
| `s.find(x)` / `s.rfind(x)` | indice de la 1re / dernière occurrence, `-1` si absent | `"banana".find("an")` → `1` |
| `s.index(x)` | comme `find`, mais `ValueError` si absent | `"banana".index("z")` → erreur |
| `s.count(x)` | nombre d'occurrences | `"banana".count("a")` → `3` |
| `s.startswith(p)` / `s.endswith(p)` | début / fin ; `p` peut être un tuple | `"file.py".endswith(".py")` → `True` |

### Transformer
| Syntaxe | Effet | Exemple |
|---|---|---|
| `s.replace(a, b)` | remplace toutes les occurrences | `"banana".replace("a", "o")` → `'bonono'` |
| `s.replace(a, b, n)` | seulement les `n` premières | `"banana".replace("a", "o", 1)` → `'bonana'` |
| `s.lower()` / `s.upper()` | minuscules / majuscules | `"Hello".lower()` → `'hello'` |
| `s.capitalize()` / `s.title()` | 1re lettre de la chaîne / de chaque mot | `"hello world".title()` → `'Hello World'` |
| `s.swapcase()` | inverse la casse | `"Hello".swapcase()` → `'hELLO'` |
| `s[::-1]` | inverse la chaîne | `"abc"[::-1]` → `'cba'` |

### Tester (renvoient un `bool`)
| Syntaxe | Vrai si… | Exemple |
|---|---|---|
| `s.isdigit()` | uniquement des chiffres | `"42".isdigit()` → `True`, `"-42".isdigit()` → `False` |
| `s.isalpha()` / `s.isalnum()` | uniquement des lettres / lettres et chiffres | `"a1".isalnum()` → `True` |
| `s.isspace()` | uniquement des blancs | `"   ".isspace()` → `True` |

### Formater
| Syntaxe | Effet | Exemple |
|---|---|---|
| `f"{x:.2f}"` | 2 décimales | `f"{3.14159:.2f}"` → `'3.14'` |
| `f"{x:>5}"` / `f"{x:<5}"` / `f"{x:^5}"` | aligné à droite / à gauche / centré sur 5 colonnes | `f"{42:>5}"` → `'   42'` |
| `f"{x:03d}"` / `f"{x:x}"` | complété par des zéros / en hexadécimal | `f"{7:03d}"` → `'007'`, `f"{255:x}"` → `'ff'` |
| `s.zfill(n)` | complète avec des `0` à gauche | `"42".zfill(5)` → `'00042'` |
| `s.center(n, c)` / `s.ljust(n, c)` / `s.rjust(n)` | centre ou aligne avec un caractère de remplissage | `"ab".center(6, "*")` → `'**ab**'` |

Hors méthodes, mais utiles : `len(s)`, `s[1:4]`, `"a" * 3` → `'aaa'`, `ord("A")` → `65`, `chr(97)` → `'a'`.

**Pièges**
- Une chaîne est immuable : `s.upper()` seul ne fait rien, il faut écrire `s = s.upper()`. `s[0] = "z"` provoque `TypeError`.
- `split()` et `split(" ")` ne font pas la même chose : sans argument, les blancs consécutifs sont fusionnés ; avec `","`, on obtient des chaînes vides (`'a,,b'` → `['a', '', 'b']`).
- `"-42".isdigit()` et `"".isdigit()` renvoient `False` : pour valider un nombre, essaie plutôt `int(s)` dans un `try`/`except ValueError`.
