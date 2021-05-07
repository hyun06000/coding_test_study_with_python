from collections import defaultdict

def solution(n, lost, reserve):
    students = defaultdict(int)
    for i in range(n):
        students[i] = 1
        if i + 1 in lost:
            students[i] -= 1
        if i + 1 in reserve:
            students[i] += 1

    for i in range(n):
        if not students[i]:
            if students[i - 1] == 2:
                students[i - 1] -= 1
                students[i] += 1
            elif students[i + 1] == 2:
                students[i + 1] -= 1
                students[i] += 1

    answer = 0
    for i in range(n):
        if students[i]:
            answer += 1
    return answer