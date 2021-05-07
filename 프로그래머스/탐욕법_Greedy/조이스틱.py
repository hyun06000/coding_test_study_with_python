import string
from collections import defaultdict, Counter

def solution(name):
    alphabet = defaultdict(int)
    for i, a in enumerate(string.ascii_uppercase):
        alphabet[a] = i

    counter = Counter(name)
    to_change = len(name) - counter["A"]
    if not to_change:
        return 0

    name = [char for char in name]

    stick = 0
    pointer = 0
    p_l = p_r = pointer
    while to_change:
        if name[p_r] != "A":
            pointer = (len(name) + p_r) % len(name)
        elif name[p_l] != "A":
            pointer = (len(name) + p_l) % len(name)

        if name[pointer] != "A":
            p_l = p_r = pointer
            up = alphabet[name[pointer]]
            down = i + 1 - up
            if up > down:
                stick += down
            else:
                stick += up
            name[pointer] = "A"
            to_change -= 1

        if p_l > -(len(name) - 1):
            p_l -= 1
        if p_r < len(name) - 1:
            p_r += 1
        stick += 1

    return stick - 1