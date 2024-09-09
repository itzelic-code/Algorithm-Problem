from functools import cmp_to_key

def compare(x, y):
	if x + y > y + x:
		return -1
	elif x + y < y + x:
		return 1
	else:
		return 0
		
def solution(numbers):
    str_num = list(map(str, numbers))
    str_num.sort(key = cmp_to_key(compare))
    answer = ''.join(str_num)
  
    return answer if answer[0] != '0' else '0'