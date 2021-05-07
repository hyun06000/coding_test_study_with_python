def solution(prices):
    answer, stack = [0] * len(prices), []
    for i, p in enumerate(prices):
        while stack and stack[-1][0] > p:
            past_i = stack.pop()[1]
            answer[past_i] = i - past_i
        stack.append([p, i])

    while stack:
        past_i = stack.pop()[1]
        answer[past_i] = i - past_i

    return answer