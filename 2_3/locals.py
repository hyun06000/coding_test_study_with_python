# locals

import numpy as np
import pprint


class MyClass():
    def __init__(self):
        self.a = 100
        self.b = 'hi'
        self.c = True
        pprint.pprint(locals())

    def change_c(self):
        if self.c:
            self.c = False
        else:
            self.c = True
        pprint.pprint(locals())


def func():
    local_val = np.array([1, 2, 3])
    pprint.pprint(locals())

a = MyClass()

a.change_c()

func()

pprint.pprint(locals())
