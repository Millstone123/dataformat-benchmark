"""Benchmark driver: run fixture rows through each codec and report timings."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Dict

from . import formats


def load_fixture(name: str) -> list:
    path = Path(__file__).resolve().parent.parent / "fixtures" / name
    return json.loads(path.read_text(encoding="utf-8"))


def run_once(fixture_name: str) -> Dict[str, float]:
    rows = load_fixture(fixture_name)
    results: Dict[str, float] = {}
    start = time.perf_counter()
    assert formats.roundtrip_json(rows) == rows
    results["json_ms"] = (time.perf_counter() - start) * 1000
    start = time.perf_counter()
    csv_rows = formats.roundtrip_csv(rows)
    assert len(csv_rows) == len(rows)
    results["csv_ms"] = (time.perf_counter() - start) * 1000
    return results


def main() -> None:
    results = run_once("records.json")
    for name, elapsed in sorted(results.items()):
        print(f"{name}: {elapsed:.3f}")


if __name__ == "__main__":
    main()
