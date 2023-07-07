import sys
from collections import deque
""" 18352번 : 특정 거리의 도시 찾기 """

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        x = queue.popleft()
        visited[x] = True
        for city in vertex_list[x]:
            if not visited[city]:
                queue.append(city)
                visited[city] = True
                city_list[city] += city_list[x] # 다음 방문하는 도시에 현재 방문한 도시의 방문 횟수를 더한다.

n, m, k, x = map(int, sys.stdin.readline().split())
edge_list= [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
vertex_list = [[] for _ in range(n + 1)]
city_list = [1] * (n + 1)

for u, v in edge_list:
    vertex_list[u].append(v)
visited = [False] * (n + 1)
bfs(x)
for i in range(1, len(city_list)):
    if i == x:
        continue
    if city_list[i] - 1 == k:
        print(i)
        
city_list = city_list[1:x] + city_list[x + 1:]
if not k + 1 in city_list:
    print(-1)