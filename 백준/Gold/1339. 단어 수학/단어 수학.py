n = int(input())
words = [input().strip() for _ in range(n)]

alpha_weight = {}

for word in words:
    k = len(word) - 1
    for char in word:
        if char in alpha_weight:
            alpha_weight[char] += pow(10, k)
        else:
            alpha_weight[char] = pow(10, k)
        k -= 1

sorted_weight = sorted(alpha_weight.items(), key=lambda x: x[1], reverse=True)
num = 9
total = 0
for _, weight in sorted_weight:
    total += weight * num
    num -= 1

print(total)
