
class NoteService:
    def __init__(self, note_storage):
        self.note_storage = note_storage

    def filter(self, limit, offset):
        return self.note_storage.filter(limit=limit, offset=offset)

    def create(self,name):
        return self.note_storage.create(name=name)

    def get(self, pk):
        return self.note_storage.get(pk)

    def update(self, user, params):
        return self.note_storage.update(user, params)

    def delete(self, pk):
        self.note_storage.delete(int(pk))

    def get_len_list_entities(self):
        self.note_storage.get_len_list_entities()