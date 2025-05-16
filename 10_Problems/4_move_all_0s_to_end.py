"""
You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. 
The operation must be performed in place, meaning you should not use extra space for another array.

Examples:
Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
"""

def move_zeros(arr):
    start = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[start], arr[i] = arr[i], arr[start]
            start += 1
    return arr

arr1 = [1, 2, 0, 4, 3, 0, 5, 0]
arr2 = [10, 20, 30]
arr3 = [0, 0]

print("Output for arr1:", move_zeros(arr1))  # Output: [1, 2, 4, 3, 5, 0, 0, 0]
print("Output for arr2:", move_zeros(arr2))  # Output: [10, 20, 30]
print("Output for arr3:", move_zeros(arr3))  # Output: [0, 0]
