n = int(input())
arr = list(map(int, input().split()))
result = [1] * n

for i in range(n):
    target = arr[i]
    for j in range(i):
        value = arr[j]
        if target > value:
            result[i] = max(result[j]+1, result[i]) # 비교대상값+1 vs 현재기준점

print(max(result))
