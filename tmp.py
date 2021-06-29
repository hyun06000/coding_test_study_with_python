from collections import deque

R, C = map(int, input().split(" "))

board =[]
for _ in range(R):
    board.append(input())

di_dj = [(1, 0), (0, 1), (-1, 0), (0, -1)]

max_len = 0
queue = deque([(0, 0, board[0][0])])
while queue:
    i, j, visited = queue.popleft()
    max_len = max(max_len, len(visited) )
    for di, dj in di_dj:
        _i, _j = i + di, j + dj
        if 0 <= _i < R and \
            0 <= _j < C and \
            not board[_i][_j] in visited:
            queue.append((_i, _j, visited + board[_i][_j]))

print(max_len)