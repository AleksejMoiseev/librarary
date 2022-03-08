from algoritmika.core.exceptions import NotFoundEntity
import falcon


class UserNotFoundException(NotFoundEntity):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        resp.body = f"User Not Found"
        resp.status = falcon.HTTP_404