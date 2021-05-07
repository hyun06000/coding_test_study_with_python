from collections import defaultdict


def solution(clothes):
    clo_dict = defaultdict(list)

    for c in clothes:
        clo_dict[c[1]].append(c[0])

    answer = 1
    for key in clo_dict:
        answer *= len(clo_dict[key]) + 1

    answer -= 1

    return answer