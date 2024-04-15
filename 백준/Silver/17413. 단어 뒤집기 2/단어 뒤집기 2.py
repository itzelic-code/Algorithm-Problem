s = input()
stack = []
tag = False

for char in s:
    if char == '<':
        while stack:
            print(stack.pop(), end='')
        print(char, end='')
        tag = True
    elif char == '>':
        print(char, end='')
        tag = False
    elif tag:
        print(char, end='')
    else:
        if char == ' ':
            while stack:
                print(stack.pop(), end='')
            print(char, end='')
        else:
            stack.append(char)

while stack:
    print(stack.pop(), end='')