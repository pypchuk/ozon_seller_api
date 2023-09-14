from os import environ
from datetime import datetime, timedelta
import pytest

from ozon_seller_api import OzonClient
from ozon_seller_api.methods.fbo_posting_list import FboPostingListFilter, FboPostingWithParams


pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_fbo_posting_list():
    async with OzonClient(
        api_key=environ.get("OZON_API_KEY"),
        client_id=environ.get("OZON_CLIENT_ID")
    ) as client:

        await client.fbo_postings_list(
            limit=5,
            offset=5,
            _with=FboPostingWithParams(
                analytics_data=True,
            ),
            _filter=FboPostingListFilter(
                since=datetime.now() - timedelta(days=1),
                to=datetime.now(),
            )
        )
