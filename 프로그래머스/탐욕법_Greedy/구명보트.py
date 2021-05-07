from collections import deque


def solution(people, limit):
    people = deque(sorted(people))

    boat = 0
    while people:
        light, heavy = people.popleft(), people.pop()

        if light + heavy > limit:
            boat += 1
            people.appendleft(light)
        else:
            boat += 1

        if len(people) == 1:
            people.pop()
            boat += 1
    return boat