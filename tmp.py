key = [[1,0,1],
       [0,0,0],
       [1,0,1]]
M = len(key)

lock = [[0,1,0],
        [1,0,1],
        [0,1,0]]
N = len(lock)

#def solution(key, lock):
M = len(key)
N = len(lock)
def _print(A):
    input()
    for a in A:
        print(a)
def list_copy(double_list : list[list],
              i_range : tuple[int,int],
              j_range : tuple[int,int]) -> list[list]:
    result = []
    for i in range(*i_range):
        row = []
        for j in range(*j_range):
            row.append(double_list[i][j])
        result.append(row)
    return result

def rotate(key):
    _key = []
    for j in range(M):
        _row = []
        for i in range(len(key) - 1, -1, -1):
            _row.append(key[i][j])
        _key.append(_row)
    return _key

def pad(key, lock):
    pad_size = N + 2 * (M - 1)
    # "pad = [[0] * pad_size] * pad_size" is wrong !!!
    pad = [[0] * pad_size for _ in range(pad_size)]
    lock_start = (M - 1)
    for i in range(N):
        for j in range(N):
            pad[lock_start + i][lock_start + j] = \
                lock[i][j]
    return pad

def overlay(start_i, start_j, padded, key):
    _padded = list_copy(
        padded,
        (0, len(padded)),
        (0, len(padded))
    )
    for i in range(M):
        for j in range(M):
            _padded[start_i + i][start_j + j] += key[i][j]
    return _padded

def check(key_on_lock):
    answer = True
    _print(key_on_lock)
    for kol in key_on_lock:
        answer &= all(kol)

    return answer

def stride_and_check(padded, key):
    for i in range(len(padded) - (M - 1)):
        for j in range(len(padded) - (M - 1)):
            key_on_lock = overlay(i, j, padded, key)
            print(i,j)

            if check(
                    list_copy(
                        key_on_lock,
                        ((M - 1), (M - 1) + N),
                        ((M - 1), (M - 1) + N)
                    )
                ):
                return True
    return False

for _ in range(4):
    key = rotate(key)
    padded = pad(key, lock)
    stride_and_check(padded, key)
