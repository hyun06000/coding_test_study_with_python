# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections


def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        if A[0] == 1:
            return 1
        else:
            return 0

    counted = collections.Counter(A)
    if len(counted) == len(A):
        if sum(counted.values()) == max(A):
            return 1
        else:
            return 0
    else:
        return 0