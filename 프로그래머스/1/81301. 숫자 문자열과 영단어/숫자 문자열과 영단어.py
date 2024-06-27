def solution(s):
    answer = s
    num = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    # 문자열 s를 숫자 기준으로 분리
       
    for key in num:
        if key in s:
            answer = answer.replace(key, str(num[key]))
    return int(answer)