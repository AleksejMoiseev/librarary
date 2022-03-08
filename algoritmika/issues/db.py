from algoritmika.core.generic import Base


class Issue(Base):
    count = 0

    def __init__(self, name):
        super().__init__(name)
        Issue.count += 1


issue_0 = Issue('issue_Alex-0')
issue_1 = Issue('issue_Alex')
issue_2 = Issue('issue_Mariya')
issue_3 = Issue('issue_Fedor')
issue_4 = Issue('issue_Peter_1')
issue_5 = Issue('issue_Ivan_4')
issue_6 = Issue('issue_Nicola-2')
issue_7 = Issue('issue_Katya')
issue_8 = Issue('issue_Fridrix')
issue_9 = Issue('issue_Kalita')

db_issues = [
    {0: issue_0},
    {1: issue_1},
    {2: issue_2},
    {3: issue_3},
    {4: issue_4},
    {5: issue_5},
    {6: issue_6},
    {7: issue_7},
    {8: issue_8},
    {9: issue_9},
]

