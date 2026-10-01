def solution(people, limit):
    people.sort(reverse=True)
    cnt = 0
    
    for p in people:
        temp = limit - p
        if temp >= people[-1]:
            people.pop()
        cnt += 1
    
    return cnt