n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
prev = arr[0]
cnt = 0
max_cnt = 0
for a in arr:
    if prev != a:
        cnt = 1
    else:
        cnt += 1
    prev = a
    max_cnt = max(max_cnt, cnt)

print(max_cnt)