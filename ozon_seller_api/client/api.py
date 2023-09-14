from __future__ import annotations

from types import TracebackType
from typing import Optional, Type

from .session.base import BaseSession
from .session.aiohttp import Session
from ..methods import (
    CreatePostingsReport,
    CreateStockReport,
    ReportInfo,
    FboPostingsList,
    StockOnWarehouses,
)
from ..types import (
    Report,
    CreateReportResponseCode,
    PostingItem,
    Language,
    StockOnWarehousesResult,
    WarehouseType,
)
from ..methods.create_postings_report import Filter as CreatePostingsReportFilter
from ..methods.fbo_posting_list import FboPostingListFilter, FboPostingWithParams


DEFAULT_HEADERS: dict[str, str] = {
    "Host": "api-seller.ozon.ru",
    "Content-Type": "application/json",
}


class OzonClient:
    def __init__(
            self,
            api_key: str,
            client_id: str,
            session: BaseSession | None = None,
    ) -> None:
        if not api_key or not client_id:
            raise RuntimeError("Both api_key and client_id must not be empty!")

        headers = {
            **DEFAULT_HEADERS,
            "Client-Id": client_id,
            "Api-Key": api_key,
        }
        self.session = session or Session(headers)

    async def create_postings_report(
            self,
            _filter: CreatePostingsReportFilter,
            language: Language = Language.DEFAULT,
    ) -> CreateReportResponseCode:
        return await self.session(CreatePostingsReport(_filter, language))

    async def create_stock_report(
            self,
            language: Language = Language.DEFAULT,
    ) -> CreateReportResponseCode:
        return await self.session(CreateStockReport(language))

    async def report_info(
            self,
            code: str,
    ) -> Report:
        return await self.session(ReportInfo(code))

    async def fbo_postings_list(
            self,
            limit: int,
            offset: int,
            _with: FboPostingWithParams,
            _filter: FboPostingListFilter,
    ) -> list[PostingItem]:
        return await self.session(
            FboPostingsList(
                limit=limit,
                offset=offset,
                _with=_with,
                filter=_filter,
            )
        )

    async def stocks_on_warehouses(
            self,
            limit: int = 1000,
            offset: int = 0,
            warehouse_type: WarehouseType = WarehouseType.ALL,
    ) -> StockOnWarehousesResult:
        return await self.session(
            StockOnWarehouses(
                limit,
                offset,
                warehouse_type,
            )
        )

    async def __aenter__(self) -> OzonClient:
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType],
    ) -> None:
        await self.session.close()
