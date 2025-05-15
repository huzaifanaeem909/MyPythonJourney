""" 
Given a list of integers, write a function that reverses the elements of the list.

Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

"""

# Method-1:
def reverse_list(numbers):
    reversed_list = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_list.append(numbers[i])
    return reversed_list

numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))

# Method-2:
def reverse_list(numbers):
    return numbers[::-1]

numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(numbers)
print(reversed_numbers)  # Output: [5, 4, 3, 2, 1]

def reverse_list(numbers):
    return numbers[::-1]

numbers = "programiz"
reversed_numbers = reverse_list(numbers)
print(reversed_numbers)  # Output: zimargorp
