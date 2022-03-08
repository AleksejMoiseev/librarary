from algoritmika.core.generic import Base


class Notes(Base):
    count = 0

    def __init__(self, name):
        super().__init__(name)
        Notes.count += 1


note_0 = Notes('note_Alex-0')
note_1 = Notes('note_Alex')
note_2 = Notes('note_Mariya')
note_3 = Notes('note_Fedor')
note_4 = Notes('note_Peter_1')
note_5 = Notes('note_Ivan_4')
note_6 = Notes('note_Nicola-2')
note_7 = Notes('note_Katya')
note_8 = Notes('note_Fridrix')
note_9 = Notes('note_Kalita')

db_notes = [
    {0: note_0},
    {1: note_1},
    {2: note_2},
    {3: note_3},
    {4: note_4},
    {5: note_5},
    {6: note_6},
    {7: note_7},
    {8: note_8},
    {9: note_9},
]

