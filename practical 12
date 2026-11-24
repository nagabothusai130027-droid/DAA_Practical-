def tsp(n, cost):
    INF = float('inf')

    # dp[mask][i] = minimum cost to visit cities in mask
    # and finish at city i
    dp = [[INF] * n for _ in range(1 << n)]

    # Start from city 0
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue

            if dp[mask][u] == INF:
                continue

            for v in range(n):
                if not (mask & (1 << v)):
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(
                        dp[new_mask][v],
                        dp[mask][u] + cost[u][v]
                    )

    # Return to starting city
    full_mask = (1 << n) - 1
    ans = INF

    for i in range(n):
        ans = min(ans, dp[full_mask][i] + cost[i][0])

    if ans == INF:
        print("No valid tour exists.")
    else:
        print("Minimum travelling cost:", ans)


# Runtime input
n = int(input("Enter number of cities: "))

cost = []

print("Enter cost adjacency matrix (use INF for no path):")

for i in range(n):
    row = input().split()
    cost.append([
        float('inf') if x.upper() == "INF" else int(x)
        for x in row
    ])

tsp(n, cost)
