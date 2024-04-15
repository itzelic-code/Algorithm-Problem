from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    start, end = 0, n-1
    min_diff = float('inf')
    count = 0 
    
    while start < end:
        current_sum = numbers[start] + numbers[end]
        diff = abs(current_sum - k)
        
        if diff < min_diff:
            min_diff = diff
            count = 1
        elif diff == min_diff:
            count += 1
        
        if current_sum < k:
            start += 1
        else:
            end -= 1
    
    print(count)
