from collections import defaultdict


def solution(genres, plays):
    gen_counter = defaultdict(int)
    g_pi_dict = defaultdict(list)
    for i, gp in enumerate(zip(genres, plays)):
        g, p = gp
        gen_counter[g] += p
        g_pi_dict[g].append([p, i])

    sorted_gen_list = sorted(gen_counter,
                             key=lambda x: gen_counter[x],
                             reverse=True)
    answer = []
    for gen in sorted_gen_list:
        sorted_pi = sorted(g_pi_dict[gen],
                           key=lambda x: x[0],
                           reverse=True)
        for pi in sorted_pi[:2]:
            answer.append(pi[1])

    return answer