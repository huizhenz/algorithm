def solution(park, routes):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    dir = ['N', 'E', 'S', 'W']
    
    w, h = len(park), len(park[0])
    y, x = 0, 0
    for r in range(w):
        for c in range(h):
            if park[r][c] == 'S':
                y, x = r, c
    
    for r in routes:
        d, cnt = r.split(' ')
        idx = dir.index(d)
        
        ny, nx = y, x
        check = True
        
        for i in range(int(cnt)):
            ny += dy[idx] 
            nx += dx[idx]
            
            if not (0 <= ny < w and 0 <= nx < h):
                check = False
                break
                
            if park[ny][nx] == 'X':
                check = False
                break
    
        if check:
            y, x = ny, nx
    
    return [y, x]