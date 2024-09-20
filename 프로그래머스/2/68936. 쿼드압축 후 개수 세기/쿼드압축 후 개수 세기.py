# 재귀를 이용한 풀이
# 배열 4등분& 모두 같으면 answer+1, 하나라도 다르면 count를 반복
# len(arr)의 길이가 1이 됨녀 재귀 스탑

def quad_zip(arr, x, y, n):
	# 사각형 순회
	for i in range(x, x + n):
		for j in range(y, y + n):
			if (arr[i][j] != arr[x][y]): # 첫 번째 요소와 값이 다르면 다시 호출
				n //= 2
				quad_zip(arr, x, y, n)
				quad_zip(arr, x + n, y, n)
				quad_zip(arr, x, y + n, n)
				quad_zip(arr, x + n, y + n, n)
				return
	answer[arr[x][y]] += 1 # 첫 번째 요소와 값이 같은 경우 + 1

def solution(arr):
	global answer
	answer = [0, 0]
	quad_zip(arr, 0, 0, len(arr))
	return answer
