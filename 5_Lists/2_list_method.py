# Method    	Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list

my_list = [12, -59, 92, 33.3, 98, 89, 43, 20]
my_list.append("Hello")
my_list.append(29.5)
print(my_list)

my_list.extend(["Mango", 24])
print(my_list)

my_list.insert(3, "Python")
print(my_list)

my_list[0] = 100  # To update any index value.
my_list[-1] = 30.5
print(my_list)

my_list.pop(6)
print(my_list)
# If no index value is provided, then by default it will remove the last value in the list.

my_list.remove(43)  # Remove by value
print(my_list)

del my_list[0]  # del mean delete. It can be used with any data_type.
print(my_list)

print(my_list.index(33.3))  # Return the index value of specified value

a = [12, -59, 92, 33.3, 98, 89, 43, 20]
a.sort()  # Sort the list in assending order.
print(a)
a.reverse()  # Reverse the order of the list.
print(a)

# In case you want to sort list in descending order.
a = [12, -59, 92, 33.3, 98, 89, 43, 20]
a.sort(reverse=True)
print(a)


x = [-59, 92, "Python", 33.3, 98, 20, "Hello", 29.5, "Mango", 30.5]
y = x.copy()
# We cannot do y=x for copy because the ID or unique adress will be the same for both x and y, and if x is updated then y will also automatically changed  because of same ID. That's why list.copy method is used to overcome this scenario.
print(x)
print(id(x))
print(y)
print(id(y))
