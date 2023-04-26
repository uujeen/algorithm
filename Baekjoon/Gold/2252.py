import sys

def dfs(v):
    global cur_time
    visited[v] = True
    pre_time[v] = cur_time
    cur_time += 1
    for vertex in edge_list[v]:
        if not visited[vertex]:
            visited[vertex] = True
            dfs(vertex)
    post_time[v] = cur_time
    cur_time += 1

n, m = map(int, sys.stdin.readline().split())
edge_list = [[] for i in range(n + 1)]
dfs_list = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edge_list[u].append(v)

cur_time = 0
pre_time = [0] * (n + 1)
post_time = [0] * (n + 1)

for i in range(1, len(edge_list)):
    if not visited[i]:
        dfs(i)
for i in range(len(post_time)):
    dfs_list[i] = [i, post_time[i]]

dfs_list.sort(key = lambda x : -x[1])

for i in range(len(dfs_list) - 1):
    print(dfs_list[i][0], end=' ')
print()