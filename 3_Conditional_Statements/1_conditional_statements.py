a = 33
b = 200
if b > a:
    print("b is greater than a")

""" The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition"."""

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

""" The else keyword catches anything which isn't caught by the preceding conditions. """

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
