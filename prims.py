import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    pq = [(0, 0)]
    Total_cost = 0

    while pq:
        w, v = heapq.heappop(pq)

        if visited[v]:
            continue

        visited[v] = True
        Total_cost += w

        for neigh, e_w in graph[v]:
            heapq.heappush(pq, (e_w, neigh))

    return Total_cost


n = int(input("Enter number of vertices: "))
graph = [[] for _ in range(n)]

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v, w = map(int, input("Enter u v weight: ").split())
    graph[u].append((v, w))
    graph[v].append((u, w))

print("Minimum Spanning Tree cost:", prim(graph))