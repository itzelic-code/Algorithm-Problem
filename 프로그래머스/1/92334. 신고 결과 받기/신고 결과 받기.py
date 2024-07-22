from collections import defaultdict

def solution(id_list, report, k):
    report_dict = defaultdict(set)
	  # 정지 메일 수
    mail_count = {user: 0 for user in id_list}
    
    # 신고 내역 순회
    for r in report:
        reporter, reported = r.split()
        report_dict[reported].add(reporter)
    
    # 정지 처리 대상자 찾기
    for user, reporters in report_dict.items():
        if len(reporters) >= k:
            for reporter in reporters:
                mail_count[reporter] += 1
    
    return list(mail_count.values())
