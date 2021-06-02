def _print(A):
    for a in A:
        print(a)

N = 5
zeros = [[0] * N for _ in range(N)]

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

start_i = start_j = 1
for i in range(len(A)):
    for j in range(len(A[0])):
        zeros[start_i + i][start_j + j] = A[i][j]

_print(zeros)

