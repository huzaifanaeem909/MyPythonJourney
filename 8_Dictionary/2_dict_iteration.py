# Iteration:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
}

# By Dictionary Keys:
for key in my_dict.keys():
    print(f"Key: {key}")
# Another Method:
for key in my_dict:
    print(key)

# By Dictionary Values:
for value in my_dict.values():
    print(f"Value: {value}")

# Another Method:
for key in my_dict:
    print(f"Key: {my_dict[key]}")

# Looping Over Dictionary Items (Key-Value Pairs):
# You can use the .items() method to iterate over both keys and values simultaneously.

for key, value in my_dict.items():
    print(f"{key} -> {value}")
