# number 2
def multiply(num):
    total = 1
    for x in num:
        total *= x
    return total
print(multiply((8, 3, 2, -1, 7)))

# number 1
def sum(num):
    total = 1
    for x in num:
        total += x
    return total
print(sum((8, 3, 2, -1, 7)))

# number 3
num = [1,7,9]
max_num = max(num)
print(f"The maximum number is {max_num}")

# number 4
num = [1,7,9]
min_num = min(num)
print(f"The maximum number is {min_num}")

# number 7
list_re = [1,6,8,9,4,4,7,3,6,2,1,1,7,6,9]
print(list(set(list_re)))

# number 8
list = input("Enter a list: ")
if list == []:
    print("The list is empty")
else:
    print("It's not empty")

# number 9
original = ["a", "b", "c"]
cloned = original
print("Original list is:", original)
print("Clone list is:", cloned)

# number 11
list1 = input("Enter the first list: ")
list2 = input("Enter the second list: ")
def common_member(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
            else:
                result = False
                return result
print(common_member(list1, list2))

# number 15
from random import shuffle
names = ['cynthia', 'maria', 'nelly', 'comfy', 'cissy', 'faith']
shuffle(names)
print(names)

# number 20
char = ['a', 'b', 'c', 'd']
string = ''.join(char)
print(string)

# dictionaries
# number 2
d = {1: "a", 2: "b"}
print(d)
d.update({3: "c"})
print(d)

# number 11
d = {1: 'a', 2: 'b', 3: 'c'}
print(d)
del d[3]
print(d)

#tuples
# number1
tuple1 = (1,2,3,4)
print(tuple1)

# number 11
list = [1,6,7,2,3]
print(list)
tuple2 = tuple(list)
print(tuple2)

# sets
# number  10
set_a = {1,2,3,4,5}
set_b = {2,4}
set_c = {1}
print(set_b.issubset(set_a))
print(set_c.issubset(set_a))

# number 12
set1 = {2,7,9,10}
print(set1)
set1.clear()
print("After clearing:", set1)
