exp = input().split('-')
result = sum(map(int, exp[0].split('+')))
for e in exp[1:]:
    result -= sum(map(int, e.split('+')))
print(result)
