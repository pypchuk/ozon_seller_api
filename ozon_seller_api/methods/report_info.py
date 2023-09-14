from dataclasses import dataclass

from .base import OzonMethod
from ..types.report import Report


@dataclass
class ReportInfo(OzonMethod[Report]):
    code: str

    __returning__: type = Report
    __api_method__: str = "v1/report/info"
    __http_method__: str = "post"
