import sys
from collections import deque

input = sys.stdin.read
queue = deque()

commands = input().splitlines()

for command in commands:
    if command.startswith("push"):
        _, value = command.split()
        queue.append(value)
    elif command == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)