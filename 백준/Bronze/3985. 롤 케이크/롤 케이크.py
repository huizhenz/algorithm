l = int(input())
n = int(input())
cake = [0]*(l+1)

expe_max = -21e8
expe_idx = -1
real_max = -21e8
real_idx = -1
for i in range(1, n+1):
    p, k = map(int, input().split())
    if expe_max < abs(p-k):
        expe_max = abs(p-k)
        expe_idx = i

    cnt = 0
    for j in range(p, k+1):
        if not cake[j]:
            cake[j] = i
            cnt += 1
    if real_max < cnt:
        real_max = cnt
        real_idx = i

print(expe_idx)
print(real_idx)