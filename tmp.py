def rearrange(s):
    for i in range(-1, -len(s) - 1, -1):
        print(i)
        if s[i] == '0':
            print(s[:len(s)+(i+1)])
            return s[:len(s)+(i+1)] + '110' + s[len(s)+(i+1):]
    return '110' + s



print(rearrange('0111'))