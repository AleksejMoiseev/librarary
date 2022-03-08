from algoritmika.core.generic import Base


class Books(Base):
    count = 0

    def __init__(self, name):
        super().__init__(name)
        self.book_id = self.count
        Books.count += 1


book_0 = Books('Alex-0')
book_1 = Books('Alex')
book_2 = Books('Mariya')
book_3 = Books('Fedor')
book_4 = Books('Peter_1')
book_5 = Books('Ivan_4')
book_6 = Books('Nicola-2')
book_7 = Books('Katya')
book_8 = Books('Fridrix')
book_9 = Books('Kalita')

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

