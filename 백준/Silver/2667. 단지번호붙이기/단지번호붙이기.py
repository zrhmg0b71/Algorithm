import sys

N = int(sys.stdin.readline())
home = []
for i in range(N):
    home.append(list(map(int, input())))
visited = [[False for _ in range(N)] for _ in range(N)]
cnt = 0
homeCnt = [0]

def DFS(row, col):
    visited[row][col] = True
    if (home[row][col] == 1):
        homeCnt[cnt] += 1
        if (row > 0):
            if not visited[row - 1][col]:
                DFS(row - 1, col)
        if (col > 0):
            if not visited[row][col - 1]:
                DFS(row, col - 1)
        if (row < N - 1):
            if not visited[row + 1][col]:
                DFS(row + 1, col)
        if (col < N - 1):
            if not visited[row][col + 1]:
                DFS(row, col + 1)

for i in range(N):
    for j in range(N):
        if (visited[i][j] == False and home[i][j] == 1):
            homeCnt.append(0)
            cnt += 1
            DFS(i, j)

print(cnt)
homeCnt.sort()
for i in range(1, len(homeCnt)):
    print(homeCnt[i])