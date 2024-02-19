"""
Name: Peggy Sturman
Assignment: Exercise 1: Convert Temperature
Date: 02/08/2024
Summary: Program that asks User to input the degree in Celsius and converts it to Farenheit
"""
# Prompts the user to enter a temperature value in degrees Celsius.
# The input is converted to an integer and stored in the variable 'celsius'.
celsius = int(input("Enter a degree in Celsius: "))

#Converts the degree using this formula
fahrenheit = (9 / 5) * celsius + 32

#prints the result of the conversion
print(celsius, "Celsius is", fahrenheit,  "Farenheit")
