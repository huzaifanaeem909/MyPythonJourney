""" Generate a list of squares of numbers from 1 to 10 using list comprehension. """

my_list = [i**2 for i in range(1, 11)]
print(my_list)

""" Given a list of strings, create a new list containing the lengths of each string using list comprehension."""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [len(i) for i in fruits]
print(new_list)

""" Generate a list of strings where each string repeats itself three times, using list comprehension. """

my_list = ["a", "b", "c", "d"]
new_list = [i * 3 for i in my_list]
print(new_list)

""" Generate a list of list using list comprehension where format should be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]]."""

my_list = [[i, "EVEN"] if i % 2 == 0 else [i, "ODD"] for i in range(1, 10)]
print(my_list)

""" Generate a list of only even numbers between 1 to 50, using list comprehension. """

my_list = [i for i in range(1, 51) if i % 2 == 0]
print(my_list)
