from collections import defaultdict

glasses, n = [], int(input())
for i in range(n):
    glasses.append(int(input()))

neighbor = 3
glasses += [0] * (neighbor -1)

dp = defaultdict(int)
for i in range(n):
    if i < neighbor - 1:
        dp[i] = dp[i-1] + glasses[i]
    else:
        for k in range(neighbor):
            win_index = i - neighbor + k
            case = dp[win_index] + sum(glasses[win_index+2 : i+1])
            dp[i] = max(dp[i], case)

print(dp[i])

'''
recursion depth error

glasses, n = [], int(input())
for i in range(n):
    glasses.append([int(input()), i])

max_v = []
def dfs(glasses, v, pre_i, visited=0, cum=1):
    if not glasses:
        return max_v.append(visited)

    if cum >= 3:
        cum = 0
    else:
        visited += v

    while glasses:
        w, i = glasses.pop(0)
        dfs(glasses, w, i, visited, cum + i - pre_i)

while glasses:
    w, i = glasses.pop(0)
    dfs(glasses, w, i)
print(max(max_v))
'''







'''
glasses, n = [], int(input())
for i in range(n):
    glasses.append([int(input()), i])

max_v = []
def dfs(glasses, v, pre_i, visited=0, cum=1):
    if not glasses:
        return max_v.append(visited)

    if cum >= 3:
        cum = 0
    else:
        visited += v

    while glasses:
        w, i = glasses.pop(0)
        dfs(glasses, w, i, visited, cum + i - pre_i)

while glasses:
    w, i = glasses.pop(0)
    dfs(glasses, w, i)
print(max(max_v))
'''