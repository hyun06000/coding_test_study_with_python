def solution(n, times):
    max_time = max(times) * n
    l_p, r_p = 0, max_time
    answer = []
    while l_p <= r_p:
        m_p = (r_p - l_p)//2 + l_p
        ability = sum(list(map(lambda x : m_p//x, times)))
        if ability >= n:
            answer.append(m_p)
            r_p = m_p - 1
        else:
            l_p = m_p + 1

    return min(answer)

### m_p가 여러개 나오는 경우 찾을 것
### l_p == r_p 여야만 하는 경우도 찾을 것