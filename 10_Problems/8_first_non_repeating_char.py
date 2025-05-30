"""
Given a string, return the index of the first non-repeating character in the string. If all characters repeat, return -1.

Example 1:
Input:  "abcdcaf"
Output: 1
'b' is the first character that does not repeat

Example 2:
Input:  "faadabcbbebdf"
Output: 6
'c' is the first character that does not repeat
"""

def first_non_repeating_char(string):
    freq = {}   # Dictionary to store frequency of each character
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
          
    print(freq)   # Output: {'a': 2, 'b': 1, 'c': 2, 'd': 1, 'f': 1}
        
    for i, char in enumerate(string):
        if freq[char] == 1:
            return i

    return -1  # if no unique character found

print(first_non_repeating_char("abcdcaf"))  # Output: 1
