"""Fixture encode/decode round-trips for JSON and CSV."""

from __future__ import annotations

import csv
import io
import json
from typing import Any, Dict, List


def roundtrip_json(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return json.loads(json.dumps(rows))


def roundtrip_csv(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    buffer.seek(0)
    return list(csv.DictReader(buffer))
