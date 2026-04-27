T = int(input())
for tc in range(1, T+1):
    n = int(input())

    Sum = 0
    num = [0] * 10
    while 1:
        Sum += n

        for i in list(str(Sum)):
            num[int(i)] = 1

        if all(num):
            print(f"#{tc} {Sum}")
            break