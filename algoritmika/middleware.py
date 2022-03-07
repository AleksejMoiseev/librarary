import base64
import json
import re

import falcon
from falcon import Request, Response

from algoritmika.jwt import get_jwt_token, BEARER, is_live_refresh_token
from algoritmika.models import user
from algoritmika.conf import config
from algoritmika.views import NoteListCreateView


class JSONTranslator:

    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header('Content-Type', 'application/json')
        resp.body = json.dumps(resp.body)


class BasicAuthMiddleware:
    basic_token = "bG9naW46cGFzc3dvcmQ="

    def check_excluded_rules(self, method, path):
        for method_rule, path_rule in config:
            path_rule = path_rule.replace('*', '.+') + "[/]?$"
            if method == method_rule and re.match(path_rule.replace('*', '.+'), path):
                break
        else:
            return False
        return True

    def process_resource(self, req, resp, resource, params):
        method = req.method
        path = req.path
        if not self.check_excluded_rules(method=method, path=path):
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

                    if self.refresh_token and not is_live_refresh_token(self.refresh_token):
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
                    print('!!!', 'Incorrect refresh token')
                    raise falcon.HTTPUnauthorized(description='Incorrect refresh token')
            else:
                raise falcon.HTTPMethodNotAllowed(allowed_methods=['POST', 'PUT'])
        else:
            data = req.get_header("Authorization").split(' ')
            if not (data[0] == BEARER and len(data) == 2):
                print("AAAAAAAA")
                raise falcon.HTTPUnauthorized(description='Invalid headers token')
            token = data[1]
            print(token, self.access_token)
            if token == self.access_token:
                resp.status = falcon.HTTP_200
            else:
                print("SSSSSSSSSSSS")
                raise falcon.HTTPUnauthorized(description='Invalid headers token')
