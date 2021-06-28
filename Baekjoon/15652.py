N, M = map(int, input().split(" "))

def dfs(v, series = []):

    series.append(v)

    if len(series) == M:
        print(' '.join(map(str,series)))
        return

    for w in range(1, N + 1):
        if w >= series[-1]:
            dfs(w, series[:])
    return

for i in range(1, N + 1):
    dfs(i, [])
