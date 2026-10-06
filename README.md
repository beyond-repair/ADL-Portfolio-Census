<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║   ATOMIC DREAM LABS  ·  BEYOND-REPAIR                        ║
╚══════════════════════════════════════════════════════════════╝
```

# ADL Portfolio Census

### Deterministic SCAN / FORK / ANCHOR inventory. Claim-capped.

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤ 1   inventory
NOT CLAIMED live 83-row completeness
```

</div>

---
## ▌ STATUS

Classification follows [ADL-Governance](https://github.com/beyond-repair/ADL-Governance). A README facelift does not raise claim level. Physics and pharmacology stay at the evidenced cap. CI green is not experimental validation.

Sweep-227 (2026-10-05) froze the 2026-09-04 snapshot (`SNAPSHOT_DATE`, 42 rows) and added `SECURITY.md`. Package version 0.1.2. A later GitHub search total of 83 is not this inventory. See `docs/SWEEP-227.md`.

---

## ▌ PRESERVED BODY

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

Claim level of this repo: **≤1** (deterministic structure over the locked 2026-09-04 snapshot; not a live GitHub crawler and not an 83-row completeness proof). The banner and this line agree. A green run does not raise the claim.

## Quick start

Python 3.10 or newer. From the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"
python -m census.engine
python -m pytest -q
```

`python -m census` prints the same report. Both exit 0 and print `OK` when every locked record passes. They exit 1 and list `ERRORS` when a record breaks the structural rules: unique name, cluster in `CLUSTERS`, lifecycle in `LIFECYCLES`, claim an integer 0–5, archived or superseded claim ≤1, at least one function, and `gaps` a list. The canonical inventory must also keep `SNAPSHOT_DATE == 2026-09-04` and 42 rows. Nothing in the checker calls GitHub. `requirements.txt` pins the same pytest used by CI for a root-directory run without an editable install.

---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

**William (Brian) Ware** · [Atomic Dream Labs](https://github.com/beyond-repair)  
Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
