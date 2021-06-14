from collections import deque

def infect(q, i, j, k):
    global boxes, zero_tomatos

    # 상자 밖으로 가면 중단
    if i >= H or j >= N or k >= M:
        return
    if i < 0 or j < 0 or k < 0:
        return

    if not boxes[i][j][k][1]:         # 방문 기록 없으면
        boxes[i][j][k][1] = True      # 방문 기록

        if not boxes[i][j][k][0]:     # 안익은 토마토
            boxes[i][j][k][0] = 1     # 상태 변화
            zero_tomatos -= 1         # 안익은 토마토 총량 감소
            q.append([i, j, k])       # 이제 익은 토마토니까 큐에 추가

        elif boxes[i][j][k][0] == 1:  # 익은 토마토
            q.append([i, j, k])       # 변화 없이 큐에 추가
        else:                         # 토마토 없음
            pass                      # 아무것도 하지마
    return


M, N, H = map(int, input().split(' '))

zero_tomatos = 0
one_tomatos = boxes = []
for h in range(H):
    box = []
    for n in range(N):
        row = []
        for m, tomato in enumerate(input().split(' ')):
            tomato = int(tomato)

            if not tomato: # 안익은 토마토
                zero_tomatos += 1 # 전체 상자의 안익은 토마토 갯수
                row.append([tomato, False]) # [토마토 상태, 방문 기록]
            elif tomato == 1: # 익은 토마토
                one_tomatos.append((h, n, m)) # 익은 토마토 위치
                row.append([tomato, True])
            else: # 토마토 없음
                row.append([tomato, False])
        box.append(row)
    boxes.append(box)

if not zero_tomatos: # 안익은 토마토 없음 -> 모든 토마토가 익은 경우
    print(0)

else:
    days = 0
    q = deque(one_tomatos)
    while q:
        q_len = len(q)
        for _ in range(q_len): # 그 전날에 감염된 애들만큼만 큐를 pop
            i, j, k = q.popleft()

            infect(q, i+1, j, k) # for 문으로 해도 좋다.
            infect(q, i, j+1, k)
            infect(q, i, j, k+1)

            infect(q, i-1, j, k)
            infect(q, i, j-1, k)
            infect(q, i, j, k-1)

        days += 1

    if zero_tomatos:  # 맨 처음 안익은 토마토 수 > 바뀐 토마토 수
        print(-1)     # -1 출력
    else:             # 아니면
        print(days-1) # q 가 비어있는지 while이 검사하도록 하루를 더 썼으므로 -1 해서 출력