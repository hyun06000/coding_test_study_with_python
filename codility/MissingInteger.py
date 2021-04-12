# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections
import sys


def solution(A):
    # write your code in Python 3.6
    # 1. All elements is negative.
    if max(A) <= 0:
        return 1

    nums = [n for n in range(1, max(A) + 1 + 1)]
    counted = collections.Counter(A)
    for key in counted.keys():
        if key <= 0:
            continue
        else:
            nums[key - 1] = sys.maxsize

    return min(nums)