#Number 2 character frequency count
string = "Programming"
freq = {}
for char in string:
    freq.setdefault(char, 0)
    freq[char] += 1
print("Character frequency: "+ str(freq))

#number 4 concatenate string and swap first two characters
string1 = "abc"
string2 = "xyz"
strings = string1 +' '+string2
print(strings)
strings_swap = string2+' '+string1

def str_swap(a , b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
print(str_swap(string1 , string2))

# number 7 remove characters at odd indices
def odd_char(char):
    result = ""
    i = 0
    for i in range(len(char)):
        if i % 2 == 0:
            result =  result + char[i]
    return result

print(odd_char("Computer science"))

# number 10 reversing strings
string = input("Enter any word: ")
reversedstring = string[::-1]
print(reversedstring)


# number 12 reversing words in a string
input_string = "hello world"
reversed_string = ' '.join(input_string.split()[::-1])
print(reversed_string)  

# number 16 sum of digits in a string
def sumdigits(str):
    sum_digit = 0
    for char in str:
        if char.isdigit():
            digit = int(char)
            sum_digit += digit
    return sum_digit
string = input("Input the string: ")
summed = sumdigits(string)
print(summed) 

# number 18
def count_chars(str):
  upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
  for i in range(len(str)):
    if str[i] >= 'A' and str[i] <= 'Z':
      upper_ctr += 1
    elif str[i] >= 'a' and str[i] <= 'z':
      lower_ctr += 1
    elif str[i] >= '0' and str[i] <= '9':
      number_ctr += 1
    else:
      special_ctr += 1
  return upper_ctr, lower_ctr, number_ctr, special_ctr
str = input("Input string: ")
print("Original string:",str)
u, l, n, s = count_chars(str)
print('\nUpper case characters: ',u) 
print('Lower case characters: ',l)
print('Number case: ',n)
print('Special case characters: ',s) 

# number 15 remove spaces from a string
def removespace(string1):
    string1 = string1.replace(' ', '')
    return string1 
print(removespace("Hello World"))

# numdber 21 swap character cases
def swap(str1):
    result_str = ""
    for item in str1:
        if item.isupper():
            result_str += item.lower()
        else:
            result_str += item.upper()
    return result_str
print(swap("Hello World"))

# number 30
"helo wo".title()
def capitalize(string):
    capitalize = string.title()
    return capitalize
string = "hello world"
capitalized_string = capitalize(string)
print(capitalized_string) 