"""Given two lists a, b. Check if two lists have at least one element common in them."""

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
set_a = set(a)  # Convert List to a Set.
for element in b:
    if element in set_a:
        print("Lists contains at least one common element.")
if element not in a:
    print("Lists does not contains any common element.")

"""Python program to find common elements in three lists using sets."""

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 7, 8, 9]
# Convert lists to sets
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

common_elements = set1.intersection(set2, set3)
print("Common elements in three lists:", common_elements)

"""Create 3 sets of your own, find the union of three sets."""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {5, 6, 7, 8, 9}

union_of_sets = set1.union(set2, set3)
print("Union of three sets:", union_of_sets)

"""Write a Python program to remove all elements from a given set."""

my_set = {1, 2, 3, 4, 5}
# Remove all elements from the set
my_set.clear()
print("Set after removing all elements:", my_set)

"""Write a Python program to find the length of a set."""

my_set = {1, 2, 3, 4, 5}
set_length = len(my_set)
print("Length of the set:", set_length)

"""Write a Python program to check if two given sets have no elements in common."""

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
found = False
for i in set1:
    if i in set2:
        found = True
        print("common elements found")
if not found:
    print("No Elements in common")

"""Write a Python program to find elements in a given set that are not in another set."""

"""Ask a string from user, remove all the duplicates from that string and print that string again (order does not matter)"""

input_string = input("Enter a string: ")
my_set = set(input_string)
result = str(my_set)
result = "".join(my_set)
print(result)
