#!/usr/bin/env bash
# Vérifications automatiques de base pour un projet 42.
# Usage : review.sh <dossier_du_projet>
# N'échoue pas au premier problème : affiche tout, section par section.

DIR="${1:-.}"
cd "$DIR" || { echo "Dossier introuvable : $DIR"; exit 1; }

section() { printf '\n===== %s =====\n' "$1"; }

section "NORMINETTE"
if ! command -v norminette >/dev/null 2>&1; then
	pip install -q norminette --break-system-packages >/dev/null 2>&1 \
		|| pip install -q norminette >/dev/null 2>&1
fi
if command -v norminette >/dev/null 2>&1; then
	norminette . | grep -v ': OK!$' || true
	norminette . >/dev/null 2>&1 && echo "Tout est OK selon norminette."
else
	echo "norminette indisponible : vérification manuelle nécessaire."
fi

if [ -f Makefile ] || [ -f makefile ]; then
	section "MAKEFILE — règles présentes"
	for r in all clean fclean re bonus; do
		grep -qE "^$r[[:space:]]*:" Makefile 2>/dev/null && echo "  $r : oui" || echo "  $r : NON"
	done
	grep -qE '\$\(NAME\)[[:space:]]*:' Makefile && echo "  \$(NAME) : oui" || echo "  \$(NAME) : NON"
	grep -q -- '-Wall' Makefile && grep -q -- '-Wextra' Makefile && grep -q -- '-Werror' Makefile \
		&& echo "  flags -Wall -Wextra -Werror : oui" || echo "  flags -Wall -Wextra -Werror : NON"
	grep -qE '\*\.c|wildcard' Makefile && echo "  ⚠ wildcard détecté dans le Makefile"

	section "COMPILATION"
	make fclean >/dev/null 2>&1
	if make 2>&1; then
		section "RELINK (second make)"
		OUT=$(make 2>&1)
		echo "$OUT"
		if echo "$OUT" | grep -qE '(^|[[:space:]])(cc|gcc|clang|ar)[[:space:]]'; then
			echo "⚠ RELINK : le second make recompile ou réarchive."
		else
			echo "Pas de relink détecté."
		fi
		section "SYMBOLES EXTERNES (à comparer aux fonctions autorisées)"
		for f in $(find . -maxdepth 1 -type f \( -name '*.a' -o -perm -u+x \) ! -name '*.sh'); do
			echo "-- $f"
			nm -u "$f" 2>/dev/null | awk '{print $NF}' | sed 's/@.*//' | sort -u | grep -vE '^_*(gmon_start|ITM_|cxa_finalize|libc_start_main|stack_chk_fail)'
		done
	else
		echo "⚠ La compilation échoue."
	fi
	make fclean >/dev/null 2>&1
else
	section "MAKEFILE"
	echo "Aucun Makefile (normal pour certains exercices de Piscine)."
fi

section "FICHIERS INDÉSIRABLES DANS LE RENDU"
find . -type f \( -name '*.o' -o -name 'a.out' -o -name '.DS_Store' -o -name '*.swp' \) -not -path './.git/*' -print
echo "(fin)"
