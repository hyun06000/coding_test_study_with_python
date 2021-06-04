def solution(n, t, m, timetable):
    def M_to_HHMM(M):
        H, M = divmod(M, 60)
        return "{0:02d}:{1:02d}".format(H, M)

    M_table = []
    for tb in timetable:
        _tb = list(map(int, tb.split(":")))
        M_table.append(_tb[0] * 60 + _tb[1])
    M_table.sort()

    can_ride = []
    bus_M = 9 * 60
    for _ in range(n):
        _m = m  # 버스가 올때마다 자리가 새로 생긴다.
        while _m and M_table:
            head = M_table.pop(0)
            if head <= bus_M:
                _m -= 1
            else:
                M_table = [head] + M_table
                break

        if _m:  # 자리가 있고 사람이 없는 경우
            can_ride.append(min(bus_M + t - 1, 9 * 60 + t * (n - 1)))
        bus_M += t

    if not _m: # 마지막 버스에 사람이 모두 탄 경우
        return M_to_HHMM(head - 1) # 맨 마지막에 탄 사람보다만 일찍

    if can_ride:  # 자리가 있는 시간대가 있을 경우
        return M_to_HHMM(max(can_ride))  # 가능한 경우 중에서 가장 늦게

    else:  # 끝까지 기다려도 자리가 없는 경우
        return M_to_HHMM(head - 1)  # 맨 마지막에 탄 사람보다만 일찍