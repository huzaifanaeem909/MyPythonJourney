"""String slicing allows you to obtain a sub-string from a given string by specifying a range of indices."""

# The syntax is:   String[Initial:End:IndexJump]
# String:          The list you want to slice.
# Initial:         The starting index (inclusive).
# End:             The ending index (exclusive).
# IndexJump:       The step size (optional).

my_string = "Pyhton is Fun"
print(my_string[0 : len(my_string)])

my_string = "Pyhton is Fun"
print(my_string[:])

my_string = "Pyhton is Fun"
print(my_string[::2])

my_string = "Pyhton is Fun"
print(my_string[-3:])

my_string = "Pyhton is Fun"
print(my_string[::-1])

# Example: Take input from User and check weather it is a Palindrome or Not?
"""
A palindrome is a sequence (such as a word, phrase, or number) that reads the same forward and backward.
Palindromes remain unchanged even when reversed for example, “madam”, “level” remains same when reversed.
"""

word = input("Enter a Word= ")
reversed_word = word[::-1]  # Reverse the word using slicing
if word == reversed_word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
