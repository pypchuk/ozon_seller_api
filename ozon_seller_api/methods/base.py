from typing import TypeVar, Any, Generic


OzonType = TypeVar("OzonType", bound=Any)


class OzonMethod(Generic[OzonType]):
    __returning__: type
    __api_method__: str
    __http_method__: str
