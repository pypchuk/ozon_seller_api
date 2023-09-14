from dataclasses import dataclass

from .base import OzonMethod
from ..types.stock_on_warehouses import StockOnWarehousesResult
from ..types import WarehouseType


@dataclass
class StockOnWarehouses(OzonMethod[StockOnWarehousesResult]):
    limit: int = 1000
    offset: int = 0
    warehouse_type: WarehouseType = WarehouseType.ALL

    __returning__: type = StockOnWarehousesResult
    __api_method__: str = "v2/analytics/stock_on_warehouses"
    __http_method__: str = "post"
