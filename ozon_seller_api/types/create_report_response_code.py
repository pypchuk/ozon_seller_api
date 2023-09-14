from dataclasses import dataclass

from .base import OzonObject


@dataclass
class CreateReportResponseCode(OzonObject):
    code: str
