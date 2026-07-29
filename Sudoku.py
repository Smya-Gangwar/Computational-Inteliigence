# SUDOKU SOLVER
# Uses backtracking to find a solution to the Sudoku puzzle.

def isSafe(board, r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False
    r1 = r - r%3
    r2 = r1+3
    c1 = c - c%3
    c2 = c1+3
    for i in range(r1,r2):
        for j in range(c1,c2):
            if board[i][j] == num:
                return False
    return True

def sudoku(board, n, r, c):
    if r == n:
        print("\n")
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print("\n")
        return
    if board[r][c] == 0:
        for i in range(1, n+1):
            if isSafe(board, r, c, i):
                board[r][c] = i
                sudoku(board, n, r+(c+1)//n, (c+1)%n)
                board[r][c] = 0
    else:
        sudoku(board, n, r+(c+1)//n, (c+1)%n)

if __name__ == "__main__":
    print("\nEnter Sudoku puzzle (1-9 & 0 for empty block)\n")
    n = 9
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            board[i][j] = int(input())
    sudoku(board, 9, 0, 0)