def worktime(time):
    hour = time // 100
    minute = time % 100 + 10
    
    hour += minute // 60
    minute %= 60
    
    return hour * 100 + minute
    
def solution(schedules, timelogs, startday):    
    answer = 0
    for i, s in enumerate(schedules):
        limit = worktime(s)
        
        check = True
        for j, t in enumerate(timelogs[i]):
            day = startday + j
            
            if day % 7 in (6, 0):
                continue
            else:
                if limit < t:
                    check = False
                    break
                    
        if check:
            answer += 1
    
    return answer