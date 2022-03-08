import json
from algoritmika.core.generic import Base


class BaseSerializer(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Base):
            return str(o.name)
        return super().default(o)
