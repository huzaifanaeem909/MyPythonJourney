"""Ask a number from user. Print all the numbers from 1 to that number."""

num = int(input("Enter any number = "))
i = 1
while i <= num:
    print(i)
    i = i + 1

""" Ask a number (N) from user. Print all the numbers from N to 1. """

N = int(input("Enter any number = "))
while N >= 1:
    print(N)
    N = N - 1

"""Ask start number and end number from user. Print all the numbers from start to end using while loop"""

start = int(input("Enter start number = "))
last = int(input("Enter last number = "))
while start <= last:
    print(start)
    start = start + 1

"""Calculate the sum of all the numbers from 1 to 10.
   Calculate product of all the numbers from 1 to 10.
"""
sum = 0
product = 1
num = 1
while num <= 10:
    sum = sum + num
    num += 1
print(sum)

while num <= 10:
    product *= num
    num += 1
print(product)

"""Calculate how many numbers are divisible by 7 from 1 to 100."""

a = 1
b = 100
num = 0
while a <= b:
    if a % 7 == 0:
        num += 1
    a += 1
print(f"The number of integers divisible by 7 from 1 to 100 is: {num}")

"""Calculate how many numbers are divisible by both 6 and 7 from 1 to 200."""

i = 1
count = 0
while i <= 200:
    if i % 7 == 0 and i % 6 == 0:
        count += 1
    i += 1
print(f"The number of integers divisible by 7 and 6 from 1 to 200 is: {count}")

"""Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50."""

i = 20
sum = 0
while i <= 50:
    if i % 4 == 0:
        sum += i
    i += 1
print(f"the sum is = {sum}")

"""Calculate how many numbers are divisible by 6 and 7 between 1 to 200. """

i = 1
num1 = 0
num2 = 0
while i <= 200:
    if i % 6 == 0:
        num1 = num1 + 1
    if i % 7 == 0:
        num2 = num2 + 1
    i += 1
print(f"the num divisible by 6= {num1}")
print(f"the num divisible by 7= {num2}")

"""Ask a number from user. Print the multiplication table of that number."""

num = int(input("Enter the Number = "))
i = 1
while i <= 10:
    temp = num * i
    print(f"{num}x{i} = {temp}")
    i = i + 1

"""Calculate factorial of a number entered by user."""

num = int(input("Enter the Number = "))
fac = 1
while num >= 1:
    fac = num * fac
    num -= 1
    print(fac)
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
