K, N = map(int, input().split())

# Please write your code here.
arr = []
def dfs(n):
    if n == N:
        print(*arr)
        return

    for i in range(1, K+1):
        arr.append(i)
        dfs(n+1)
        arr.pop()
dfs(0)