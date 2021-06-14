from collections import deque

def bfs(q, i, j, k):
    global boxes, zero_tomatos
    if i >= H or j >= N or k >= M:
        return
    if i < 0 or j < 0 or k < 0:
        return

    if not boxes[i][j][k][1]:
        boxes[i][j][k][1] = True

        if not boxes[i][j][k][0]:
            boxes[i][j][k][0] = 1
            zero_tomatos -= 1
            q.append([i, j, k])
        elif boxes[i][j][k][0] == 1:
            q.append([i, j, k])
        else:
            pass
    return


M, N, H = map(int, input().split(' '))

zero_tomatos = 0
one_tomatos = []
boxes = []
for h in range(H):
    box = []
    for n in range(N):
        row = []
        for m, tomato in enumerate(input().split(' ')):
            tomato = int(tomato)
            if not tomato:
                zero_tomatos += 1
                row.append([tomato, False])
            elif tomato == 1:
                one_tomatos.append((h, n, m))
                row.append([tomato, True])
            else:
                row.append([tomato, False])
        box.append(row)
    boxes.append(box)

if not zero_tomatos:
    print(0)
else:
    days = 0
    q = deque(one_tomatos)
    while q:
        q_len = len(q)
        for _ in range(q_len):
            i, j, k = q.popleft()

            bfs(q, i+1, j, k)
            bfs(q, i, j+1, k)
            bfs(q, i, j, k+1)

            bfs(q, i-1, j, k)
            bfs(q, i, j-1, k)
            bfs(q, i, j, k-1)

        days += 1

    if zero_tomatos:
        print(-1)
    else:
        print(days)
