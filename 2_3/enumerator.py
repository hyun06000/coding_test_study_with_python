# enumerator

list_to_count = [1, 1, 11, 111, 11, 1111, 1, 1, 1, 111, 1, 1, 1, 1, 3, 3, 3, 2, 2, 2, 44, 2]

# Q_1 : print the each element with it's index

# method 1
for i in range(len(list_to_count)):
    print(i, list_to_count[i])

# method 2
i = 0
for ele in list_to_count:
    print(i, ele)
    i += 1

# method 3
for i, ele in enumerate(list_to_count):
    print(i, ele)