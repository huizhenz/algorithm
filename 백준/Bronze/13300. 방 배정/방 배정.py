n, k = map(int, input().split())
students = [[0]*2 for _ in range(7)]

for i in range(n):
    s, y = map(int, input().split())
    students[y][s] += 1

cnt = 0
for i in range(1, len(students)):
    for j in range(len(students[i])):
        cnt += (students[i][j]//k)
        if students[i][j]%k:
            cnt += 1

print(cnt)