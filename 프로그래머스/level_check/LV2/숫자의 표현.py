def solution(n):
    cases = 0
    for start in range(1, n + 1):
        cumulated = 0
        for i in range(start, n+1):
            cumulated += i
            if cumulated > n:
                break
            elif cumulated == n:
                cases += 1
    return cases