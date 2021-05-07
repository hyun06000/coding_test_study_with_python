def solution(n, costs):
    # sort with cost
    costs.sort(key=lambda x: x[2])
    visited = set([costs[0][0]])

    total_cost, count = 0, 0
    while len(visited) < n:
        for i, cost in enumerate(costs):
            # if cyclic
            if cost[0] in visited and cost[1] in visited:
                continue
            # if not cyclic graph but edge can start
            if cost[0] in visited or cost[1] in visited:
                visited.add(cost[0])
                visited.add(cost[1])

                costs[i] = [-1, -1, -1]
                total_cost += cost[2]
                break

    return total_cost