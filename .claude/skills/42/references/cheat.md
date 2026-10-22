# /42 cheat — antisèche d'un thème

> Mode déjà rapide : `--work` est sans objet. Options communes : voir `SKILL.md`.

But : `doc --work` couvre une fonction ou une commande ; `cheat` couvre **toute une famille** sur un ou deux écrans, pour l'avoir sous les yeux pendant qu'on code : `/42 cheat méthodes str python`, `/42 cheat gdb`, `/42 cheat options valgrind`, `/42 cheat formats printf`, `/42 cheat git`.

## Contenu

- Les éléments les plus utilisés d'abord ; laisse de côté ce qui sert rarement (une ligne « Aussi : … » peut les citer en fin de groupe).
- Regroupe par usage (« chercher », « découper », « transformer » pour les chaînes ; « lancer », « s'arrêter », « inspecter » pour `gdb`).
- Un tableau par groupe : `syntaxe` | effet | exemple court (avec son résultat si utile).
- Termine par **Pièges** : 1–3 lignes.

Vise 15 à 40 lignes de tableau en tout. Si le thème est trop large (`cheat python`), propose 2–3 thèmes plus étroits en une ligne et fais le plus probable.

## Format

```
# Antisèche : <thème>

### <groupe 1>
| Syntaxe | Effet | Exemple |
|---|---|---|

### <groupe 2>
…

**Pièges** : …
```

## Règles

- **Vérifie** : exécute les exemples, consulte `man` ou `help()` pour les options et les signatures. Une ligne fausse dans une antisèche est recopiée des dizaines de fois.
- Pour un thème lié à un projet 42 (`cheat push_swap`), l'antisèche liste les règles, les opérations et les commandes de test, jamais l'algorithme de la solution (règle de l'easter-egg).
- Si l'étudiant veut la garder, propose de l'enregistrer dans un fichier `CHEAT_<thème>.md`.
