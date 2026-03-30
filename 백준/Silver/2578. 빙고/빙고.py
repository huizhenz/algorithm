arr = [list(map(int, input().split())) for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]
flat = []
for i in num:
    for j in i:
        flat.append(j)

def bingo_check():
    global arr
    bingo = 0

    # 가로세로 체크
    for _ in range(2):
        for i in range(5):
            temp = 0
            for j in range(5):
                if arr[i][j] == 0:
                    temp += 1
            if temp == 5:
                bingo += 1

        # 가장 외부 for문이 2가 되면 다시 arr이 원래대로 돌아옴
        arr = list(map(list, zip(*arr)))

    # 대각선 체크
    temp5 = 0
    temp7 = 0
    for i in range(5):
        if arr[i][i] == 0:
            temp5 += 1
        if arr[i][4-i] == 0:
            temp7 += 1

    if temp5 == 5:
        bingo += 1
    if temp7 == 5:
        bingo += 1

    return bingo

ans = 0
for k in range(len(flat)):
    for i in range(5):
        for j in range(5):
            if flat[k] == arr[i][j]:
                arr[i][j] = 0

    ret = bingo_check()
    if ret >= 3:
        ans = k+1
        break
print(ans)