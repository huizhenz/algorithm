T = int(input())
for tc in range(1, T+1):
    # 오른쪽에서 n번째까지 모두 1인가 ?
    n, m = map(int, input().split())
	
    # b = bin(m)[2:]
    
    # ans = ""
    # if n > len(b):
    #     ans = "OFF"
    # elif b[-n:].count('0'):
    #     ans = "OFF"
    # else:
    #     ans = "ON"
    # print(f"#{tc} {ans}")

    # ------------------------- #
  
    if (m & ((1 << n) - 1)) == (1 << n) - 1:
        ans = "ON"
    else:
        ans = "OFF"
    print(f"#{tc} {ans}")