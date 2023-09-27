import json

from dataclasses import dataclass

from adaptix import Retort, name_mapping


@dataclass
class Response:
    http_status: int


RESPONSE_RETORT = Retort(
    recipe=[
        name_mapping(skip="http_status")
    ]
)


def to_json(response: Response) -> str:
    json_data = RESPONSE_RETORT.dump(response)
    return json.dumps(json_data)
