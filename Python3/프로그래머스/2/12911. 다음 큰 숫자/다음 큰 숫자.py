def solution(n):
    answer = 0
    i = 1
    while 1:
        m = n + i
        
        if bin(n)[2:].count("1") == bin(m)[2:].count("1"):
            answer = m
            break
        
        i += 1
    return answer