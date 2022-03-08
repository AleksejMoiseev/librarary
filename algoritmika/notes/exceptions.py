import falcon


class NotesNotFoundEntity(Exception):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        resp.body = f"Notes Not Found"
        resp.status = falcon.HTTP_404