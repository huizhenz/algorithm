def solution(t, p):
    len_t = len(t)
    len_p = len(p)
    answer = 0
    for i in range(0, len_t-len_p+1):
        if int(t[i:i+len_p]) <= int(p):
            answer += 1
    return answer