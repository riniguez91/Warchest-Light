from cell import Cell, Unit
from player import Player

class Board:
    def __init__(self, crow: Player, wolf: Player):
        self.board = [[Cell(row, col, Unit()) for col in range(5)] for row in range(5)]
        # Set the initial control points
        self.control_points(crow, wolf)

    def control_points(self, crow, wolf):
        # Crow starting control point
        self.board[0][2] = Cell(0, 1, Unit(crow, 0, 'Control', 'C'))
        # Wolf starting control point
        self.board[4][2] = Cell(4, 1, Unit(wolf, 0, 'Control', 'C'))

        # Set the 'free' control points
        self.board[2][0] = Cell(0, 1, Unit(None, 0, 'Control', '@'))
        self.board[2][2] = Cell(0, 1, Unit(None, 0, 'Control', '@'))
        self.board[2][4] = Cell(0, 1, Unit(None, 0, 'Control', '@'))

    def print_board(self):
        # letter_to_num = {'a': 0, 'b': '1', 'c': 2, 'd': 3, 'e': 4}
        letters = ['a', 'b', 'c', 'd', 'e']

        print('\n    0  1  2  3  4')
        print('    -------------')
        for i in range(len(self.board)):
            print(f'{letters[i]}|', end='')
            for j in range(len(self.board[0])):
                print(f'  {self.board[i][j].unit.unit_symbol}', end='')
            print()
