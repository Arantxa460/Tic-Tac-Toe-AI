from minimax import *

def print_board(board):
    print()
    for row in board:
        print(row)
    print()


def initial_state():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]


def main():
    board = initial_state()

    print("Tic Tac Toe")
    print("You are O, AI is X")

    while not terminal(board):
        print_board(board)

        if player(board) == X:
            print("AI thinking...")
            move = minimax(board)
            print("AI plays:", move)
            board = result(board, move)

        else:
            print("Your turn")
            i = int(input("Row (0-2): "))
            j = int(input("Col (0-2): "))

            if (i, j) not in actions(board):
                print("Invalid move, try again")
                continue

            board = result(board, (i, j))

    print_board(board)

    win = winner(board)
    if win == X:
        print("X wins")
    elif win == O:
        print("O wins")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
