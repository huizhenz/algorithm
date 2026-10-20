n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_value = 21e8
for i in range(n):
    total = 0
    for j, a in enumerate(A, 0):
        total += a * abs(j-i)
    min_value = min(min_value, total)

print(min_value)