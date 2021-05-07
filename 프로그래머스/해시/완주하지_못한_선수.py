from collections import defaultdict


def solution(participant, completion):
    name_dict = defaultdict(int)
    for par in participant:
        name_dict[par] += 1

    for com in completion:
        name_dict[com] -= 1

    for key, val in name_dict.items():
        if val:
            return key