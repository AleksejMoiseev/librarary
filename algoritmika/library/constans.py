import enum


class Action(enum.Enum):
    take = 'take'
    return_book = 'return'
    status = 'status'