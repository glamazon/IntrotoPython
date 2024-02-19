"""
Name: Peggy Sturman
Assignment: Exercise 3: BMI with Result
Date: 02/15/2024
Summary: Program that prompts the user to enter a weight in pounds and height in inches
and displays the BMI and tell them if the BMI is Normal, Overweight or Obese.
"""
def calculate_bmi(weight_pounds, height_inches):
    """
    Calculates the Body Mass Index (BMI) for a given weight and height.

    Args:
        weight_pounds (float): Weight in pounds.
        height_inches (float): Height in inches.

    Returns:
        float: The calculated BMI.
    """

    pounds_to_kg = 0.45359
    inches_to_meters = 0.0254

    weight_kg = weight_pounds * pounds_to_kg
    height_meters = height_inches * inches_to_meters

    bmi = weight_kg / (height_meters * height_meters)

    return bmi

def interpret_bmi(bmi):
    """
    Interprets the calculated BMI.

    Args:
        bmi (float): The calculated BMI.

    Returns:
        str: The interpretation of the BMI.
    """

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Get user input and validate it
weight_pounds = float(input("Enter your weight in pounds: "))
height_inches = float(input("Enter your height in inches: "))

# Calculate BMI
bmi = calculate_bmi(weight_pounds, height_inches)

# Interpret BMI
bmi_interpretation = interpret_bmi(bmi)

print(f"BMI is {bmi:.2f}.")
print(f"{bmi_interpretation}.")