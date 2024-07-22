def solution(bandage, health, attacks):

    now_health = health # 최대 체력
    attack_time = [i[0] for i in attacks]
    dealing = [i[1] for i in attacks]
    max_time = max([i[0] for i in attacks]) # 최대시간
    bandage_time = bandage[0] # 시전 시간
    second_healing = bandage[1] # 초당 회복량
    more_healing = bandage[2] # 추가회복량
    cnt = 0 # 붕대 시간
    
    for time in range(1,max_time+1):
        if time in attack_time: # 시간이 경과했을 때 공격 상태일 때
            cnt = 0 #연속 성공 초기화
            now_health -= dealing[attack_time.index(time)] #몬스터 공격
            if now_health <= 0: # 몬스터 공격했을때 피가 0이하면 종료
                answer = -1
                return answer
                # break
        else:
            cnt +=1
            if cnt == bandage_time: # 시전 시간이 됐을 때
                cnt = 0
                now_health += more_healing
                if now_health >= health :
                    now_health = health
            if now_health == health: # 체력이 최대 체력일 때
                pass
            else: # 체력이 최대 체력이 아닐 때
                now_health += second_healing
                if now_health >= health:
                    now_health = health
    print(now_health)

    if now_health <= 0:
        answer = -1
    else:
        answer = now_health
    return answer