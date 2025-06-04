"""
Given an integer array nums of size n, return the number with the valueclosest to 0 in nums. If there are multiple answers, return the number with
the largest value.

Example 1:
Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4
The distance from -2 to 0 is |-2| = 2
The distance from 1 to 0 is |1| = 1
The distance from 4 to 0 is |4| = 4
The distance from 8 to 0 is |4| = 8

Thus, the closest number to 0 in the array is 1.
"""

# Time complexity: O(n)
# Space complexity: O(1)

def findClosestToZero(nums):
    closest = nums[0]
  
    for num in nums:
      if abs(num) < abs(closest):
        closest = num
      elif abs(num) == abs(closest):
        closest = max(closest, num)
        
    return closest

nums = [-4,-2,1,4,8]
print(findClosestToZero(nums))
