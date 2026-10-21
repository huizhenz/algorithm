n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def calc(r, w):
    cnt = 0
    for i in range(r, r+3):
        for j in range(w, w+3):
            if grid[i][j] == 1:
                cnt += 1
    return cnt

max_v = -21e8
for i in range(n-2):
    for j in range(n-2):
        max_v = max(max_v,  calc(i, j))

print(max_v)