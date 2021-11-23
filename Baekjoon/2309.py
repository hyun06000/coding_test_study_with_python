'''
일곱 난쟁이 문제

'''
def get_heights(heights):
    for i in range(0,8):
        for j in range(i,9):
            imposter = ( heights[i] + heights[j] )
            if prefix - imposter == 100:
                del heights[j]
                del heights[i]
                return heights

import sys
input = sys.stdin.readline

prefix, heights = 0, []
for i in range(9):
    h = int(input())
    prefix += h
    heights.append(h)

heights.sort()
heights = get_heights(heights)
for rtn in heights:
    print(rtn)


