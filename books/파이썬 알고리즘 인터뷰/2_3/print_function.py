# print function in python

# the default separator is a single space
print('A1', 'B1')

# 'sep' kwargs change the separator
print('A1', 'B2', sep=',')
print('A1', 'B2', sep='/')

# the default line separator is '\n'
print('A1', 'B1', sep='*')
print('C3', 'D4', sep='^')

# 'end' kwargs change the line separator
# ( carriage return is not working on windows )
print('A1', 'B1', sep='*', end=" ")
print('C3', 'D4', sep='^')
print('A7', 'G1', sep='*')

# ''.jion(a) print joined string in list A
a = ['foo', 'boo', 'buz']
print(''.join(a))

# '{}{}{}...'.format(a,b,...) makes formatting
print('{} is {}'.format('this', 'nice'))
print('{} > {}'.format(1, 0))
print('{0} > {2} > {1}'.format(12, 0, 7))

# f'' is formatted string
num = 128
fruit = 'apples'
print(f'{num*2} of {fruit}')