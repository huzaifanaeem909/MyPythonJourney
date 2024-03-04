""" Membership operators are used to test if a sequence is presented in an object."""

# Operator	                                    Description	                                           Example
#   in 	        Returns True if a sequence with the specified value is present in the object	       x in y
# not in	    Returns True if a sequence with the specified value is not present in the object	  x not in y

my_list = [-59, 92, "Python", 33.3, 98, 20, "Hello", 29.5, "Mango", 30.5]
print(92 in my_list)
print(21 in my_list)
print("Hello" not in my_list)
print(21 not in my_list)

num = int(input("Enter a Number= "))
if num in my_list:
    print("YES")
else:
    print("NO")
