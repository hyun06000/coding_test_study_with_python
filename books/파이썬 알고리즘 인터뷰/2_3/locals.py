# locals

import numpy as np
import pprint


# case of a function

def func():
    local_val = np.array([1, 2, 3])
    pprint.pprint(locals())

func()

# case of a class

class MyClass(object):
    def __init__(self):
        self.a = 100
        self.b = 'hi'
        self.c = True
        pprint.pprint(self.__dict__)

    def change_c(self):
        if self.c:
            self.c = False
        else:
            self.c = True
        pprint.pprint(self.__dict__)


a = MyClass()

a.change_c()

pprint.pprint(globals())
pprint.pprint(locals())
