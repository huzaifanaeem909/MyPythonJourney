"""
Write a Python program that takes a number as input from the user and determines whether it is a prime number or not.
Prime number is only divisible by 1 and itself without leaving a remainder.
"""

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
  
num = int(input("Enter a Number:"))
print(is_prime(num))
