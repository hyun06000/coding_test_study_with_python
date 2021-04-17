# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    if len(S) == 0:
        return 1
    elif len(S) == 1:
        return 0

    brakets = {")": "(",
               "}": "{",
               "]": "["}
    if S[0] in brakets:
        return 0
    stack = []
    for char in S:
        if char in brakets:
            if stack and brakets[char] == stack[-1]:
                stack.pop()
            else:  # if stack is empty
                return 0
        else:
            stack.append(char)

    if stack:
        return 0
    else:
        return 1

    # simpler code ( Korean Book : Python algorithm interview )
    # for char in S:
    #     if char not in brakets:
    #         stack.append(char)
    #     elif not stack and brakets[char] != stack.pop():
    #         return 0
    # return len(stack) == 0