### 백준 2749 피보나치 수
# https://www.acmicpc.net/problem/2749

import sys
n = int(sys.stdin.readline())

m = 10**6
p = 15*m//10

a_i, a_ii = 0, 1
for _ in range((n)%p-1):
    a_i, a_ii = a_ii, (a_i + a_ii)%m

print(a_ii)
