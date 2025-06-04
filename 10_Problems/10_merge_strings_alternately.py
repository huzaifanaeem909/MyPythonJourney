"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
"""


def mergeStrings(word1,word2):
    len1,len2 = len(word1),len(word2)
    min_len = min(len1,len2)
    res=[]
    
    for i in range(min_len):
      res.append(word1[i])
      res.append(word2[i])
    
    if len1 > len2:
      res.append(word1[min_len:])
    else:
      res.append(word2[min_len:])
    
    return ''.join(res)

word1 = 'abcd'
word2 = 'pq'
print(mergeStrings(word1,word2))
