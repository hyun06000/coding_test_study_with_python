### 백준
### 1920번
### 수 찾기

### 문제 링크
# https://www.acmicpc.net/problem/1920

import sys

readline = sys.stdin.readline

N = int(readline().strip())
A = list(map(int, readline().strip().split(" ")))

M = int(readline().strip())
B = list(map(int, readline().strip().split(" ")))

A.sort()
for b in B:
    exist = False
    l_p, r_p = 0, N - 1
    while r_p >= l_p:
        m_p = (r_p - l_p)//2 + l_p
        if A[m_p] == b:
            exist = True
            break
        elif A[m_p] > b:
            r_p = m_p - 1
        elif A[m_p] < b:
            l_p = m_p + 1

    answer = 1 if exist else 0
    print(answer)
