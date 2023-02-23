from player import Player

# Unit class with its respective methods and properties
class Unit:
    def __init__(self, player: Player = None, no_of_units: int = 0, unit_type: str = 'Empty', unit_symbol: str = '·'):
        self.player = player
        self.no_of_units = no_of_units
        self.unit_type = unit_type
        self.unit_symbol = unit_symbol

    def move(self):
        pass

    def attack(self):
        pass

# Archer class with its respective methods and properties
class Archer(Unit):
    def __init__(self):
        self.no_of_units = 4
        self.unit_type = 'Archer'
        self.unit_symbol = 'A'
    
    def move(self):
        print('I move the archer way')

    def attack(self):
        print('I attack the archer way')

# Knight class with its respective methods and properties
class Knight(Unit):
    def __init__(self):
        super().__init__(self)
        self.no_of_units = 5
        self.unit_type = 'Knight'
        self.unit_symbol = 'K'
    
    def move(self):
        print('I move the knight way')

    def attack(self):
        print('I attack the knight way')

# Mercenary class with its respective methods and properties
class Mercenary(Unit):
    def __init__(self):
        super().__init__(self)
        self.no_of_units = 5
        self.unit_type = 'Mercenary'
        self.unit_symbol = 'M'
    
    def move(self):
        print('I move the mercenary way')

    def attack(self):
        print('I attack the mercenary way')

# Berserker class with its respective methods and properties
class Berserker(Unit):
    def __init__(self):
        super().__init__(self)
        self.no_of_units = 4
        self.unit_type = 'Berserker'
        self.unit_symbol = 'B'
    
    def move(self):
        print('I move the berserker way')

    def attack(self):
        print('I attack the berserker way')

# Royal class with its respective methods and properties
class Royal(Unit):
    def __init__(self):
        super().__init__(self)
        self.no_of_units = 1
        self.unit_type = 'Royal'
        self.unit_symbol = 'R'
    
    def move(self):
        print('I move the royal way')

    def attack(self):
        print('I attack the royal way')

# Cell class with its respective methods and properties
class Cell:
    def __init__(self, row: int = 0, col: int = 0, unit: Unit = None):
        self.row = row
        self.col = col
        self.unit = unit
