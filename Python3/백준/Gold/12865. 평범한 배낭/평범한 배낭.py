n, k = map(int, input().split())
knapsack = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    w, v = map(int, input().split())

    for j in range(k+1):
        if j < w:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(knapsack[i - 1][j], v + knapsack[i - 1][j - w])

print(knapsack[n][k])