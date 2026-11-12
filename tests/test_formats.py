from dataformat_benchmark.formats import roundtrip_csv, roundtrip_json
from dataformat_benchmark.pickle_probe import roundtrip_pickle

ROWS = [
    {"id": 1, "name": "alpha", "value": 10},
    {"id": 2, "name": "beta", "value": 20},
]


def test_json_roundtrip():
    assert roundtrip_json(ROWS) == ROWS


def test_csv_roundtrip_preserves_row_count():
    assert len(roundtrip_csv(ROWS)) == len(ROWS)


def test_pickle_roundtrip_matches_source():
    assert roundtrip_pickle(ROWS) == ROWS
