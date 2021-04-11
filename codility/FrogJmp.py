def solution(X, Y, D):
    # write your code in Python 3.6
    between = Y - X
    if not between:
        return 0

    div, mod = divmod(between,D)
    if not mod: # equal to
        return div
    else: # greater than
        return div +1