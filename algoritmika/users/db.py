from algoritmika.core.generic import Base


class User(Base):
    count = 0

    def __init__(self, name):
        super().__init__(name)
        User.count += 1


user_0 = User('Alex-0')
user_1 = User('Alex')
user_2 = User('Mariya')
user_3 = User('Fedor')
user_4 = User('Peter_1')
user_5 = User('Ivan_4')
user_6 = User('Nicola-2')
user_7 = User('Katya')
user_8 = User('Fridrix')
user_9 = User('Kalita')

db_users = [
    {0: user_0},
    {1: user_1},
    {2: user_2},
    {3: user_3},
    {4: user_4},
    {5: user_5},
    {6: user_6},
    {7: user_7},
    {8: user_8},
    {9: user_9},
]
