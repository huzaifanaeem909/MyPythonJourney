"""Ask a string from user. Count how many alphabets are there in that string."""

my_string = input("Enter a String= ")
count = 0
for ch in my_string:
    if ch.isalpha():
        count += 1
print(count)

# Another solution:

my_string = input("Enter a String= ")
count = 0
for ch in my_string:
    ascii = ord(ch)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        count += 1
print(count)

"""Ask a string from user. Count the number of uppercase and lowercase characters in that String."""

my_string = input("Enter a String= ")
count_upper = 0
count_lower = 0
for ch in my_string:
    if ch.isupper():
        count_upper += 1
    elif ch.islower():
        count_lower += 1
print(count_upper)
print(count_lower)

# Another solution:

my_string = input("Enter a String= ")
count_upper = 0
count_lower = 0
for ch in my_string:
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90:
        count_upper += 1
    elif ascii >= 97 and ascii <= 122:
        count_lower += 1
print(count_upper)
print(count_lower)

"""Ask a string from user. Convert all the alphabets to uppercase."""

my_string = input("Enter a String= ")
new_string = my_string.upper()
print(new_string)

# Another solution:

my_string = input("Enter a String= ")
result = ""
for ch in my_string:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        upper_ascii = ascii - 32
        char = chr(upper_ascii)
        result += char
    else:
        result += ch
print(result)

"""Ask a string from user. Convert all the alphabets to lowercase."""

my_string = input("Enter a String= ")
new_string = my_string.lower()
print(new_string)

# Another solution:

my_string = input("Enter a String= ")
result = ""
for ch in my_string:
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90:
        lower_ascii = ascii + 32
        char = chr(lower_ascii)
        result += char
    else:
        result += ch
print(result)

"""Ask a string from user. Convert uppercase to lowercase and convert lowercase to uppercase and dont change the other letters."""

my_string = input("Enter a String= ")
new_string = my_string.upper()
print(new_string)

# Another solution:

my_string = input("Enter a String= ")
result = ""
for ch in my_string:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        upper_ascii = ascii - 32
        upper_char = chr(upper_ascii)
        result += upper_char
    elif ascii >= 65 and ascii <= 90:
        lower_ascii = ascii + 32
        lower_char = chr(lower_ascii)
        result += lower_char
    else:
        result += ch

print(result)

""" Count the number of spaces in a string entered by user."""

my_string = input("Enter a String= ")
count = 0
for ch in my_string:
    if ch.isspace():
        count += 1
print(count)

# Another solution:

my_string = input("Enter a String= ")
count = 0
for ch in my_string:
    ascii = ord(ch)
    if ascii == 32:  # ASCII code for Space is equal to 32.
        count += 1
print(count)

"""Ask a string from user. Print the count of how many alphabets, digits, spaces and symbols (everything else) are there in that string."""

my_string = input("Enter a String= ")
count_alpha = 0
count_int = 0
count_space = 0
count_sym = 0
for ch in my_string:
    ascii = ord(ch)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii < 122):
        count_alpha += 1
    elif ascii >= 48 and ascii < 57:
        count_int += 1
    elif ascii == 32:
        count_space += 1
    else:
        count_sym += 1

print(count_alpha)
print(count_int)
print(count_space)
print(count_sym)

""" Write a program to reverse the order of words."""

my_string = "Hello Worlds! Python is Good"
words = my_string.split()[::-1]
output = " ".join(words)
print(output)

"""Write a program that accepts a string and capitalizes the first letter of each word while converting all other letters to lowercase."""

my_string = "Hello World, PYTHON is GOOD"
words = my_string.split()
output = " ".join(i.capitalize() for i in words)
print(output)

"""Write a program that reverses each word in a sentence while maintaining the word order. 
   For example, "Hello World" should become "olleH dlroW". """

my_string = "Hello World, PYTHON is GOOD"
words = my_string.split()
output = " ".join(i[::-1] for i in words)
print(output)

"""Write a program that converts a string in camel_case to snake_case.
For example, converting "helloWorldHowAreYou" should result in "hello_world_how_are_you"."""

my_string = "helloWorldHowAreYou"
result = ""
for char in my_string:
    if char.isupper():
        result += "_" + char.lower()
    else:
        result += char
print(result)

# Another Solution:

my_string = "helloWorldPythonIsGood"
result = ""
for ch in my_string:
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90:
        lower_ascii = ascii + 32
        val = chr(lower_ascii)
        result += "_" + val
    else:
        result += ch

print(result)
