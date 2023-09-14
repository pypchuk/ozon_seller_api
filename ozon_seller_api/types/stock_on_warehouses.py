from dataclasses import dataclass

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
class StockOnWarehouseRow:
    sku: int
    item_code: str
    item_name: str
    free_to_sell_amount: int
    promised_amount: int
    reserved_amount: int
    warehouse_name: str


@dataclass
class StockOnWarehousesResult:
    rows: list[StockOnWarehouseRow]
