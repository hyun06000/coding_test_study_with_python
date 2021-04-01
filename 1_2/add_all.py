# Add all from 1 to 10

# 1
summation = 0
for i in range(1,10+1):
    summation += i
print('#1 : ', summation)

#2
summation = sum(i for i in range(1,10+1))
print('#2 : ', summation)

#3
summation = sum(range(1,10+1))
print('#3 : ', summation)