"""
  Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
  Note: The second largest element should not be equal to the largest element.
  
  Examples:
  
  Input: arr[] = [12, 35, 1, 10, 34, 1]
  Output: 34
  Explanation: The largest element of the array is 35 and the second largest element is 34.
  Input: arr[] = [10, 5, 10]
  Output: 5
  Explanation: The largest element of the array is 10 and the second largest element is 5.
  Input: arr[] = [10, 10, 10]
  Output: -1
  Explanation: The largest element of the array is 10 and the second largest element does not exist.
"""

def second_largest(arr):
    largest = second = float('-inf')
  
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num < largest:
            second = num

    return second if second != float('-inf') else -1  # Return -1 if no valid second largest exists

arr1 = [12, 35, 1, 10, 34, 1]
arr2 = [10, 5, 10]
arr3 = [10, 10, 10]

print("Output for arr1:", second_largest(arr1))  # Output: 34
print("Output for arr2:", second_largest(arr2))  # Output: 5
print("Output for arr3:", second_largest(arr3))  # Output: -1
