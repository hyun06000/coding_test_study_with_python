# list_2

# making a list
a = list()
b = []

# making a list with initialization
a = [0, 1, 2, 3, 4]

# inserting an element
a.insert(2, 7)
print(a)

# a list with vatiable types of elements
b = [1, 1.5]
b.append('hi')
b.append(True)
print(b)

# slicing with a step
c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(c[1:6:2])
print(c[::5])

# IndexError
# print(c[10]) -> IndexError: list index out of range

# try-exception
try:
    print(c[10])
except IndexError:
    print('invalid index')

# deleting
a = [0, 0, 2, 3, 5, 1, 0, 4, 6, 3]
# by index
del a[1]
print(a)
# by value (first index)
a.remove(0)
print(a)
# by index with return
a.pop(2)
print(a)
