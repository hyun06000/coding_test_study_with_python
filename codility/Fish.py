# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    if len(A) == 1:
        return 1

    stack = []
    upstream_alive = 0
    for a, b in zip(A, B):
        if b:
            stack.append(a)
        else:
            while stack and stack[-1] < a:
                stack.pop()

            if not stack:
                upstream_alive += 1

    return upstream_alive + len(stack)