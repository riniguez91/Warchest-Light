from cell import Unit

# Player class with its respective methods and properties
class Player:
    def __init__(self):
        self.bag: list[Unit] = []
        self.hand: list[Unit] = []
        self.recruitment: list[Unit] = []
        self.discard: list[Unit] = []
        self.control_tokens: int = 3
