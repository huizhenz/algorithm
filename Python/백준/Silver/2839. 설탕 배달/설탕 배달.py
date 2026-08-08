n = int(input())
cnt = -1
while 1:
    if n >= 5:
        if n % 5 == 0:
            cnt = n // 5
            break
        else:
            q = n // 5
            r = n % 5
            if r % 3 == 0:
                cnt = q + 1
                break
            else:
                for i in range(1, q+1):
                    if (r + 5 * i) % 3 == 0:
                        cnt = q-i
                        cnt += (r + 5 * i) // 3
                        break
                break
    else:
        if n % 3 == 0:
            cnt = n // 3
            break
        else:
            cnt = -1
            break
print(cnt)