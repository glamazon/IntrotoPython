"""
Name: Peggy Sturman
Assignment: Exercise 2: Body mass index (BMI)
Date: 02/08/2024
Summary: Program that prompts the user to enter a weight in pounds and height in inches
and displays the BMI.
"""
def calculate_bmi(weight_pounds, height_inches):


  # Conversion factors
  pounds_to_kg = 0.45359
  inches_to_meters = 0.0254

  # Calculate weight in kilograms and height in meters
  weight_kg = weight_pounds * pounds_to_kg
  height_meters = height_inches * inches_to_meters

  # Calculate BMI
  bmi = weight_kg / (height_meters * height_meters)

  return bmi

# Get user input and validate it
weight_pounds = float(input("Enter your weight in pounds: "))
height_inches = float(input("Enter your height in inches: "))

# Calculate and display BMI
bmi = calculate_bmi(weight_pounds, height_inches)
print(f"BMI is {bmi:.2f}")