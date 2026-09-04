"""Deterministic validation of the locked portfolio inventory."""

from __future__ import annotations

from dataclasses import dataclass, field

from .inventory import (
    CLUSTERS,
    COMPATIBLE_BUILDS,
    INVENTORY,
    LIFECYCLES,
    RepoRecord,
)


@dataclass(frozen=True)
class CensusReport:
    repo_count: int
    cluster_counts: dict[str, int]
    lifecycle_counts: dict[str, int]
    gap_count: int
    compatible_not_built: list[str]
    errors: tuple[str, ...] = field(default_factory=tuple)

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0


def _check_record(i: int, rec: RepoRecord) -> list[str]:
    errors: list[str] = []
    prefix = f"INVENTORY[{i}].{rec.get('name', '?')}"
    if not rec.get("name"):
        errors.append(f"{prefix}: name required")
    if rec.get("cluster") not in CLUSTERS:
        errors.append(f"{prefix}: invalid cluster {rec.get('cluster')!r}")
    if rec.get("lifecycle") not in LIFECYCLES:
        errors.append(f"{prefix}: invalid lifecycle {rec.get('lifecycle')!r}")
    claim = rec.get("claim", -1)
    if not isinstance(claim, int) or claim < 0 or claim > 5:
        errors.append(f"{prefix}: claim must be int 0-5")
    if rec.get("lifecycle") in {"ARCHIVED", "SUPERSEDED"} and isinstance(claim, int) and claim > 1:
        errors.append(f"{prefix}: archived/superseded claim must be ≤1")
    if not rec.get("functions"):
        errors.append(f"{prefix}: at least one function required")
    if not isinstance(rec.get("gaps"), list):
        errors.append(f"{prefix}: gaps must be a list")
    return errors


def validate_inventory(records: list[RepoRecord] | None = None) -> CensusReport:
    records = INVENTORY if records is None else records
    errors: list[str] = []
    names: set[str] = set()
    cluster_counts: dict[str, int] = {c: 0 for c in CLUSTERS}
    lifecycle_counts: dict[str, int] = {l: 0 for l in LIFECYCLES}
    gap_count = 0

    for i, rec in enumerate(records):
        errors.extend(_check_record(i, rec))
        name = rec.get("name", "")
        if name in names:
            errors.append(f"duplicate name: {name}")
        names.add(name)
        cluster = rec.get("cluster")
        if cluster in cluster_counts:
            cluster_counts[cluster] += 1
        life = rec.get("lifecycle")
        if life in lifecycle_counts:
            lifecycle_counts[life] += 1
        gaps = rec.get("gaps") or []
        gap_count += len(gaps)

    not_built = [
        item["name"]
        for item in COMPATIBLE_BUILDS
        if item.get("status") == "not_built"
    ]
    if "ADL-Portfolio-Census" not in {item["name"] for item in COMPATIBLE_BUILDS}:
        errors.append("COMPATIBLE_BUILDS missing this repository")

    return CensusReport(
        repo_count=len(records),
        cluster_counts=cluster_counts,
        lifecycle_counts=lifecycle_counts,
        gap_count=gap_count,
        compatible_not_built=not_built,
        errors=tuple(errors),
    )


def main() -> int:
    report = validate_inventory()
    print(f"repos={report.repo_count} gaps={report.gap_count}")
    print("clusters=", report.cluster_counts)
    print("lifecycle=", report.lifecycle_counts)
    print("not_built=", report.compatible_not_built)
    if report.errors:
        print("ERRORS:")
        for e in report.errors:
            print(" -", e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
