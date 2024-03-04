""" Write a Python program to swap the values of two variables without using a temporary variable. """

a = 20
b = 50
a = a + b
b = a - b
a = a - b
print(a)
print(b)

""" Write a Python program that takes the radius of a circle as input and calculates its area. Use the formula: Area = 3.14 * r^2."""

radius = float(input("Enter Radius = "))
area = 3.14 * radius**2
print(f"The area of circle = {area}")
