import sys
from collections import deque
""" 1260번: DFS와 BFS """

""" DFS 비재귀적, 재귀적"""
class DFS:
    def __init__(self, n, edge_list):
        self.n = n
        self.parent = [i for i in range(n + 1)] # 부모정점 초기엔 자기 자신, DFS 트리를 만들 수 있다.
        self.vertex_list = [[] for _ in range(n + 1)]; self.make_vertex_set(edge_list) # 간선 집합으로 정점 집합 만들기
        self.visited = [False] * (n + 1) # 방문 여부 체크, N번 인덱스에 False값을 주기 위해 N + 1
        self.cur_time = 0 # 현재 시간
        self.pre_time = [0] * (n + 1) # 방문 정점의 dfs 시작 시간
        self.post_time = [0] * (n + 1) # 방문 정점의 dfs 종료 시간
        self.dfs_stack = [] # dfs 완료된 배열 저장

    def make_vertex_set(self, edge_list): # 양방향 간선이므로 현재 정점의 연결된 정점 저장
        for u, v in edge_list:
            self.vertex_list[u].append(v)
            self.vertex_list[v].append(u)
        for i in range(len(self.vertex_list)): # 문제 풀이용 코드, 작은 정점부터 방문하기 위해
            self.vertex_list[i].sort()

    def dfs(self, v): # 비재귀적 dfs
        self.pre_time[v] = self.cur_time
        self.cur_time += 1 # dfs 시작

        stack = []
        stack.append([self.parent[v], v]) # 부모정점와, 자식정점을 stack에 넣는다.

        while stack: # 모든 정점을 방문해서 스택에 더 이상 방문할 정점이 없을 때 까지
            p, v = stack.pop()
            self.post_time[v] = self.cur_time # dfs 종료
            self.cur_time += 1 # 현재 시간 증가

            if not self.visited[v]: # 만약 방문하지 않은 노드일 경우
                self.dfs_stack.append(v) # dfs 완료된 정점 추가
                self.visited[v] = True 
                self.parent[v] = p
                for u in self.vertex_list[v][::-1]: # 낮은 정점부터 방문하기위해 역으로 입력
                    if not self.visited[u]:
                        stack.append([self.parent[u], u])

    def dfs_recur(self, v): # 재귀적 dfs
        self.visited[v] = True
        self.pre_time[v] = self.cur_time # dfs 시작
        self.cur_time +=1 # 현재 시간 증가
        self.dfs_stack.append(v) # dfs 완료된 정점 추가

        for u in self.vertex_list[v]: 
            if not self.visited[u]:
                self.parent[u] = v # 현재 노드와 연결된 노드의 부모를, 현재 노드로 저장
                self.dfs_recur(u) # 깊이 탐색 재귀적 호출
        self.post_time[v] = self.cur_time # dfs 종료
        self.cur_time += 1

    def print_dfs(self): # 완료된 dfs 배열로 출력
        for i in self.dfs_stack:
            print(i, end=' ')
        print()
    
    def print_parent(self): # 부모정점 출력, 부모 정점의 인덱스에 있는 값이 부모를 가르키므로, 연결시 DFS 트리를 만들 수 있다.
        for i in self.parent[1:]: # 추가로 사용되지 않은 간선은, back edge라고 부르며 back edge의 존재 여부로 사이클이 형성되어 있는 그래프였는지 알 수 있다.
            print(i, end=' ')
        print()
    
    def print_post(self): # dfs가 완료된 시간 각 정점별로 출력, 내림차순으로 출력시 위상정렬된 값을 얻을 수 있다.
        for i in self.post_time[1:]:
            print(i, end=' ')
        print()

""" BFS """
class BFS:
    def __init__(self, n, edge_list):
        self.vertex_list = [[] for _ in range(n + 1)]; self.make_vertex_set(edge_list) # 간선 집합으로 정점 집합 만들기
        self.visited = [False] * (n + 1) # 방문 여부 체크, N번 인덱스에 False값을 주기 위해 N + 1
        self.bfs_stack = [] # bfs 완료된 배열 저장

    def make_vertex_set(self, edge_list): # 양방향 간선이므로 현재 정점의 연결된 정점 저장
        for u, v in edge_list:
            self.vertex_list[u].append(v)
            self.vertex_list[v].append(u)
        for i in range(len(self.vertex_list)): # 문제 풀이용 코드, 작은 정점부터 방문하기 위해
            self.vertex_list[i].sort()

    def bfs(self, v):
        queue = deque() # 큐 생성
        queue.append(v) # 해당 정점을 큐에 넣는다. 이후 해당 정점과 연결된 정점들을 탐색한다.
        self.visited[v] = True # 방문 체크
        while queue: # 모든 정점을 방문할 때 까지
            v = queue.popleft() # v 와 연결된 정점을 순차적으로 pop한다.
            self.bfs_stack.append(v) # bfs 완료된 정점을 저장한다.
            for i in self.vertex_list[v]: # 해당 정점과 연결된 모든 정점을 확인하고
                if not self.visited[i]: # 그 중 방문하지 않은 정점만
                    queue.append(i) # 큐에 넣는다.
                    self.visited[i] = True # 방문 체크

    def print_bfs(self): # 완료된 bfs 배열로 리턴
        for i in self.bfs_stack:
            print(i, end=' ')
        print()


n, m, v = map(int, sys.stdin.readline().split())
edge_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

""" DFS """
dfs_recur = DFS(n, edge_list)
dfs_recur.dfs_recur(v)
print("재귀적 DFS : ", end='')
dfs_recur.print_dfs()

dfs = DFS(n, edge_list)
dfs.dfs(v)
print("비재귀적 DFS : ", end='')
dfs_recur.print_dfs()

""" BFS """
bfs = BFS(n, edge_list)
print("BFS : ", end='')
bfs.bfs(v)
bfs.print_bfs()