import logging

from typing import Callable, Coroutine, Any
from json import loads, JSONDecodeError

from aiohttp.web import Application, post, Request, Response

from adaptix.load_error import LoadError
from adaptix.struct_path import StructPathRendererFilter

from .responses import (
    Response as OzonResponse,
    Error,
    Success,
    PingSuccess,
)
from .responses.base import to_json
from .responses.error import ResponseCode
from .types.base import OzonEvent
from .types.message_type import MessageType

from .type_loader import load_event


logging.getLogger().addFilter(StructPathRendererFilter())

Handler = Callable[[OzonEvent], Coroutine[Any, Any, Error | Success]]
HandlersTable = dict[MessageType, Handler]


class Server:
    def __init__(self, app_version: str, app_name: str, aiohttp_app: Application) -> None:
        self.handlers_table: HandlersTable = {}
        self.app = aiohttp_app

        aiohttp_app.add_routes([post('/', self.push_event_endpoint)])

        async def handle_ping(_) -> PingSuccess:
            return PingSuccess.create(version=app_version, name=app_name)

        # All handlers should return Error or Success response
        # The only exception is ping event, which handler is not created by user directly
        # So I think it's OK not to use separate type hint and just supress error
        self.set_handler(MessageType.TYPE_PING, handle_ping)  # type: ignore

    def set_handler(self, event_type: MessageType, handler: Handler) -> None:
        self.handlers_table[event_type] = handler

    async def push_event_endpoint(self, request: Request) -> Response:
        service_response: OzonResponse = Error.create(
            http_status=500,
            message="Unknown error",
            code=ResponseCode.ERROR_UNKNOWN,
        )

        try:
            obj = await request.json(loads=loads)
            logging.debug("Successfully decoded JSON from string")

            event = load_event(obj)
            logging.debug("Successfully loaded event model from JSON.")

        except JSONDecodeError as e:
            logging.error("JSON decode error.", exc_info=e)

            service_response = Error.create(
                http_status=400,
                message="JSON decode error."
            )
        except LoadError as e:
            logging.error("Error creating model from request data.", exc_info=e)

            service_response = Error.create(
                http_status=400,
                message="Error creating model from request data."
            )
        else:
            try:
                handler = self.handlers_table[event.message_type]
            except KeyError:
                logging.warning("No handler for event")

                service_response = Error.create(
                    http_status=500,
                    message="No handler for event",
                    code=ResponseCode.ERROR_UNKNOWN,
                )
            else:
                try:
                    service_response = await handler(event)
                    logging.debug("Successfully handled event")
                except Exception as e:
                    logging.error("Unknown error during handling event", exc_info=e)
                    service_response = Error.create(
                        http_status=500,
                        message="Unknown error",
                        code=ResponseCode.ERROR_UNKNOWN,
                    )
        finally:
            return Response(
                status=service_response.http_status,
                text=to_json(service_response)
            )
