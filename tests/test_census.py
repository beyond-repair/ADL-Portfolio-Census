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


def test_public_api_and_version():
    import census

    assert census.__version__ == "0.1.1"
    assert census.validate_inventory().ok
    assert "ADL-Governance" in {row["name"] for row in census.INVENTORY}


def test_duplicate_name_is_rejected():
    bad = [dict(INVENTORY[0]), dict(INVENTORY[0])]
    report = validate_inventory(bad)
    assert not report.ok
    assert any("duplicate name" in err for err in report.errors)


def test_claim_out_of_range_is_rejected():
    bad = [dict(INVENTORY[0])]
    bad[0]["claim"] = 9
    report = validate_inventory(bad)
    assert not report.ok
    assert any("claim must be int 0-5" in err for err in report.errors)


def test_archived_claim_above_one_is_rejected():
    bad = [dict(INVENTORY[0])]
    bad[0]["lifecycle"] = "ARCHIVED"
    bad[0]["claim"] = 4
    report = validate_inventory(bad)
    assert not report.ok
    assert any("archived/superseded" in err for err in report.errors)


def test_unknown_cluster_and_empty_functions_are_rejected():
    bad = [dict(INVENTORY[0])]
    bad[0]["cluster"] = "not-a-cluster"
    bad[0]["functions"] = []
    report = validate_inventory(bad)
    assert not report.ok
    assert any("invalid cluster" in err for err in report.errors)
    assert any("at least one function" in err for err in report.errors)


def test_engine_module_exits_without_runpy_warning():
    import subprocess
    import sys

    proc = subprocess.run(
        [sys.executable, "-m", "census.engine"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "RuntimeWarning" not in proc.stderr
    assert proc.stdout.rstrip().endswith("OK")


def test_census_module_main_exits_ok():
    import subprocess
    import sys

    proc = subprocess.run(
        [sys.executable, "-m", "census"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "RuntimeWarning" not in proc.stderr
    assert "OK" in proc.stdout
