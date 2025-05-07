# Backtracking Example: N-Queens Problem
# This program solves the N-Queens problem using backtracking.
# It places N queens on an N×N chessboard so that no two queens threaten each other.

def print_solution(board):
    for row in board:
        print(" ".join(row))

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True

def solve_n_queens(board, col, n):
    if col >= n:
        print_solution(board)
        print()
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            res = solve_n_queens(board, col + 1, n) or res
            board[i][col] = '.'
    return res

def main():
    n = 4
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists")

if __name__ == "__main__":
    main()