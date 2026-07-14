/*
TRAVELLING SALESMAN PROBLEM
Uses backtracking to find the shortest possible route that visits each city and returns to the origin city.
*/

#include <bits/stdc++.h>

using namespace std;

vector<int> bestPath;
int minCost = INT_MAX;

void TSP(vector<vector<int>>& dist, int curr, vector<int>& path, vector<bool>& visited, int cost, int n)
{
    if(path.size() == n)
    {
        if(cost+dist[curr][path[0]] < minCost)
        {
            minCost = cost+dist[curr][path[0]];
            path.push_back(path[0]);
            bestPath = path;
            path.pop_back();
        }
        return;
    }
    if(cost >= minCost)
        return;
    for(int i=0;i<n;i++)
    {
        if(!visited[i])
        {
            visited[i] = true;
            path.push_back(i);
            TSP(dist, i, path, visited, cost + dist[curr][i], n);
            path.pop_back();
            visited[i] = false;
        }
    }
}

int main()
{
    int n;
    cout<<"\nEnter the number of cities: ";
    cin>>n;
    vector<vector<int>> dist(n, vector<int>(n,0));
    cout<<"\nEnter distance between cities : \n";
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<i;j++)
        {
            cout<<"\n"<<i+1<<" to "<<j+1<<" : ";
            cin>>dist[i][j];
            dist[j][i] = dist[i][j];
        }
    }
    int start;
    cout<<"\nEnter the starting city : ";
    cin>>start;
    start--;
    vector<int> path;
    vector<bool> visited(n,false);
    visited[start] = true;
    path.push_back(start);
    TSP(dist, start, path, visited, 0, n);
    cout<<"\nBEST PATH : ";
    for(int x:bestPath)
        cout<<x+1<<" ";
    cout<<" : "<<minCost;
}