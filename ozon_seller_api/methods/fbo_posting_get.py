from dataclasses import dataclass

from .base import OzonMethod
from ..types import PostingItem, FboPostingWithParams


@dataclass
class FboPostingsGet(OzonMethod[PostingItem]):
    posting_number: str
    _with: FboPostingWithParams
    translit: bool = True

    __returning__: type = PostingItem
    __api_method__: str = "v2/posting/fbo/get"
    __http_method__: str = "post"
