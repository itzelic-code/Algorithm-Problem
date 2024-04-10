"""
* 메모리 : KB
* 시간 : ms
* 사용된 개념 : 정렬
--------------------------------------------------
* 접근 방법
1. 열림 괄호 만날 때마다 스택에 추가
2. 닫힘 괄호 만났을 때
	2-1. 이전 괄호가 열림 괄호였으면 레이저이므로 스택의 열림 괄호를 카운트에 추가
	2-2. 이전 괄호도 닫힘 괄호였으면 쇠막대기 끝이므로 카운트 + 1
--------------------------------------------------
"""
from sys import stdin
input = stdin.readline

sequence = input().strip()
stack = []
count = 0

for i in range(len(sequence)):
	if sequence[i] == '(':
		stack.append('(')
	else:
		if sequence[i-1] == '(':
			stack.pop()
			count += len(stack)
		else:
			stack.pop()
			count += 1
			
print(count)