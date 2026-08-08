from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

dir_y = [-1, 0, 1, 0]
dir_x = [0, 1, 0, -1]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1

q = deque()
q.append((0, 0, 1))

while q:
    y, x, cnt = q.popleft()

    if y == n-1 and x == m-1:
        print(cnt)
        break

    for i in range(4):
        dy = y + dir_y[i]
        dx = x + dir_x[i]

        if 0>dy or 0>dx or dy>=n or dx>=m: continue
        if visited[dy][dx] or arr[dy][dx] == 0: continue
        visited[dy][dx] = 1
        q.append((dy, dx, cnt+1))