""" Set is a collection of unique elements and it do not allow duplicate values. 
Sets are:
Unordered: Items do not have a defined order.
Mutable: You can modify (add or remove) the items from a set.
You can create a set by placing elements inside curly braces {}.
"""

student_id = {112, 114, 116, 118, 115}  # Set of integer type
vowel_letters = {"a", "e", "i", "o", "u"}  # Set of string type
mixed_set = {"Hello", 101, -2, "Bye"}  # Set of mixed data types

# Empty Set Creation: To create an empty set, use the set() function without any argument.
empty_set = set()

# Handling Duplicate Items: Sets automatically remove duplicate values.
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)

"""
Set Methods
add(item):                Add specified item to a set.
remove(item):             Removes the specified item from the set.
discard(item):            Removes the specified item (if present) without raising an error.
pop():                    Removes and returns an arbitrary item from the set.
clear():                  Removes all items from the set.
union(other_set):         Returns a new set containing all unique elements from both sets.
intersection(other_set):  Returns a new set with common elements between two sets.
difference(other_set):    Returns a new set with elements present in the first set but not in the second.
issubset(other_set):      Checks if the set is a subset of another set.
issuperset(other_set):    Checks if the set is a superset of another set.
"""

# Union Method:
set1 = {"Python", "Java"}
set2 = {"C++", "Java"}
result = set1.union(set2)
print(result)
result = set1 | set2  # The | operator performs the union operation on sets.
print("Union:", result)

nums1 = {1, 2, 2, 3, 4, 5}
nums2 = {4, 5, 6, 6, 7, 8, 8}
nums3 = {7, 8, 9, 10}
distinct_nums = nums1 | nums2 | nums3
print("The union of three sets is:", distinct_nums)

# Comparison: union() Method vs. Set Union Operator (|):
"""The union() method accepts one or more iterables and converts them to sets before performing the union."""
"""The | operator only works with sets and does not accept other iterables."""

test_set = {1, 2, 3}
test_list = [2, 3, 4]
result = test_set.union(test_list)
print(result)
# Using | operator with non-set iterable (causes an error)
# test_set | test_list  # TypeError: unsupported operand type(s) for |: 'set' and 'list'


# Intersection Method:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
result = set1.intersection(set2)
print(result)

result = set1 & set2  # The & operator performs the intersection operation on sets.
print("Intersection:", result)
