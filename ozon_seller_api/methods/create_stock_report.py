from dataclasses import dataclass
from enum import Enum

from .base import OzonMethod
from ..types.create_report_response_code import CreateReportResponseCode


class Lang(str, Enum):
    EN = "EN"
    RU = "RU"
    DEFAULT = "DEFAULT"


@dataclass
class CreateStockReport(OzonMethod[CreateReportResponseCode]):
    language: str = Lang.DEFAULT

    __returning__: type = CreateReportResponseCode
    __api_method__: str = "v1/report/stock/create"
    __http_method__: str = "post"
