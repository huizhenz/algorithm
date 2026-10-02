def solution(clothes):
    d = {}
    for name, kind in clothes:
        d[kind] = d.get(kind, 0) + 1
    
    temp = 1
    for value in d.values():
        temp *= (value + 1)
    
    return temp - 1
    