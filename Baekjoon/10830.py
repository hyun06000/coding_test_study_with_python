# 백준
# 10830 번 행렬 제곱 문제 (골드 4)

def mat_mul(A, B, size):

    '''
    C_ik = sum(A_ij * B_jk)
    '''
    rtn = []
    for i in range(size):
        raw = []
        for k in range(size):
            a = 0
            for j in range(size):
                a += A[i][j] * B [j][k]
            raw.append(a % 1000)
        rtn.append(raw)
    
    return rtn

N, B = list(map(int, input().strip().split(" ")))

matrix = []
for _ in range(N):
    raw = list(map(int, input().strip().split(" ")))
    matrix.append(raw)

exp_list, exp = [[1, matrix]], 1
while exp <= B:
    exp *= 2
    matrix = mat_mul(matrix, matrix, N)
    exp_list.append([exp, matrix])
exp_list.reverse()

I = []
for i in range(N):
    I_raw = []
    for j in range(N):
        if i == j:
            I_raw.append(1)
        else:
            I_raw.append(0)
    I.append(I_raw)

answer = I
for e, m in exp_list:
    while B - e >= 0:
        answer = mat_mul(answer, m, N)
        B -= e

for a in answer:
    print(" ".join(list(map(str,a))))
