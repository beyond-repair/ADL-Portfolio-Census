# ADL-Portfolio-Census

Deterministic **SCAN → FORK → ANCHOR** implementation for the [beyond-repair](https://github.com/beyond-repair) portfolio.

This repository exists because [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) defined the vocabulary and no executable census existed.

## What this is

| Layer | Role |
|-------|------|
| `census/inventory.py` | Locked snapshot of classified repositories |
| `census/engine.py` | Structural + claim-cap validator |
| `tests/` | Falsification of uniqueness, claim caps, required anchors |
| CI | `python -m census.engine` then pytest |

Claim level of this repo: **3** (deterministic structure over a dated snapshot; not a live GitHub crawler).

## Quick start

```bash
pip install -r requirements.txt
python -m census.engine
python -m pytest -q
```
