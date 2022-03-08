from algoritmika.core.exceptions import NotFoundEntity
import falcon


class UserNotFoundException(NotFoundEntity):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        resp.body = f"User Not Found"
        resp.status = falcon.HTTP_404


class DataNotFoundException(NotFoundEntity):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        resp.body = f"Data Not Found"
        resp.status = falcon.HTTP_404


class UserNameNotFoundException(NotFoundEntity):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        resp.body = f"username Not Found in request"
        resp.status = falcon.HTTP_404