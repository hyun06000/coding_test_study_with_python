from collections import defaultdict


def solution(numbers, target):
    g = defaultdict(list)
    for i, n in enumerate(numbers):
        g[i] += [n, -n]

    result = []

    def dfs(i=0, summ=0):
        if i == len(numbers):
            result.append(summ)
            return

        for w in g[i]:
            dfs(i + 1, summ + w)

    dfs()
    answer = 0
    for r in result:
        if not (r - target):
            answer += 1
    return answer