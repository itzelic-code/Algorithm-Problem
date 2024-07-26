def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    for progress, speed in zip(progresses, speeds):
        if (progress + time * speed) < 100:
            if count > 0:
                answer.append(count)
                count = 0
            time = (100 - progress + speed - 1) // speed
        count += 1
    
    if count > 0:
        answer.append(count)
    
    return answer
