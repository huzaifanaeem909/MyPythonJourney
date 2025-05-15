""" 
Given a list of integers, write a function to check whether the list is a palindrome or not.
A list is considered a palindrome if it reads the same backward as forward.

Input: [1, 2, 3, 2, 1]
Output: True

Input: "madam"
Output: True

"""

def is_palindrome(sequence):
    return sequence == sequence[::-1]

print(is_palindrome([1, 2, 3, 2, 1]))  # Output: True
print(is_palindrome("madam"))          # Output: True
print(is_palindrome([1, 2, 3, 4, 5]))  # Output: False
