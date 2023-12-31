from dataclasses import dataclass

from typing import Any

from enum import Enum
from datetime import datetime


class ReportType(Enum):
    SELLER_PRODUCTS = "seller_products"
    SELLER_TRANSACTIONS = "seller_transactions"
    SELLER_PRODUCT_PRICES = "seller_product_prices"
    SELLER_STOCK = "seller_stock"
    SELLER_PRODUCT_MOVEMENT = "seller_product_movement"
    SELLER_RETURNS = "seller_returns"
    SELLER_POSTINGS = "seller_postings"
    SELLER_FINANCE = "seller_finance"


class Status(Enum):
    SUCCESS = "success"
    PROCESSING = "processing"
    FAILED = "failed"


@dataclass
class Report:
    code: str
    created_at: datetime
    error: str
    file: str
    params: dict[str, Any]
    report_type: ReportType
    status: Status
