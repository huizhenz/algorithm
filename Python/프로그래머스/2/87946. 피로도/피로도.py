from itertools import permutations

def solution(k, dungeons):
    p = []
    for i in range(len(dungeons)):
        p.append(i)
    
    result = -1
    for i in permutations(p):
        cnt = 0
        hp = k
        for j in i:
            require, use = dungeons[j]
            
            if hp >= require:
                hp -= use
                cnt += 1
            else:
                break
        result = max(result, cnt)
    return result