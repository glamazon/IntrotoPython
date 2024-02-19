"""
Name: Peggy Sturman
Assignment: Exercise 4: Compute Your Pay
Date: 02/17/2024
Summary: Program that prompts the user for working hours and rate per hour to compute gross pay.
"""

def computePay(hours, rate):
    """
    Computes the gross pay based on given hours & rate.

    Args:
        hours (float): The number of hours worked.
        rate (float): The hourly rate.

    Returns:
        float: gross pay.
    """

    if hours <= 40:
        return hours * rate
    else:
        overtime_hours = hours - 40
        return 40 * rate + overtime_hours * 1.5 * rate

# Get hours and rate from the user
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

# Calculate gross pay
gross_pay = computePay(hours, rate)

# Print the gross pay
print(f"Gross pay: ${gross_pay:.2f}")