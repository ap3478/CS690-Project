"""S-1 status pipeline domain (docs/design/S-1.md)."""
from __future__ import annotations

import uuid
from dataclasses import dataclass, replace
from enum import Enum


class Stage(str, Enum):
    APPLIED = "Applied"
    SCREENED = "Screened"
    INTERVIEW = "Interview"
    OFFER = "Offer"
    REJECTED = "Rejected"


@dataclass(frozen=True)
class Application:
    application_id: str
    posting_id: str
    applicant_id: str
    stage: Stage


class PipelineError(Exception):
    """Base class for S-1 domain errors (S-1.md D4)."""


class ApplicationNotFound(PipelineError):
    def __init__(self, application_id: str) -> None:
        super().__init__(f"application not found: {application_id}")
        self.application_id = application_id


class InvalidTransition(PipelineError):
    def __init__(self, from_stage: Stage, to_stage: Stage) -> None:
        super().__init__(f"invalid transition: {from_stage.value} -> {to_stage.value}")
        self.from_stage = from_stage
        self.to_stage = to_stage


# R1 transition table (S-1.md §6). Moves out of Offer are a non-goal until OQ-1 (Q-3) is answered.
_ALLOWED: dict[Stage, frozenset[Stage]] = {
    Stage.APPLIED: frozenset({Stage.SCREENED, Stage.REJECTED}),
    Stage.SCREENED: frozenset({Stage.INTERVIEW, Stage.REJECTED}),
    Stage.INTERVIEW: frozenset({Stage.OFFER, Stage.REJECTED}),
    Stage.OFFER: frozenset(),
    Stage.REJECTED: frozenset(),
}


def allowed_next(stage: Stage) -> frozenset[Stage]:
    return _ALLOWED[stage]


class ApplicationStore:
    """In-memory store (S-1.md D3). Dict insertion order gives creation order."""

    def __init__(self) -> None:
        self._apps: dict[str, Application] = {}

    def create(self, posting_id: str, applicant_id: str) -> Application:
        app = Application(
            application_id=uuid.uuid4().hex,
            posting_id=posting_id,
            applicant_id=applicant_id,
            stage=Stage.APPLIED,
        )
        self._apps[app.application_id] = app
        return app

    def get(self, application_id: str) -> Application:
        try:
            return self._apps[application_id]
        except KeyError:
            raise ApplicationNotFound(application_id) from None

    def list_for_posting(self, posting_id: str) -> list[Application]:
        return [a for a in self._apps.values() if a.posting_id == posting_id]

    def _put(self, app: Application) -> None:
        self._apps[app.application_id] = app


def move_stage(store: ApplicationStore, application_id: str, to_stage: Stage) -> Application:
    current = store.get(application_id)
    if to_stage not in allowed_next(current.stage):
        raise InvalidTransition(current.stage, to_stage)
    moved = replace(current, stage=to_stage)
    store._put(moved)
    return moved
