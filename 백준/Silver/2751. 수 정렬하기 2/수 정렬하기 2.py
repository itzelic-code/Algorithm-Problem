from sys import stdin
input = stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

print(" ".join(map(str, nums)))