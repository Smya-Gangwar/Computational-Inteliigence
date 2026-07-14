# N-QUEEN PROBLEM
# Uses backtracking to find all possible arrangements of N queens on an N x N chessboard

def isSafePlace(rows, r, c, n):
    if rows[r] != -1:
        return False
    for i in range(r):
        if rows[i] == c or abs(r-i) == abs(c-rows[i]):
            return False
    return True

def NQueen(rows, r, n):
    if(r==n):
        print("\n")
        for i in range(n):
            for j in range(n):
                if rows[i] == j:
                    print("X ", end="")
                else:
                    print(". ", end="")
            print()
        return
    for c in range(n):
        if isSafePlace(rows, r, c, n):
            rows[r] = c
            NQueen(rows, r+1, n)
            rows[r] = -1

if __name__ == "__main__":
    n = int(input("Enter the size of chess grid (nXn) : "))
    if n > 3:
        print("\n POSSIBLE ARRANGEMENTS : ")
        rows = [-1] * n
        NQueen(rows, 0, n)
    else:
        print("\nNo queens can be placed in this grid.")