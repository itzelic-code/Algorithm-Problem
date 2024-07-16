def solution(players, callings):
    player_index = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        idx = player_index[calling]
        if idx > 0:
            # 현재 선수의 순위를 한 단계 올리기
            player_index[calling] -= 1
            player_index[players[idx - 1]] += 1
            
            # 선수 순서 바꾸기
            players[idx], players[idx - 1] = players[idx - 1], players[idx]
    
    return players
