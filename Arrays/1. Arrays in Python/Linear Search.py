print("hello world form PyCharm and Python!")

array = [10, 42, 55, 2, 1, 0, 10, 42, 55, -57, 1, 0, 10, 42, 55, 2, 1, 0, 10, 42, 55, 2, 1, 0, 10, 42, 55, 2, 1, 0, 10,
         42, 55, 2, 1, 0, 10, 42, 55, 2, 1, 0, 10, 4002, 55, 2, 1, 0, 10, 42, 55, 2, 1, 0, 10, 42, 55, 2, 1, 0, 10, 42]

# this is called linear search O(N)

biggestNum = array[0]
smallestNum = array[0]

for num in array:
    if num > biggestNum:
        biggestNum = num

for num in array:
    if num < smallestNum:
        smallestNum = num

print(biggestNum)
print(smallestNum)

# array = sorted(array)
# biggestNum = array[-1]
# smallestNum = array[0]
# print(biggestNum)
# print(smallestNum)
