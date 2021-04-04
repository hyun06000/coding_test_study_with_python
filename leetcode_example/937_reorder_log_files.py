from frame import Solution as frame

inputs = [["dig1 8 1 5 1",
           "let1 art can",
           "dig2 3 6",
           "let2 own kit dig",
           "let3 art zero"]]
labels = [["let1 art can",
           "let3 art zero",
           "let2 own kit dig",
           "dig1 8 1 5 1",
           "dig2 3 6"]]

# 1
class Solution(frame):
    def answer_method(self, strs : list[str]) -> list[str]:
        # separate logs into the let_logs and dig_logs.
        let_logs, dig_logs = [], []
        for log in strs:
            if log.split()[1].isdigit():
                dig_logs.append(log)
            elif log.split()[1].isalpha():
                let_logs.append(log)
            else:
                print('invalid log')

        # sort let_logs with the condition.
        let_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        # merge and return
        return let_logs+dig_logs

sol_1 = Solution()
sol_1.checker(inputs, labels)