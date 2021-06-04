# generator

# Q_1 : print the number form 1 to 100 with a generator
def get_accumulated_number():
    # initialize
    n = 0
    while True:
        n += 1
        yield n


gen_num = get_accumulated_number()
for _ in range(1, 100 + 1):
    print(next(gen_num))


# q_2 : print 3 different types of variables with a single generator, for example int, bool, string.
def diff_type_generator():
    yield int(1)
    yield True
    yield 'hello'


dtg = diff_type_generator()
print(type(next(dtg)))
print(type(next(dtg)))
print(type(next(dtg)))


# range() generator
list_many_num = [n for n in range(1000000)]
gen_many_num = range(1000000)

print(len(list_many_num) == len(gen_many_num))

# comparison
import sys
print(sys.getsizeof(list_many_num))
print(sys.getsizeof(gen_many_num))

import time
tic = time.time()
[n for n in range(1000000)]
toc = time.time()
print(toc-tic)

tic = time.time()
range(1000000)
toc = time.time()
print(toc-tic)
