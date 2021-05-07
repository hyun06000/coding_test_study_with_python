from collections import defaultdict, deque

def solution(tickets):
    graph = defaultdict(list)
    for frm, to in sorted(tickets):
        graph[frm] += [to]

    journey = []

    def dfs(frm):
        while graph[frm]:
            dfs(graph[frm].pop(0))
        journey.append(frm)

    dfs("ICN")

    return journey[::-1]