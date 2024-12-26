n = int(input())  # 과일의 개수 n을 입력받음
arr = list(map(int, input().split()))  # 과일의 종류를 나타내는 배열 arr을 입력받음

answer = 0  # 최대 과일 탕후루 길이를 저장할 변수
left = 0  # 탕후루의 왼쪽 끝 인덱스
count = {}  # 각 과일의 개수를 저장할 딕셔너리 {과일명 : 개수}
kind = 0  # 현재 탕후루에 포함된 서로 다른 과일의 개수

for right in range(n):  # 오른쪽 끝 인덱스를 0부터 n-1까지 이동하며 반복
    if arr[right] in count:  # 현재 과일이 이미 count에 있는 경우
        count[arr[right]] += 1  # 해당 과일의 개수 증가
    else:  # 현재 과일이 count에 없는 경우
        count[arr[right]] = 1  # 해당 과일의 개수를 1로 초기화
        kind += 1  # 서로 다른 과일의 개수 증가
    
    while kind > 2:  # 서로 다른 과일의 개수가 2보다 큰 동안 반복
        count[arr[left]] -= 1  # 왼쪽 끝 과일의 개수 감소
        if count[arr[left]] == 0:  # 해당 과일의 개수가 0이 되면
            del count[arr[left]]  # count에서 해당 과일 제거
            kind -= 1  # 서로 다른 과일의 개수 감소
        left += 1  # 왼쪽 끝 인덱스 오른쪽으로 이동
    answer = max(answer, right - left + 1) # 현재 길이, 최대 길이 중 최댓값으로 갱신
print(answer)