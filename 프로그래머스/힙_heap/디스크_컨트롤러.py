from heapq import heappop, heappush, heapify


def solution(jobs):
    num_jobs = len(jobs)
    if num_jobs == 1:
        return jobs[0][1]

    heapify(jobs)
    pq = []
    cur_pointer, processing = 0, 0

    while jobs or pq:
        if jobs and not pq:
            start, take = heappop(jobs)
            heappush(pq, [take, start])

        take, start = heappop(pq)
        if start > cur_pointer:
            cur_pointer += 1
            heappush(pq, [take, start])
        else:
            cur_pointer += take
            processing += cur_pointer - start
            while jobs and jobs[0][0] <= cur_pointer:
                start, take = heappop(jobs)
                heappush(pq, [take, start])

    return processing // num_jobs