sum_odds = 0
min_odd = 1501

for _ in range(7):
	n = int(input())
	if n % 2 != 0:
		sum_odds += n
		if min_odd > n:
			min_odd = n

if min_odd == 1501:
	print(-1)
else:
	print(sum_odds)
	print(min_odd)