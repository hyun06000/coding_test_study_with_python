N = int(input())

plate = [[' ']*N for _ in range(N)]

def stars(i, j, length, no_mark):
    global plate
    if no_mark:
        return

    if length > 1:
        _len = length // 3
        for p in range(3):
            for q in range(3):
                stars(i + p * _len,j + q * _len, _len, p == 1 and q == 1)
    else:
        plate[i][j] = '*'

stars(0,0,N,False)

for row in plate:
    print(''.join(row))