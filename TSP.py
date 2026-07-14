# TRAVELLING SALESMAN PROBLEM
# Uses backtracking to find the shortest possible route that visits each city and returns to the origin city.

bestPath = []
minCost = float("inf")

def TSP(dist, curr, path, visited, cost, n):
    global bestPath, minCost
    if len(path) == n:
        if cost + dist[curr][path[0]] < minCost:
            minCost = cost + dist[curr][path[0]]
            path.append(path[0])
            bestPath = path[:]
            path.pop()
        return
    if cost >= minCost:
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            TSP(dist, i, path, visited, cost + dist[curr][i], n)
            path.pop()
            visited[i] = False

if __name__ == "__main__":
    n = int(input("Enter the number of cities: "))
    dist = []
    print("Enter the distance matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        dist.append(row)
    start = int(input("\nEnter the starting city : ")) - 1
    path = []
    visited = [False] * n
    visited[start] = True
    path.append(start)
    TSP(dist, start, path, visited, 0, n)
    print("\nBEST PATH : ")
    for x in bestPath:
        print(x+1, end=" ")
    print(" : ", minCost)