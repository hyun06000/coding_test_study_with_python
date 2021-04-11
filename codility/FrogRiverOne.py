# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(X, A):
    # write your code in Python 3.6
    count = collections.defaultdict(int)

    for i, n in enumerate(A):
        count[n] = i
        if len(count) == X:
            return i

    return -1