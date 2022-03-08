from algoritmika.core.generic import DICTStorage
from algoritmika.issues.db import Issue, db_issues
from algoritmika.issues.exceptions import IssuesNotFoundEntity

issues_storage = DICTStorage(
    db=db_issues,
    exception=IssuesNotFoundEntity(),
    model=Issue
)