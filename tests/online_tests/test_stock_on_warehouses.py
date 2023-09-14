from os import environ
import pytest

from ozon_seller_api import OzonClient


pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_stock_on_warehouses():
    async with OzonClient(
        api_key=environ.get("OZON_API_KEY"),
        client_id=environ.get("OZON_CLIENT_ID")
    ) as client:

        await client.stocks_on_warehouses(
            limit=5,
        )
