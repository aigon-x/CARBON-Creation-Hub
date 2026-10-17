import json
from pathlib import Path

from fastapi.testclient import TestClient

from backend.app import create_app


def partner_client(tmp_path: Path) -> TestClient:
    (tmp_path / "evidence").mkdir(parents=True)
    house = tmp_path / "house/remediation"
    house.mkdir(parents=True)
    (tmp_path / "evidence/index.json").write_text(json.dumps({"records": []}), encoding="utf-8")
    (house / "index.html").write_text("<html>house</html>", encoding="utf-8")

    source_root = Path(__file__).resolve().parents[1] / "house/remediation"
    for name in (
        "carbon-partner-tour.html",
        "carbon-service-website.html",
        "carbon-service-quick-technical-review.html",
    ):
        (house / name).write_text((source_root / name).read_text(encoding="utf-8"), encoding="utf-8")

    return TestClient(create_app(tmp_path, tmp_path / "data/test.db"))


def test_public_partner_and_service_routes(tmp_path):
    client = partner_client(tmp_path)
    assert client.get("/carbon/partner").status_code == 200
    assert client.get("/carbon/partner/").status_code == 200
    page = client.get("/carbon/partner").text
    assert "Welcome, Alfie" not in page
    assert "Hello, what should we call you?" in page
    assert 'id="preferredName"' in page
    assert 'data-contribution="suggestion"' in page
    assert 'data-contribution="referral"' in page
    assert "assigns each person’s role and permissions separately" in page
    assert "AI Commercial Manager" in page
    assert "Website service" in client.get("/carbon/services/website").text
    assert "Quick Technical Review" in client.get("/carbon/services/quick-technical-review").text
    assert client.get("/carbon/services/not-a-service").status_code == 404


def test_partner_pages_are_business_facing_and_truthful(tmp_path):
    client = partner_client(tmp_path)
    page = client.get("/carbon/partner").text
    assert "MTXID" not in page
    assert "65%" not in page
    assert "external search provider and Marketplace connector are not configured yet" in page
    assert "No listings yet" in page
    website = client.get("/carbon/services/website").text
    assert "automatic paid-demo/trial provisioning flow is not yet available" in website
    assert all(token in website for token in ("WhatsApp", "Telegram", "SMS", "Copy direct service link"))
