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

a = ['a', 'b', 'c']
print(a.sort())
# print(a.sorted()) error

b = "cghr"
# print(sort(b)) error
print(sorted(b))

print(sorted(a))