from census.engine import validate_inventory
from census.inventory import COMPATIBLE_BUILDS, INVENTORY, LIFECYCLES


def test_inventory_validates():
    report = validate_inventory()
    assert report.ok, report.errors
    assert report.repo_count == len(INVENTORY)
    assert report.repo_count >= 40
    assert report.gap_count >= 1


def test_unique_names():
    names = [r["name"] for r in INVENTORY]
    assert len(names) == len(set(names))


def test_claims_in_range():
    for rec in INVENTORY:
        assert 0 <= rec["claim"] <= 5
        if rec["lifecycle"] in {"ARCHIVED", "SUPERSEDED"}:
            assert rec["claim"] <= 1


def test_every_lifecycle_known():
    for rec in INVENTORY:
        assert rec["lifecycle"] in LIFECYCLES


def test_this_repo_is_registered_as_built():
    names = {item["name"] for item in COMPATIBLE_BUILDS}
    assert "ADL-Portfolio-Census" in names
    this = next(i for i in COMPATIBLE_BUILDS if i["name"] == "ADL-Portfolio-Census")
    assert this["status"] == "this_repository"


def test_governance_and_substrate_present():
    names = {r["name"] for r in INVENTORY}
    for required in (
        "ADL-Governance",
        "ADL-SEEM",
        "forge-aegis",
        "sovereign-clean-room",
        "sunder",
    ):
        assert required in names
