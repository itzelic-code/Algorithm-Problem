def solution(n):
    # 삼각형 생성
    triangle = [[0 for j in range(1,i+1)] for i in range(1,n+1) ]
    x,y = -1,0 # 시작 좌표
    num = 1    # 시작값

    for i in range(n): # n번 반복
        for j in range(i,n):
            if i % 3 == 0: # 아랫쪽
		            x += 1
            elif i % 3 == 1: # 오른쪽
                y += 1
            else: # 윗쪽
                x -= 1
                y -= 1
            triangle[x][y] = num # 값 갱신
            num += 1 # 다음 값으로
            
    return sum(triangle,[])