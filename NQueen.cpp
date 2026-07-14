/* 
N-QUEEN PROBLEM
Uses backtracking to find all possible arrangements of N queens on an N x N chessboard
*/

#include <bits/stdc++.h>

using namespace std;
int countt = 0;

bool isSafePlace(vector<int>& rows, int r, int c, int n)
{
    if(rows[r] != -1) return false;
    for(int i=0;i<r;i++)
    {
        if(rows[i]==c || (abs(r-i)==abs(c-rows[i])))
            return false;
    }
    return true;
}

void NQueen(vector<int>& rows, int r, int n)
{
    if(r==n)
    {
        cout<<"\n";
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(rows[i]==j)
                    cout<<"X ";
                else
                    cout<<". ";
            }
            cout<<"\n";
        }
        countt++;
        return;
    }
    for(int c=0;c<n;c++)
    {
        if(isSafePlace(rows,r,c,n))
        {
            rows[r] = c;
            NQueen(rows, r+1, n);
            rows[r] = -1;
        }
    }
}

int main() {
    int n;
    cout<<"Enter the size of chess grid (nXn) : ";
    cin>>n;
    if(n>3)
    {
        cout<<"\n POSSIBLE ARRANGEMENTS : ";
        vector<int> rows(n,-1);
        NQueen(rows,0,n);
        cout<<"\nCount = "<<countt;
    }
    else
        cout<<"\nNo queens can be placed in this grid.";
    return 0;
}