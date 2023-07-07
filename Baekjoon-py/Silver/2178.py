import sys
from collections import deque

""" 2178번: 미로 탐색 """

def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if visited[nx][ny] == False:
                graph[nx][ny] += graph[x][y]
                visited[nx][ny] = True
                queue.append([nx, ny])
    print(graph[-1][-1])

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[False] * (m) for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))
bfs(0, 0)