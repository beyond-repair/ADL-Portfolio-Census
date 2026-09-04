"""ADL-Portfolio-Census — deterministic inventory checks."""

from .engine import CensusReport, validate_inventory
from .inventory import COMPATIBLE_BUILDS, INVENTORY

__all__ = [
    "COMPATIBLE_BUILDS",
    "CensusReport",
    "INVENTORY",
    "validate_inventory",
]
__version__ = "0.1.0"
