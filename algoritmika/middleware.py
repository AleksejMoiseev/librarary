import base64
import json
import re

import falcon
from falcon import Request, Response

from algoritmika.jwt import get_jwt_token, BEARER, is_valid_refresh_token, is_valid_access_token
from algoritmika.models import user
from algoritmika.conf import config, jwt_skip_rules
from algoritmika.views import NoteListCreateView
from algoritmika.users.serializer import UserSerializer


class JSONTranslator:

    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header('Content-Type', 'application/json')
        resp.body = json.dumps(resp.body,cls=UserSerializer)


def check_excluded_rules(method, path, config):
    for method_rule, path_rule in config:
        path_rule = path_rule.replace('*', '.+') + "[/]?$"
        if method == method_rule and re.match(path_rule.replace('*', '.+'), path):
            break
    else:
        return False
    return True


class BasicAuthMiddleware:
    basic_token = "bG9naW46cGFzc3dvcmQ="

    def process_resource(self, req, resp, resource, params):
        method = req.method
        path = req.path
        if not check_excluded_rules(method=method, path=path, config=config):
            auth_header = req.get_header("Authorization")
            if not auth_header:
                raise falcon.HTTPUnauthorized()
            _, access_token = auth_header.split(' ')
            if access_token != self.basic_token:
                raise falcon.HTTPUnauthorized()
        resp.context['user'] = user


class JWTAuthMiddleware:

    def __init__(self):
        self.refresh_token = None
        self.access_token = None

    def process_resource(self, req: Request, resp: Response, resource, params):
        if isinstance(resource, (NoteListCreateView, )):
            return
        if req.path == "/login/":
            if req.method == "POST":
                data = req.get_media()
                login = data.get('login')
                password = data.get('password')
                if not(login and password):
                    raise falcon.HTTPUnauthorized(description='The request must contain a login and password')
                if login == user.login and password == user.password:

                    if self.refresh_token and not is_valid_refresh_token(self.refresh_token):
                        self.refresh_token, self.access_token = None, None

                    if not self.access_token or not self.refresh_token:
                        self.refresh_token, self.access_token = get_jwt_token()

                    resp.body = {
                        "refresh_token": self.refresh_token,
                        "access_token": self.access_token
                    }
                    resp.status = falcon.HTTP_200
            elif req.method == "PUT":
                data = req.get_header("Authorization").split(' ')
                if not (data[0] == BEARER and len(data) == 2):
                    raise falcon.HTTPUnauthorized(description='Custom Tholen Header Parameters')
                token = data[1]
                if token == self.refresh_token:
                    self.refresh_token, self.access_token = get_jwt_token()
                    resp.body = {
                        "refresh_token": self.refresh_token,
                        "access_token": self.access_token
                    }
                else:
                    raise falcon.HTTPUnauthorized(description='Incorrect refresh token')
            else:
                raise falcon.HTTPMethodNotAllowed(allowed_methods=['POST', 'PUT'])
        else:
            data = req.get_header("Authorization").split(' ')
            if not (data[0] == BEARER and len(data) == 2):
                raise falcon.HTTPUnauthorized(description='Invalid headers token')
            token = data[1]
            if token == self.access_token:
                resp.status = falcon.HTTP_200
            else:
                raise falcon.HTTPUnauthorized(description='Invalid headers token')


class JWTUserAuthMiddleware:

    def process_resource(self, req: Request, resp: Response, resource, params):
        if check_excluded_rules(method=req.method, path=req.path, config=jwt_skip_rules):
            return

        data = req.get_header("Authorization", required=True).split(' ')
        token_auth = self.validate_data(data)
        token = token_auth["value"]
        if not is_valid_access_token(token):
            raise falcon.HTTPUnauthorized(description='Invalid headers token')

    @staticmethod
    def validate_data(data):
        if not (data[0] == BEARER and len(data) == 2):
            raise falcon.HTTPUnauthorized(description='Data is not valid')
        return {
            "name": data[0],
            "value": data[1]
        }


class JWTUserAuthView:

    def on_post(self, req, resp):
        data = req.get_media()
        login = data.get('login')
        password = data.get('password')
        if not (login and password):
            raise falcon.HTTPUnauthorized(description='The request must contain a login and password')
        if login == user.login and password == user.password:
            refresh_token, access_token = get_jwt_token()

            resp.body = {
                "refresh_token": refresh_token,
                "access_token": access_token
            }
            resp.status = falcon.HTTP_200

    def on_put(self, req, resp):
        data = req.get_header("Authorization").split(' ')
        token_auth = JWTUserAuthMiddleware.validate_data(data)
        token = token_auth["value"]
        if is_valid_refresh_token(token):
            refresh_token, access_token = get_jwt_token()
            resp.body = {
                "refresh_token": refresh_token,
                "access_token": access_token
            }
        else:
            raise falcon.HTTPUnauthorized(description='Incorrect refresh token')
