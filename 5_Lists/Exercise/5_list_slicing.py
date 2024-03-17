""" Write a python program to reverse a list using slicing. """

my_list = [5, 2, 10, "Python", 10, 20, 5, 2, 19, 33.3]
reversed_list = my_list[::-1]
print(reversed_list)

""" Write a python program to get every third element from a list using slicing."""

my_list = [5, 2, 10, "Python", 10, 20, 5, 2, 19, 33.3]
new_list = my_list[::3]
print(new_list)

""" Implement a python program to split a list into two equal parts using slicing. One list should contain 1st half and another list should contain 2nd half. """

my_list = [5, 2, 10, "Python", 10, 20, 5, 2, 19, 33.3, 42]
midpoint = len(my_list) // 2
first_half = my_list[:midpoint]
second_half = my_list[midpoint:]

print(first_half)
print(second_half)

""" Implement a python program to get the last 'n' elements from a listusing slicing."""

my_list = [5, 2, 10, "Python", 10, 20, 5, 2, 19, 33.3, 42]
num = int(input("Enter Number= "))
new_list = my_list[-num:]
print(new_list)

""" Ask "n" from user. Create a list of last n elements but in reverse order using slicing."""

my_list = [5, 2, 10, "Python", 10, 20, 5, 2, 19, 33.3, 42]
N = int(input("Enter Number= "))
new_list = my_list[-N:][::-1]
print(new_list)

""" Ask start and end index from the user. Create a list from start index to end index using slicing."""

my_list = [5, 2, 10, "Python", 10, 20, 5, 2, 19, 33.3, 42]
start_index = int(input("Enter Start Index= "))
end_index = int(input("Enter End Index= "))
new_list = my_list[start_index : end_index + 1]
print(new_list)

""" Ask "n" from user. Create a list of first n elements but in reverse order using slicing."""

my_list = [5, 2, 10, "Python", 10, 20, 5, 2, 19, 33.3, 42]
N = int(input("Enter Number= "))
new_list = my_list[:N][::-1]
print(new_list)
