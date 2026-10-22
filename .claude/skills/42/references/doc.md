# /42 doc — leçon structurée dans le chat

But : l'étudiant veut **apprendre un sujet** (« /42 doc les file descriptors », « /42 doc malloc », « /42 doc le tri par chunks »). Tu lui fais une leçon **directement dans le chat**, comme un développeur expérimenté qui explique au tableau.

## Options

`doc` accepte trois options, dans n'importe quel ordre, placées avant le sujet (reconnais-les aussi si elles sont ailleurs dans les arguments, et retire-les du sujet) :

```
/42 doc [--beginner | --intermediate | --expert] [--work] [--web] <sujet>
```

- **Niveau** : `--intermediate` par défaut (détails ci-dessous).
- **`--work`** : fiche de travail rapide au lieu d'une leçon (description, syntaxe, liens, exemple, exemple concret). Si `--work` est présent, **lis `references/doc-work.md` et suis-le à la place de tout le reste de ce fichier**.
- **`--web`** : appuie la leçon sur une recherche web. **Sans `--web`, pas de recherche web** : la leçon part de tes connaissances, des pages `man` locales et de ce que tu vérifies en exécutant du code. C'est plus rapide, et souvent suffisant pour les bases du C et d'Unix, qui bougent peu.

Exemples : `/42 doc malloc` (intermédiaire, sans web), `/42 doc --expert --web les signaux`, `/42 doc --web --beginner les pointeurs`, `/42 doc --work malloc`, `/42 doc --work --web print python`.

Annonce les options retenues en une ligne sous le titre : « Niveau : intermédiaire · sans recherche web ».

**L'angle : le métier de programmeur, pas l'école.** La leçon enseigne le sujet tel qu'on l'utilise dans le développement logiciel réel : où on le rencontre en production, comment les professionnels l'emploient, ses compromis (performance, complexité, mémoire, lisibilité), les bonnes pratiques et les alternatives. 42 n'est qu'un **contexte secondaire** : on le mentionne brièvement quand c'est utile — un piège typique d'un projet, une contrainte de la Norm, une question de soutenance — mais la leçon doit rester valable pour quelqu'un qui n'a jamais entendu parler de 42. Pas de document : le chat permet à l'étudiant d'interrompre, de poser des questions et de creuser tout de suite. Quand il aura fini, il tapera `/42 resume` pour obtenir un document de révision qui reprend toute la discussion (voir `references/resume.md`).

## Niveau : `--beginner`, `--intermediate`, `--expert`

L'étudiant choisit le niveau de la leçon avec une option placée avant le sujet :

```
/42 doc --beginner <sujet>
/42 doc --intermediate <sujet>
/42 doc --expert <sujet>
```

**Sans option, le niveau est `--intermediate`.** L'option peut être en majuscules ou minuscules ; si elle apparaît ailleurs dans les arguments (après le sujet, par exemple), reconnais-la quand même et retire-la du sujet. Une option inconnue (`--advanced`, `--noob`) : prends le niveau le plus proche s'il est évident, sinon `--intermediate`, et dis-le en une ligne au début.

Le niveau ne change **ni la structure** (les cinq parties restent), **ni l'exigence de recherche et de vérification** : il change la profondeur, le vocabulaire, ce qu'on suppose acquis et le type de démo. L'idée : un débutant décroche si on lui parle de cache CPU avant qu'il sache ce qu'est un pointeur ; un expert s'ennuie si on lui réexplique la stack avec une pile d'assiettes.

