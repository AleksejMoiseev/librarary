class IssueService:
    def __init__(self, issue_storage):
        self.issue_storage = issue_storage

    def filter(self, limit, offset):
        return self.issue_storage.filter(limit=limit, offset=offset)

    def create(self,name):
        return self.issue_storage.create(name=name)

    def get(self, pk):
        return self.issue_storage.get(pk)

    def update(self, user, params):
        return self.issue_storage.update(user, params)

    def delete(self, pk):
        self.issue_storage.delete(int(pk))

    def get_len_list_entities(self):
        self.issue_storage.get_len_list_entities()