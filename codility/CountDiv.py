# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    len_AB = B + 1 - A

    if len_AB < K:
        for n in range(A, B + 1):
            if n % K == 0:
                return 1

    div, mod = divmod(len_AB, K)
    # last chunk
    for n in range(A + div * K, B + 1):
        if n % K == 0:
            return div + 1
    return div