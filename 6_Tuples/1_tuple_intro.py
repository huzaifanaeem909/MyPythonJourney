""" 
A tuple is similar to a list but immutable. 
Once created, you cannot modify its elements. 
Attempting to modify a tuple will result in an error that is TypeError: 'tuple' object does not support item assignment.
Tuples are written with round brackets ().
"""

numbers = (1, 2, -5)
print(numbers)  # Output: (1, 2, -5)

languages = ("Python", "Swift", "C++")
print(languages[0])  # Output: Python

cars = ("BMW", "Tesla", "Ford", "Toyota")
print("Total Items:", len(cars))  # Output: Total Items: 4

# Iterating Through a Tuple:
fruits = ("apple", "banana", "orange")
for fruit in fruits:
    print(fruit)

# Checking Item Existence:
colors = ("red", "orange", "blue")
print("yellow" in colors)  # False
print("red" in colors)  # True