| | `--beginner` | `--intermediate` (défaut) | `--expert` |
|---|---|---|---|
| **Pour qui** | Piscine, ou découvre le sujet | A les bases du C, a codé quelques projets | Maîtrise le sujet, veut le fonctionnement interne |
| **Suppose acquis** | Presque rien : variables, fonctions, `printf` | Pointeurs, `malloc`/`free`, compilation, structures | Tout le niveau intermédiaire + appels système, modèle mémoire |
| **Vocabulaire** | Chaque terme technique défini à sa première apparition, en mots simples | Termes courants utilisés directement, les spécialisés définis | Vocabulaire précis sans le définir (UB, syscall, page, ABI…) |
| **Analogies** | Une pour chaque notion, concrète et du quotidien | Pour les notions abstraites seulement | Rarement : on préfère le mécanisme réel |
| **Explications** | Le « quoi » et le « pourquoi », une idée à la fois ; on laisse de côté perf et cas limites rares | Le « comment » en plus : complexité, compromis, usage en production | Les entrailles : implémentation (glibc, noyau Linux), norme C / POSIX, comportements indéfinis, cas limites, perf mesurée, alternatives et leur histoire |
| **Démo** | Très courte (10–20 lignes), commentée ligne à ligne, sortie montrée et expliquée | Programme complet commenté, ou trace pas à pas | Expérience qui révèle l'interne : `strace`, `valgrind`, `gdb`, benchmark, comparaison de deux implémentations |
| **Schémas** | Systématiques, simples, annotés | Dès que c'est spatial | Détaillés (layout mémoire réel, adresses, états du noyau) |
| **Sources** (avec `--web`) | Pages pédagogiques claires + `man` | Mix référence officielle, cours, articles d'ingénieurs | Sources primaires en priorité : norme, POSIX, code source, articles de recherche, docs du noyau |
| **Questions de vérification** | Simples : « que se passe-t-il si… ? » sur l'exemple vu | Application à un cas voisin | Cas limites, conception, « pourquoi l'implémentation fait-elle X plutôt que Y ? » |
| **Longueur** | Courte ; si le sujet est gros, découpe plus tôt | Comme décrit plus bas | Peut être plus dense, mais sans remplissage |

Au niveau **débutant**, ajoute au début des explications une ligne « Avant de commencer, tu dois savoir : … » qui liste les 1–3 prérequis ; s'il en manque un essentiel, propose de commencer par lui. Au niveau **expert**, saute les rappels de base et va directement à ce qui n'est pas évident.

Le niveau vaut pour toute la discussion qui suit la leçon : les réponses aux questions restent au même niveau. Si l'étudiant semble perdu (ou au contraire trop à l'aise), propose en une ligne de passer au niveau voisin. La règle de l'easter-egg s'applique à tous les niveaux : `--expert` ne donne pas plus de code de projet que `--beginner`.

## Préparer (avant d'écrire)

### Sans `--web` (par défaut)

