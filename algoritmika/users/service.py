

class UserService:
    def __init__(self, user_storage):
        self.user_storage = user_storage

    def get_users(self, limit, offset):
        return self.user_storage.filter(limit=limit, offset=offset)

    def create(self,name):
        return self.user_storage.create(name=name)

    def get(self, pk):
        return self.user_storage.get(pk)

    def update(self, user, params):
        return self.user_storage.update(user, params)

    def delete(self, pk):
        self.user_storage.delete(int(pk))

    def count(self):
        self.user_storage.get_len_list_entities()