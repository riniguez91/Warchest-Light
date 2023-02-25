from player import Player

# Unit class with its respective methods and properties
class Unit:
    """
    A class to represent a Unit.

    Attributes:
        player: The Player class object defining the current player.
        unit_type: The type belonging to a unit, e.g: Archer.
        unit_symbol: The symbol belonging to a unit, e.g: A
    """
    def __init__(self, player: Player = None, unit_type: str = 'Empty', unit_symbol: str = '·') -> None:
        self.player = player
        self.unit_type = unit_type
        self.unit_symbol = unit_symbol

    def move(self):
        """
        Defines how a particular unit moves.
        """
        pass

    def attack(self):
        """
        Defines how a particular unit attacks.
        """
        pass

    def is_orthogonal(self, start: tuple, end: tuple) -> bool:
        """
        Checks whether two coordiantes are orthogonal to each other, with a maximum distance of 1 unit.

        Args:
            start: Tuple containing the start coordinates.
            end: Tuple containing the end coordiantes.

        Returns:
            True if the coordinates are orthogonal, False if they are not.
        """
        x1, y1 = start 
        x2, y2 = end 
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1)

# Archer class with its respective methods and properties
class Archer(Unit):
    """
    A class to represent an Archer, subclass of Unit.

    Attributes:
        player: The Player class object defining the current player.
        unit_type: The type belonging to a unit, e.g: Archer.
        unit_symbol: The symbol belonging to a unit, e.g: A
        no_of_attacks: The number of attacks a unit has assigned.
    """
    def __init__(self, player: Player = None) -> None:
        super().__init__(self)
        self.player = player
        self.unit_type: str = 'Archer'
        self.unit_symbol: str = 'A'
        self.no_of_attacks = 1
    
    def move(self, from_position, to_position) -> bool:
        """
        Defines how the Archer class moves.

        Args:
            from_position: Tuple containing the start coordinates.
            to_position: Tuple containing the end coordinates.

        Returns:
            True if it follows the Archer move rules, False if it doesn't.
        """
        # Archer can only move one orthogonal space
        if not self.is_orthogonal(from_position, to_position):
            print('Archers can only move 1 unit at a time in an orthogonal way')
            return False 
        return True

    def attack(self, from_position, to_position) -> bool:
        """
        Defines how the Archer class attacks.

        Args:
            from_position: Tuple containing the start coordinates.
            to_position: Tuple containing the end coordinates.

        Returns:
            True if it follows the Archer attack rules, False if it doesn't.
        """
        # Allows for attack up to two units: vertically, horizontally or diagonally
        # Only allows for a distance of at most 2, and from_position & to_position can not be the same position 
        dx, dy = abs(from_position[0] - to_position[0]), abs(from_position[1] - to_position[1])
    
        if dx <= 2 and dy <= 2:
            if (dx == 0 or dy == 0 or dx == dy) and from_position != to_position:
                return True

        return False

# Knight class with its respective methods and properties
class Knight(Unit):
    """
    A class to represent a Knight, subclass of Unit.

    Attributes:
        player: The Player class object defining the current player.
        unit_type: The type belonging to a unit, e.g: Knight.
        unit_symbol: The symbol belonging to a unit, e.g: K
        no_of_attacks: The number of attacks a unit has assigned.
    """
    def __init__(self, player: Player = None) -> None:
        super().__init__(self)
        self.player = player
        self.unit_type: str = 'Knight'
        self.unit_symbol: str = 'K'
        self.no_of_attacks = 1
    
    def move(self, from_position, to_position) -> bool:
        """
        Defines how the Knight class moves.

        Args:
            from_position: Tuple containing the start coordinates.
            to_position: Tuple containing the end coordinates.

        Returns:
            True if it follows the Knight move rules, False if it doesn't.
        """
        # Knights can only move one orthogonal space
        if not self.is_orthogonal(from_position, to_position):
            print('Knights can only move 1 unit at a time in an orthogonal way')
            return False 
        return True

    def attack(self, from_position, to_position) -> bool:
        """
        Defines how the Knight class attacks.

        Args:
            from_position: Tuple containing the start coordinates.
            to_position: Tuple containing the end coordinates.

        Returns:
            True if it follows the Knight attack rules, False if it doesn't.
        """
        # Allows for attacks in one adjacent unit: vertical, horitzontal or diagonal
        # from_position & to_position can not be the same position
        dx, dy = abs(from_position[0] - to_position[0]), abs(from_position[1] - to_position[1])
        
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)

