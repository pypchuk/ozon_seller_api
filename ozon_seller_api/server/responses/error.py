from dataclasses import dataclass
from enum import StrEnum
from .base import Response


class ResponseCode(StrEnum):
    ERROR_UNKNOWN = "ERROR_UNKNOWN"
    ERROR_PARAMETER_VALUE_MISSED = "ERROR_PARAMETER_VALUE_MISSED"
    ERROR_REQUEST_DUPLICATED = "ERROR_REQUEST_DUPLICATED"


@dataclass
class DetailedInfo:
    code: ResponseCode
    message: str
    details: str | None


@dataclass
class Error(Response):
    error: DetailedInfo

    @classmethod
    def create(
            cls,
            http_status: int,
            message: str,
            details: str | None = None,
            code: ResponseCode = ResponseCode.ERROR_UNKNOWN
    ) -> "Error":
        response = cls(
            http_status,
            DetailedInfo(
                code=code,
                message=message,
                details=details,
            )
        )

        return response
