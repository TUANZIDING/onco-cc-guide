#!/usr/bin/env python3
"""OnCo关键词检索示例 v1.0 / OnCo keyword search example v1.0

用法 Usage:  python3 示例/检索示例v1.0.py <关键词 keyword> [最多条数 limit]
数据 Data:   https://onco.cc/api/v1/search.json (CC BY-NC 4.0, Data from OnCo (onco.cc))
只用Python标准库。Standard library only.
"""
import json
import sys
import urllib.request

API = "https://onco.cc/api/v1/search.json"
ATTRIBUTION = "Data from OnCo (onco.cc), CC BY-NC 4.0; commercial use needs a licence."


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    keyword = sys.argv[1].lower()
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    req = urllib.request.Request(API, headers={"User-Agent": "onco-cc-guide/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        docs = json.load(resp)
    hits = [
        d for d in docs
        if keyword in " ".join(str(d.get(k, "")) for k in ("name", "aka", "tldr", "tags")).lower()
    ]
    print(f"{len(hits)} matches for '{keyword}' (showing up to {limit})\n")
    for d in hits[:limit]:
        print(f"[{d.get('kind')}] {d.get('name')}\n    https://onco.cc{d.get('route')}")
    print("\n" + ATTRIBUTION, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
