from __future__ import annotations

import abc
import json
from datetime import datetime

from types import TracebackType

from typing import Callable, Any, Optional, Type

import adaptix
from adaptix.load_error import LoadError

from ozon_seller_api.methods.base import OzonMethod, OzonType
from ozon_seller_api.types.base import ErrorObject

from ozon_seller_api.exceptions import JsonDecodeError, ObjectLoadError, ServerError

DEFAULT_TIMEOUT: float = 60.0

_JsonLoads = Callable[..., Any]


class BaseSession(abc.ABC):
    def __init__(
        self,
        json_loads: _JsonLoads = json.loads,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        self.json_loads = json_loads
        self.timeout = timeout
        self.retort = adaptix.Retort(
            recipe=[
                adaptix.name_mapping(skip="__.*"),
                adaptix.dumper(datetime, lambda x: x.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            ]
        )

    def check_response(
        self,
        method: OzonMethod[OzonType],
        status_code: int,
        content: str,
    ) -> OzonType:
        try:
            json_data = self.json_loads(content)
        except Exception as e:
            raise JsonDecodeError(content) from e

        if status_code == 200:
            try:
                obj = self.retort.load(json_data["result"], method.__returning__)
            except LoadError as e:
                raise ObjectLoadError(json_data, method.__returning__) from e
            return obj
        else:
            try:
                error_obj = self.retort.load(json_data, ErrorObject)
            except LoadError as e:
                raise ObjectLoadError(json_data, ErrorObject) from e

            raise ServerError(
                status_code,
                error_obj,
            )

    @abc.abstractmethod
    async def make_request(
        self,
        method: OzonMethod[OzonType],
    ) -> OzonType:
        ...

    @abc.abstractmethod
    async def close(self) -> None:
        ...

    async def __aenter__(self) -> BaseSession:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.close()

    async def __call__(
        self,
        method: OzonMethod[OzonType],
    ) -> OzonType:
        return await self.make_request(method)
