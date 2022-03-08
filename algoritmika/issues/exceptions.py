import falcon


class IssuesNotFoundEntity(Exception):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        resp.body = f"Issues Not Found"
        resp.status = falcon.HTTP_404