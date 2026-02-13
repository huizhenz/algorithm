T = int(input())
for tc in range(1, T+1):
    stu = list(map(int, input().split()))
    line_stu = []

    cnt = 0
    for i in range(1, len(stu)):
        line_stu.append(stu[i])

        if i > 1:
            for j in range(i-1, 0, -1):
                if line_stu[j] < line_stu[j-1]:
                    cnt += 1
                    line_stu[j], line_stu[j-1] = line_stu[j-1], line_stu[j]
                else:
                    continue

    print(f"{tc} {cnt}")
