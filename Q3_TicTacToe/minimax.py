import math
import copy

X = "X"
O = "O"
EMPTY = None

def player(board):
    x = sum(row.count(X) for row in board)
    o = sum(row.count(O) for row in board)
    return X if x == o else O

def actions(board):
    return {
        (i, j)
        for i in range(3)
        for j in range(3)
        if board[i][j] is None
    }
def result(board, action):
    i, j = action
    if board[i][j] is not None:
        raise Exception("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    lines = []

    lines.extend(board)
    lines.extend([[board[i][j] for i in range(3)] for j in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])

    for line in lines:
        if line[0] and line.count(line[0]) == 3:
            return line[0]
    return None

def terminal(board):
    return winner(board) is not None or all(cell is not None for row in board for cell in row)

def utility(board):
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    return 0

def minimax(board):
    if terminal(board):
        return None

    turn = player(board)

    def max_value(b):
        if terminal(b):
            return utility(b)
        v = -math.inf
        for action in actions(b):
            v = max(v, min_value(result(b, action)))
        return v

    def min_value(b):
        if terminal(b):
            return utility(b)
        v = math.inf
        for action in actions(b):
            v = min(v, max_value(result(b, action)))
        return v

    best_move = None

    if turn == X:
        best_val = -math.inf
        for action in actions(board):
            val = min_value(result(board, action))
            if val > best_val:
                best_val = val
                best_move = action
    else:
        best_val = math.inf
        for action in actions(board):
            val = max_value(result(board, action))
            if val < best_val:
                best_val = val
                best_move = action

    return best_move

if __name__ == "__main__":
    print("Running Q3 standalone...")

    board = [
        ["X", "O", "X"],
        ["O", "X", None],
        [None, None, "O"]
    ]

    move = minimax(board)
    print("Best Move:", move)
