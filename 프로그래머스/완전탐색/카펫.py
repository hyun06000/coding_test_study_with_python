def solution(brown, yellow):
    def shell(v, h):
        return (v * 2 + h * 2 + 4)

    v, h = 0, yellow
    while v <= h:
        v += 1
        h = yellow / v
        if shell(v, h) == brown:
            return [h + 2, v + 2]