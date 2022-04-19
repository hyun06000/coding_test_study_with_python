### 3048 백준 개미

import sys

input = sys.stdin.readline

n_1, n_2 = list(map(int, input().strip().split(" ")))

groups = {
    0: [ant for ant in input().strip()][::-1],
    1: [ant for ant in input().strip()],
}
T = int(input().strip())

ant_line = []
for i in range(n_1):
    ant_line.append((0,i))

for i in range(n_2):
    ant_line.append((1,i))

while T:
    l, r = 0, 1
    while r < len(ant_line):
        if ant_line[l][0] < ant_line[r][0]:
            ant_line[l], ant_line[r] = ant_line[r], ant_line[l]
            l, r = r + 1, r + 2
        else:
            l, r = l + 1, r + 1
    T -= 1

final_state = []
for group_idx, ant_idx in ant_line:
    final_state.append(groups[group_idx][ant_idx])
print(''.join(final_state))
