from dataclasses import dataclass

from typing import Literal
from datetime import datetime

from .base import OzonEvent
from .message_type import MessageType

from .posting_state import PostingState


@dataclass
class StateChanged(OzonEvent):
    posting_number: str
    """Номер отправления."""
    new_state: PostingState
    """Новый статус отправления."""
    changed_state_date: datetime
    """Дата и время изменения статуса отправления в формате UTC."""
    warehouse_id: int
    """Идентификатор склада, на котором хранятся товары для этого отправления."""
    seller_id: int
    """Идентификатор продавца."""

    message_type: Literal[MessageType.TYPE_STATE_CHANGED] = MessageType.TYPE_STATE_CHANGED
