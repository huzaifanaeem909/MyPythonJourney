'''
Write a program that checks if a given year is a leap year. Leap years
are divisible by 4, but not by 100 unless they are also divisible by 400.
'''
year = int(input("Enter the year: "))
if year % 4 == 0:  # divisible by 4
        if year % 100 == 0:  # divisible by 100
            if year % 400 == 0:  # divisible by 400
                print("leap year")
            else:
                print("not a leap year")
        else:
            print("leap year")
else:
        print("not a leap year")

"""
Create a program that calculates the price of a movie ticket based on
the age of the customer. If the customer is under 12, the ticket costs $5; if
they are between 12 and 65, the ticket costs $10; otherwise, it's $7
"""
age = int(input("Enter your age: "))
if(age>12):
    if(age<65):
        print("ticket price= 10$")
    else:
        print("ticket price= 7$")
else:
    print("ticket price= 5$")

        