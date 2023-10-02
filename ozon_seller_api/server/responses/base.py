from typing import cast

import json

from datetime import datetime

from dataclasses import dataclass

from adaptix import Retort, name_mapping, dumper


@dataclass
class Response:
    http_status: int


RESPONSE_RETORT = Retort(
    recipe=[
        name_mapping(skip="http_status"),
        dumper(datetime, lambda x: cast(datetime, x).strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
    ]
)


def to_json(response: Response) -> str:
    json_data = RESPONSE_RETORT.dump(response)
    return json.dumps(json_data)
