/*
SUDOKU SOLVER
Uses backtracking to find a solution to the Sudoku puzzle.
*/

#include <bits/stdc++.h>

using namespace std;

bool isSafe(vector<vector<int>>& board, int r, int c, int num)
{
    for(int i=0;i<9;i++)
    {
        if(board[r][i] == num || board[i][c] == num)
            return false;
    }
    int row = r - r%3;
    int col = c - c%3;
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            if(board[i+row][j+col] == num)
                return false;
    return true;
}

void sudoku(vector<vector<int>>& board, int n, int r, int c)
{
    if(r==n)
    {
        cout<<"\n";
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
                cout<<board[i][j]<<" ";
            cout<<"\n";
        }
        return;
    }
    if(board[r][c] == 0)
    {
        for(int i=1;i<=n;i++)
        {
            if(isSafe(board, r, c, i))
            {
                board[r][c] = i;
                sudoku(board, n, r+(c+1)/n, (c+1)%n);
                board[r][c] = 0;
            }
        }
    }
    else
        sudoku(board, n, r+(c+1)/n, (c+1)%n);
}

int main()
{
    cout<<"\nEnter Sudoku puzzle (1-9 & 0 for empty block)\n";
    int n = 9;
    vector<vector<int>> board(n, vector<int>(n,0));
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            cin>>board[i][j];
    sudoku(board,9,0,0);
    return 0;
}