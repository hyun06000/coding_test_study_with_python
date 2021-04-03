# list

# length of list
# [ O(1) ]
a = [0, 1, 2, 3, 4, 5]
print(len(a))

# i-th element
# [ O(1) ]
print(a[3])

# from i-th to j th elements
# [ O(k) if j - i = k ]
print(a[2:4])

# searching an element is in the list a
# [ O(n) if n = len(a) ]
print(7 in a)
print(3 in a)

# the number of the specific element
# [ O(n) ]
b = [0, 0, 1, 0, 1, 2, 0, 3, 4, 5]
print(b.count(0))

# the first index of the specific element
# [ O(n) ]
print(b.index(0))
print(b.index(1))

# appending an element at the end of a list
# [ O(1) ]
a.append(7)
print(a)

# picking up and deleting the last element (stack operation)
# [ O(1) ]
print(a.pop())

# picking up and deleting the first element (Queue operation)
# [ O(n) ]
print(a.pop(0))

# picking up and deleting the i-th element (Queue operation)
# [ O(n) ]
print(a.pop(3))

# deleting the i-th element
# [ O(n) ]
del a[0]
print(a)

# sorting a list (Timsort algorithm)
# [ O(n) or O(n log n) ]
b.sort()
print(b)

# searching the minimum or maximum value
# [ O(n) ]
d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(d))
print(max(d))

# reversing all index of elements
# [ O(n) ]
d.reverse()
print(d)