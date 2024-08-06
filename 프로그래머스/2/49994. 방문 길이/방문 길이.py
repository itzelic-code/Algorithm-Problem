def solution(dirs):
    loc = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    answer = set()
    x, y = 0, 0
    for d in dirs:
        dx, dy = loc[d]
        nx, ny = x + dx, y + dy
        
        if abs(nx) <= 5 and abs(ny) <= 5:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x = nx 
            y = ny
            
    return len(answer) // 2