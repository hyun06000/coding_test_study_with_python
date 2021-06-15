def solution(s):

    def extract(s):
        count, stack = 0, []
        for _s in s:
            if _s == '0' and stack[-2:] == ['1', '1']:
                stack.pop();
                stack.pop();
                count += 1
            else:
                stack.append(_s)
        return ''.join(stack), count

    def rearrange(s):
        for i in range(-1, -len(s) - 1, -1):
            pointer = len(s) + (i + 1)
            if s[i] == '0':
                return s[:pointer] + '110' + s[pointer:]
        return '110' + s

    answer = []
    for _s in s:
        _s, count = extract(_s)
        for _ in range(count):
            _s = rearrange(_s)
        answer.append(_s)
    return answer