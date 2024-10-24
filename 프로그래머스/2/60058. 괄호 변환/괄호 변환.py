def is_balance(s):  # 균형잡힌 괄호 문자열인지 확인하는 함수
    check = 0
    for i in s:
        if (i == '('):
            check += 1
        else:
            check -= 1
    if (check == 0):
        return True
    return False


def is_correct(s):  # 올바른 괄호 문자열인지 확인하는 함수
    li = []
    for i in s:
        if (i == '('):
            li.append(i)
        else:
            if (len(li) == 0):
                return False
            else:
                li.pop()

    if (len(li) == 0):
        return True
    return False


def solution(p):
    answer = ''
    u = ""
    v = ""

    if (len(p) == 0 or is_correct(p)):
        return p

    for i in range(2, len(p) + 1, 2):
        if (is_balance(p[0:i])):
            u = p[:i]
            v = p[i:]
            break

    if (is_correct(u)):
        answer += u + solution(v)
    else:
        answer += '(' + solution(v) + ')'
        for i in u[1 : -1]:
            if (i == '('):
                answer += ')'
            else:
                answer += '('

    return answer
