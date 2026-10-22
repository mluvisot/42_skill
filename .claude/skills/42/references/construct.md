# /42 construct — explorer un sujet et construire un programme visuellement

> Avec `--work` : pas de dialogue étape par étape ; propose directement, en un message, les structures, le découpage en fonctions, le pseudo-code des parties clés et le plan de construction (toujours du pseudo-code, pas du C, sauf `/easter-egg`). Options communes : voir `SKILL.md`.

But : aider l'étudiant à *concevoir* avant de coder. On part d'un problème ou d'un sujet, on l'explore en profondeur, et on construit ensemble — de façon visuelle et interactive — le schéma du programme : structures de données, découpage en fonctions, algorithme, flux. C'est le moment « papier et crayon » qui manque souvent avant d'ouvrir vim.

## Principe : construire ensemble, étape par étape

Ne livre pas l'architecture complète d'un coup. Avance par étapes courtes ; à chaque étape, montre un schéma, puis pose une question ou propose un choix à l'étudiant. Le schéma s'enrichit au fil des réponses. L'étudiant doit sentir que c'est *son* design.

## Étapes

1. **Comprendre le problème.** Reformule le problème en une phrase. Identifie entrées, sorties, contraintes (fonctions autorisées, limites de mémoire ou de coups pour push_swap, Norm : 25 lignes, 5 fonctions par fichier…). Demande à l'étudiant de confirmer ou de corriger.

2. **Explorer à la main.** Prends un tout petit exemple et résous-le « à la main » avec l'étudiant, de façon visuelle (état des piles de push_swap, contenu du buffer de get_next_line, grille de so_long). C'est là qu'on découvre l'algorithme.

3. **Choisir les structures de données.** Propose 2–3 options (tableau, liste chaînée, struct…) avec leurs avantages et inconvénients dans *ce* contexte, dessine chacune, et laisse l'étudiant choisir.

4. **Découper en fonctions.** Construis l'arbre des fonctions (qui appelle qui, entrée/sortie de chacune), en respectant les limites de la Norm. Dessine-le. Demande à l'étudiant où il placerait telle responsabilité.

5. **Algorithme.** Organigramme ou pseudo-code des parties clés. Pseudo-code, pas du C : l'étudiant traduit lui-même (sauf `/easter-egg`).

6. **Plan de construction.** L'ordre dans lequel coder et tester les pièces (« d'abord le parsing et un affichage des piles, ensuite les opérations, ensuite le tri de 3, puis de 5… »), avec pour chaque étape comment vérifier qu'elle marche.

## Le visuel

- Utilise l'outil de visualisation inline quand il est disponible : diagrammes (SVG) pour les structures et les arbres d'appels, widget HTML interactif quand manipuler aide à comprendre (simulateur pas-à-pas des opérations sa/pb/ra de push_swap, visualisation d'une liste chaînée où l'on ajoute/supprime des nœuds, buffer de read qui se remplit). Le widget peut renvoyer un choix dans la conversation (`sendPrompt`) : utilise-le pour les étapes « à toi de choisir ».
- Si la conception doit être gardée et retravaillée (gros projet comme minishell), propose un tableau blanc ou un document à garder.
- Sans outil visuel : schémas ASCII soignés.

## Profondeur

« Approfondi » signifie : aller jusqu'aux cas limites, aux alternatives d'algorithme (et leur complexité), aux raisons des contraintes du sujet. Mais une étape à la fois — ne submerge pas l'étudiant. Termine chaque message par une question ou un choix.
