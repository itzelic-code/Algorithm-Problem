from itertools import combinations

modify = list(input())
bracket = []
stack = []
answer = set()

# 괄호 쌍 찾기
for i in range(len(modify)):
    if modify[i] == '(':
        stack.append(i)
    elif modify[i] == ')':
        bracket.append((stack.pop(), i)) # 쌍을 이루는 괄호의 인덱스 쌍 리스트

# 조합을 이용하여 가능한 경우의 수 찾기
for i in range(len(bracket)):
    for comb in combinations(bracket, i + 1):
        temp = modify[:]
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""
        answer.add("".join(temp)) # 중복 제거 및 저장

# 정렬 및 출력
for i in sorted(list(answer)):
    print(i)