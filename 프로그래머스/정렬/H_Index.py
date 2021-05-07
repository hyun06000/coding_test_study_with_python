def solution(citations):
    citations.sort()
    l = len(citations)
    h = 0
    while h <= citations[-1]:
        count = 0
        for i, cite in enumerate(citations):
            if cite >= h:
                count += 1
        if count >= h:
            H = h
        h += 1

    return H