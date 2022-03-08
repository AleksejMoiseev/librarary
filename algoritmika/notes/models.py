from algoritmika.core.generic import DICTStorage
from algoritmika.notes.db import Notes
from algoritmika.notes.db import db_notes
from algoritmika.notes.exceptions import NotesNotFoundEntity

notes_storage = DICTStorage(
    db=db_notes,
    exception=NotesNotFoundEntity(),
    model=Notes
)