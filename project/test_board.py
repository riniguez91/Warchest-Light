import unittest
from unittest.mock import patch
from player import Player
from board import Board
from cell import Cell, Unit, Knight, Archer, Mercenary, Berserker

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.crow = Player('Crow', 'C')
        self.crow.hand = [Knight(self.crow), Knight(self.crow), Archer(self.crow)]
        self.wolf = Player('Wolf', 'W')
        self.wolf.hand = [Mercenary(self.wolf), Mercenary(self.wolf), Berserker(self.wolf)]
        self.board = Board(self.crow, self.wolf)

    def test_control_points(self):
        # Call the function
        self.board.control_points(self.crow, self.wolf)
    
        # Test valid positions
        self.assertTrue(self.board.grid[0][2].compare(Cell(0, 2, Unit(self.crow, 'Control', 'C'))))
        self.assertTrue(self.board.grid[4][2].compare(Cell(4, 2, Unit(self.wolf, 'Control', 'C'))))
        self.assertTrue(self.board.grid[2][0].compare(Cell(2, 0, Unit(None, 'Control', '@'))))
        self.assertTrue(self.board.grid[2][2].compare(Cell(2, 2, Unit(None, 'Control', '@'))))
        self.assertTrue(self.board.grid[2][3].compare(Cell(2, 3, Unit(None, 'Control', '@'))))
        self.assertTrue(self.board.grid[2][4].compare(Cell(2, 4, Unit(None, 'Control', '@'))))

        # Test invalid positions
        self.assertFalse(self.board.grid[0][1].compare(Cell(0, 4, Unit(self.crow, 'Control', 'C'))))
        self.assertFalse(self.board.grid[4][2].compare(Cell(16, 2, Unit(self.wolf, 'Control', 'C'))))
        self.assertFalse(self.board.grid[2][3].compare(Cell(2, 3, Unit(None, 'Bad unit type', '@'))))

    def test_valid_board_position(self):
        # Test valid positions
        self.assertTrue(self.board.valid_board_position('a,0'))
        self.assertTrue(self.board.valid_board_position('e,4'))
        self.assertTrue(self.board.valid_board_position('c,2'))

        # Test invalid positions
        self.assertFalse(self.board.valid_board_position('f,3'))
        self.assertFalse(self.board.valid_board_position('d,5'))
        self.assertFalse(self.board.valid_board_position('2,2'))

    def test_valid_start_position(self):
        # Test valid inputs
        self.assertTrue(self.board.valid_start_position(Unit(self.crow, 'Knight', 'K'), self.crow))
        self.assertTrue(self.board.valid_start_position(Unit(self.crow, 'Archer', 'A'), self.crow))
                        
        # Test invalid inputs
        self.assertFalse(self.board.valid_start_position(Unit(self.crow, 'Knight', 'K'), self.wolf))
        self.assertFalse(self.board.valid_start_position(Unit(self.crow, 'Control', 'C'), self.crow))
        self.assertFalse(self.board.valid_start_position(Unit(self.crow, 'Empty', '·'), self.crow))

    @patch('builtins.input', side_effect=['Knight', 'a,1'])
    def test_place_valid_knight_piece(self, mock_input):
        # The unit in that position should be assigned to the crow player
        self.board.place(self.crow)
        self.assertEquals(self.board.grid[0][1].unit.player.name, self.crow.name)

    @patch('builtins.input', side_effect=['Archer', 'a,3'])
    def test_place_valid_archer_piece(self, mock_input):
        # The unit in that position should be assigned to the crow player
        self.board.place(self.crow)
        self.assertEquals(self.board.grid[0][3].unit.player.name, self.crow.name)

    @patch('builtins.input', side_effect=['Mercenary', 'a,1'])
    def test_place_invalid_mercenary_piece(self, mock_input):
        # Assert is none as it shouldn't place the unit in that position
        self.board.place(self.crow)
        self.assertIsNone(self.board.grid[0][1].unit.player)

    @patch('builtins.input', side_effect=['Berserker', 'a,1'])
    def test_place_invalid_berserker_piece(self, mock_input):
        # Assert is none as it shouldn't place the unit in that position
        self.board.place(self.crow)
        self.assertIsNone(self.board.grid[0][1].unit.player)
        
if __name__ == '__main__':
    unittest.main()
