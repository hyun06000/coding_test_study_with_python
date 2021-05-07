import itertools

def solution(numbers):
    answer = set()
    for r in range(len(numbers)):
        for i in itertools.permutations(numbers, r + 1):
            n = int(''.join(i))
            if n > 1:
                prime = True
                for p in range(2, n):
                    if not n % p:
                        prime = False
                        break
                if prime:
                    answer.add(n)

    return len(answer)