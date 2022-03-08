import falcon


class BaseNotFoundException(Exception):
    def __init__(self, msg: str, entity:str):
        self.msg = msg
        self.entity = entity

    def handle(self, req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        msg = f"{self.entity} -> {self.msg}"
        resp.body = msg
        resp.status = falcon.HTTP_404