from collections import defaultdict

memo = defaultdict(int)

def w(a, b, c):
    global memo

    abc = "a{}b{}c{}".format(a, b, c)
    if memo[abc]:
        return memo[abc]
    elif a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b < c:
        memo[abc] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return memo[abc]
    else:
        memo[abc] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return memo[abc]

while True:
    a, b, c = map(int, input().split(" "))
    if a == -1 and b == -1 and c == -1:
        break

    template = "w({}, {}, {}) = {}"
    print(template.format(a, b, c, w(a, b, c)))

