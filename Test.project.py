import unittest
from P1controller import *


class MyTestCase(unittest.TestCase):
    def testlogic(self):
        self.assertEqual(logic('Rock', 'Rock'), 'Tie')
        self.assertEqual(logic('Scissors', 'Rock'), 'Computer Rock, User Scissors')
        self.assertEqual(logic('Paper', 'Scissors'), 'Computer Scissors, User Paper')
        self.assertEqual(logic('Rock', 'Paper'), 'Computer Paper, User Rock')
        self.assertEqual(logic('Rock', 'Scissors'), 'Computer Scissors, User Rock')
        self.assertEqual(logic('Scissors', 'Paper'), 'Computer paper, User Scissors')
        self.assertEqual(logic('Paper', 'Rock'), 'Computer Rock, User paper')




if __name__ == '__main__':
    unittest.main()
