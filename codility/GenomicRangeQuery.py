# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    # you can write to stdout for debugging purposes, e.g.
    # print("this is a debug message")
    A, C, G, T = 0, 0, 0, 0

    cummulated = [[0, 0, 0, 0]]
    for char in S:
        if char == "A":
            A += 1
        elif char == "C":
            C += 1
        elif char == "G":
            G += 1
        elif char == "T":
            T += 1
        cummulated.append([A, C, G, T])

    i_f_table = {"A": 1, "C": 2, "G": 3, "T": 4}
    answer = []
    for p, q in zip(P, Q):
        left, right = cummulated[p], cummulated[q + 1]
        if left[0] != right[0]:
            answer.append(1)
        elif left[1] != right[1]:
            answer.append(2)
        elif left[2] != right[2]:
            answer.append(3)
        elif left[3] != right[3]:
            answer.append(4)
        else:
            answer.append(i_f_table[S[p]])
    return answer