T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(1, n+1): 
        v, c = arr[i-1] 
        for j in range(k+1): 
            if j < v:
               dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-v]+c)

    print(f"#{tc} {dp[n][k]}")