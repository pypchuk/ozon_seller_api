from dataclasses import dataclass


class OzonObject:
    pass


@dataclass
class ErrorDetails:
    typeUrl: str
    value: str


@dataclass
class ErrorObject(OzonObject):
    code: int
    details: list[ErrorDetails]
    message: str
