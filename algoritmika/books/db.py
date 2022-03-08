from algoritmika.core.generic import Base


class Books(Base):
    count = 0

    def __init__(self, name):
        super().__init__(name)
        self.status = {'status': False, 'user': None}
        Books.count += 1


book_0 = Books('book_Alex-0')
book_1 = Books('book_Alex')
book_2 = Books('book_Mariya')
book_3 = Books('book_Fedor')
book_4 = Books('book_Peter_1')
book_5 = Books('book_Ivan_4')
book_6 = Books('book_Nicola-2')
book_7 = Books('book_Katya')
book_8 = Books('book_Fridrix')
book_9 = Books('book_Kalita')

db_books = [
    {0: book_0},
    {1: book_1},
    {2: book_2},
    {3: book_3},
    {4: book_4},
    {5: book_5},
    {6: book_6},
    {7: book_7},
    {8: book_8},
    {9: book_9},
]

