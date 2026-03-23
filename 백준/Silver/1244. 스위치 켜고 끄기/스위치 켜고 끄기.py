n = int(input())
arr = list(map(int, input().split()))
k = int(input())
for _ in range(k):
    g, s = map(int, input().split())

    if g == 1:
        for i in range(n):
            if (i+1) % s == 0:
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    arr[i] = 0
    else:
        if arr[s - 1] == 0:
            arr[s - 1] = 1
        else:
            arr[s - 1] = 0
        for i in range(1, n+1):
            if (s - 1 - i) < 0 or (s - 1 + i) >= n: break
            if arr[s-1-i] != arr[s-1+i]:
                break
            else:
                if arr[s-1-i] == 0:
                    arr[s-1-i], arr[s-1+i] = 1, 1
                else:
                    arr[s-1-i], arr[s-1+i] = 0, 0

for i in range(0,len(arr),20):
    print(*arr[i:i+20])