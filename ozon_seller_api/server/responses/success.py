from typing import Literal
from dataclasses import dataclass

from .base import Response


@dataclass
class Success(Response):
    http_status: Literal[200] = 200
    result: Literal[True] = True
