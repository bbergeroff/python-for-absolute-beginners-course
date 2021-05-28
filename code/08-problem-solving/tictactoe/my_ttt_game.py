# Chapter 8 Work along code
import random
# Tic Tac Toe game

def main ():

    call_header()

    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    active_players_turn = random.randint(0,1)
    player_1 = input("Please tell me what I should call you.")
    players = [player_1, "Computer"]
    symobols = ["X", "O"]
    player = players.index(active_players_turn)
    print(f"{player} will start the match")


def make_play():
    pass

def call_header():
    print("---------------------------")
    print("  Let's Play Tik Tac Toe")
    print("---------------------------")


if __name__ == '__main__':
    main()
