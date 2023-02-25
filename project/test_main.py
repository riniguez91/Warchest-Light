import unittest

from main import generate_unit_coin, initialize_player, swap_turns
from player import Player
from cell import Archer, Knight

class TestMain(unittest.TestCase):
    def setUp(self):
        self.crow: Player = Player('Crow', 's')
        self.wolf: Player = Player('Wolf', 'v')

    def test_generate_unit_coin(self):
        # Valid tests
        self.assertEqual(type(generate_unit_coin('Archer', self.crow)), Archer)
        self.assertEqual(type(generate_unit_coin('Knight', self.crow)), Knight)

        # Invalid tests
        self.assertNotEqual(type(generate_unit_coin('Archer', self.crow)), Knight)
        self.assertNotEqual(type(generate_unit_coin('Knight', self.crow)), Archer)
    
    def test_initialize_player(self):
        units: list[tuple]= [('Archer', 4), ('Knight', 5), ('Mercenary', 5), ('Berserker', 4)]
        initialize_player(self.crow, units)

        # Player should have a total of 5 units in the bag
        self.assertEqual(len(self.crow.bag), 5)

        # Player should have a total of 2 assigned units
        self.assertEqual(len(self.crow.assigned_units), 2)

    def test_swap_turns(self):
        curr_player: Player = self.wolf

        # should return a Player class object
        self.assertEqual(type(swap_turns(curr_player, self.crow, self.wolf)), Player)

        # curr_player should be crow
        curr_player = swap_turns(curr_player, self.crow, self.wolf)
        self.assertEqual(curr_player, self.crow)

        # curr_player should be crow as he has the initative
        curr_player.has_initiative = True
        curr_player = swap_turns(curr_player, self.crow, self.wolf)
        self.assertEqual(curr_player, self.crow)

        # curr_player should be wolf as althought crow has the initiative it can not play more than 2 rounds in a row
        curr_player = swap_turns(curr_player, self.crow, self.wolf)
        self.assertEqual(curr_player, self.wolf)

if __name__ == '__main__':
    unittest.main()