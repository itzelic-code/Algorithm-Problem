import math

def solution(fees, records):
    answer= []
    times = {}
    car = {}
    
    for i in records:
        time, number, io = i.split()
        hour, minute = time.split(':')
        minutes = int(hour) * 60 + int(minute)
        if io == "IN":
            car[number] = minutes
        elif io == "OUT":
            time = minutes - car[number]
            if number in times:
                times[number] += time
            else:
                times[number] = time
            del(car[number])
            
    for key, val in car.items():
        time = 23 * 60 +59 - val
        if key in times:
            times[key] += time
        else:
            times[key] = time
    for key,val in times.items():
        time= max(0, val- fees[0])
        money = fees[1] + math.ceil(time/fees[2]) * fees[3]
        times[key] = money
    times = sorted(times.items())
    for key, val in times:
        answer.append(val)
    return answer