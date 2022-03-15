
from algoritmika.library.exceptions import InccorectedRequestException


class LibraryBase:
    def __init__(self, actors, books):
        self.actors = actors
        self.books = books

    def get_actors(self, limit, offset):
        return self.actors.filter(limit=limit, offset=offset)

    def get_books(self, limit, offset):
        return self.books.filter(limit=limit, offset=offset)

    def get_status_book(self, pk):
        book = self.books.get(pk)
        return book.status

    def take_book(self, book_id, user_id):
        idx, book = self.books.get(book_id)
        is_busy_book = book.status['status']
        if not is_busy_book:
            book.status['user'] = user_id
            book.status['status'] = True
            return book
        return book.status

    def return_book(self, pk):
        idx, book = self.books.get(pk)
        is_busy_book = book.status['status']
        if not is_busy_book:
            raise InccorectedRequestException()
        book.status['user'] = None
        book.status['status'] = False
        return book.status

    def len_books(self):
        return self.books.get_len_list_entities()

    def len_actors(self):
        return self.actors.get_len_list_entities()

