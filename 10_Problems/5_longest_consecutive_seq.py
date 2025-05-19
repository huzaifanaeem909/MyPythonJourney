"""
Given an unsorted array of integers nums, find the length of the longest consecutive elements sequence. Return the length of this sequence.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1,2,3,4]. Its length is 4.
Input: nums = [100,101,103,200,201,202,1,2]
Output: 3
Explanation: The longest consecutive sequence is [200,201,202]. Its length is 3.
"""

def longestConsecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)  # Convert to set: {100, 4, 200, 1, 3, 2}
    max_length = 0
    
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            if current_length > max_length:
                max_length = current_length
    
    print(max_length)

input = [100, 4, 200, 1, 3, 2]
longestConsecutive(input)
