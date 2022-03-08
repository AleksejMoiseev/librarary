from algoritmika.core.generic import DICTStorage
from algoritmika.books.db import db_books, Books
from algoritmika.books.exceptions import BookNotFoundException


books_storage = DICTStorage(
    db=db_books,
    exception=BookNotFoundException(),
    model=Books
)