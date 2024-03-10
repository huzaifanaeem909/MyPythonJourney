""" Logical operators are used to combine conditional statements. """

# Operator	                   Description	                                   Example
#   and              Returns True if both statements are true	           x < 5 and  x < 10
#   or	          Returns True if one of the statements is true	            x < 5 or x < 4
#   not	     Reverse the result, returns False if the result is true	 not(x < 5 and x < 10)

Math = 50
Physics = 20
print(Math > 33 and Physics > 33)
print(Math > 33 or Physics > 33)
print(not Physics > 33)
