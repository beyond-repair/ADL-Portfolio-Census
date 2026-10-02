"""ADL-Portfolio-Census — deterministic inventory checks.

Exports are lazy so ``python -m census.engine`` does not import this module's
engine before runpy executes it (that import order emits a RuntimeWarning).
"""

from __future__ import annotations

from typing import Any

__all__ = [
    "COMPATIBLE_BUILDS",
    "CensusReport",
    "INVENTORY",
    "validate_inventory",
]
__version__ = "0.1.1"


def __getattr__(name: str) -> Any:
    if name in {"CensusReport", "validate_inventory"}:
        from .engine import CensusReport, validate_inventory

        return {
            "CensusReport": CensusReport,
            "validate_inventory": validate_inventory,
        }[name]
    if name in {"COMPATIBLE_BUILDS", "INVENTORY"}:
        from .inventory import COMPATIBLE_BUILDS, INVENTORY

        return {
            "COMPATIBLE_BUILDS": COMPATIBLE_BUILDS,
            "INVENTORY": INVENTORY,
        }[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
