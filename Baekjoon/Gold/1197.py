# kruskal 알고리즘
import sys
import heapq
""" 1197번: 최소 스패닝 트리"""

""" Kruskal Algorithm"""
class Kruskal:
    def __init__(self, v, e, edge_list):
        self.v = v
        self.e = e
        self.edge_list = edge_list
        self.parent = [i for i in range(v + 1)] # 부모 리스트 생성 초기값은 자기자신을 가리킨다. 1부터 정점의 개수까지
        self.sum_weight = 0

    def find(self, x): # 해당 정점의 부모를 찾는다.
        if self.parent[x] != x: # 부모가 같지 않을 시 재귀적으로 부모를 호출한다.
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x # find의 재귀 호출이 끝나고 부모 정점을 반환한다.
    
    def union(self, u, v): # 부모를 갱신해준다. (두 정점을 간선으로 이어준다.라고 이해할 수 있다.)
        u = self.find(u)
        v = self.find(v)
        if u > v: # 정렬의 기준을 정하는 것이라, u < v로 해도 무방하다.
            self.parent[u] = v
        else:
            self.parent[v] = u

    def kruskal(self):
        self.edge_list.sort(key = lambda x : x[2]) # 간선들의 가중치를 오름차순으로 정렬
        for u, v, weight in edge_list:
            if self.find(u) != self.find(v): # 두 정점의 부모가 다를 경우 (같을 경우 이미 연결되어 있기 때문에 싸이클이 생성된다.)
                self.union(u, v) # 이어준다.
                self.sum_weight += weight
        return self.sum_weight

""" Prim Algorithm"""
class Prim:
    def __init__(self, v, e, edge_list):
        self.v = v
        self.e = e
        self.vertex_list = [[] for _ in range(self.v + 1)] # 해당 정점에 연결된 정점들의 집합
        self.make_vertex_set(edge_list)
        self.visited = [False] * (v + 1) # 해당 정점의 방문 여부
        self.heap = [[0, 1]] # [weight, 현재 정점]
        self.sum_weight = 0

    def make_vertex_set(self, edge_list): # 간선의 집합을 통해 정점의 집합을 만든다.
        for u, v, w in edge_list:
            self.vertex_list[u].append([w, v])
            self.vertex_list[v].append([w, u])

    def prim(self):
        while self.heap: # heap이 빌 때 까지
            w, v = heapq.heappop(self.heap) # weight, vertex
            if not self.visited[v]: # 만약 현재 노드를 방문하지 않았다면
                self.visited[v] = True # 방문 체크
                self.sum_weight += w # 가중치를 더한다.
                for i in self.vertex_list[v]: # 현재 정점과 연결된 정점의 집합을 heap에 넣는다. (다음 정점 탐색을 위해)
                    heapq.heappush(self.heap, i)
        return self.sum_weight

v, e = map(int, sys.stdin.readline().split())
edge_list = [list(map(int, sys.stdin.readline().split())) for _ in range(e)] # 간선들의 집합

""" Kruskal Algorithm"""
kruskal = Kruskal(v, e, edge_list)
print('kruskal :', kruskal.kruskal())

""" Prim Algorithm"""
prim = Prim(v, e, edge_list)
print('prim :', prim.prim())