Pas de `WebSearch` ni de `WebFetch`. Appuie-toi sur :
- tes connaissances, en t'en tenant à ce qui est stable et établi ;
- les pages `man` locales quand un shell est disponible (`man 3 malloc`, `man 2 read`) : elles font foi pour les prototypes, les valeurs de retour et les erreurs ;
- la vérification par exécution : compile, teste, mesure (voir « Vérifie la démo » plus bas, qui s'applique dans les deux cas).

Ne présente pas comme certain ce que tu n'as pas pu vérifier : un chiffre précis, une version de bibliothèque, un comportement qui a pu changer récemment. Dis-le simplement (« de mémoire, à vérifier ») et, si le point compte vraiment, suggère en une ligne de relancer avec `--web`. Ne fabrique jamais d'URL.

### Avec `--web`

La leçon s'appuie sur une recherche web, même si tu connais bien le sujet. Le but : étayer ce que tu enseignes avec des sources que l'étudiant peut vérifier, repérer ce qui fait consensus, et montrer comment le sujet est pratiqué dans le métier.

- Fais plusieurs recherches distinctes (au moins 3–5), en priorité côté métier : la notion elle-même (`radix sort LSD`), la référence technique (`man 2 read`, POSIX, norme C, documentation officielle), l'usage réel (`radix sort used in practice`, `memory allocator production`, bibliothèques ou systèmes connus qui l'emploient), et les bonnes pratiques ou erreurs courantes en entreprise (guides de style, CERT C, articles d'ingénieurs). Une recherche côté 42 (`push_swap radix`) seulement si elle apporte un piège ou une contrainte utile. Une recherche en anglais donne en général plus de résultats techniques.
- **Ouvre les pages** dont tu tires un fait (un extrait de résultat de recherche n'est pas une source). Vise au moins 3 sources réellement lues, de types différents si possible : référence officielle (man7.org, cppreference, POSIX, documentation d'un langage ou d'une bibliothèque), cours universitaire ou ouvrage de référence, article d'ingénieur ou blog technique reconnu. Les dépôts et articles d'étudiants 42 sont des sources d'appoint, pas la base.
- **Croise.** Un point affirmé par plusieurs sources indépendantes est un point clé. Une affirmation trouvée dans une seule source (surtout un blog ou un dépôt d'étudiant) est signalée comme telle, ou vérifiée par toi-même (code, simulation). Si deux sources se contredisent, dis-le et tranche par une vérification quand c'est possible.
- **Ne recopie pas.** Reformule tout avec tes mots ; au plus une très courte citation par source, quand la formulation exacte compte.
- Si un sujet PDF de 42 est fourni ou évident, garde-le en tête pour signaler les contraintes et pièges qui le concernent, sans en faire le centre de la leçon.

### Dans les deux cas

- **Vérifie la démo.** Compile les exemples (`cc -Wall -Wextra -Werror`, puis `valgrind`), exécute les traces, mesure les chiffres que tu annonces. Une démo fausse dans une leçon est pire qu'aucune démo. Avec `--web`, quand tes mesures confirment ou contredisent un chiffre trouvé en ligne, dis-le.

Si `--web` est demandé mais que la recherche web n'est pas disponible dans la session, dis-le en une ligne au début de la leçon et fais la leçon comme sans `--web`.

## Structure de la leçon

Toujours ces cinq parties, avec ces titres, dans cet ordre :

### 1. Intro
2–4 phrases : ce qu'est le sujet, pourquoi il compte pour un programmeur (où on le rencontre dans du vrai logiciel : systèmes, bases de données, réseau, outils…), et ce que l'étudiant saura faire à la fin de la leçon.

### 2. Explications
Les notions, de la plus simple à la plus avancée. Pour chaque notion abstraite : une définition simple, puis une analogie concrète. Dès que c'est spatial (mémoire, piles, flux, appels), un schéma (visuel inline si disponible, sinon ASCII). Un tableau quand plusieurs fonctions ou opérations se comparent (prototype, header, retour, erreur). Inclus ce qu'un professionnel regarde : complexité en temps et en mémoire, cas où on choisit cette solution et cas où on en prend une autre, comment c'est fait dans les bibliothèques ou systèmes réels.

**Dans le contexte 42** (facultatif, court) : un encadré de quelques lignes en fin d'explications, seulement s'il apporte quelque chose — un piège propre à un projet, une contrainte de la Norm ou du sujet, une question typique de soutenance.

### 3. Démo
Le concept en action, vérifié :
- un petit programme complet et compilable, commenté, avec sa sortie réelle ;
- ou une trace pas à pas (état des variables, des piles, de la mémoire) ;
- ou des mesures (nombre de coups, temps) obtenues en exécutant réellement.
La démo porte sur un exemple **tiré de la pratique réelle** (un cas concret de programme, de données ou de système), indépendant des projets 42 : elle montre le concept sans écrire le projet à la place de l'étudiant (sauf `/easter-egg`). Si elle porte sur la logique d'un projet 42, reste en pseudo-code ou en trace.

### 4. Conclusion
- **Points clés** : 3–5 points à retenir, en une ligne chacun. On les **répète volontairement** même s'ils ont été vus dans les explications : la répétition fixe la mémoire. Avec `--web`, marque ceux que plusieurs sources confirment ; sans, marque ceux que tu as vérifiés par exécution ;
- les 2–3 pièges classiques du métier (bugs fréquents, failles de sécurité, mauvaises pratiques), plus au besoin un piège propre à 42 ;
- 1 ou 2 questions de vérification (sans les réponses) ;
- une ligne qui invite à poser des questions, et rappelle que `/42 resume` produira la fiche de révision quand il aura fini.

### 5. Sources analysées
**Sans `--web`** : liste les références réellement utilisées, sans lien inventé : pages `man` consultées (`man 3 malloc`), « vérifié par exécution » pour ce que tu as testé, et éventuellement une ou deux références de fond que l'étudiant peut aller lire (norme C, POSIX, un ouvrage connu), marquées « non consultée pendant la leçon ». Termine par une ligne : « Pour une leçon appuyée sur des sources en ligne : `/42 doc --web <sujet>` ».

**Avec `--web`** : termine par la liste des sources **réellement ouvertes et lues**, une par ligne : `[Titre](URL)` — ce qu'elle apporte à la leçon et son type (référence officielle, cours ou ouvrage, article d'ingénieur, ressource 42), en quelques mots. Ajoute « vérifié par exécution » pour ce que tu as testé toi-même. Ne liste jamais une page que tu n'as pas ouverte.

## Longueur et rythme

Vise une leçon qui se lit en quelques minutes : titres courts, phrases courtes, paragraphes de 2–3 phrases. Si le sujet est trop gros pour une seule leçon (processus et `fork`, minishell…), fais l'intro, annonce le découpage en parties, traite la première, et propose la suivante à la fin.

## Pendant la discussion

L'étudiant va poser des questions, corriger, demander d'approfondir. Réponds directement dans le chat, court et précis, sans refaire toute la leçon. Quand il apporte une précision juste (une meilleure formulation, une intuition à lui), valide-la et intègre-la : elle fera partie du résumé final. Quand il se trompe, ne donne pas tout de suite la bonne réponse : oriente-le d'abord avec une question.
