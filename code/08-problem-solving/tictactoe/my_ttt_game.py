# Chapter 8 Work along code
import random
# Tic Tac Toe game

def main ():

    call_header()

    # Define the board data structure
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    # Define base values for gameplay: Who's turn it is, the human players name, the sybols being used to play the game, and set the starting player. 
    active_players_turn = random.randint(0,1)
    player_1 = input("Please tell me what I should call you.")
    players = [player_1, "Computer"]
    player = players[active_players_turn]
    print(f"{player} will start!")
    symobols = ["X", "O"]

    # Loop through game until the check for a winner comes back True
    while not find_winner(board):
        player = players[active_players_turn]
        symbols = symobols[active_players_turn]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbols):
            print("That isn't an option, try again")
            continue
        # Alternate players using # of players as the modulo
        active_players_turn = (active_players_turn + 1) % len(players)
    
    print(f"Game over!! {player} has won the Game!!!")
    print("The ending board was: ")
    show_board()


def choose_location(board, symbol):
    row = int(input("Choose which row: "))
    col = int(input("Choose which column: "))

    # Rectify user input with system index
    row -= 1
    col -= 1
    # Ensure input is within bounds of the board
    if row < 0  or row > len(board):
        return False
    if col < 0 or row > len(board):
        return False

    # Check if spot was already declared in previous turn
    cell = board[row][col]
    if cell is not None:
        return False

    # If the choice is valid, set the space with the players symbol and return true
    board[row][col] = symbol
    return True


def announce_turn(player):
    print("")
    print(f"It is {player}'s turn. Here's the board:")
    print()
        

def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else '_'
            print(symbol, end = ' | ')
        print()


def find_winner(board):
    # TODO: Implement how we check for a winner
    return False


def make_play():
    pass


def call_header():
    print("---------------------------")
    print("  Let's Play Tik Tac Toe")
    print("---------------------------")


if __name__ == '__main__':
    main()
