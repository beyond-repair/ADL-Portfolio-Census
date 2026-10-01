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
NOT CLAIMED live 81-row completeness
```

</div>

---
## ▌ STATUS

Classification follows [ADL-Governance](https://github.com/beyond-repair/ADL-Governance). A README facelift does not raise claim level. Physics and pharmacology stay at the evidenced cap. CI green is not experimental validation.

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

Claim level of this repo: **3** (deterministic structure over a dated snapshot; not a live GitHub crawler).

## Quick start

```bash
pip install -r requirements.txt
python -m census.engine
python -m pytest -q
```

---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

**William (Brian) Ware** · [Atomic Dream Labs](https://github.com/beyond-repair)  
Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
