# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 1

    doubled = A + [n for n in range(1, len(A)+1 +1)]

    counted = collections.Counter(doubled)
    for key, val in counted.items():
        if val == 1:
            return key