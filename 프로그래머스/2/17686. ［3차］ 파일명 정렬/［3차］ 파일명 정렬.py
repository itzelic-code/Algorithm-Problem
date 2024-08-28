def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''
        number_check = False
        
        # 문자열 자르기
        for i in range(len(f)):
            if f[i].isdigit():  # 처음 나오는 숫자 = NUMBER
                number += f[i]
                number_check = True
            elif not number_check:  # NUMBER가 나오기 전 =  HEAD
                head += f[i]
            else:               # NUMBER가 이미 나온 경우, 숫자가 아닌 문자면 TAIL로
                tail = f[i:]
                break
        answer.append((head, number, tail))  # HEAD, NUMBER, TAIL 저장

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
    return [''.join(t) for t in answer]