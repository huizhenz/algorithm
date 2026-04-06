n = int(input())
arr = list(map(int, input().split()))
arr.sort()

Sum = 0
for i in range(n):
    Sum += sum(arr[0:i+1])

print(Sum)