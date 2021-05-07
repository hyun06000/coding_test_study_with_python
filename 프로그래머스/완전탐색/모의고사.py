def solution(answers):
    l = len(answers)
    student_1 = [n % 5 + 1 for n in range(l)]
    seed = [2, 1, 2, 3, 2, 4, 2, 5]
    student_2 = [seed[n % 8] for n in range(l)]
    student_3 = []
    while len(student_3) < l:
        student_3 += [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    student_3 = student_3[:l]

    score_1, score_2, score_3 = 0, 0, 0
    for i, ans in enumerate(answers):
        if student_1[i] == ans:
            score_1 += 1
        if student_2[i] == ans:
            score_2 += 1
        if student_3[i] == ans:
            score_3 += 1
    max_score = max(score_1, score_2, score_3)

    out = []
    if max_score == score_1:
        out.append(1)
    if max_score == score_2:
        out.append(2)
    if max_score == score_3:
        out.append(3)

    return out