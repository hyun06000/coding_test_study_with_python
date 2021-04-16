# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    if len(S) == 0:
        return 1
    elif len(S) == 1 or S[0] == ")":
        return 0

    stack = []
    for char in S:
        if char == "(":
            stack.append(char)
        else:  # char == ")"
            if stack:
                stack.pop()
            else:
                return 0

    if stack:
        return 0
    else:
        return 1