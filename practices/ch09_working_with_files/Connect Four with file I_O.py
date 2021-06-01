# Connect Four
import random
import datetime
import json
import os
  
# Check for winners
# End game when complete

def main ():
    log("App Starting up...")

    call_header()
    show_leaderboard()

    board = [
        [None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None,],
    ]

    # Define base values for gameplay: Who's turn it is, the human players name, the sybols being used to play the game, and set the starting player. 
    starting_player = random.randint(0,1)
    player_1, player_2 = get_players()
    players = [player_1, player_2]
    player = players[starting_player]
    log(f"New game starting between {player_1} and {player_2}")
    msg = f"{player} will start!"
    print(msg)
    log(msg)
    symbols = ["X", "O"]
    play_game(players, board, symbols, starting_player)
    log("Game over.")

def play_game(players, board, symbols, active_players_turn):
    # Loop through game until the check for a winner comes back True
    while not find_winner(board):
        player = players[active_players_turn]
        symbol = symbols[active_players_turn]

        announce_turn(player)
        show_board(board)
        print()
        if not choose_location(board, symbol, player):
            continue
        # Alternate players using # of players as the modulo
        active_players_turn = (active_players_turn + 1) % len(players)
    
    msg = f"Game over!! {player} has won the Game!!!"
    print(msg)
    log(msg)
    print("The ending board was: ")
    show_board(board)
    record_win(active_players_turn)

def get_players():
    p1 = input("Player 1, what is your name? ")
    p2 = "Computer"

    return p1,p2

def announce_turn(player):
    print()
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
    sequences = get_winning_sequences(board)
        
    for seq in sequences:
        symbol1 = seq[0]
        if symbol1 and all(symbol1 == cell for cell in seq):
            return True 

    return False


def get_winning_sequences(board):
    sequences = []

    # Row Based Wins
    for row_idx in range(0, 6):
        for cell in range(0, 4):
            row_seq = [board[row_idx][cell], board[row_idx][cell + 1], board[row_idx][cell + 2], board[row_idx][cell + 3]]
            sequences.append(row_seq)
                   
    # Column based Wins
    for col_idx in range(0, 7):
        for cell in range(0, 3):
            column = [
                board[cell][col_idx],
                board[cell + 1][col_idx],
                board[cell + 2][col_idx],
                board[cell + 3][col_idx],
            ]
            sequences.append(column) 

    # \ Diag Based Wins
    for row_idx in range(0, 3):
        for col_idx in range(0, 4):
            diag = [
                board[row_idx][col_idx],
                board[row_idx + 1][col_idx + 1],
                board[row_idx + 2][col_idx + 2],
                board[row_idx + 3][col_idx + 3],
            ]
            sequences.append(diag) 

    # / Diag based winds
    for row_idx in range(0, 3):
            for col_idx in range(3, 7):
                diag = [
                    board[row_idx][col_idx],
                    board[row_idx + 1][col_idx - 1],
                    board[row_idx + 2][col_idx - 2],
                    board[row_idx + 3][col_idx - 3],
                ]
                sequences.append(diag) 

    return(sequences)


def choose_location(board, symbol, player):
    col = int(input("Choose a column: "))
    log(f"{player} chose columm {col}")
    # Rectify User input
    col -= 1
    # Ensure input does not fall outside range of board
    if col < 0 or col > len(board):
        print("That isn't an option, try again")
        log(f"{player} chose and invalid column.")
        return False

    # Check to make sure the row is not full
    top_cell = board[0][col]
    if top_cell is not None:
        print("That row is full, pick a different row!")
        log(f"{player} chose a full column.")
        return False
    
    row_idx = 0
    for row in board:
        if row[col] is not None:
            board[row_idx - 1][col] = symbol
            return True
        row_idx += 1

    board[5][col] = symbol
    col += 1
    log(f"{player} picked column {col}")

    return True


def call_header():
    print("-----------------------------------")
    print("      Let's Play Connect 4!!!      ")
    print("-----------------------------------")


def show_leaderboard():
    leaders = load_leaders()
    
    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print("LEADERS: ")
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins:,} -- {name}")
    print("---------------------------")
    print()


def record_win(winner_name):
    leaders = load_leaders()

    if winner_name in leaders:
        leaders[winner_name] += 1
    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'c4_leaderboard.json')    

    with open(filename, 'w', encoding='utf-8') as fout:
        json.dump(leaders, fout)



def load_leaders():
    
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'c4_leaderboard.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'connect_four.log')

    with open(filename, 'a', encoding='utf-8') as fout:
        fout.write(f"[{datetime.datetime.now().isoformat()}]")
        fout.write(msg)
        fout.write('\n')


if __name__ == '__main__':
    main()