N = int(input())
char_separators = set(input().split())

M = int(input())
digit_separators = set(input().split())

K = int(input())
mergers = set(input().split())

S = int(input())
base_string = input()

effective_separators = (char_separators | digit_separators | {' '}) - mergers
result = []
token = ''

for ch in base_string:
    if ch in effective_separators:
        if token:
            result.append(token)
            token = ''
    else:
        token += ch

if token:
    result.append(token)

for s in result:
    print(s)