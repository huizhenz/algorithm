def solution(today, terms, privacies):
    def to_days(date):
        y, m, d = map(int, date.split('.'))
        return y * 12 * 28 + m * 28 + d
    
    term_map = {}
    for t in terms:
        type, month = t.split()
        term_map[type] = int(month)
    
    answer = []
    for i, p in enumerate(privacies, 1):
        date, type = p.split()
        expire = to_days(date) + term_map[type] * 28
        
        if expire <= to_days(today):
            answer.append(i)
            
    return sorted(answer);