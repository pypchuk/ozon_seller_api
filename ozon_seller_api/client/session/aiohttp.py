import json
from aiohttp import ClientSession
from ozon_seller_api.client.session.base import DEFAULT_TIMEOUT, _JsonLoads

from ozon_seller_api.methods.base import OzonMethod, OzonType

from .base import BaseSession

API_BASE_URL = "https://api-seller.ozon.ru/{}"


class Session(BaseSession):
    def __init__(
        self,
        headers: dict[str, str],
        json_loads: _JsonLoads = json.loads,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        super().__init__(json_loads, timeout)
        self.session = ClientSession(headers=headers)

    async def make_request(self, method: OzonMethod[OzonType]) -> OzonType:
        async with self.session.request(
            method.__http_method__,
            API_BASE_URL.format(method.__api_method__),
            json=self.retort.dump(method)
        ) as response:
            return self.check_response(
                method,
                response.status,
                await response.text()
            )

    async def close(self) -> None:
        await self.session.close()
