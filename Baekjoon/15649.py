N, M = map(int, input().split(' '))

integers = [n+1 for n in range(N)]

def dfs(v, visited = []):
    global integers

    visited.append(v)

    if len(visited) == M:
        print(' '.join(map(str, visited)))
        return

    for w in integers:
        if not w in visited:
            dfs(w, visited[:])
    return

for i in range(N):
    dfs(i+1, [])