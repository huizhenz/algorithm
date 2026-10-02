import math

def solution(progresses, speeds):
    result = []
    for i in range(len(progresses)):
        result.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    cnt = 1
    prev = result[0]
    answer = []
    for i in range(1, len(result)):
        if prev >= result[i]:
            cnt += 1
        else:
            prev = result[i]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
            
    return answer