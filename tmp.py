class A:
    def tmp(self):
        pass
    def p(self):
        print(self.tmp())

class B(A):
    def tmp(self):
        return 'hi'


a = A()
a.p()

b = B()
b.p()
