### 백준 1780번
# 종이의 개수


import sys

N = int(sys.stdin.readline().strip())

paper = []
for _ in range(N):
    raw = sys.stdin.readline().strip().split(' ')
    paper.append(raw)
count = {'-1':0, '0':0, '1':0}

def check(i_start, i_end, j_start, j_end):
    num_set = set()
    for i in range(i_start, i_end):
        for j in range(j_start, j_end):
            num_set.add(paper[i][j])
    if len(num_set) == 1:
        return True
    return False

def tree(i_start, i_end, j_start, j_end):
    if i_start == i_end:
        return
    if check(i_start, i_end, j_start, j_end):
        count[paper[i_start][j_start]] += 1
    else:
        i_step = (i_end-i_start)//3
        j_step = (j_end-j_start)//3
        for m in range(3):
            for n in range(3):
                tree(
                    m*i_step+i_start, (m+1)*i_step+i_start,
                    n*j_step+j_start, (n+1)*j_step+j_start,
                )
                
tree(0, len(paper), 0, len(paper))
for k in count.values():
    print(k)
