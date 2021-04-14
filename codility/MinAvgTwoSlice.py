# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys


def solution(A):
    # write your code in Python 3.6
    two_index, two_min_avg = 0, sys.maxsize
    for i in range(len(A) - 1):
        avg = (A[i] + A[i + 1]) / 2
        if avg < two_min_avg:
            two_index, two_min_avg = i, avg

    three_index, three_min_avg = 0, sys.maxsize
    for i in range(len(A) - 2):
        avg = (A[i] + A[i + 1] + A[i + 2]) / 3
        if avg < three_min_avg:
            three_index, three_min_avg = i, avg

    if three_min_avg < two_min_avg:
        return three_index
    elif three_min_avg > two_min_avg:
        return two_index
    else:
        return min(two_index, three_index)