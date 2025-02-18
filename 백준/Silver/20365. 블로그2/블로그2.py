N = int(input())
colors = input().strip()
current_color = colors[0]
blue = 0  # 연속된 블록의 개수
red = 0 

if current_color == 'B':
    blue += 1
else:
    red += 1

for color in colors[1:]:
    if color != current_color:
        current_color = color
        if current_color == 'B':
            blue += 1
        else:
            red += 1

print(min(blue, red) + 1)