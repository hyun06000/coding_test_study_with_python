from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            graph[f] += [t]

        path = []

        def dfs(f):
            while graph[f]:
                dfs(graph[f].pop())
            path.append(f)

        dfs("JFK")

        return path[::-1]