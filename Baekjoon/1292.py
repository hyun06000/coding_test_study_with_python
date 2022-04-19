### 백준
### 1292번
### 쉽게 푸는 문제

### 문제 링크
# https://www.acmicpc.net/problem/1292

import sys

readline = sys.stdin.readline

A, B = list(map(int, readline().strip().split(" ")))

prefix, prefix_sum = 0, [0]
i, n, c = 0, 1, 0
while i < B:
    if c == n:
        c = 0
        n += 1
    prefix += n
    prefix_sum.append(prefix)
    i += 1
    c += 1

print(prefix_sum[B] - prefix_sum[A-1])
