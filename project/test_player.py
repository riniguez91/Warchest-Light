import unittest

from cell import Knight, Archer, Royal
from player import Player

class TestPlayer(unittest.TestCase):

    def test_get_hand(self):
        self.player = Player('Crow', 's')
        self.player.bag = [Knight(), Knight(), Archer(), Archer(), Royal()]
        self.player.hand = []
        self.player.discarded = []
        initial_bag_size = len(self.player.bag)
        
        # Should get hand
        self.assertTrue(self.player.get_hand())
        
        # Bag size should be 3 less
        self.assertEqual(initial_bag_size - len(self.player.bag), 3)

        # Hand should contain 3 units
        self.assertEqual(len(self.player.hand), 3)

        # Shouldn't be able to get a new hand now that the bag only contains 2 units
        self.assertFalse(self.player.get_hand())
        
if __name__ == '__main__':
    unittest.main()