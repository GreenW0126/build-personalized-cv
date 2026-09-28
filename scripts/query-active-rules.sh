#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "usage: query-active-rules.sh STORE_DIR CATEGORY [MAX_RULES]" >&2
  exit 2
fi

store_dir="$1"
category="$2"
max_rules="${3:-10}"

case "$category" in
  orchestration|dashboard|career-market|writing-evidence) ;;
  *) echo "unknown category: $category" >&2; exit 2 ;;
esac

if [[ ! "$max_rules" =~ ^[1-9][0-9]*$ ]] || (( max_rules > 20 )); then
  echo "MAX_RULES must be an integer from 1 to 20" >&2
  exit 2
fi

rules_file="$store_dir/decisions/active/$category.jsonl"
if [[ ! -f "$rules_file" ]]; then
  echo "active-rule shard not found: $rules_file" >&2
  exit 1
fi

jq -s --argjson max "$max_rules" '.[0:$max]' "$rules_file"