# Mercenary class with its respective methods and properties
class Mercenary(Unit):
    """
    A class to represent a Mercenary, subclass of Unit.

    Attributes:
        player: The Player class object defining the current player.
        unit_type: The type belonging to a unit, e.g: Mercenary.
        unit_symbol: The symbol belonging to a unit, e.g: M
        no_of_attacks: The number of attacks a unit has assigned.
    """
    def __init__(self, player: Player = None) -> None:
        super().__init__(self)
        self.player = player
        self.unit_type: str = 'Mercenary'
        self.unit_symbol: str = 'M'
        self.no_of_attacks = 1
    
    def move(self, from_position, to_position) -> bool:
        """
        Defines how the Mercenary class moves.

        Args:
            from_position: Tuple containing the start coordinates.
            to_position: Tuple containing the end coordinates.

        Returns:
            True if it follows the Archer move rules, False if it doesn't.
        """
        # Mercenaries can only move one orthogonal space
        if not self.is_orthogonal(from_position, to_position):
            print('Mercenaries can only move 1 unit at a time in an orthogonal way')
            return False 
        return True

    def attack(self, from_position, to_position) -> bool:
        """
        Defines how the Mercenary class attacks.

        Args:
            from_position: Tuple containing the start coordinates.
            to_position: Tuple containing the end coordinates.

        Returns:
            True if it follows the Mercenary attack rules, False if it doesn't.
        """
        # Allows for attacks in one adjacent unit: vertical, horitzontal or diagonal
        # from_position & to_position can not be the same position
        dx, dy = abs(from_position[0] - to_position[0]), abs(from_position[1] - to_position[1])
        
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)

# Berserker class with its respective methods and properties
class Berserker(Unit):
    """
    A class to represent a Berserker, subclass of Unit.

    Attributes:
        player: The Player class object defining the current player.
        unit_type: The type belonging to a unit, e.g: Berserker.
        unit_symbol: The symbol belonging to a unit, e.g: B.
        no_of_attacks: The number of attacks a unit has assigned.
    """
    def __init__(self, player: Player = None) -> None:
        super().__init__(self)
        self.player = player
        self.unit_type: str = 'Berserker'
        self.unit_symbol: str = 'B'
        self.no_of_attacks = 2
    
    def move(self, from_position, to_position) -> bool:
        """
        Defines how the Berserker class moves.

        Args:
            from_position: Tuple containing the start coordinates.
            to_position: Tuple containing the end coordinates.

        Returns:
            True if it follows the Berserker move rules, False if it doesn't.
        """
        # Berserkers can only move one orthogonal space
        if not self.is_orthogonal(from_position, to_position):
            print('Berserkers can only move 1 unit at a time in an orthogonal way')
            return False 
        return True

    def attack(self, from_position, to_position) -> bool:
        """
        Defines how the Berserker class attacks.

        Args:
            from_position: Tuple containing the start coordinates.
            to_position: Tuple containing the end coordinates.

        Returns:
            True if it follows the Berserker attack rules, False if it doesn't.
        """
        # Allows for attacks in one adjacent unit: vertical, horitzontal or diagonal
        # from_position & to_position can not be the same position
        dx, dy = abs(from_position[0] - to_position[0]), abs(from_position[1] - to_position[1])
        
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)

# Royal class with its respective methods and properties
class Royal(Unit):
    """
    A class to represent a Royal, subclass of Unit.

    Attributes:
        unit_type: The type belonging to a unit, e.g: Royal.
        unit_symbol: The symbol belonging to a unit, e.g: R
    """
    def __init__(self) -> None:
        super().__init__(self)
        self.unit_type: str = 'Royal'
        self.unit_symbol: str = 'R'

# Cell class with its respective methods and properties
class Cell:
    """
    A class to represent a Cell.

    Attributes:
        row: The row index in the board.
        col: The col index in the board.
        unit: The Unit class object in that cell.
        previous_unit: The Unit class object it was previously.
    """
    def __init__(self, row: int = 0, col: int = 0, unit: Unit = None, previous_unit: Unit = Unit()) -> None:
        self.row = row
        self.col = col
        self.unit = unit
        self.previous_unit = previous_unit
