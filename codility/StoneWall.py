# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    if len(H) == 1:
        return 1

    stack = [0]
    stones = 0
    for height in H:
        while stack[-1] > height:
            stack.pop()
        if stack[-1] == height:
            continue
        elif stack[-1] < height:
            stones += 1
            stack.append(height)

    return stones