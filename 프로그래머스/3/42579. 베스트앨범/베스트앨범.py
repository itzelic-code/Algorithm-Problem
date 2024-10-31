def solution(genres, plays):
    answer = []
    total_plays = {}  # {장르: 총 재생 횟수}
    genre_songs = {}  # {장르: [(플레이 횟수, 고유번호)]}

    # 각 곡의 장르와 재생 횟수 기반 해시 테이블 생성
    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]
        total_plays[genre] = total_plays.get(genre, 0) + play_count
        genre_songs[genre] = genre_songs.get(genre, []) + [(play_count, i)]

    # 1번 조건) 재생 횟수 내림차순으로 장르별 정렬
    sorted_genres = sorted(total_plays.items(),
                           key=lambda x: x[1],
                           reverse=True)

    for genre, _ in sorted_genres:
        # 2, 3번 조건) 해당 장르의 곡들을 재생 횟수 내림차순, 인덱스 오름차순으로 정렬
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        # 상위 두 곡 인덱스를 결과 리스트에 추가
        answer += [idx for _, idx in sorted_songs[:2]]

    return answer