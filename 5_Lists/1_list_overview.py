"""
Lists are mutable, which means you can modify their elements after creation. 
You can add, remove, or change items in a list.
"""

# List is always represented in Square brakets
a = [12, -59, "Hello", 33.3, 98, "Python", 43, 20]
print(a)  # Print complete list
print(a[3])  # Print specific index value in List
print(type(a[3]))  # Check class of specific index value

# to check the length of given List
x = len(a)
print(x)

# Iterate by index/position
for i in range(0, len(a)):
    print(a[i], end=" ")
print()

# Iterate by Value
for i in a:
    print(i, end=" ")

# Some useful functions
my_list = [12, -59, 92, 33.3, 98, 89, 43, 20]
print(len(my_list))
print(sum(my_list))
print(max(my_list))
print(min(my_list))
