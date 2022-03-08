from algoritmika.core.exceptions import NotFoundEntity
import falcon


class BookNotFoundException(NotFoundEntity):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        resp.body = f"Book not found is library"
        resp.status = falcon.HTTP_404


class PATHNotFoundException(NotFoundEntity):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        resp.body = f"Invalid params path"
        resp.status = falcon.HTTP_404


class InccorectedRequestException(Exception):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        resp.body = f"The submitted request is invalid."
        resp.status = falcon.HTTP_404

