import falcon
from falcon import Request, Response

from algoritmika.library.constans import Action
from algoritmika.library.exceptions import PATHNotFoundException
from algoritmika.library.models import LibraryBase
from algoritmika.users.exceptions import DataNotFoundException

library = LibraryBase()


class LibraryCreateView:

    def on_post(self, req: Request, resp: Response, action):
        data = req.get_media()
        book_id = int(data.get('book'))
        user_id = int(data.get('user'))
        if not book_id or not user_id:
            raise DataNotFoundException()
        if action == Action.take.value:
            resp.body = library.take_book(book_id=book_id, user_id=user_id)
            resp.status = falcon.HTTP_200
        elif action == Action.return_book.value:
            resp.body = library.return_book(book_id)
            resp.status = falcon.HTTP_200
        elif action == Action.status.value:
            resp.body = library.get_status_book(book_id)
            resp.status = falcon.HTTP_200
        else:
            raise PATHNotFoundException()


class BooksLibraryView:
    def on_get(self, req: Request, resp: Response):
        limit = req.get_param_as_int('limit') or library.len_books()
        offset = req.get_param_as_int('offset') or 0
        resp.body = library.get_books(limit=limit, offset=offset)
        resp.status = falcon.HTTP_200


class UsersLibraryView:
    def on_get(self, req: Request, resp: Response):
        limit = req.get_param_as_int('limit') or library.len_books()
        offset = req.get_param_as_int('offset') or 0
        resp.body = library.get_actors(limit=limit, offset=offset)
        resp.status = falcon.HTTP_200

