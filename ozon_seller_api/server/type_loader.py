from typing import Union, Any
from adaptix import Retort

from .types.base import OzonEvent

from .types import (
    Ping,
    NewPosting,
    StateChanged,
)


EVENT_RETORT = Retort()

EVENT_TYPES = Union[
    Ping,
    NewPosting,
    StateChanged
]


def load_event(json: Any) -> OzonEvent:
    return EVENT_RETORT.load(json, EVENT_TYPES)
