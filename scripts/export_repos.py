#!/usr/bin/env python3
"""Parse README.md and export a flat CSV of all listed repos with live GitHub metadata.

Reads every Markdown table under a `##` heading (excluding the scope/contents sections)
and treats each row whose first cell links to a GitHub repo as an entry. Section name
becomes the `category` column. Stars and last-commit date are fetched from the GitHub API.

Output: data/repos.csv
"""
from __future__ import annotations

import csv
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"
OUTPUT = REPO_ROOT / "data" / "repos.csv"

GITHUB_URL_RE = re.compile(r"https://github\.com/([^/\s)]+)/([^/\s)]+)")
SKIP_SECTIONS = {"Scope", "Discovery sources", "Machine-readable index", "Contents", "List Authorship", "List Author", "License"}

API_TOKEN = os.environ.get("GITHUB_TOKEN")


def api_get(url: str) -> dict | None:
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-ai-evals-exporter",
        **({"Authorization": f"Bearer {API_TOKEN}"} if API_TOKEN else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            import json
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        sys.stderr.write(f"  HTTP {e.code} for {url}\n")
        if e.code == 403:
            reset = e.headers.get("X-RateLimit-Reset")
            if reset:
                wait = max(0, int(reset) - int(time.time())) + 2
                sys.stderr.write(f"  rate-limited, sleeping {wait}s\n")
                time.sleep(wait)
                return api_get(url)
        return None
    except Exception as e:
        sys.stderr.write(f"  error for {url}: {e}\n")
        return None


def parse_readme(text: str) -> list[dict]:
    entries: list[dict] = []
    current_section: str | None = None
    seen: set[tuple[str, str]] = set()

    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            current_section = m.group(1).strip()
            continue
        if not current_section or current_section in SKIP_SECTIONS:
            continue
        if not line.startswith("| ["):
            continue

        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        name_cell, desc_cell = cells[0], cells[1]
        name_match = re.match(r"\[([^\]]+)\]\(([^)]+)\)", name_cell)
        url_match = GITHUB_URL_RE.search(name_cell)
        if not (name_match and url_match):
            continue
        owner, repo = url_match.group(1), url_match.group(2).rstrip(".")
        key = (owner.lower(), repo.lower())
        if key in seen:
            continue
        seen.add(key)
        entries.append({
            "name": name_match.group(1),
            "owner": owner,
            "repo": repo,
            "url": f"https://github.com/{owner}/{repo}",
            "category": current_section,
            "description": desc_cell,
        })
    return entries


def enrich(entry: dict) -> dict:
    data = api_get(f"https://api.github.com/repos/{entry['owner']}/{entry['repo']}")
    if data:
        entry["stars"] = data.get("stargazers_count", "")
        entry["last_commit"] = (data.get("pushed_at") or "")[:10]
        entry["archived"] = data.get("archived", False)
        entry["language"] = data.get("language") or ""
        entry["license"] = (data.get("license") or {}).get("spdx_id") or ""
        entry["full_name"] = data.get("full_name") or f"{entry['owner']}/{entry['repo']}"
    else:
        entry["stars"] = ""
        entry["last_commit"] = ""
        entry["archived"] = ""
        entry["language"] = ""
        entry["license"] = ""
        entry["full_name"] = f"{entry['owner']}/{entry['repo']}"
    return entry


def main() -> int:
    entries = parse_readme(README.read_text(encoding="utf-8"))
    sys.stderr.write(f"parsed {len(entries)} entries from README\n")

    for i, e in enumerate(entries, 1):
        sys.stderr.write(f"[{i}/{len(entries)}] {e['owner']}/{e['repo']}\n")
        enrich(e)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fields = ["category", "name", "full_name", "url", "stars", "last_commit", "language", "license", "archived", "description"]
    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for e in sorted(entries, key=lambda x: (x["category"], -int(x["stars"] or 0))):
            w.writerow(e)

    sys.stderr.write(f"wrote {OUTPUT}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
