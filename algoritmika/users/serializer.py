import json
from algoritmika.users.db import User
from algoritmika.core.generic import Base


class UserSerializer(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Base):
            return str(o.name)
        return super().default(o)
