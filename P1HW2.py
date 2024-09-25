
# 9/25/2024
# P1HW2
# A program that calulates and displays travel expenses

print("This program calulates and displays travel expenses")
print()

# This section of the program allows the user to put in information that will be calulated later
# for example gas/food/accomodations

budget = float(input("Enter your budget:  "))

destination = input("Enter your travel destination:  ")

gas = float(input("How much do you think you will spend on gas?  "))

accomodations = float(input("Approximately, how much will you need for accomodation/hotel?  "))

food = float(input("Last, how much do you need for food?  "))


# Travel Expenses section. all the data above will be calulated and you'll receive your budget plan

print()
print("-------Travel Expenses-------")
print()

print (f"Location:  {destination}")
print (f"Initial Budget:  {budget}")

print()

print (f"Fuel:  ${gas}")
print (f"Accomodation:  ${accomodations}")
print (f"Food:  ${food}")

print()

# Your balance that remains

print (f"Remaining Balance ${budget-gas-accomodations-food}")


