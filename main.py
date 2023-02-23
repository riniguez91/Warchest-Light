from board import Board

def main():
    # Main entry point of the app
    start_game = str(input('Start game? (y/n): '))
    if start_game == 'y':
        # Start the game
        play_game()
    else:
        print('\nYou exited the game.\n')

def play_game():
    # Initialize board
    board = Board()

    game_ended: bool = False
    while not game_ended:
        # Show board
        board.print_board()
        break

        # Decide player turn
        
        # Show player stats (hand, recruitment pieces, discard pile & control tokens)

        # Make action until hand is empty (or the equivalent to three moves)


if __name__ == "__main__":
    # This is executed when run from the command line
    main()
