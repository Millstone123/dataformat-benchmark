from dataformat_benchmark.pickle_sample import load_sample_rows


def test_bundled_sample_rows_match_fixture_prefix():
    rows = load_sample_rows()
    assert rows == [
        {"id": 1, "name": "alpha", "value": 10},
        {"id": 2, "name": "beta", "value": 20},
    ]
