# Nested dictionary: A nested dictionary is essentially a dictionary where the values can themselves be dictionaries.

my_dict = {
    "Alice": {
        "age": 20,
        "gender": "Female",
        "Roll no": 15,
        "Bio": 30,
        "Physics": 44,
        "Math": 50,
    },
    "John": {
        "age": 22,
        "gender": "Male",
        "Roll no": 65,
        "Bio": 50,
        "Physics": 34,
        "Math": 58,
    },
    "Sikandar": {
        "age": 18,
        "gender": "Male",
        "Roll no": 10,
        "Bio": 72,
        "Physics": 68,
        "Math": 75,
    },
}
print(my_dict["Sikandar"]["age"])

for name, details in my_dict.items():
    print(name)
    print(details["Bio"])

for name, details in my_dict.items():
    total = details["Bio"] + details["Physics"] + details["Math"]
    gender = details["gender"]
    print(f"Total Marks of {name}: {total}, gender= {gender}")


my_dict = {
    "Alice": {
        "age": 20,
        "gender": "Female",
        "Roll no": 15,
        "marks": [59, 92, 67, 75, 78, 84],
    },
    "John": {
        "age": 22,
        "gender": "Male",
        "Roll no": 65,
        "marks": [65, 92, 67, 73, 60, 76],
    },
    "Sikandar": {
        "age": 18,
        "gender": "Male",
        "Roll no": 10,
        "marks": [90, 92, 77, 85, 82, 94],
    },
}

# for name, details in my_dict.items():
#     total = sum(details["marks"])
#     print(f"{name} got total marks: {total}")

for name, details in my_dict.items():
    list = details["marks"]
    a = 0
    total_marks_scored = 0
    for i in list:
        if a < i:
            total_marks_scored += i
    print(f"{name} scored total {total_marks_scored} marks ")


my_dict = {
    "Alice": {
        "age": 20,
        "gender": "Female",
        "Roll no": 15,
        "marks": {"Bio": 30, "Physics": 44, "Math": 50},
    },
    "John": {
        "age": 22,
        "gender": "Male",
        "Roll no": 65,
        "marks": {"Bio": 50, "Physics": 34, "Math": 58},
    },
    "Sikandar": {
        "age": 18,
        "gender": "Male",
        "Roll no": 10,
        "marks": {"Bio": 68, "Physics": 65, "Math": 75},
    },
}

for name, details in my_dict.items():
    total = (
        details["marks"]["Bio"] + details["marks"]["Physics"] + details["marks"]["Math"]
    )
    print(f"{name} scored total {total} marks.")
