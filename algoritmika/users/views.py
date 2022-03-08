from algoritmika.users.models import UserBaseView
import falcon
from falcon import Request, Response
from algoritmika.users.exceptions import UserNotFoundException


class UserListCreateController(UserBaseView):
    def on_get(self, req, resp):
        limit = req.get_param_as_int('limit') or self.get_len_list_entities()
        offset = req.get_param_as_int('offset') or 0
        resp.body = self.filter(limit=limit, offset=offset)
        resp.status = falcon.HTTP_200

    def on_post(self, req: Request, resp: Response):
        data = req.get_media()
        if not data:
            raise UserNotFoundException(msg="not valid POST request", entity="User")
        name = data.get('name')
        if not name:
            raise UserNotFoundException(msg="Name not found", entity="User")
        user = self.create_user(name=name)
        resp.body = {
            'id': user.pk,
            'name': user.name,
        }
        resp.status = falcon.HTTP_200


class UserRetrieveController(UserBaseView):

    def on_put(self, req: Request, resp: Response, user_id):
        params = req.get_media()
        if not params:
            raise UserNotFoundException(msg="Params not found", entity="User")
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
