# 백준 5430

# 구현문제다.
# 파이썬의 class의 특성을 살려서 구현해보도록 하겠다.
# getattr을 통해서 attr을 가져오고 실행하는 방식
# __call__을 통해서 callable 하게 다루는 방식
# __stㄱ__ 을 통해서 print 하는 방식
# 이렇게 구현하면 될 것이다.
# EOS

import re

class Solution:
    def __init__(self):
        pass
    
    def __call__(self, string):
        string = list(string)
        while string:
            if getattr(self, string.pop(0))():
                return True
    
    def set_arr(self, arr):
        self.arr = arr
    def R(self):
        if self.arr:
            self.arr.reverse()
    def D(self):
        if self.arr :
            self.arr.pop(0)
        else:
            return True

    def __str__(self):
        return ",".join(self.arr).join(["[","]"])
        

sol  = Solution()

for _ in range(int(input())):

    query = input()
    input()
    arr = re.sub("[\[\],]"," ",input()).strip()
    if arr:
        arr = arr.split(" ")
    sol.set_arr(arr)
    
    if sol(query):
        print("error")
    else:
        print(sol)