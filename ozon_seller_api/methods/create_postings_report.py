from dataclasses import dataclass, field
from datetime import datetime

from .base import OzonMethod
from ..types.create_report_response_code import CreateReportResponseCode
from ..types import Language


@dataclass
class Filter:
    processed_at_from: datetime
    processed_at_to: datetime
    cancel_reason_id: list[int] = field(default_factory=list)
    delivery_schema: list[str] = field(default_factory=list)
    sku: list[int] = field(default_factory=list)
    status_alias: list[str] = field(default_factory=list)
    statuses: list[int] = field(default_factory=list)
    offer_id: str = ""
    title: str = ""


@dataclass
class CreatePostingsReport(OzonMethod[CreateReportResponseCode]):
    filter: Filter
    language: Language

    __returning__: type = CreateReportResponseCode
    __api_method__: str = "v1/report/postings/create"
    __http_method__: str = "post"
