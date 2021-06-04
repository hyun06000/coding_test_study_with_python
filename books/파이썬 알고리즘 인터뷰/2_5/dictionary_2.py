import collections

# defaultdict

a = collections.defaultdict(int)
a['one'] = 1
a['two'] = 2
a['three'] = 3
print(a)

print(a['zero'])
print(a['five'])

# Counter

b = ['a',
     'b', 'b',
     'c', 'c', 'c',
     'd', 'd', 'd', 'd',
     'e', 'e', 'e', 'e', 'e',
     'f', 'f', 'f', 'f', 'f', 'f']
c = collections.Counter(b)
print(c)
print(type(c))

print(c.most_common(3))

# OrderedDict

d = {'banana': 3, 'apple': 5, 'pear': 1}
e = collections.OrderedDict(d)
print(e)