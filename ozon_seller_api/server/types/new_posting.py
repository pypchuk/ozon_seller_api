from dataclasses import dataclass

from datetime import datetime
from typing import Literal

from .base import OzonEvent
from .message_type import MessageType


@dataclass
class Product:
    sku: int
    """SKU товара."""
    quantity: int
    """Количество товара."""


@dataclass
class NewPosting(OzonEvent):
    posting_number: str
    """Номер отправления."""
    products: list[Product]
    """Информация о товарах."""
    in_process_at: datetime
    """Дата и время начала обработки отправления в формате UTC."""
    warehouse_id: int
    """Идентификатор склада, на котором хранятся товары для этого отправления."""
    seller_id: int
    """Идентификатор продавца."""

    message_type: Literal[MessageType.TYPE_NEW_POSTING] = MessageType.TYPE_NEW_POSTING
