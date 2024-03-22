"""Given a list and dictionary, map each element of list with each item of dictionary, forming nested dictionary as value."""

test_dict = {
    "Name": "Sikandar",
    "Age": 20,
    "Gender": "Male",
}
test_list = [10, 10.5, 11]
result = {}

for item in test_list:
    for key, value in test_dict.items():
        nested_dict = {}
        nested_dict[key] = value
    result[item] = nested_dict

print(result)


"""
Create a dictionary like this given below and solve the questions based on that.
Student_marks = {
    "Alice": {"marks": [59, 67, 75]},
    "John": {"marks": [65, 92, 67]},
    "Sikandar": {"marks": [90, 92, 94]},
}
"""
"""Add a new student named "Eva" with marks [95, 91, 89] to the student_marks dictionary."""

student_marks = {
    "Alice": {"marks": [59, 67, 75]},
    "John": {"marks": [65, 92, 67]},
    "Sikandar": {"marks": [90, 92, 94]},
}
student_marks["Eva"] = {"marks": [95, 91, 89]}
print(student_marks)

# Another method:
# student_marks.update({"Eva": {"marks": [95, 91, 89]}})
# print(student_marks)

"""Write a python program that prints all the students name along with their average marks."""

for name, details in student_marks.items():
    total = sum(details["marks"])
    avg = total / len(details["marks"])
    print(f"The average marks of {name} is {avg:.2f}")

"""Update the marks of "John" to [85, 88, 92] in the student_marks dictionary. """

student_marks["John"] = {"marks": [85, 88, 92]}
print(student_marks)

# Another method:
# student_marks.update({"John": {"marks": [85, 88, 92]}})
# print(student_marks)

"""Write a program that displays the name of the student that has scored highest marks overall."""

highest_marks = 0
top_student = " "
for name, details in student_marks.items():
    total_marks = sum(details["marks"])
    if total_marks > highest_marks:
        highest_marks = total_marks
        top_student = name

print(f"The student with the highest marks overall is: {top_student}")

"""Create another nested dictionary named additional_marks with information for two more students.
Merge this dictionary with the student_marks dictionary."""

student_marks = {
    "Alice": {"marks": [59, 67, 75]},
    "John": {"marks": [65, 92, 67]},
    "Sikandar": {"marks": [90, 92, 94]},
}
additional_marks = {
    "Eva": {"marks": [95, 91, 89]},
    "Michael": {"marks": [80, 85, 88]},
}
# Merge additional_marks with student_marks
student_marks.update(additional_marks)
print(student_marks)

"""Remove the entry for the student "John" from the student_marks dictionary."""

del student_marks["John"]
print(student_marks)

# Remove the entry for "John" using pop
# student_marks.pop("John")
# print(student_marks)
