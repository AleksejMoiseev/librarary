from algoritmika.core.generic import BaseView, AbstractStorage
from algoritmika.users.db import db_users, User
from algoritmika.users.exceptions import UserNotFoundException


class UserBaseView(AbstractStorage):
    """ Storage DICT"""

    db = db_users

    def get_list_entities(self):
        return list(self.db)

    def all(self):
        return self.db

    def get(self, pk: int):
        for idx,  d in enumerate(self.db):
            user = list(d.values())[0]
            if user.pk == pk:
                return idx, user
        raise UserNotFoundException(msg="Wrong User_id")

    def save(self, user):
        self.db.append({user.pk: user})

    def create_user(self, name):
        user = User(name)
        self.save(user)
        return user

    def delete(self, pk):
        idx, user = self.get(pk)
        return self.db.pop(idx)

    def update(self, entity, params):
        return entity.update(**params)

    def get_len_list_entities(self):
        return len(self.db)

    def filter(self, limit=None, offset=0):
        if not limit:
            limit = self.get_len_list_entities()
        return self.get_list_entities()[offset: offset + limit]


if __name__ == '__main__':
    idx, user = UserBaseView().get(5)
    print(user)
    user.update(**{"name": 'gggg'})
    print(user)
