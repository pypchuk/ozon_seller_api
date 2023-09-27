from typing import NamedTuple


class FboPostingWithParams(NamedTuple):
    analytics_data: bool = False
    financial_data: bool = False
