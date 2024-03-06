"""Ask a number from user. Print all the numbers from 1 to that number."""

num = int(input("Enter any number = "))
for i in range(1, num + 1):
    print(i, end=" ")

""" Ask a number (N) from user. Print all the numbers from N to 1. """

N = int(input("Enter any number = "))
for i in range(N, 0, -1):
    print(i, end=" ")

"""Ask start number and end number from user. Print all the numbers from start to end using for loop"""

start = int(input("Enter start number = "))
last = int(input("Enter last number = "))
for i in range(start, last + 1):
    print(i, end=" ")

"""Calculate the sum of all the numbers from 1 to 10.
   Calculate product of all the numbers from 1 to 10.
"""
sum = 0
product = 1
for i in range(1, 11):
    sum = sum + i
print(sum)

for i in range(1, 11):
    product = product * i
print(product)

"""Calculate how many numbers are divisible by 7 from 1 to 100."""

count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1
print(f"The number of integers divisible by 7 from 1 to 100 is: {count}")

"""Calculate how many numbers are divisible by both 6 and 7 from 1 to 200."""

count = 0
for i in range(1, 201):
    if i % 7 == 0 and i % 6 == 0:
        count += 1
print(f"The number of integers divisible by 7 and 6 from 1 to 200 is: {count}")

"""Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50."""

sum = 0
for i in range(20, 51):
    if i % 4 == 0:
        sum += i
print(f"the sum is = {sum}")

"""Calculate how many numbers are divisible by 6 and 7 between 1 to 200. """

num1 = 0
num2 = 0
for i in range(1, 201):
    if i % 6 == 0:
        num1 = num1 + 1
    if i % 7 == 0:
        num2 = num2 + 1
    i += 1
print(f"the num divisible by 6= {num1}")
print(f"the num divisible by 7= {num2}")

"""Ask a number from user. Print the multiplication table of that number."""

num = int(input("Enter the Number = "))
for i in range(1, 11):
    temp = num * i
    print(f"{num}x{i} = {temp}")

"""Calculate factorial of a number entered by user."""

num = int(input("Enter the Number = "))
fac = 1
for i in range(num, 0, -1):
    fac = i * fac
print(f"The Factorial of number is = {fac}")

"""Ask to numbers x and y from the user. If x<y then print all the
numbers from x to y, but if y<x then print all the numbers from y to x."""

x = int(input("Enter X = "))
y = int(input("Enter Y = "))
if x > y:
    while x >= y:
        print(x)
        x -= 1
else:
    while x <= y:
        print(y)
        y -= 1
