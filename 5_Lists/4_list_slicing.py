""" Slicing in Python is a powerful technique that allows you to extract specific portions of sequences like strings, lists, or tuples."""

# The syntax is:   List[Initial:End:IndexJump]
# List:        The list you want to slice.
# Initial:     The starting index (inclusive).
# End:         The ending index (exclusive).
# IndexJump:   The step size (optional).

# Positive Indexing:
list = [50, 70, 30, 20, 90, 10, 50]
new_list = list[1:5]
print(new_list)

# Negative Indexing:
list = [50, 70, 30, 20, 90, 10, 50]
new_list = list[-5:-1:1]
print(new_list)

# Step Indexing:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
new_list = my_list[::2]  # Output: [10, 30, 50, 70, 90]

# Omitting Indices:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sub_list1 = my_list[:2]  # Output: [10, 20]
sub_list2 = my_list[2:]  # Output: [30, 40, 50, 60, 70, 80, 90, 100]
