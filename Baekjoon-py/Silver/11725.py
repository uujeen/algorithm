import sys
""" 11725번 : 트리의 부모 찾기 """
sys.setrecursionlimit(1000000)
def dfs(v):
    visited[v] = True
    p = parent[v]
    for child in vertex_list[v]:
        if not visited[child]:
            visited[child] = True
            parent[child] = v
            dfs(child)

n = int(sys.stdin.readline())
vertex_list = [[] for _ in range(n + 1)]
parent = [i for i in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    vertex_list[u].append(v)
    vertex_list[v].append(u)
dfs(1)
for i in range(2, len(parent)):
    print(parent[i])