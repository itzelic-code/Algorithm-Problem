# 브루트포스 사용 예시 : 모든 조합을 평가해야 하는 경우
# 여러 개의 연산자를 동시에 분리하려면 re.split이 적절
from re import split
from itertools import permutations

def solution(expression):
    values = []
    
    for priority in permutations(['*', '+', '-'], 3):
        # 연산자, 피연산자 저장
        operands = list(map(int, split('[\*\+\-]', expression)))
        operators = [c for c in expression if c in '*+-']
        
        # 우선순위 배열을 순회하며 연산 수행
        for op in priority:
            
            while op in operators:
                # i번째 연산자 -> i번째 피연산자와 i+1번째 피연산자로 연산 수행
                i = operators.index(op)
                
                if op == '*':
                    v = operands[i] * operands[i+1]
                elif op == '+':
                    v = operands[i] + operands[i+1]
                else:
                    v = operands[i] - operands[i+1]
                
                operands[i] = v # 피연산자 업데이트
                operands.pop(i+1) # 연산자 업데이트
                operators.pop(i)
        
        values.append(operands[0])
        
    return max(abs(v) for v in values)