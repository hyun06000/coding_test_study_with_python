# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(N, A):
    # write your code in Python 3.6
    max_count = 0
    p_left = p_right = -1
    for i, n in enumerate(A):
        # max_count
        if n > N:
            p_left, p_right = p_right + 1, i

            # if first max_count is not the first element
            if A[p_left: p_right]:
                increase = collections.Counter(A[p_left: p_right])
                max_count += max(increase.values())

    if len(A) == p_right:
        return [max_count] * N
    else:
        count = [max_count] * N
        increase = collections.Counter(A[p_right + 1:])
        for key, val in increase.items():
            count[key - 1] += val
        return count