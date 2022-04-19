# 백준 1347 미로 만들기

import sys

input = sys.stdin.readline

n = int(input().strip())
path = input().strip()

F_move = {
    "S": [0, 1],
    "N": [0, -1],
    "E": [1, 0],
    "W": [-1, 0],
}

R_rot = {
    "S": "W",
    "W": "N",
    "N": "E",
    "E": "S"
}

L_rot = {
    "S": "E",
    "E": "N",
    "N": "W",
    "W": "S"
}

# init visited and pos
cur_pos, visited = [0, 0, "S"], [[0, 0]]

min_x, max_x = 0, 0
min_y, max_y = 0, 0
for p in path:
    if p == "F":
        cur_pos[0] += F_move[cur_pos[2]][0]
        cur_pos[1] += F_move[cur_pos[2]][1]
        visited.append(cur_pos[:-1])
        min_x, max_x = min(cur_pos[0], min_x), max(cur_pos[0], max_x)
        min_y, max_y = min(cur_pos[1], min_y), max(cur_pos[1], max_y)
    elif p == "R":
        cur_pos[2] = R_rot[cur_pos[2]]
    else: # p == "L"
        cur_pos[2] = L_rot[cur_pos[2]]

for y in range(min_y, max_y + 1):
    row_of_maze = ""
    for x in range(min_x, max_x + 1):
        if [x, y] in visited:
            row_of_maze += "."
        else:
            row_of_maze += "#"
    print(row_of_maze)