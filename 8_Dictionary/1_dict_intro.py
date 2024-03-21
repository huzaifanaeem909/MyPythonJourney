"""Dictionaries are a fundamental data structure in Python.
They allow you to store and manage data in the form of key-value pairs.
Each key maps to a corresponding value.
A dictionary is defined by enclosing a comma-separated list of key-value pairs in curly braces {}.
Dictionaries are mutable (you can modify their contents).
The syntax is as follows:
my_dict = {
    "key1": "value1",
    "key2": "value2",
    # ... more key-value pairs ...
}
"""

# Unlike lists, where elements are accessed by their position (via indexing), dictionary elements are accessed via their keys.

my_dict = {
    "league": "FIFA",
    "teams": 32,
    "groups": 8,
}
print(my_dict["league"])
print(my_dict["teams"])
print(my_dict["groups"])

# Getting a Value:
# Method 1:

my_dict = {"name": "Alice", "age": 30}
age_value = my_dict["age"]  # Retrieves the value associated with the key "age".
print(age_value)

# Method 2: When accessing a key that doesn’t exist, you can use the get() method to avoid raising an error.

k = input("Enter a Key= ")
age_value = my_dict.get(k)
if age_value is not None:
    print(age_value)
else:
    print("Key does not Exist.")

# Adding or Updating a Key-Value Pair: To add a new key-value pair or update an existing one, you can use the update() method.
# Using update():

my_dict.update({"city": "New York"})  # Adds a new key "city" with value "New York"
print(my_dict)

# Using assignment:

my_dict["age"] = 31  # Updates the value associated with the key "age"
print(my_dict)

# Removing a Key-Value Pair: To remove a key-value pair from a dictionary, you can use the del statement or the pop() method.

# Using del[]:

del my_dict["name"]  # Removes the key "name" and its associated value
print(my_dict)

# Using pop():

# removed_value = my_dict.pop("age")  # Removes the key "age" and returns its value
removed_value = my_dict.pop("age")  # Removes the key "age" and returns its value
print(my_dict)
