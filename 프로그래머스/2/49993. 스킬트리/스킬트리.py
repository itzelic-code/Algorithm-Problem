def solution(skill, skill_trees):
    answer = 0
    skill_set = set(skill) # 스킬을 문자열 -> 집합으로 변환
    
    for tree in skill_trees:
	    # 각 스킬트리에서 유효한 스킬 추출
	    filtered_skills = [s for s in tree if s in skill_set]
	    
	    # 필터링된 스킬이 순서에 맞는지 확인
	    if filtered_skills == list(skill[:len(filtered_skills)]):
		    answer += 1
    
    return answer