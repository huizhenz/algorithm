def solution(numbers, hand):
    keypad = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
    
    def find_index(n):    
        result = []
        for row in keypad:
            if n in row:
                result = [keypad.index(row), row.index(n)]
        return result
    
    def get_distance(lh, rh, nh):
        y1, x1 = lh
        y2, x2 = rh
        y3, x3 = nh
        
        if abs(y1-y3)+abs(x1-x3) < abs(y2-y3)+abs(x2-x3):
            return 'left'
        elif abs(y1-y3)+abs(x1-x3) > abs(y2-y3)+abs(x2-x3):
            return 'right'
        else:
            return ''

    lh = [3,0]
    rh = [3,2]
    answer = ''
    for n in numbers:
        if n in (1, 4, 7):
            answer += 'L'
            lh = find_index(n)
        elif n in (3, 6, 9):
            answer += 'R'
            rh = find_index(n)
        else:
            nh = find_index(n)
            result = get_distance(lh, rh, nh)
            
            if result == 'left':
                answer += 'L'
                lh = nh
            elif result == 'right':
                answer += 'R'
                rh = nh
            else:
                if hand == 'left':
                    answer += 'L'
                    lh = nh
                else:
                    answer += 'R'
                    rh = nh
    
    return answer