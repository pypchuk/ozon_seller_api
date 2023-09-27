from enum import Enum
from typing import NamedTuple
from dataclasses import dataclass
from datetime import datetime

from .base import OzonMethod
from ..types import Dir, PostingItem, FboPostingWithParams


class Status(str, Enum):
    AWAITING_PACKAGING = "awaiting_packaging"
    AWAITING_DELIVER = "awaiting_deliver"
    DELIVERING = "delivering"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    ALL = ""


class FboPostingListFilter(NamedTuple):
    since: datetime
    to: datetime
    status: Status = Status.ALL


@dataclass
class FboPostingsList(OzonMethod[list[PostingItem]]):
    limit: int
    offset: int
    filter: FboPostingListFilter
    _with: FboPostingWithParams
    dir: Dir = Dir.DESC
    translit: bool = True

    __returning__: type = list[PostingItem]
    __api_method__: str = "v2/posting/fbo/list"
    __http_method__: str = "post"
