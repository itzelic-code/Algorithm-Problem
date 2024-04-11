from sys import stdin
input = stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target: # 찾았을때 mid 인덱스 리턴
            return mid
        elif array[mid] > target: # 찾는 값이 더 작은 경우 왼쪽
            end = mid - 1
        else: # 찾는 값이 더 큰 경우 오른쪽으로
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('1', end=' ')
    else:
        print('0', end=' ')