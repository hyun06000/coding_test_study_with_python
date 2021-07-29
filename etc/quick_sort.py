### beakjoon 2751
import sys
sys.setrecursionlimit(100000)

N = int(input())
inputs = [int(sys.stdin.readline()) for _ in range(N)]

def quick_sort(p_left, p_right):
    global inputs
    if p_left >= p_right:
        return

    pivot = inputs[(p_left + p_right)//2]
    i, j = p_left, p_right
    while i < j:
        while inputs[i] < pivot:
            i += 1
        while inputs[j] > pivot:
            j -= 1
        if i <= j:
            inputs[i], inputs[j] = inputs[j], inputs[i]
            i += 1
            j -= 1

    quick_sort(p_left, j)
    quick_sort(i, p_right)

quick_sort(0, N - 1)
for i in inputs:
    print(i)