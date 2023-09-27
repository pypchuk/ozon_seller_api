from dataclasses import dataclass

from typing import Literal
from datetime import datetime

from .base import OzonEvent
from .message_type import MessageType


@dataclass
class Ping(OzonEvent):
    time: datetime

    message_type: Literal[MessageType.TYPE_PING] = MessageType.TYPE_PING
