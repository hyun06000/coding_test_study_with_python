def check(string):
    stack = []
    for char in string:
        if not stack:
            stack.append(char)
        else:
            if char == '(':
                stack.append(char)
            elif stack.pop() != '(':
                return False
    return len(stack) == 0

def u_proc(u):
    _u = u[1:-1]
    rtn, mapping = '', {'(':')',')':'('}
    for _c in _u:
        rtn += mapping[_c]
    return rtn

def solution(p):
    # 1
    if len(p) == 0:
        return ''
    #2
    left, right = 0, 0
    for i, char in enumerate(p):
        if char == '(':
            left += 1
        else:
            right += 1
        
        if right == left:
            break
    u, v = p[:i+1], p[i+1:]
    
    #3
    if check(u):
        answer = solution(v)
        return u + answer
    else:
        answer = '(' + solution(v) + ')' + u_proc(u)
        return answer

