""" Make your own list. Print the list in reverse. """

my_list = [12, -59, "Hello", 33.3, 98, "Python", 43, 20]
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i], end=" ")

""" Make your own list. Print all the even numbers present in the list."""

my_list = [12, -59, 92, 33.3, 98, 89, 43, 20]
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        print(my_list[i], end=" ")

"""  Make your own list. Print all the odd numbers present in the list. """

my_list = [12, -59, 92, 33.3, 98, 89, 43, 20]
for i in range(0, len(my_list)):
    if my_list[i] % 2 != 0:
        print(my_list[i], end=" ")

""" Make your own list. Print all the elements present at even index position. """

my_list = [12, -59, 92, 33.3, 98, 89, 43, 20]
for i in range(0, len(my_list)):
    if i % 2 == 0:
        print(my_list[i], end=" ")

"""  Make your own list. Print the sum of all elements present in that list. """

my_list = [12, -59, 92, 33.3, 98, 89, 43, 20]
sum = 0
for i in range(0, len(my_list)):
    sum = sum + my_list[i]
print(f"The total sum is equal to = {sum}")

""" Make your own list. Count the number of even numbers present in that list."""

my_list = [12, -59, 92, 33.3, 98, 89, 43, 20]
count = 0
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        count += 1
print(f"Total even numbers are = {count}")

""" Make your own list. Count how many numbers are divisible by both 2 and 5 in that list. """

my_list = [12, -59, 92, 33.3, 98, 90, 43, 20]
count = 0
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0 and my_list[i] % 5 == 0:
        count += 1
print(f"Total numbers divisible by both 2 and 5 = {count}")

""" Make your own list. Find the sum of all even numbers present in that list."""

my_list = [12, -59, 92, 33.3, 98, 89, 43, 20]
sum = 0
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        sum = sum + my_list[i]
print(f"The total sum of even numbers = {sum}")

""" Make your own list. Find the sum of all numbers divisible by 3 or 4. """

my_list = [12, -59, 92, 33.3, 98, 90, 43, 20]
sum = 0
for i in range(0, len(my_list)):
    if my_list[i] % 3 == 0 or my_list[i] % 4 == 0:
        sum += my_list[i]
print(f"Sum of total numbers divisible by both 3 and 4 = {sum}")

""" Make your own list. Print how many positive and negative numbers are here."""

my_list = [12, -59, 92, 33.3, 98, 90, 43, 20]
positive_count = 0
negative_count = 0
for i in range(0, len(my_list)):
    if my_list[i] > 0:
        positive_count += 1
    else:
        negative_count += 1
print(f"Total positive numbers = {positive_count}")
print(f"Total negative numbers = {negative_count}")

""" Make your own list. Print the largest number present in that list. """

my_list = [12, -59, 92, 33.3, 98, 90, 43, 20]
largest_num = my_list[0]
for i in range(0, len(my_list)):
    if my_list[i] > largest_num:
        largest_num = my_list[i]
print(f"The largest number is = {largest_num}")
