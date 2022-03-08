import falcon
from falcon import Request, Response
from algoritmika.core.generic import AbstractStorage, DICTStorage
from algoritmika.notes.models import notes_storage
from algoritmika.notes.exceptions import NotesNotFoundEntity


class BaseListCreateView:
    storage: DICTStorage
    exception: Exception()

    def on_get(self, req, resp):
        limit = req.get_param_as_int('limit') or self.storage.get_len_list_entities()
        offset = req.get_param_as_int('offset') or 0
        resp.body = self.storage.filter(limit=limit, offset=offset)
        resp.status = falcon.HTTP_200

    def on_post(self, req: Request, resp: Response):
        data = req.get_media()
        if not data:
            raise self.exception
        name = data.get('name')
        if not name:
            raise self.exception
        user = self.storage.create(name=name)
        resp.body = {
            'id': user.pk,
            'name': user.name,
        }
        resp.status = falcon.HTTP_200


class BaseRetrieveView:
    storage: DICTStorage
    exception: Exception()

    def on_put(self, req: Request, resp: Response, pk):
        params = req.get_media()
        if not params:
            raise self.exception
        idx, user = self.storage.get(int(pk))
        user_updated = self.storage.update(user, params)
        resp.body = {
            'id': user_updated.pk,
            'name': user_updated.name,
        }
        resp.status = falcon.HTTP_200

    def on_patch(self, req: Request, resp: Response, pk):
        self.on_put(req, resp, int(pk))

    def on_get(self, req: Request, resp: Response, pk):
        idx, user = self.storage.get(int(pk))
        resp.body = {
            'id': user.pk,
            'name': user.name,
        }
        resp.status = falcon.HTTP_200

    def on_delete(self, req: Request, resp: Response, pk):
        resp.body = self.storage.delete(int(pk))
        resp.status = falcon.HTTP_200
