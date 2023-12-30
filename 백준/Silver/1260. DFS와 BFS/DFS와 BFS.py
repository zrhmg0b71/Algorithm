import sys
from queue import Queue

def dfs(adj, v, s):
    def recur(v):
        visited[v] = True
        ans.append(v)
        for w in adj[v]:
            if not visited[w]:
                recur(w)
    ans = []
    visited = [False for _ in range(v)]
    recur(s)
    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()

def bfs(adj, v, s):
    ans = []
    visited = [False for _ in range(v)]
    queue = Queue()
    queue.put(s)
    visited[s] = True
    while queue.qsize() > 0:
        vertex = queue.get()
        ans.append(vertex)
        for w in adj[vertex]:
            if not visited[w]:
                queue.put(w)
                visited[w] = True
    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()

N, M, V = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]
graph = []
for i in range(M):
    v, w = map(int, sys.stdin.readline().split())
    adj[v].append(w)
    adj[w].append(v)

for i in range(1, N + 1):
    adj[i] = sorted(adj[i])

dfs(adj, N + 1, V)
bfs(adj, N + 1, V)