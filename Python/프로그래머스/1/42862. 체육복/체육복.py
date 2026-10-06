def solution(n, lost, reserve):
    lst = [1] * (n + 1)
    
    for l in lost:
        if not l in reserve:
            lst[l] -= 1
        else:
            reserve.remove(l)
    
    for r in sorted(reserve):
        if r-1 >= 0 and lst[r-1] == 0:
            lst[r-1] += 1
            continue
        elif r+1 <= n and lst[r+1] == 0:
            lst[r+1] += 1
            continue
    
    answer = 0
    for i in lst[1:]:
        if i > 0:
            answer += 1
    return answer