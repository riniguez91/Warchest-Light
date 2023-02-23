from cell import Cell, Unit

class Board:
    def __init__(self):
        self.board = [[Cell(row, col, Unit()) for col in range(5)] for row in range(5)]

    def print_board(self):
        # letter_to_num = {'a': 0, 'b': '1', 'c': 2, 'd': 3, 'e': 4}
        letters = ['a', 'b', 'c', 'd', 'e']

        print('\n    0  1  2  3  4')
        print('    -------------')
        for i in range(len(self.board)):
            print(f'{letters[i]}|  ·  ·  ·  ·  ·')
