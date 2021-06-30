# 공유기 설치
import sys
N, C = map(int, input().split(" "))

houses = []
# for _ in range(N):
#     houses.append(int(input()))
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

min_dist, max_dist = 1, houses[-1] - houses[0]
routers = 0
while min_dist <= max_dist:
    pivot = (min_dist + max_dist) // 2

    routers = 1
    pre_house = houses[0]
    for post_house in houses[1:] :
        if post_house - pre_house >= pivot:
            routers += 1
            pre_house = post_house

    if routers >= C:
        ans = pivot
        min_dist = pivot + 1

    elif routers < C:
        max_dist = pivot - 1

print(ans)