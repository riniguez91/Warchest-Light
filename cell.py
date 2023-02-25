from player import Player

# Unit class with its respective methods and properties
class Unit:
    def __init__(self, player: Player = None, unit_type: str = 'Empty', unit_symbol: str = '·') -> None:
        self.player = player
        self.unit_type = unit_type
        self.unit_symbol = unit_symbol

    def move(self):
        pass

    def attack(self):
        pass

    def is_orthogonal(self, start: tuple, end: tuple):
        x1, y1 = start 
        x2, y2 = end 
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1)

# Archer class with its respective methods and properties
class Archer(Unit):
    def __init__(self, player: Player = None) -> None:
        super().__init__(self)
        self.player = player
        self.unit_type: str = 'Archer'
        self.unit_symbol: str = 'A'
        self.no_of_attacks = 1
    
    def move(self, from_position, to_position):
        # Archer can only move one orthogonal space
        if not self.is_orthogonal(from_position, to_position):
            print('Archers can only move 1 unit at a time in an orthogonal way')
            return False 
        return True

    def attack(self, from_position, to_position):
        # Allows for attack up to two units: vertically, horizontally or diagonally
        # Only allows for a distance of at most 2, and from_position & to_position can not be the same position 
        dx, dy = abs(from_position[0] - to_position[0]), abs(from_position[1] - to_position[1])
    
        if dx <= 2 and dy <= 2:
            if (dx == 0 or dy == 0 or dx == dy) and from_position != to_position:
                return True

        return False

# Knight class with its respective methods and properties
class Knight(Unit):
    def __init__(self, player: Player = None) -> None:
        super().__init__(self)
        self.player = player
        self.unit_type: str = 'Knight'
        self.unit_symbol: str = 'K'
        self.no_of_attacks = 1
    
    def move(self, from_position, to_position):
        # Knights can only move one orthogonal space
        if not self.is_orthogonal(from_position, to_position):
            print('Knights can only move 1 unit at a time in an orthogonal way')
            return False 
        return True

    def attack(self, from_position, to_position):
        # Allows for attacks in one adjacent unit: vertical, horitzontal or diagonal
        # from_position & to_position can not be the same position
        dx, dy = abs(from_position[0] - to_position[0]), abs(from_position[1] - to_position[1])
        
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)

# Mercenary class with its respective methods and properties
class Mercenary(Unit):
    def __init__(self, player: Player = None) -> None:
        super().__init__(self)
        self.player = player
        self.unit_type: str = 'Mercenary'
        self.unit_symbol: str = 'M'
        self.no_of_attacks = 1
    
    def move(self, from_position, to_position):
        # Mercenaries can only move one orthogonal space
        if not self.is_orthogonal(from_position, to_position):
            print('Mercenaries can only move 1 unit at a time in an orthogonal way')
            return False 
        return True

    def attack(self, from_position, to_position):
        # Allows for attacks in one adjacent unit: vertical, horitzontal or diagonal
        # from_position & to_position can not be the same position
        dx, dy = abs(from_position[0] - to_position[0]), abs(from_position[1] - to_position[1])
        
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)

# Berserker class with its respective methods and properties
class Berserker(Unit):
    def __init__(self, player: Player = None) -> None:
        super().__init__(self)
        self.player = player
        self.unit_type: str = 'Berserker'
        self.unit_symbol: str = 'B'
        self.no_of_attacks = 2
    
    def move(self, from_position, to_position):
        # Berserkers can only move one orthogonal space
        if not self.is_orthogonal(from_position, to_position):
            print('Berserkers can only move 1 unit at a time in an orthogonal way')
            return False 
        return True

    def attack(self, from_position, to_position):
        # Allows for attacks in one adjacent unit: vertical, horitzontal or diagonal
        # from_position & to_position can not be the same position
        dx, dy = abs(from_position[0] - to_position[0]), abs(from_position[1] - to_position[1])
        
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)

# Royal class with its respective methods and properties
class Royal(Unit):
    def __init__(self) -> None:
        super().__init__(self)
        self.unit_type: str = 'Royal'
        self.unit_symbol: str = 'R'

# Cell class with its respective methods and properties
class Cell:
    def __init__(self, row: int = 0, col: int = 0, unit: Unit = None, previous_unit: Unit = Unit()) -> None:
        self.row = row
        self.col = col
        self.unit = unit
        self.previous_unit = previous_unit
