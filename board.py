from cell import Cell, Unit
from player import Player

class Board:
    def __init__(self, crow: Player, wolf: Player):
        self.board: list = [[Cell(row, col, Unit()) for col in range(5)] for row in range(5)]
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
        letters: list = ['a', 'b', 'c', 'd', 'e']

        print('\n    0  1  2  3  4')
        print('    -------------')
        for i in range(len(self.board)):
            print(f'{letters[i]}|', end='')
            for j in range(len(self.board[0])):
                print(f'  {self.board[i][j].unit.unit_symbol}', end='')
            print()
    
    def choose_action(self, player):
        action = str(input('Make an action (move/recruit/place/attack/control/initiative/forfeit): '))
        # match statement requires python 3.10+
        match action.lower():
            case 'move':
                self.move(player)

            case 'recruit':
                self.recruit(player)

            case 'place':
                self.place(player)

            case 'attack':
                self.attack(player)

            case 'control':
                self.control(player)

            case 'initiative':
                self.initiative(player)

            case 'forfeit':
                self.forfeit(player)

            case _:
                print('That is not a valid action, please try again.')
                
    
    def move(self, player):
        print('move message')

    def recruit(self, player):
        print('recruit message')

    def place(self, player):
        print('place message')

    def attack(self, player):
        print('attack message')

    def control(self, player):
        print('control message') 

    def initiative(self, player):
        print('initiative message')

    def forfeit(self, player):
        print('forfeit message')
