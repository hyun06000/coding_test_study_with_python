class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not n:
            return len(tasks)

        counter = collections.Counter(tasks)

        process = 0
        while counter:
            sub_count = 0

            # n + 1 = [a, b, c or idle]
            for t, _ in counter.most_common(n + 1):
                sub_count += 1
                process += 1

                counter[t] -= 1
                counter += collections.Counter()

            if counter:
                process += n - sub_count + 1  # idle

        return process  # last idel