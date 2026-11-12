"""Optional pickle round-trip probe, run only when explicitly requested."""

from __future__ import annotations

import pickle
from typing import Any, Dict, List


def roundtrip_pickle(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return pickle.loads(pickle.dumps(rows))
