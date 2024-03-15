"""A list comprehension in Python is a concise way to create lists. It provides a compact syntax for generating lists based on existing iterable objects."""

# list from 1 to 10.
my_list = [i for i in range(1, 11)]
print(my_list)

# List to print Python 10 times.
my_list = ["Python" for i in range(1, 11)]
print(my_list)

# list of squares of numbers from 1 to 10.
my_list = [i**2 for i in range(1, 11)]
print(my_list)

# list of only even numbers between 1 to 10
my_list = [i for i in range(1, 11) if i % 2 == 0]
print(my_list)


my_list = [[i, "EVEN"] if i % 2 == 0 else [i, "ODD"] for i in range(1, 10)]
print(my_list)
