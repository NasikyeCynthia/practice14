#number 1
num = [1,7,9]
max_num = max(num)
print(f"The maximum number is {max_num}")

# number 4
string = input("Enter a string: ")
rev_string = string[::-1]
print("Reversed string is", rev_string)

# number 11
string = input("Enter a string: ")
rev_string = string[::-1]
if string == rev_string:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

# number 3
def multiply(num):
    total = 1
    for x in num:
        total *= x
    return total
print(multiply((8, 3, 2, -1, 7)))

# number 2
def sum(num):
    total = 1
    for x in num:
        total += x
    return total
print(sum((8, 3, 2, -1, 7)))
