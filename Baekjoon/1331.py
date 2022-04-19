import sys

input = sys.stdin.readline

def reach(position):
    x = ord(position[0])
    y = int(position[1])

    possible = [
        [x-2,y-1], [x-2,y+1], [x-1,y-2], [x-1,y+2],
        [x+1,y-2], [x+1,y+2], [x+2,y-1], [x+2,y+1],
    ]
    rtn = []
    for p in possible:
        rtn.append(
            chr(p[0]) + str(p[1])
        )
    return rtn

def solution():
    path = []
    invalid = False
    for _ in range(6*6):
        pos = input().strip()
        if pos in path:
            invalid = True
            
        path.append(pos)
        
    if invalid  or ( len(path) != 6*6 ):
        print("Invalid")
        return
    
    now_pos = path[0]
    for next_pos in path[1:] + path[:1]:
        if next_pos not in reach(now_pos):
            print("Invalid")
            return
        now_pos = next_pos
    
    print("Valid")
    return

solution()