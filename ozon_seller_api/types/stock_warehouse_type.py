from enum import Enum


class WarehouseType(str, Enum):
    ALL = "ALL"
    EXPRESS_DARK_STORE = "EXPRESS_DARK_STORE"
    NOT_EXPRESS_DARK_STORE = "NOT_EXPRESS_DARK_STORE"
