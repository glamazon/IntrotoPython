"""
Name: Peggy Sturman
Assignment: Exercise 4: Assign a Letter Grade
Date: 02/15/2024
Summary: Program that prompts the user for a score between 0.0 and 1.0.
If the score is out of range, print an error message. If the score is between 0.0 and 1.0, prints a grade.

"""
score = float(input("Enter a score between 0.0 and 1.0: "))

if score > 1.0:
    print("Score must be less than or equal to 1.0.")
elif score < 0.0:
    print("Score cannot be negative.")
else:
    print("Your grade is:")
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")