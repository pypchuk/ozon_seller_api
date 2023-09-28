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
class PostingServices:
    marketplace_service_item_deliv_to_customer: float
    """Последняя миля."""

    marketplace_service_item_direct_flow_trans: float
    """Магистраль."""

    marketplace_service_item_dropoff_ff: float
    """Обработка отправления на фулфилмент складе(ФФ)."""

    marketplace_service_item_dropoff_pvz: float
    """Обработка отправления в ПВЗ."""

    marketplace_service_item_dropoff_sc: float
    """Обработка отправления в сортировочном центре."""

    marketplace_service_item_fulfillment: float
    """Сборка заказа."""

    marketplace_service_item_pickup: float
    """Выезд транспортного средства по адресу продавца для забора отправлений(Pick - up)."""

    marketplace_service_item_return_after_deliv_to_customer: float
    """Обработка возврата."""

    marketplace_service_item_return_flow_trans: float
    """Обратная магистраль."""

    marketplace_service_item_return_not_deliv_to_customer: float
    """Обработка отмен."""

    marketplace_service_item_return_part_goods_customer: float
    """Обработка невыкупа."""


@dataclass
class FinancialDataProduct:
    actions: list[str]
    currency_code: CurrencyCode
    client_price: str
    commission_amount: float
    commission_percent: int
    # commissions_currency_code
    item_services: PostingServices
    old_price: float
    payout: float
    # picking: None
    price: float
    product_id: int
    quantity: int
    total_discount_percent: float
    total_discount_value: float


@dataclass
class FinancialData:
    posting_services: PostingServices | None
    cluster_from: str
    cluster_to: str
    products: list[FinancialDataProduct]


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
    analytics_data: AnalyticsData | None
    financial_data: FinancialData | None
