# N = 컴퓨터의 수, M = 컴퓨터 쌍의 수
import sys

def dfs(adj, v, s):
    def recur(v):
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                recur(w)
    
    visited = [False for _ in range(v)]
    recur(s)
    cnt = 0
    for i in range(2, len(visited)):
        if visited[i]:
            cnt += 1
    print(cnt)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj = [[] for _ in range(N + 1)]
for i in range(M):
    v, w = map(int, sys.stdin.readline().split())
    adj[v].append(w)
    adj[w].append(v)

dfs(adj, N + 1, 1)