# Q_1 : make a list which has elements is multiplied odd numbers by 2 from a range.

# without list comprehension method
answer = []
for n in range(1, 10):
    if n % 2 == 1:
        answer.append(n * 2)
print(answer)

# by list comprehension method
answer = [n * 2 for n in range(1, 10) if n % 2 == 1]
print(answer)

# Q_1 : make a list which has elements is multiplied odd numbers by 2 from the given dictionary.

# given dictionary
original = {1: 'odd',
            2: 'even',
            3: 'odd',
            4: 'even',
            5: 'odd',
            6: 'even',
            7: 'odd',
            8: 'even',
            9: 'odd',
            10: 'even'}

# without dictionary comprehension
answer = {}
for key, val in original.items():
    if val == 'odd':
        answer[key * 2] = 'even'
print(answer)

# initialize the answer
del answer

# with dictionary comprehension
answer = {key * 2: 'even' for key, val in original.items() if val == 'odd'}
print(answer)
