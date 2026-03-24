T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
 
        for k in range(1, j+1):
            if i-1-k < 0 or i-1+k >= N: continue
            if stones[i-1-k] == stones[i-1+k]:
                if stones[i-1-k] == 0:
                    stones[i-1-k], stones[i-1+k] = 1, 1
                else:
                    stones[i-1-k], stones[i-1+k] = 0, 0
 
    print(f"#{tc}", end=" ")
    print(*stones)