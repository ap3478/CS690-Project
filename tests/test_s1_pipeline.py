"""Acceptance tests for S-1, the status pipeline (docs/design/S-1.md).

Written from AC-1 to AC-4 in backlog/backlog.md before any code existed.
Expected values come from the criteria, not from the code.
"""
import uuid

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client() -> TestClient:
    from jobsboard.api import app  # imported here so a missing module fails each test, not collection

    return TestClient(app)


@pytest.fixture
def posting_id() -> str:
    # A unique posting per test keeps tests isolated (S-1.md §9, D11).
    return f"posting-{uuid.uuid4().hex}"


def _apply(client: TestClient, posting_id: str) -> str:
    resp = client.post(f"/postings/{posting_id}/applications", json={"applicant_id": "applicant-1"})
    assert resp.status_code == 201
    assert resp.json()["stage"] == "Applied"
    return resp.json()["application_id"]


def _move(client: TestClient, application_id: str, to_stage: str):
    return client.post(f"/applications/{application_id}/stage", json={"to_stage": to_stage})


def _pipeline(client: TestClient, posting_id: str) -> dict:
    resp = client.get(f"/postings/{posting_id}/pipeline")
    assert resp.status_code == 200
    return resp.json()["stages"]


# AC-1: Given an application for posting P at Applied, When the recruiter moves it to
# Screened, Then the pipeline view for P lists it under Screened and no longer under Applied.
def test_ac1_applied_to_screened_listed_under_screened(client, posting_id):
    app_id = _apply(client, posting_id)

    resp = _move(client, app_id, "Screened")

    assert resp.status_code == 200
    stages = _pipeline(client, posting_id)
    assert app_id in stages["Screened"]
    assert app_id not in stages["Applied"]


# AC-2: Given an application for posting P at Applied, When the recruiter tries to move it
# straight to Interview, Then the request is refused with an "invalid transition" error naming
# Applied and Interview, and the pipeline view for P still lists it under Applied.
def test_ac2_skip_applied_to_interview_refused(client, posting_id):
    app_id = _apply(client, posting_id)
    before = _pipeline(client, posting_id)

    resp = _move(client, app_id, "Interview")

    assert resp.status_code == 409
    assert resp.json()["detail"] == {
        "error": "invalid_transition",
        "from_stage": "Applied",
        "to_stage": "Interview",
    }
    after = _pipeline(client, posting_id)
    assert app_id in after["Applied"]
    assert after == before  # R4: a refused move changes nothing


# AC-3: Given an application for posting P at Interview, When the recruiter moves it to
# Rejected, Then the pipeline view for P lists it under Rejected.
def test_ac3_interview_to_rejected_listed_under_rejected(client, posting_id):
    app_id = _apply(client, posting_id)
    assert _move(client, app_id, "Screened").status_code == 200
    assert _move(client, app_id, "Interview").status_code == 200

    resp = _move(client, app_id, "Rejected")

    assert resp.status_code == 200
    stages = _pipeline(client, posting_id)
    assert app_id in stages["Rejected"]
    assert app_id not in stages["Interview"]


# AC-4: Given an application for posting P at Rejected, When the recruiter tries to move it to
# Screened, Then the request is refused with an "invalid transition" error naming Rejected and
# Screened, and the pipeline view for P still lists it under Rejected.
def test_ac4_rejected_to_screened_refused(client, posting_id):
    app_id = _apply(client, posting_id)
    assert _move(client, app_id, "Rejected").status_code == 200
    before = _pipeline(client, posting_id)

    resp = _move(client, app_id, "Screened")

    assert resp.status_code == 409
    assert resp.json()["detail"] == {
        "error": "invalid_transition",
        "from_stage": "Rejected",
        "to_stage": "Screened",
    }
    after = _pipeline(client, posting_id)
    assert app_id in after["Rejected"]
    assert after == before  # R4
