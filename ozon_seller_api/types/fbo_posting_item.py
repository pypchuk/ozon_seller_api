from dataclasses import dataclass
from datetime import datetime

from enum import Enum


class CurrencyCode(Enum):
    RUB = "RUB"
    BYN = "BYN"
    KZT = "KZT"
    EUR = "EUR"
    USD = "USD"
    CNY = "CNY"


@dataclass
class PostingProduct:
    digital_codes: list[str]
    name: str
    offer_id: str
    currency_code: CurrencyCode
    price: str
    quantity: int
    sku: int


class Status(Enum):
    AWAITING_PACKAGING = "awaiting_packaging"
    AWAITING_DELIVER = "awaiting_deliver"
    DELIVERING = "delivering"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


@dataclass
class AnalyticsData:
    city: str
    delivery_type: str
    is_legal: bool
    is_premium: bool
    payment_type_group_name: str
    region: str
    warehouse_id: int
    warehouse_name: str


@dataclass
class PostingItem:
    order_id: int
    order_number: str
    posting_number: str
    status: Status
    products: list[PostingProduct]
    in_process_at: datetime
    cancel_reason_id: int
    created_at: datetime
    analytics_data: AnalyticsData
