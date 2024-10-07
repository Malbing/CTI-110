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
print("-------Travel Expenses----------------")
print()

# Printing the expenses but making it look pretty

print(f"{'destination:':<18}{destination:<25}")
print(f"{'budget:':<18}${budget:<25.2f}")
print(f"{'gas:':<18}${gas:<25.2f}")
print(f"{'accomodations:':<18}${accomodations:<25,.2f}")
print(f"{'food:':<18}${food:<25,.2f}")

print("--" * 20)




# Your balance that remains

print (f"Remaining Balance ${budget-gas-accomodations-food:.2f}")


