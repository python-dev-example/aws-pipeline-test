import json
from typing import Optional, Awaitable

from datetime import datetime
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado_sqlalchemy import SessionMixin

from app.constants import HttpHeaders, ContentType


def create_json_error(reason, status_code, exception):
    response = dict()

    response['error'] = reason
    response['status'] = status_code
    response['timestamp'] = datetime.now().timestamp()

    if exception:
        response['exception'] = exception[0].__name__
        response['message'] = str(exception[1])

    return response


class JsonRequestHandler(SessionMixin, RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def prepare(self):
        if self.request.body:
            try:
                json_data = json.loads(self.request.body)
                self.request.json_body = json_data
            except ValueError:
                message = {"message": "Bad request"}
                self.send_error(400, message=message)

    def set_default_headers(self):
        self.set_header(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON)

    def write_error(self, status_code, **kwargs):
        self.set_header(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON)

        response = create_json_error(self._reason, status_code, kwargs.get('exc_info'))

        self.finish(response)

    def write_as_json(self, response):
        if isinstance(response, (list, tuple)) and not response:
            response = []
        elif isinstance(response, dict) and not response:
            response = {}

        response = response if response else {}
        self.write(json.dumps(response))


class HealthCheckRequestHandler(JsonRequestHandler):
    async def get(self):
        self.write_as_json({})


routes = [
    (r'/api/v1/scheduler/create', HealthCheckRequestHandler),
]


def create_app():
    return Application(
        routes,
        compress_response=True,
    )


if __name__ == '__main__':
    application = create_app()

    application.listen(5000)
    IOLoop.instance().start()
