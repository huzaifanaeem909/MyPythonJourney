# title(): Converts each word’s first character to uppercase (title case).
sentence = "programming is awesome"
title_case = sentence.title()
print(title_case)  # Output: "Programming Is Awesome"

# capitalize(): Converts the first character of a string to uppercase.
original_string = "hello, world!"
capitalized_string = original_string.capitalize()
print(capitalized_string)  # Output: "Hello, world!"

# lower() and upper(): Convert a string to lowercase and uppercase, respectively.
text = "Python Is Fun"
lower_text = text.lower()
upper_text = text.upper()
print(lower_text)  # Output: "python is fun"
print(upper_text)  # Output: "PYTHON IS FUN"

# swapcase(): Swaps the case of all characters in a string.
mixed_case = "PyThOn Is FuN"
swapped_case = mixed_case.swapcase()
print(swapped_case)  # Output: "pYtHoN iS fUn"

# isupper(): It is used to check whether all characters in a given string are in uppercase or not.
a = "Hello World!"
b = "hello 123"
c = "DEEP BLUE SEA"
print(a.isupper())  # Output: False
print(b.isupper())  # Output: False
print(c.isupper())  # Output: True

# islower(): It is used to check whether all characters in a given string are in lowercase.
a = "Hello world!"
b = "hello 123"
c = "the quick brown fox jumps over the lazy dog."
print(a.islower())  # Output: False
print(b.islower())  # Output: False
print(c.islower())  # Output: True

# isalpha(): It is used to checks whether all characters in a given string are alphabet letters (from ‘a’ to ‘z’ or ‘A’ to ‘Z’).
a = "Hello123"
b = "Python!"
c = "OnlyLetters"
print(a.isalpha())  # Output: False (contains digits)
print(b.isalpha())  # Output: False (contains an exclamation mark)
print(c.isalpha())  # Output: True (only letters)

# isdigit(): This method in Python is a built-in function that checks if all characters in a given string are digits.
text = "50800"
result = text.isdigit()
print(result)  # Output: True

# isalnum(): This method in Python is used to check whether a string contains only alphanumeric characters.
a = "Python 3"
b = "Hello, World!"
c = "Python12345"
print(a.isalnum())  # Output: False (contains a space)
print(b.isalnum())  # Output: False (contains punctuation)
print(c.isalnum())  # Output: True (only alphanumeric characters)

# isspace(): This method in Python is used to check whether a string contains only whitespace characters.
a = "Hello World!"  # Contains non-whitespace characters
b = "   "  # Only whitespace characters
c = "\t\t"  # Only tabs
print(a.isspace())  # Output: False
print(b.isspace())  # Output: True
print(c.isspace())  # Output: True

# split() Method: The split() method is used to split a string into substrings based on a specified separator.
# It returns a list of substrings. By default, it splits the string on whitespaces.

sentence = "Hello, world! How are you today?"
words = sentence.split()  # Splits on whitespaces by default
print(words)

my_string = "Apples,Oranges,Pears,Bananas,Berries"
fruits_list = my_string.split(",")
print(fruits_list)

# join() Method: The join() method is used to join a list of strings into a single string.
# It takes an iterable (e.g., a list) and concatenates its elements using the specified separator.

fruits = ["Apples", "Oranges", "Pears", "Bananas", "Berries"]
fruits_string = " ".join(fruits)
print(fruits_string)

fruits = ["Apple", "Banana", "Orange", "Grapes"]
separator = " and "
fruit_sentence = separator.join(fruits)
print(fruit_sentence)

# count() method: It is used to determine the number of non-overlapping occurrences of a specified substring within a given string.

text = "I love apples, apples are my favorite fruit"
count_apple = text.count("apple")

# startswith() & endswith(): True if the original sentence starts or ends with the search_string, otherwise False.

text = "The quick brown fox jumps over a lazy dog"
print(text.startswith("The"))  # True
print(text.endswith("dog"))  # True

# index(): It searches for the first occurrence of a specified substring within a string and returns the index value where it was found.

text = "Hello, world!"
index = text.index("w")
index_hello = text.index("Hello")
print(f"The index of 'w' is: {index}")  # Output: The index of 'w' is: 7
print(f"The index of 'Hello' is: {index_hello}")  # Output: The index of 'Hello' is: 0

# find(): This method also searches for a specified substring within a string and returns the index where it was found.
# If the substring is not found, it returns -1.

text = "Python is amazing!"
index = text.find("o")
index_amazing = text.find("amazing")
print(f"The index of 'o' is: {index}")
print(f"The index of 'amazing' is: {index_amazing}")

# replace(): This method replaces occurrences of a specified substring with another substring in the original string.

sentence = "I love programming. Programming is fun!"
new_sentence = sentence.replace("Programming", "Coding")
print(new_sentence)  # Output: "I love coding. Coding is fun!"

# strip(): This method removes leading and trailing whitespace (spaces, tabs, or newline characters) from a string.

text = "   Python is great!   "
cleaned_text = text.strip()
print(cleaned_text)  # Output: "Python is great!"
