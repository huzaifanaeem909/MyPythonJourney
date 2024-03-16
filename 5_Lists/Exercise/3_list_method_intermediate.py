""" Make a list of your own. And remove all the duplicates element from that list."""

# my_list = [5, 2, 10, "Python", 10, 20, 5, 2, 19]
# result = []
# for num in my_list:
#     if num not in result:
#         result.append(num)
# print(result)

""" Make a list. Then ask a number from user. If number exists in that list then print the position of the element else print -1. """

# my_list = [5, 2, 10, "Python", 10, 20, 5, 2, 19]
# num = int(input("Enter a Number= "))
# if num in my_list:
#     print(my_list.index(num))
# else:
#     print(-1)

"""Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order. """

# my_list = []
# for i in range(0, 10):
#     value = int(input(f"Entrer a value at index {i}="))
#     my_list.append(value)
# print(my_list)
# my_list.reverse()
# reverse_list = my_list.copy()
# print(reverse_list)

"""  Write a program to find the average of all the numbers present in the list. """

# my_list = [23, 45, 98, 765, 90, 22, 58, 21, 73, 46]
# sum = 0
# for i in my_list:
#     sum += i
# avg = sum / len(my_list)
# print(sum)
# print(avg)

"""Write a Python code to find the occurrence of each element in a list and print the element with the highest occurrence."""

# my_list = [23, 46, 98, 23, 73, 22, 58, 23, 73, 46]
# result = []

# for num in my_list:
#     if num not in result:
#         result.append(num)

# highest_occurance = 0
# highest_occ_element = 0

# for num in result:
#     c = my_list.count(num)
#     print(f"{num} occurs {c} times")
#     if c > highest_occurance:
#         highest_occurance = c
#         highest_occ_element = num
# print(
#     f"The element with highest occurance is {highest_occ_element} which occured {highest_occurance} times."
# )

""" Write a program that has two lists and make a new list that contains only the common elements between them without duplicates."""

# my_list1 = [1, 2, 3, 4, 5, 6, 7, 7, 8]
# my_list2 = [6, 7, 8, 9]
# result = []

# for num in my_list1:
#     if num in my_list2:
#         if num not in result:
#             result.append(num)
# print(result)

""" Write a Python code to find the second largest element in a list without sorting."""

# my_list = [23, 46, 98, 23, 73, 22, 58, 23, 73, 46]

# largest = float("-inf")
# second_largest = float("-inf")

# for num in my_list:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num < largest and num > second_largest:
#         second_largest = num

# print(second_largest)

""" Make a program that takes a list of integers and returns the product of all the elements."""

# my_list = [23, 46, 98, 23, 73, 22, 58, 23, 73, 46]
# product = 1

# for num in my_list:
#     product *= num
# print(product)

""" Write a program to find and print all prime numbers within a given list."""

# my_list = [23, 46, 98, 23, 73, 22, 58, 23, 73, 46]
# for num in my_list:
#     factors = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors += 1
#     if factors == 2:
#         print(num, end=" ")

""" Write a program to split a given list into two halves. """

my_list = [23, 46, 98, 73, 22, 58, 23, 73, 46, 100]

first_half = []
second_half = []
midpoint = int(len(my_list) / 2)
print(midpoint)

for i in range(0, len(my_list)):
    if i < midpoint:
        first_half.append(my_list[i])
    else:
        second_half.append(my_list[i])

print("First half of the list:", first_half)
print("Second half of the list:", second_half)

""" Write a program that swaps the first and last elements of a given list. """

# my_list = [23, 98, 23, 73, 22, 58, 23, 73, 46]
# if len(my_list) >= 2:
#     first_element = my_list[0]
#     last_element = my_list[-1]

#     my_list[-1] = first_element
#     my_list[0] = last_element

# print("List after swapping first and last elements:", my_list)
