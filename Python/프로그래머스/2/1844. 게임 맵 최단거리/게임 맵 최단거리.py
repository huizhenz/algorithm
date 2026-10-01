from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1
    q = deque([(0, 0)])
    
    while 1:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            
            if 0 <= ny < n and 0 <= nx < m: 
                if maps[ny][nx] == 1 and dist[ny][nx] == -1: 
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
        
        if not q:
            break
        
    return dist[n-1][m-1]