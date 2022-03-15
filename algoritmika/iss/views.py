import json
from datetime import datetime
from enum import Enum
from wsgiref import simple_server

import falcon

app = falcon.App()


class IssueStatus(Enum):
    NEW = 1
    TO_APPROVE = 2
    APPROVED = 3
    DECLINED = 4


ent_data = {
    '1': {
        "id": 1,
        "status": IssueStatus.NEW.value,
        "title": "A",
        "text": "B",
        "assignee": "Not Me",
        "tags": ["a", "b", "c"],
        "author": "me",
        "created_date": datetime.strftime(datetime.utcnow(), "%s"),
        "modified_date": datetime.strftime(datetime.utcnow(), "%s"),
    },
    '2': {
        "id": 2,
        "status": IssueStatus.NEW.value,
        "title": "B",
        "text": "A",
        "assignee": "Not Me2",
        "tags": ["a2", "b2", "c2"],
        "author": "me2",
        "created_date": datetime.strftime(datetime.utcnow(), "%s"),
        "modified_date": datetime.strftime(datetime.utcnow(), "%s"),
    }
}


class IssueResource:
    def on_get(self, req, resp, eid):
        if eid not in ent_data:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPNotFound(title='Entity with specified ID not found', description='Some description here')
        ent = ent_data[eid]
        resp.body = json.dumps(ent)
        resp.status = falcon.HTTP_200

    def on_put(self, req, resp, eid):
        if eid not in ent_data:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPNotFound(title='Entity with specified ID not found', description='Some description here')
        updated_ent = req.media
        ent_data[eid] = updated_ent
        resp.status = falcon.HTTP_204

    def on_patch(self, req, resp, eid):
        if eid not in ent_data:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPNotFound(title='Entity with specified ID not found', description='Some description here')
        patched_ent = req.get_media()
        old_ent = ent_data[eid]
        if "title" in patched_ent:
            old_ent["title"] = patched_ent.get("title")
        if "text" in patched_ent:
            old_ent["text"] = patched_ent.get("text")
        if "assignee" in patched_ent:
            old_ent["assignee"] = patched_ent.get("assignee")
        if "tags" in patched_ent:
            old_ent["tags"] = patched_ent.get("tags")
        if "author" in patched_ent:
            old_ent["author"] = patched_ent.get("author")
        if "status" in patched_ent:
            old_ent["status"] = patched_ent.get("status")
        old_ent["modified_date"] = datetime.strftime(datetime.utcnow(), "%s")
        resp.status = falcon.HTTP_204

    def on_delete(self, req, resp, eid):
        if eid not in ent_data:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPNotFound(title='Entity with specified ID not found', description='Some description here')
        ent_data.pop(eid)
        resp.status = falcon.HTTP_204


class IssuesResource:
    def on_get(self, req, resp):
        limit = req.get_param_as_int('limit') or 50
        offset = req.get_param_as_int('offset') or 0
        sort_by = req.get_param('sort_by') or None
        order_by = req.get_param('order_by') or None

        response_data = list(ent_data.values())[offset:limit + offset]
        if sort_by is not None:
            response_data.sort(key=lambda x: x[sort_by], reverse=order_by == "desc")

        resp.body = json.dumps(response_data)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        new_ent = req.get_media()
        new_ent_id = len(ent_data.keys()) + 1
        new_ent["id"] = new_ent_id
        new_ent["created_date"] = datetime.strftime(datetime.utcnow(), "%s")
        new_ent["modified_date"] = datetime.strftime(datetime.utcnow(), "%s")
        ent_data[str(new_ent_id)] = new_ent
        resp.status = falcon.HTTP_201
        resp.location = f'/issues/{new_ent_id}'
