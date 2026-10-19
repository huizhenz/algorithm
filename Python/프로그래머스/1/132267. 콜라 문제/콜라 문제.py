def solution(a, b, n):
    answer = 0
    while n > a - 1:
        temp = n // a
        remain = n % a
        
        n = (temp * b) + remain
        answer += (temp * b)
    return answer