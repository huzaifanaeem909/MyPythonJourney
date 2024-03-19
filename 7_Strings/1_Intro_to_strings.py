"""In Python, a string is a sequence of characters. 
For instance, the word “hello” is a string composed of the individual characters "h", "e", "l", "l", and "o".
Strings are also immutable like tuples. Once created, you cannot modify its characters (neither insert nor change) . 
Attempting to modify will result in an error.
"""

# Creating Strings:
name = "Python"
print(name)  # Output: Python

message = "I love Python."
print(message)  # Output: I love Python.

# Accessing Characters in a String:
greet = "hello"
print(greet[1])  # Output: e

greet = "hello"
print(greet[-4])  # Output: e

# Multiline String:
message = """Never gonna give you up
Never gonna let you down """
print(message)

# Iterate Strings by Index:

my_string = "Never gonna give you up, Never gonna let you down "
for index in range(0, len(my_string)):
    print(my_string[index])

# Iterate Strings by Value:

my_string = "Never gonna give you up, Never gonna let you down "
for ch in my_string:
    print(ch)
