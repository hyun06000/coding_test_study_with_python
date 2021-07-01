import sys

<<<<<<< HEAD
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
=======
N, C = map(int, (input().split()))
house = [int(sys.stdin.readline()) for _ in range(N)]


# 해당 거리를 유지하며 공유기가 몇 개 설치될 수 있는가?
def router_counter(distance):
    count = 1
    cur_house = house[0]  # 시작점
    for i in range(1, N):  # 집모두를 돈다
        if cur_house + distance <= house[i]:  # 이전 집에서 해당 거리보다 멀리 떨어진 집이라면
            count += 1
            cur_house = house[i]  # 공유기 설치된 집 갱신
    return count


house = sorted(house)  # 이분탐색을 위한 정렬
start, end = 1, house[-1] - house[0]  # 1, 첫집과 끝집

while start <= end:  # 이분탐색 알고리즘
    mid = (start + end) // 2

    if router_counter(mid) >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
>>>>>>> 8caf0a00b7811729a0bb62fd33338f040a69a11e

print(answer)