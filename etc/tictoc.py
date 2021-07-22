import time as T
from collections import defaultdict

def tictoc(func):
    def wrapper(*arg,**kwarg):
        repeat = 10000

        tic = T.time()
        for _ in range(repeat):
            func(*arg,**kwarg)

        toc = T.time()
        print( (toc - tic) / repeat )
    return wrapper