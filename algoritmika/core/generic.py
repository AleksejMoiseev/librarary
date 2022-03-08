from abc import ABC, abstractmethod

from algoritmika.core.exceptions import BaseNotFoundException


class Base:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def update(self, **params: dict):
        for attr, value in params.items():
            if getattr(self, attr, False):
                setattr(self, attr, value)
        return self


class AbstractStorage(ABC):
    """Storage"""

    db = None

    @abstractmethod
    def filter(self, limit=None, offset=0):
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def get(self, pk):
        pass

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass


class BaseView(ABC):
    """
    Storage
    """
    db = None

    @abstractmethod
    def get_entities(self, limit=None, offset=0):
        pass

    @abstractmethod
    def get_entity(self, pk):
        pass

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass

    @abstractmethod
    def update(self, pk):
        pass

    @abstractmethod
    def create(self):
        pass


class DICTStorage(AbstractStorage):
    """ Storage DICT"""

    def __init__(self, db: list , exception: BaseNotFoundException, model: Base):
        self.db = db
        self.exception = exception
        self.model = model

    def get_list_entities(self):
        return list(self.db)

    def all(self):
        return self.db

    def get(self, pk: int):
        for idx,  d in enumerate(self.db):
            entity = list(d.values())[0]
            if entity.pk == pk:
                return idx, entity
        raise self.exception

    def save(self, user):
        self.db.append({user.pk: user})

    def create_user(self, name):
        user = self.model(name)
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


