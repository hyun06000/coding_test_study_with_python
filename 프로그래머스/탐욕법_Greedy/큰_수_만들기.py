def solution(number, k):
    deleted, p_l, p_r = set(), 0, 1
    while len(deleted) < k and p_r < len(number):
        if p_l < 0 or number[p_l] >= number[p_r]:
            p_l = p_r
            p_r = p_l + 1
        else:
            deleted.add(p_l)
            p_l -= 1

    for d in sorted(deleted, reverse=True):
        number = number[:d] + number[d + 1:]

    if len(deleted) < k:
        return number[:-(k - len(deleted))]
    return number