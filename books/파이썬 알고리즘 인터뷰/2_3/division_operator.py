# division operators in python

# '/' -> return high precision (float)
print('/')
print(6 / 3)
print(5 / 3)
print(5.1 / 3)
print(5 / 3.1)
print(5.1 / 3.1)

# '//' -> return highest precision of args with lowering function
print('//')
print(5 // 3)
print(5.1 // 3)
print(5 // 3.1)
print(5.1 // 3.1)

# '%' -> return modulus with highest precision args with lowering function
print('%')
print(((5 / 2) - (5 // 2)) * 2)
print(5 % 2)
print(5.0 % 2)
print(5 % 2.0)
print(5.0 % 2.0)

# 'divmod()' -> return a tuple (div, mod) with highest precision args with lowering function
print('divmod()')
print(divmod(5  , 2  ))
print(divmod(5.0, 2  ))
print(divmod(5  , 2.0))
print(divmod(5.0, 2.0))
