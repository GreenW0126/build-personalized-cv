#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "usage: query-evidence.sh STORE_DIR EXPERIENCE_ID [MAX_UNITS]" >&2
  exit 2
fi

store_dir="$1"
experience_id="$2"
max_units="${3:-5}"

if [[ ! "$max_units" =~ ^[1-9][0-9]*$ ]] || (( max_units > 20 )); then
  echo "MAX_UNITS must be an integer from 1 to 20" >&2
  exit 2
fi

index_file="$store_dir/evidence/index.json"
if [[ ! -f "$index_file" ]]; then
  echo "evidence index not found: $index_file" >&2
  exit 1
fi

ids_json="$(jq --arg exp "$experience_id" --argjson max "$max_units" '[.[] | select(.experience_id==$exp) | .evidence_id][0:$max]' "$index_file")"
shard="$(jq -r --arg exp "$experience_id" '[.[] | select(.experience_id==$exp) | .shard] | unique | if length==1 then .[0] else empty end' "$index_file")"

if [[ "$ids_json" == "[]" || -z "$shard" ]]; then
  echo '[]'
  exit 0
fi

jq -e --arg exp "$experience_id" --arg shard "$shard" 'all(.[] | select(.experience_id==$exp); .shard==$shard)' "$index_file" >/dev/null

jq -s --arg exp "$experience_id" --argjson ids "$ids_json" '
  map(select(.experience_id==$exp and (.evidence_id as $id | $ids | index($id))))
' "$store_dir/evidence/by-experience/$shard"
