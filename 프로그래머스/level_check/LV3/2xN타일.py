def solution(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = (a + b) % 1000000007, a
    return a
