
V = 4
INF = float('inf')

d = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

for k in range(V):
    for i in range(V):
        for j in range(V):
            d[i][j] = min(d[i][j],
                          d[i][k] + d[k][j])

print("Shortest distance matrix:")
for row in d:
    print(row)
