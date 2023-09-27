from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from .base import Response


@dataclass
class PingSuccess(Response):
    version: str
    name: str
    time: datetime

    @classmethod
    def create(cls, version: str, name: str) -> PingSuccess:
        return cls(
            200,
            version,
            name,
            datetime.now()
        )
