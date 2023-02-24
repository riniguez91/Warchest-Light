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

def initialize_player(player: Player, units: list[Unit]):
    # Repeat until we have assigned two units to the player
    for _ in range(2):
        # Generate the random number
        random_no: int = random.randint(0, len(units) - 1)
        # Get the unit and no_of_units assigned to it
        unit, no_of_units = units[random_no][0], units[random_no][1]
        # Assign them to our player assigned units (remembering to remove two units we inserted in the player bag)
        player.assigned_units[unit] = no_of_units - 2
        # Place two of the units in the bag
        for _ in range(2):
            player.bag.append(unit)
        # Remove them from the pool of available units
        del units[random_no]
    
    # Add the royal card (one available to each player)
    player.assigned_units[Royal()] = 1
    return player

def show_player_information(player: Player):
    print(f'  ===== {player.name} =====')
    # Other player has won if the current player can't create a new hand
    if not player.get_hand():
        return False
    player.get_recruitment_units()
    player.get_discard_pile()
    player.get_control_tokens()

def play_game():
    # Initialize the list of units where the tuple represents (type of unit, the no. of units corresponding to it)
    units: list[tuple]= [(Archer(), 4), (Knight(), 5), (Mercenary(), 5), (Berserker(), 4)]
    # Initialize players
    crow: Player = initialize_player(Player('CROW'), units)
    wolf: Player = initialize_player(Player('WOLF'), units)
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

        # Decide player turn
        
        # Show player information (hand, recruitment pieces, discard pile & control tokens)
        # If the method returns False that means the curr_player couldn't create a hand, therefore ending the game
        if not show_player_information(curr_player):
            winner = crow.name if curr_player == crow else wolf.name
            break

        break
        # Make action until hand is empty (or the equivalent to three moves)
    
    print(f'\nThe winner of the game is {winner}!\n')


if __name__ == "__main__":
    # This is executed when run from the command line
    main()
