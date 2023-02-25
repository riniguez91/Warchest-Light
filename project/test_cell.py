import unittest

from cell import Unit, Archer

class TestCell(unittest.TestCase):
    def setUp(self):
        self.unit = Unit()
        self.archer = Archer()

    def test_is_orthogonal(self):
        # Valid tests
        self.assertTrue(self.unit.is_orthogonal((0,0), (0,1)))
        self.assertTrue(self.unit.is_orthogonal((0,0), (1,0)))
        self.assertTrue(self.unit.is_orthogonal((1,1), (1,2)))
        self.assertTrue(self.unit.is_orthogonal((3,7), (4,7)))

        # Invalid tests
        self.assertFalse(self.unit.is_orthogonal((0,0), (0,0)))
        self.assertFalse(self.unit.is_orthogonal((0,0), (0,2)))
        self.assertFalse(self.unit.is_orthogonal((0,0), (1,1)))

    def test_archer_move(self):
        # Valid tests
        self.assertTrue(self.archer.move((2,2), (3,2))) # up
        self.assertTrue(self.archer.move((2,2), (2,3))) # right
        self.assertTrue(self.archer.move((2,2), (1,2))) # down
        self.assertTrue(self.archer.move((2,2), (2,1))) # left

        # Invalid tests
        self.assertFalse(self.archer.move((2,2), (2,4))) # more than 1 unit
        self.assertFalse(self.archer.move((2,2), (3,3))) # diagonally

    def test_archer_attack(self):
        # Valid tests
        self.assertTrue(self.archer.attack((2,2), (3,2))) # up
        self.assertTrue(self.archer.attack((2,2), (4,2))) # up two units
        self.assertTrue(self.archer.attack((2,2), (1,2))) # left 
        self.assertTrue(self.archer.attack((2,2), (0,2))) # left two units
        self.assertTrue(self.archer.attack((2,2), (3,3))) # diagonal

        # Invalid tests
        self.assertFalse(self.archer.attack((2,2), (2,2))) # 0 units
        self.assertFalse(self.archer.attack((2,2), (6,2))) # more than 2 units
        self.assertFalse(self.archer.attack((2,2), (4,3))) # l-shape

if __name__ == '__main__':
    unittest.main()