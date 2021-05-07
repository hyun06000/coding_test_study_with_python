from collections import Counter

def solution(priorities, location):
    pri_counter = Counter(priorities)

    pri_loc_que = []
    for loc, pri in enumerate(priorities):
        pri_loc_que.append([pri, loc])

    indx = 1
    while pri_loc_que:
        cur_doc = pri_loc_que.pop(0)
        if max(pri_counter) == cur_doc[0]:
            if cur_doc[1] == location:
                return indx

            pri_counter[cur_doc[0]] -= 1
            if not pri_counter[cur_doc[0]]:
                del pri_counter[cur_doc[0]]

            indx += 1
        else:
            pri_loc_que.append(cur_doc)