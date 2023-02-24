import random 

from board import Board
from player import Player
from cell import Archer, Knight, Mercenary, Berserker, Unit, Royal

def main():
    # Main entry point of the app
    start_game = str(input('Start game? (y/n): '))
    if start_game == 'y':
        # Start the game
        play_game()
    else:
        print('\nYou exited the game.\n')

def generate_unit_coin(unit: str, player: Player):
    match unit:
        case 'Archer':
            return Archer(player)
        case 'Knight':
            return Knight(player)
        case 'Mercenary':
            return Mercenary(player)
        case 'Berserker':
            return Berserker(player)

def initialize_player(player: Player, units: list[Unit]):
    # Repeat until we have assigned two units to the player
    for _ in range(2):
        # Generate the random number
        random_no: int = random.randint(0, len(units) - 1)
        # Get the unit and no_of_units assigned to it
        unit, no_of_units = units[random_no][0], units[random_no][1]
        # Create two unit coins
        unit_coin_one, unit_coin_two = generate_unit_coin(unit, player), generate_unit_coin(unit, player)

        # The assigned units dictionary follows the structure '{ unit_type: [stack of class Units] }'
        player.assigned_units[unit] = []
        # Create the stack of unit coins (remembering to remove two units we inserted in the player bag)
        for _ in range(no_of_units - 2):
            player.assigned_units[unit].append(generate_unit_coin(unit, player))

        # Place the two units in the bag
        player.bag.append(unit_coin_one)
        player.bag.append(unit_coin_two)
        # Remove them from the pool of available units
        del units[random_no]
    
    # Add the royal card (one available to each player)
    royal_unit: Royal = Royal()
    player.bag.append(royal_unit)
    return player

def show_player_information(player: Player):
    print(f'  ==== {player.name} ({player.symbol}) ====')
    # Other player has won if the current player can't create a new hand
    if not player.get_hand():
        return False
    player.get_recruitment_units()
    player.get_discard_pile()
    player.get_control_tokens()
    
    return True

def prompt_player_actions(board: Board, player: Player):
    # Prompt the user to choose three actions
    for _ in range(3):
        board.choose_action(player)

def play_game():
    # Initialize the list of units where the tuple represents (type of unit, the no. of units corresponding to it)
    units: list[tuple]= [('Archer', 4), ('Knight', 5), ('Mercenary', 5), ('Berserker', 4)]
    # Initialize players
    crow: Player = initialize_player(Player('CROW', 's'), units)
    wolf: Player = initialize_player(Player('WOLF', 'v'), units)
    # Initialize board
    board: Board = Board(crow, wolf)
    # Set random starting player
    curr_player: Player = crow if random.randint(0, 1) == 0 else wolf

    # Stop the game when there is a winning condition
    game_ended: bool = False
    winner: str = ''
    
    while not game_ended:
        # Show board
        board.print_board()

        # Decide player turn only if the current player has no initiative action
        if not curr_player.has_initiative:
            # Swap turns
            curr_player = crow if curr_player == wolf else wolf

        # Show player information (hand, recruitment pieces, discard pile & control tokens)
        # If the method returns False that means the curr_player couldn't create a hand, therefore ending the game
        if not show_player_information(curr_player):
            winner = crow.name if curr_player.has_initiative or curr_player == crow else wolf.name
            break

        # Make action until hand is empty (or the equivalent to three moves)
        prompt_player_actions(board, curr_player)
    
    print(f'\nThe winner of the game is {winner}!\n')


if __name__ == "__main__":
    # This is executed when run from the command line
    main()
