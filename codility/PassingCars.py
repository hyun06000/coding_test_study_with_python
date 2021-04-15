# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    cummulated, summ = [0], 0
    for n in A:
        summ += n
        cummulated.append(summ)

    passing_cars = 0
    for i, n in enumerate(A):
        if not n:
            passing_cars += summ - cummulated[i + 1]
            if passing_cars > 1e9:
                return -1
    return passing_cars