def solution(A):
    # write your code in Python 3.6
    sub_arr_avg = []
    for i in range(len(A) - 1):  # O(N)
        sub_arr_avg.append((A[i] + A[i + 1]) / 2)

    min_avg = min(sub_arr_avg)
    return sub_arr_avg.index(min_avg)  # O(n)

A = [-3, -5, -8, -4, -10]
print(solution(A))