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
        self.board[2][3] = Cell(2, 3, Unit(None, 'Control', '@'))
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
        forfeit = False
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
                forfeit = True

            case _:
                print('That is not a valid action, please try again.')

        # Show the current state of the player hand
        if not forfeit:
            player.print_hand()
        return forfeit

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
    
    def valid_attack_position(self, end_position: tuple, curr_player: Player):
        # Get the unit at the end position
        unit: Unit = self.board[end_position[0]][end_position[1]].unit
        # Check it can only be a unit that doesn't belong to the current player and is not a control or empty unit
        if unit.player == curr_player or unit.unit_type == 'Control' or unit.unit_type == 'Empty':
            print('Can\'t attack own player unit, control units or empty units.')
            return False
        # Valid attack position
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
        # We also need to check if the previous_unit.unit_symbol is a control point as that means that a unit
        # is directly above a control point, but is still a valid control point
        # Check upward
        if ( 
            x - 1  >= 0 
            and (self.board[x-1][y].unit.unit_symbol[0] == 'C' or self.board[x-1][y].previous_unit.unit_symbol[0] == 'C') 
            and self.board[x-1][y].unit.player == player
        ):
            return True 
        # Check rightward
        if (
            y + 1 < len(self.board[0]) 
            and (self.board[x][y+1].unit.unit_symbol[0] == 'C' or self.board[x][y+1].previous_unit.unit_symbol[0] == 'C')
            and self.board[x][y+1].unit.player == player
        ):
            return True 
        # Check downward
        if (
            x + 1 < len(self.board) 
            and (self.board[x+1][y].unit.unit_symbol[0] == 'C' or self.board[x+1][y].previous_unit.unit_symbol[0] == 'C')
            and self.board[x+1][y].unit.player == player
        ):
            return True
        # Check leftward
        if (
            y - 1 >= 0 
            and (self.board[x][y-1].unit.unit_symbol[0] == 'C' or self.board[x][y-1].previous_unit.unit_symbol[0] == 'C') 
            and self.board[x][y-1].unit.player == player
        ):
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
        from_position = str(input('Move from position (row, col): '))
        if not self.valid_board_position(from_position):
            return
        
        unit: Unit = self.get_unit(from_position)
        # Check the position isn't empty and belongs to the player (but is not a control point)
        if not self.valid_start_position(unit, player):
            return 
        
        # Check the piece to move is contained in the hand and the board
        piece = str(input('Select a piece of the same type in your hand: '))
        if not (self.piece_in_hand(piece, player, remove=True, discard=True) and unit.unit_type == piece):
            return
        
        to_position = str(input('To position (row, col): '))
        # Check if the to_position is a valid position
        if not self.valid_board_position(to_position):
            return
        
        # Get the translated coordinates
        translated_start = self.translate_to_coordinate(from_position)
        translated_end = self.translate_to_coordinate(to_position)

        # Check the to_position is either a control unit or an empty unit
        if not self.valid_end_position(translated_end):
            return
        
        # If it was an invalid move due to the speficic unit coin movement, end the function
        if not unit.move(translated_start, translated_end):
            return
        
        # Change the board status given that all of the above operations were valid
        # Revert the previous cell to its previous unit status
        prev_cell: Cell = self.board[translated_start[0]][translated_start[1]]
        prev_cell.unit = prev_cell.previous_unit
        # Assign the new cell previous unit to its actual unit, and then change the actual unit to the new unit
        new_cell: Cell = self.board[translated_end[0]][translated_end[1]]
        new_cell.previous_unit = new_cell.unit
        new_cell.unit = unit

    def recruit(self, player: Player):
        # Check the piece is in the hand
        piece_to_discard = str(input('Piece to discard from hand to recruit the same kind: '))
        if not self.piece_in_hand(piece_to_discard, player, remove=True, discard=True):
            return
        
        # Check there are available units in order to recruit
        piece_to_recruit = str(input(f'Used {piece_to_discard} coin, type the piece you want to recruit: '))
        if not self.can_recruit_piece(piece_to_recruit, player):
            return

    def place(self, player: Player):
        piece_to_place = str(input('Piece to place from hand: '))
        # Check the piece is in the hand
        if not self.piece_in_hand(piece_to_place, player):
            return
        
        # Check it's not a royal unit (they can't be placed in the board)
        if piece_to_place == 'Royal':
            print('Royal unit coins can not be placed in the board')
            return

        position_to_place = str(input('Position to place (row, col): '))
        # Check if the position to place is a valid position
        if not self.valid_board_position(position_to_place):
            return
        
        translated_coordinate = self.translate_to_coordinate(position_to_place)
        # Only allow the position where the unit will be placed to be an 'Empty' unit
        if not self.valid_end_position(translated_coordinate, control_pos_allowed=False):
            return
        
        # Check its orthogonal to a control point
        if not self.is_orthogonal_to_control(translated_coordinate, player):
            return
        
        # Place it in the board
        row, col = translated_coordinate[0], translated_coordinate[1]
        # Save it's previous status so we can revert back to it whenever a piece moves from that position
        self.board[row][col].previous_unit = self.board[row][col].unit
        self.board[row][col].unit = self.get_unit_from_hand(piece_to_place, player, remove=True)

    def can_attack(self, from_position: str, player: Player, unit: Unit):
        to_position = str(input('To position (row, col): '))
        # Check if the to_position is a valid position
        if not self.valid_board_position(to_position):
            return
        
        # Get the translated coordinates
        translated_start = self.translate_to_coordinate(from_position)
        translated_end = self.translate_to_coordinate(to_position)

        # Check the to_position contains another player unit (can't attack empty units/control units/own player units)
        if not self.valid_attack_position(translated_end, player):
            return
        
        # If it was an invalid move due to the speficic unit coin movement, end the function
        if not unit.attack(translated_start, translated_end):
            return

        # Change the board status given that all of the above operations were valid
        attacked_cell: Cell = self.board[translated_end[0]][translated_end[1]]
        attacked_cell.unit = attacked_cell.previous_unit

    def attack(self, player: Player):
        # Check if the from_position is a valid position
        from_position = str(input('Attack from position (row, col): '))
        if not self.valid_board_position(from_position):
            return
        
        unit: Unit = self.get_unit(from_position)
        # Check the position isn't empty and belongs to the player (but is not a control point)
        if not self.valid_start_position(unit, player):
            return 
        
        # Check the piece to move is contained in the hand and the board
        piece = str(input('Select a piece of the same type in your hand: '))
        if not (self.piece_in_hand(piece, player, remove=True, discard=True) and unit.unit_type == piece):
            return
        
        # Check if the current unit can attack more than once
        for i in range(unit.no_of_attacks):
            if i == 1:
                confirm_attack = str(input(f'This unit can attack {unit.no_of_attacks} times, would you like to attack again? (yes/no): '))
                if confirm_attack.lower() == 'no':
                    break
            self.can_attack(from_position, player, unit)

    def control(self, player: Player):
        piece_to_discard = str(input('Piece to discard from hand: '))
        # Check the piece is in the hand
        if not self.piece_in_hand(piece_to_discard, player, remove=True, discard=True):
            return
        
        position_to_control = str(input('Position to control (row, col): '))
        # Check if the position to control is a valid position
        if not self.valid_board_position(position_to_control):
            return
        
        # Check it is in fact a control unit
        translated_coordinate = self.translate_to_coordinate(position_to_control) 
        row, col = translated_coordinate[0], translated_coordinate[1]
        if self.board[row][col].previous_unit.unit_type != 'Control':
            print('The current coordinate does not contain a control unit')
            return
        
        # Since none of the above error-check conditions were satisfied, control the coordianate
        curr_cell = self.board[row][col]
        curr_cell.previous_unit = Unit(player, 'Control', 'C')
        player.control_tokens -= 1

    def initiative(self, player: Player):
        piece = str(input('Piece to discard from hand: '))
        # Improvement: Allow for user input by changing it to lower case
        if self.piece_in_hand(piece, player, remove=True, discard=True):
            # Give player initiative
            player.has_initiative = True
            return
