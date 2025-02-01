input_time = int(input())

hours = input_time // 100
minutes = input_time % 100
total_minutes = hours * 60 + minutes

city_time_deltas = [
    ('Ottawa', 0),
    ('Victoria', -180),
    ('Edmonton', -120),
    ('Winnipeg', -60),
    ('Toronto', 0),
    ('Halifax', 60),
    ("St. John's", 90)
]

for city, delta in city_time_deltas:
    adjusted_minutes = (total_minutes + delta) % 1440  # 하루는 1440분이므로 모듈러 연산
    adjusted_hours = adjusted_minutes // 60
    adjusted_mins = adjusted_minutes % 60
    adjusted_time = adjusted_hours * 100 + adjusted_mins  # 시간을 다시 HHMM 형식으로 변환
    print(f"{int(adjusted_time)} in {city}")