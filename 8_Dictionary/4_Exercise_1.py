""" Ask subject name and marks from the user and keep adding it to dictionary. """

# my_dict = {}
# total_subjects = int(input("Enter the number of subjects= "))
# for _ in range(0, total_subjects):
#     subject_name = input("Enter Subject name: ")
#     subject_marks = int(input(f"Enter Marks for {subject_name}: "))
#     my_dict[subject_name] = subject_marks
# print(my_dict)

"""Convert two lists into a dictionary. Make two list on your own of same length, and convert them to dictionary. """

list_1 = ["Pyhton", "Hello", "Thirty", "NYC"]
list_2 = ["Good", "World", 30, 212]
my_dict = {}
for i in range(0, len(list_1)):
    my_dict[list_1[i]] = list_2[i]
    # my_dict.update({list_1[i]: list_2[i]})
print(my_dict)

"""Write a Python program to sum all the items in a dictionary. """

my_dict = {
    "Math": 57,
    "Chem": 30,
    "Phy": 99,
}
total = 0
for values in my_dict.values():
    total = total + values
print(total)

# Another Method:
print(sum(list(my_dict.values())))

"""Write a Python program to multiply all the items in a dictionary. """

my_dict = {
    "Math": 57,
    "Chem": 30,
    "Phy": 99,
}
total = 1
for values in my_dict.values():
    total = total * values
print(total)

"""Ask a string from user. Display the dictionary where each key is a character and 
value is the frequency of that character that comes in that string."""

# my_string = input("Enter a String: ")
# my_dict = {}
# for ch in my_string:
#     if ch in my_dict:
#         my_dict[ch] += 1
#     else:
#         my_dict[ch] = 1
# print(my_dict)

"""Store “name” of a student as Key, “list of 5 marks” of that student as a Value. 
Store atleast 5 student names. Print the sum and percentage of all the students."""

students_data = {
    "student1": [85, 78, 90, 40, 70],
    "student2": [85, 99, 78, 67, 45],
    "student3": [94, 67, 86, 84, 90],
    "student4": [90, 67, 92, 85, 78],
    "student5": [88, 67, 90, 55, 79],
}
for name, marks in students_data.items():
    # total = sum(marks)
    total = 0
    for i in marks:
        total += i
    percentage = total / 500 * 100
    print(f"{name} has scored total {total} marks, Percentage= {percentage:.2f}")

"""Store marks of 5 different subjects in a dictionary. Ask subject name as an input from the User. 
Print the marks of that subject entered by User. If subject does not exist, print “Invalid”."""

my_dict = {
    "Math": 100,
    "Chemistry": 87,
    "Physics": 99,
    "Biology": 90,
    "Computer Science": 95,
}
subject_name = input("Enter Subject Name: ")
# Method 1:
# if subject_name in my_dict:
#     print(f"Marks for {subject_name}: {my_dict[subject_name]}")
# else:
#     print("Invalid")

# Method 2:
for subject, marks in my_dict.items():
    if subject_name == subject:
        print(f"Marks for {subject_name}: {marks}")
else:
    print("Invalid")

"""Store name as a Key, and 5 marks in a List as a value in dictionary. Store details of at least 5 students. 
Print the name of the student who got highest marks."""

students_data = {
    "student1": [85, 78, 90, 40, 70],
    "student2": [85, 99, 78, 67, 45],
    "student3": [94, 67, 86, 84, 90],
    "student4": [90, 67, 92, 85, 78],
    "student5": [88, 67, 90, 55, 79],
}
highest_marks = 0
student_name = " "
for name, marks in students_data.items():
    total = sum(marks)
    if total > highest_marks:
        highest_marks = total
        student_name = name
print(f"The {student_name} got highest marks: {highest_marks}")

"""Write a Python program to combine two dictionary by adding values for common keys."""

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 200, "b": 300, "d": 400}
d3 = {}
for key, value in d1.items():
    d3[key] = value
for key, value in d2.items():
    if key in d3:
        d3[key] = d3[key] + value
    else:
        d3[key] = value
print(d3)
