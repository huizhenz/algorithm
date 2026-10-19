def solution(d, budget):
    d.sort()
    total = 0
    answer = 0
    for i in d:
        total += i
        if total <= budget:
            answer += 1
    return answer