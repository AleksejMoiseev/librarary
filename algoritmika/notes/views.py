from algoritmika.core.views import BaseListCreateView, BaseRetrieveView
from algoritmika.notes.exceptions import NotesNotFoundEntity
from algoritmika.notes.models import notes_storage
from algoritmika.notes.service import NoteService


notes_service = NoteService(notes_storage)


class NotesBase:
    storage = notes_service
    exception = NotesNotFoundEntity()


class NotesListCreateView(NotesBase, BaseListCreateView):
    pass


class NotesRetrieveView(NotesBase, BaseRetrieveView):
    pass
