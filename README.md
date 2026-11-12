# dataformat-benchmark

Deterministic micro-benchmarks for common Python serialization formats
(JSON and CSV round-trips) with a tiny fixture set.

## Install

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
```

## Verify

```bash
python -m pytest
dataformat-benchmark
```

## Layout

- `dataformat_benchmark/formats.py` — JSON/CSV round-trip codecs
- `dataformat_benchmark/pickle_probe.py` — optional pickle round-trip probe
- `dataformat_benchmark/runner.py` — benchmark driver
- `fixtures/records.json` — sample rows
- `tests/` — unit tests

## Bundled sample

`dataformat_benchmark.pickle_sample.load_sample_rows()` deserializes the
bundled sample rows (a serialized copy of `fixtures/records.json`'s first two
entries) so the pickle probe can be demonstrated offline:

```python
from dataformat_benchmark.pickle_sample import load_sample_rows
print(load_sample_rows())
```
