def solution(brown, yellow):
    total = brown + yellow
    temp = []
    
    for i in range(1, total):
        if total % i == 0:
            if i >= (total // i) :
                temp.append((i, total // i))
    
    for w, h in temp:
        if brown == w * 2 + ((h - 2) * 2):
            return [w, h]