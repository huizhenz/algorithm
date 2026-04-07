n, k = map(int, input().split())
knapsack = [10001] * (k + 1)
knapsack[0] = 0

for _ in range(n):
    c = int(input())
    for i in range(c, k+1):
        knapsack[i] = min(knapsack[i], knapsack[i-c]+1)

if knapsack[k] >= 10001:
    print(-1)
else:
    print(knapsack[k])
