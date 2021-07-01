import sys

N, C = map(int, input().split(' '))

houses = []
for _ in range(N):
    houses.append(int(sys.stdin.readline()))
houses.sort()

min_dist, max_dist = 1, houses[-1] - houses[0]
while min_dist <= max_dist:
    pivot = (max_dist + min_dist) // 2

    routers = 1
    pre_house = houses[0]
    for post_house in houses[1:]:
        if pivot <= post_house - pre_house:
            routers += 1
            pre_house = post_house

    if routers >= C:
        answer = pivot
        min_dist = pivot + 1
    else:
        max_dist = pivot - 1

print(answer)
