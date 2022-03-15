import falcon
from falcon import Request, Response

from algoritmika.users.exceptions import (
    DataNotFoundException, UserNameNotFoundException
)
from algoritmika.users.models import UserBaseView, user_storage
from algoritmika.users.service import UserService

user_service = UserService(user_storage)


class UserListCreateController(UserBaseView):
    def on_get(self, req, resp):
        limit = req.get_param_as_int('limit') or self.get_len_list_entities()
        offset = req.get_param_as_int('offset') or 0
        resp.body = self.filter(limit=limit, offset=offset)
        resp.status = falcon.HTTP_200

    def on_post(self, req: Request, resp: Response):
        data = req.get_media()
        if not data:
            raise DataNotFoundException()
        name = data.get('name')
        if not name:
            raise UserNameNotFoundException()
        user = self.create(name=name)
        resp.body = {
            'id': user.pk,
            'name': user.name,
        }
        resp.status = falcon.HTTP_200


class UserRetrieveController(UserBaseView):

    def on_put(self, req: Request, resp: Response, user_id):
        params = req.get_media()
        if not params:
            raise DataNotFoundException()
        idx, user = self.get(int(user_id))
        user_updated = self.update(user, params)
        resp.body = {
            'id': user_updated.pk,
            'name': user_updated.name,
        }
        resp.status = falcon.HTTP_200

    def on_patch(self, req: Request, resp: Response, user_id):
        self.on_put(req, resp, int(user_id))

    def on_get(self, req: Request, resp: Response, user_id):
        idx, user = self.get(int(user_id))
        resp.body = {
            'id': user.pk,
            'name': user.name,
        }
        resp.status = falcon.HTTP_200

    def on_delete(self, req: Request, resp: Response, user_id):
        resp.body = self.delete(int(user_id))
        resp.status = falcon.HTTP_200


class UserListCreateView:
    def on_get(self, req, resp):
        limit = req.get_param_as_int('limit') or user_service.count()
        offset = req.get_param_as_int('offset') or 0
        resp.body = user_service.get_users(limit=limit, offset=offset)
        resp.status = falcon.HTTP_200

    def on_post(self, req: Request, resp: Response):
        data = req.get_media()
        if not data:
            raise DataNotFoundException()
        name = data.get('name')
        if not name:
            raise UserNameNotFoundException()
        user = user_service.create(name=name)
        resp.body = {
            'id': user.pk,
            'name': user.name,
        }
        resp.status = falcon.HTTP_200


class UserRetrieveView:
    def on_put(self, req: Request, resp: Response, user_id):
        params = req.get_media()
        if not params:
            raise DataNotFoundException()
        idx, user = user_service.get(int(user_id))
        user_updated = user_service.update(user, params)
        resp.body = {
            'id': user_updated.pk,
            'name': user_updated.name,
        }
        resp.status = falcon.HTTP_200

    def on_patch(self, req: Request, resp: Response, user_id):
        self.on_put(req, resp, int(user_id))

    def on_get(self, req: Request, resp: Response, user_id):
        idx, user = user_service.get(int(user_id))
        resp.body = {
            'id': user.pk,
            'name': user.name,
        }
        resp.status = falcon.HTTP_200

    def on_delete(self, req: Request, resp: Response, user_id):
        resp.body = user_service.delete(int(user_id))
        resp.status = falcon.HTTP_200

