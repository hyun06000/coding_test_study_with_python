# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0

    edges = []
    for i, n in enumerate(A):
        left_edge, right_edge = i - n, i + n

        edges.append((left_edge, -1))  # "start_disc"
        edges.append((right_edge, +1))  # "end_disc"

    edges.sort()

    curr_disc_num, pairs = 0, 0
    for point in edges:
        if point[1] == -1:  # "start_disc"
            pairs += curr_disc_num
            curr_disc_num += 1
            if pairs > 1e7:
                return -1
        else:  # "end_disc"
            curr_disc_num -= 1

    return pairs