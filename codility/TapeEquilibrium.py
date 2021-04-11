# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys


def solution(A):
    # write your code in Python 3.6
    left, right = 0, sum(A)

    min_dist = sys.maxsize
    for n in A[:-1]:
        left, right = left + n, right - n
        min_dist = min(min_dist, abs(left - right))

    return min_dist