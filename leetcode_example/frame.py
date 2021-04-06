# frame.py

# 1
class Solution:
    def __init__(self,n):
        print("### Solution {}".format(n))

    def answer_method(self):
        pass

    def checker(self, inputs, labels):
        count_cor = 0
        for i in range(len(inputs)):

            ans = self.answer_method(inputs[i])

            if ans == labels[i]:
                print('case_{} : correct answer'.format(i))
                count_cor += 1
            else:
                print('case_{} : incorrect answer'.format(i))
        print('score : {}/{}'.format(count_cor,len(inputs)))



''' use it
from frame import Solution as frame

inputs = []
labels = []

# 1
class Solution(frame):
    def answer_method(self) -> :
'''