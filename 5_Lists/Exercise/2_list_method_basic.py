""" Write a program that prompts the user to specify the length of a list and then requests numbers to populate that list. Display the final list as the output. """

list_length = int(input("Enter the length of the List= "))
my_list = []
for i in range(0, list_length):
    num = int(input("Enter number= "))
    my_list.append(num)
print(my_list)

""" Create a list and prompt the user for an 'old number' followed by a 'new number.' If the 'old number' exists in the list, replace it with the 'new number' provided by the user. """
"""Remove all the even numbers from the list."""

list_length = int(input("Enter the length of the List= "))
my_list = []
for i in range(0, list_length):
    num = int(input("Enter number= "))
    my_list.append(num)
print(my_list)

old_num = int(input("Enter Old number= "))
new_num = int(input("Enter New number= "))
for i in range(0, len(my_list)):
    if my_list[i] == old_num:
        my_list[i] = new_num
print(my_list)

for i in range(len(my_list) - 1, -1, -1):  # Iterate in reverse order
    if my_list[i] % 2 == 0:
        my_list.pop(i)
print(my_list)

"""  Ask the user for a number. Then, from a list of numbers, remove all the numbers that can be divided by the number the user entered. """

my_list = [10, 14, 20, 60, 48, 35]
num = int(input("Enter a Number= "))
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] % num == 0:
        my_list.pop(i)
print(my_list)

""" Generate a list of at least 10 numbers. Then, create two separate lists called 'odd' and 'even.' Put all the odd numbers from the original list into the 'odd' list, and all the even numbers into the 'even' list."""

my_list = [3, 8, 12, 17, 22, 30, 35, 41, 48, 50]
even = []
odd = []
for i in my_list:  # Iterate by Value
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Even list= {even}")
print(f"Odd list= {odd}")

""" Start by creating two separate lists with random numbers. Then, create a third list that merges the numbers from the first and second lists together."""

list_1 = [5, 8, 12, 15]
list_2 = [3, 10, 18, 21]
new = []
for i in list_1:
    new.append(i)
for i in list_2:
    new.append(i)
print(new)

# Another Method
print(list_1 + list_2)
