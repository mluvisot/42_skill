# /42 resume — la fiche de révision de la discussion

> Avec `--work` : au lieu du document, une antisèche d'une page directement dans le chat (points clés, syntaxe, pièges, exemples vérifiés). Options communes : voir `SKILL.md`.

But : à la fin d'une leçon (`/42 doc`) et des questions qui ont suivi, l'étudiant tape `/42 resume`. Tu produis un **document de révision** qui rassemble tout ce qui a été appris dans la discussion, pour qu'il le garde et le relise avant l'évaluation ou l'examen. C'est « la doc de la doc ».

Ne pas confondre avec `/42 summary`, qui résume un sujet PDF de 42.

## Ce que tu reprends

Relis toute la discussion depuis le dernier `/42 doc` (ou depuis le début si aucun) et rassemble :
- le contenu de la leçon (intro, explications, démo, conclusion) ;
- **chaque question posée par l'étudiant et la réponse obtenue** — c'est souvent là que se trouve ce qu'il n'avait pas compris, donc le plus précieux pour réviser ;
- les précisions et reformulations apportées par l'étudiant lui-même, intégrées dans les explications (elles sont souvent la version qui lui parle le mieux) ;
- les corrections faites en cours de route : seule la version corrigée va dans le document ;
- les mesures, traces et exemples vérifiés.

N'ajoute pas de nouvelle matière qui n'a pas été vue, sauf un point indispensable à la cohérence (une ligne, signalée comme ajout). Si `<sujet>` est donné (`/42 resume malloc`), ne garde que ce qui concerne ce sujet.

## Où le mettre

Un document à garder : le type d'artefact Docs s'il est disponible, sinon un fichier Markdown `RESUME_<sujet>.md` envoyé à l'étudiant. En français. Dans le chat, une seule ligne avec le titre du document.

## Structure du document

1. **En bref** — le sujet en 2–3 phrases et pourquoi il compte pour un programmeur (usage réel), avec au besoin une ligne sur son lien avec 42.
2. **L'essentiel** — les explications, réorganisées dans un ordre logique (pas dans l'ordre chronologique de la discussion), avec les analogies.
3. **Schémas** — les schémas de la leçon, redessinés proprement dans le document.
4. **Démo** — les exemples et traces vérifiés, avec leurs sorties réelles.
5. **Tes questions** — chaque question posée pendant la discussion, avec une réponse claire et courte. Formule-les comme l'étudiant les a posées.
6. **Pièges** — les erreurs classiques et comment les détecter.
7. **Pour t'entraîner** — 3–5 questions de vérification, réponses à la fin.
8. **Pour aller plus loin** — `man` et références à lire, notions connexes, où ce savoir sert dans le métier (et, en une ligne, les projets 42 qui le réutilisent).
9. **Sources** — toutes les sources analysées pendant la leçon et la discussion, avec ce que chacune apporte (reprises de la section « Sources analysées » de la leçon, plus celles consultées en répondant aux questions).

Adapte : une petite leçon n'a pas besoin de toutes les sections, mais garde toujours les Sources. Un document court et juste vaut mieux qu'un document long.
