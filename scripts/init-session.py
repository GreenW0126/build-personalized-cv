#!/usr/bin/env python3
"""Safely initialize an empty build-personalized-cv session store."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_empty(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8")


def initialize(root):
    root = root.resolve()
    session = root / ".cv-workflow-session"
    store = session / "store"
    manifest = store / "manifest.json"

    if manifest.exists():
        print(f"existing:{manifest}")
        return 0
    if session.exists() and any(session.iterdir()):
        raise SystemExit(
            f"Refusing to initialize non-empty session without manifest: {session}. "
            "Inspect or migrate it first."
        )

    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    paths = {
        "experiences": "evidence/experiences.json",
        "evidence_index": "evidence/index.json",
        "evidence_shards": "evidence/by-experience/",
        "jd_sources": "market/jd-sources.jsonl",
        "demand_clusters": "market/demand-clusters.json",
        "capability_mappings": "capabilities/capability-mappings.json",
        "capability_package": "capabilities/capability-package.json",
        "active_rule_index": "decisions/active/index.json",
        "active_rule_shards": "decisions/active/",
        "active_rules_compatibility_snapshot": "decisions/active-rules.jsonl",
        "decision_history": "decisions/history.jsonl",
        "agent_registry": "agent-registry.json",
    }
    write_json(
        manifest,
        {
            "schema_version": "2.0",
            "generated_at": now,
            "updated_at": now,
            "retention": "user_managed",
            "run_id": str(uuid4()),
            "experience_count": 0,
            "evidence_count": 0,
            "bootstrap_state": "empty",
            "paths": paths,
        },
    )
    write_json(store / paths["experiences"], [])
    write_json(store / paths["evidence_index"], [])
    (store / paths["evidence_shards"]).mkdir(parents=True, exist_ok=True)
    write_empty(store / paths["jd_sources"])
    write_json(store / paths["demand_clusters"], {"status": "empty", "clusters": [], "source_ids": []})
    write_json(store / paths["capability_mappings"], {"status": "empty", "mappings": []})
    write_json(
        store / paths["capability_package"],
        {"status": "empty", "capabilities": [], "evidence_gaps": [], "confidence": "low"},
    )
    write_json(store / paths["active_rule_index"], [])
    for category in ("orchestration", "dashboard", "career-market", "writing-evidence", "artifact-export"):
        write_empty(store / "decisions" / "active" / f"{category}.jsonl")
    write_empty(store / paths["active_rules_compatibility_snapshot"])
    write_empty(store / paths["decision_history"])
    write_json(
        store / paths["agent_registry"],
        {
            "status": "ready",
            "roles": [
                "master",
                "evidence-curator",
                "market-analyst",
                "capability-synthesizer",
                "writer-auditor",
            ],
        },
    )
    print(f"initialized:{manifest}")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    return initialize(args.root)


if __name__ == "__main__":
    raise SystemExit(main())
