# dictionary

a = dict()
a = {}


a = {'one': 1, 'two': 2, 'three': 3}

# length of a
# [ O(1) ]
print(len(a))

# search a value with a key
# [ O(1) ]
print(a['two'])

# insert a value with a key
# [ O(1) ]
a['seven'] = 7
print(a)

# check a dictionary has the key
# [ O(1) ]
print('five' in a)
print('seven' in a)

# try-exception
try:
    a['ten']
except KeyError:
    print('invalid key')

# for
for k, v in a.items():
    print(k, v)