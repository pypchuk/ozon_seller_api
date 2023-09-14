from os import environ

import pytest
from datetime import datetime, timedelta

from ozon_seller_api import OzonClient
from ozon_seller_api.methods.create_postings_report import Filter


pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_create_stock_report():
    async with OzonClient(
        api_key=environ.get("OZON_API_KEY"),
        client_id=environ.get("OZON_CLIENT_ID")
    ) as client:

        r = await client.create_stock_report()

        report = await client.report_info(r.code)


@pytest.mark.asyncio
async def test_create_postings_report():
    async with OzonClient(
        api_key=environ.get("OZON_API_KEY"),
        client_id=environ.get("OZON_CLIENT_ID")
    ) as client:

        r = await client.create_postings_report(
            Filter(
                processed_at_from=datetime.now() - timedelta(days=1),
                processed_at_to=datetime.now(),
            )
        )

        report = await client.report_info(r.code)
