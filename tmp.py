import numpy as np

a = np.array([0, 1, 2, 3, 4])
b = np.array([2, 2, 2, 2, 2])

print(a * (a>=b))

import matplotlib
print(matplotlib.__version__)

a = True
print(not a)

b = []
print(b)
print(not b)

# caution!
print(b is False)
print(b == False)
