from cell import Cell, Unit, Archer
from player import Player

class Board:
    def __init__(self, crow: Player, wolf: Player):
        self.board: list = [[Cell(row, col, Unit()) for col in range(5)] for row in range(5)]
        # Translates a letter to its respective row coordinate
        self.letter_to_num: dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
        # Set the initial control points
        self.control_points(crow, wolf)

    def control_points(self, crow, wolf):
        # Crow starting control point
        self.board[0][2] = Cell(0, 2, Unit(crow, 'Control', 'C'))
        # Wolf starting control point
        self.board[4][2] = Cell(4, 2, Unit(wolf, 'Control', 'C')) 

        # Set the 'free' control points
        self.board[2][0] = Cell(2, 0, Unit(None, 'Control', '@'))
        self.board[2][2] = Cell(2, 2, Unit(None, 'Control', '@'))
        self.board[2][4] = Cell(2, 4, Unit(None, 'Control', '@'))

    def print_board(self):
        row_letters: list = ['a', 'b', 'c', 'd', 'e']

        print('\n    0   1   2   3   4')
        print('    -----------------')
        for i in range(len(self.board)):
            print(f'{row_letters[i]}|', end='')
            for j in range(len(self.board[0])):
                unit: Unit = self.board[i][j].unit
                if unit.player is not None:
                    print(f'  {unit.unit_symbol}{unit.player.symbol}'.ljust(4), end='')
                else:
                    print(f'  {unit.unit_symbol}'.ljust(4), end='')
            print()

    def choose_action(self, player: Player):
        action = str(input('Make an action (move/recruit/place/attack/control/initiative/forfeit): '))
        successful_action = False
        # match statement requires python 3.10+
        match action.lower():
            case 'move':
                successful_action = self.move(player)
            
            case 'recruit':
                successful_action = self.recruit(player)

            case 'place':
                successful_action = self.place(player)

            case 'attack':
                successful_action = self.attack(player)

            case 'control':
                successful_action = self.control(player)

            case 'initiative':
                successful_action = self.initiative(player)

            case 'forfeit':
                self.forfeit(player)

            case _:
                print('That is not a valid action, please try again.')

        # If there has been a successful action, show the current state of the player hand
        if successful_action:
            player.print_hand()

    def remove_piece_from_hand(self, piece: str, player: Player):
        for unit in player.hand:
            if unit.unit_type == piece:
                player.hand.remove(unit)

    def piece_in_hand(self, piece: str, player: Player, remove = False, discard = False):
        for unit in player.hand:
            if unit.unit_type == piece:
                # Move to discard section
                if discard:
                    player.discarded.append(unit)
                # Remove from hand
                if remove:
                    player.hand.remove(unit)
                # Piece has been found in player hand
                return True
        # If it's not in hand return False
        print('Invalid input, piece is not in hand')
        return False
    
    def valid_board_position(self, position: str):
        row, col = position.split(',')
        # If any of the coordinates are out of bounds, we return False as it is an invalid position
        # By checking first if the row or col are valid letters and integers we make sure that the function is robust 
        # against inputs such as 'f,f' or '1, 1'
        if (
            row not in self.letter_to_num 
            or not col.isdigit()
            or self.letter_to_num[row] < 0 
            or self.letter_to_num[row] >= len(self.board) 
            or int(col) < 0 
            or int(col) >= len(self.board[0])
            ):
            print('Invalid coordinate input')
            return False
        # Else return True
        return True

    def valid_start_position(self, unit: Unit, player: Player):
        # Check if the cell at the start coordinate is valid
        if unit.unit_type == 'Empty' or unit.player != player or unit.unit_type == 'Control':
            print('Cell is empty, a control point or it doesn\'t belong to the player')
            return False
        # Valid cell
        return True
    
    def valid_end_position(self, end_position: tuple, control_pos_allowed: bool = True):
        # Check the to_position is either a control unit or an empty unit
        unit: Unit = self.board[end_position[0]][end_position[1]].unit
        # Allow the end position to be a 'Control' unit
        if control_pos_allowed:
            if unit.unit_type != 'Control' and unit.unit_type != 'Empty':
                print('Cell is occupied and piece can not be moved to the position')
                return False
        # Don't allow it and only allow the end position to be an 'Empty' unit
        else:
            if unit.unit_type != 'Empty':
                return False
        # Valid cell
        return True
    
    def translate_to_coordinate(self, position: str):
        # Get row and column values respectively
        row, col = position.split(',')
        # Translate row letter to row number
        row_no: int = self.letter_to_num[row]
        return (row_no, int(col))

    def get_unit(self, position: str):
        coordinate = self.translate_to_coordinate(position)
        row, col = coordinate[0], coordinate[1]
        # Get the unit at that position
        return self.board[row][col].unit
    
    def is_orthogonal_to_control(self, coordinate: tuple, player: Player):
        x, y = coordinate[0], coordinate[1]
        # Check it's not a control point
        if self.board[x][y].unit.unit_symbol[0] == 'C':
            print('Placing in the same coordinates as a control point is not valid.')
            return False
        
        # We need to get the first letter of the unit_symbol since a Control point could be associated to a 
        # player and thus the unit_symbol could contain something like 'Cv', so we can't directly compare it
        # Check upward
        if x - 1  >= 0 and self.board[x-1][y].unit.unit_symbol[0] == 'C' and self.board[x-1][y].unit.player == player:
            return True 
        # Check rightward
        if y + 1 < len(self.board[0]) and self.board[x][y+1].unit.unit_symbol[0] == 'C' and self.board[x][y+1].unit.player == player:
            return True 
        # Check downward
        if x + 1 < len(self.board) and self.board[x+1][y].unit.unit_symbol[0] == 'C' and self.board[x+1][y].unit.player == player:
            return True
        # Check leftward
        if y - 1 >= 0 and self.board[x][y-1].unit.unit_symbol[0] == 'C' and self.board[x][y-1].unit.player == player:
            return True
        
        # If none of the above conditions haven't been satisfied then it is not orthogonal to a control point
        print('The coordinates to place the piece are not orthogonal to a control point')
        return False
    
    def get_unit_from_hand(self, piece: str, player: Player, remove: bool = False):
        for unit in player.hand:
            if unit.unit_type == piece:
                # Remove from hand if the optional parameter is set to True
                if remove:
                    player.hand.remove(unit)
                return unit
            
    def can_recruit_piece(self, piece: str, player: Player):
        # Check if the piece still exists in the assigned units
        if piece not in player.assigned_units:
            print('There are no more units of that type')
            return False
        
        # Add it to the bag (pop a coin from the stack of coins)
        player.bag.append(player.assigned_units[piece].pop())
        print(f'Added the {piece} coin to the bag')

        # If there are no more units, remove them from the assigned units
        if len(player.assigned_units[piece]) == 0:
            del player.assigned_units[piece]
        
        return True
    
    def move(self, player: Player):
        # Check if the from_position is a valid position
        from_position = str(input('From position (row, col): '))
        if not self.valid_board_position(from_position):
            return False
        
        unit: Unit = self.get_unit(from_position)
        # Check the position isn't empty and belongs to the player (but is not a control point)
        if not self.valid_start_position(unit, player):
            return False 
        
        # Check the piece to move is contained in the hand and the board
        piece = str(input('Select a piece of the same type in your hand: '))
        if not (self.piece_in_hand(piece, player) and unit.unit_type == piece):
            return False
        
        to_position = str(input('To position (row, col): '))
        # Check if the to_position is a valid position
        if not self.valid_board_position(to_position):
            return False
        
        # Get the translated coordinates
        translated_start = self.translate_to_coordinate(from_position)
        translated_end = self.translate_to_coordinate(to_position)

        # Check the to_position is either a control unit or an empty unit
        if not self.valid_end_position(translated_end):
            return False
        
        # returns True if it was a valid move, False if it was invalid
        if not unit.move(translated_start, translated_end):
            return False
        
        # Change the board status given that all of the above operations were valid
        self.board[translated_start[0]][translated_start[1]].unit = Unit()
        self.board[translated_end[0]][translated_end[1]].unit = unit
        # Remove from hand
        self.remove_piece_from_hand(unit.unit_type, player)

        return True

    def recruit(self, player: Player):
        # Check the piece is in the hand
        piece_to_discard = str(input('Piece to discard from hand to recruit the same kind: '))
        if not self.piece_in_hand(piece_to_discard, player, remove=True, discard=True):
            return False
        
        # Check there are available units in order to recruit
        piece_to_recruit = str(input(f'Used {piece_to_discard} coin, type the piece you want to recruit: '))
        if not self.can_recruit_piece(piece_to_recruit, player):
            return False

        return True

    def place(self, player: Player):
        piece_to_place = str(input('Piece to place from hand: '))
        # Check the piece is in the hand
        if not self.piece_in_hand(piece_to_place, player):
            return False
        
        # Check it's not a royal unit (they can't be placed in the board)
        if piece_to_place == 'Royal':
            print('Royal unit coins can not be placed in the board')
            return False

        position_to_place = str(input('Position to place (row, col): '))
        # Check if the position to place is a valid position
        if not self.valid_board_position(position_to_place):
            return False
        
        translated_coordinate = self.translate_to_coordinate(position_to_place)
        # Only allow the position where the unit will be placed to be an 'Empty' unit
        if not self.valid_end_position(translated_coordinate, control_pos_allowed=False):
            return False
        
        # Check its orthogonal to a control point
        if not self.is_orthogonal_to_control(translated_coordinate, player):
            return False
        
        # Place it in the board
        row, col = translated_coordinate[0], translated_coordinate[1]
        self.board[row][col].unit = self.get_unit_from_hand(piece_to_place, player, remove=True)

        return True

    def attack(self, player: Player):
        print('attack message')

    def control(self, player: Player):
        print('control message') 

    def initiative(self, player: Player):
        piece = str(input('Piece to discard from hand: '))
        # TODO: Allow for user input by changing it to lower case
        if self.piece_in_hand(piece, player, remove=True, discard=True):
            # Give player initiative
            player.has_initiative = True
            return True
        # TODO: Make the user retype input until its valid
        return False

    def forfeit(self, player: Player):
        print('forfeit message')
