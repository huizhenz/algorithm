N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
def penalty():
    temp = [0] * (N + 1)
    for s in student:
        temp[s] += 1

        if temp[s] >= K:
            return s

result = penalty()
if result:
    print(result)
else:
    print(-1)

