def Kruskal(vertices, edges):
    edges.sort(key=lambda edge: edge[2])
    groups = [[v] for v in vertices]
    mst = []
    cost = 0

    for i, j, weight in edges:
        grp_i = None
        grp_j = None

        for group in groups:
            if i in group:
                grp_i = group
            if j in group:
                grp_j = group

        if grp_i != grp_j:
            mst.append((i, j, weight))
            cost += weight
            grp_i.extend(grp_j)
            groups.remove(grp_j)

    return mst, cost


vertices = input("Enter vertices: ").split()

n = int(input("Enter number of edges: "))
edges = []

for _ in range(n):
    u, v, w = input("Enter edge (u v weight): ").split()
    edges.append((u, v, int(w)))

mst, cost = Kruskal(vertices, edges)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Minimum Cost:", cost)