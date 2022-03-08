from algoritmika.core.views import BaseListCreateView, BaseRetrieveView
from algoritmika.issues.exceptions import IssuesNotFoundEntity
from algoritmika.issues.models import issues_storage


class IssuesBase:
    storage = issues_storage
    exception = IssuesNotFoundEntity()


class IssuesListCreateView(IssuesBase, BaseListCreateView):
    pass


class IssuesRetrieveView(IssuesBase, BaseRetrieveView):
    pass
