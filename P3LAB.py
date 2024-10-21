# Matthew Setter
# 10/14/2024
# P3LAB
# Calulate most efficient coin combination

'''
# Regular Division
print(100/3)

# Floor Division - returns interger portion of the quotient
print (100//3)

# Modulo - returns ONLY the remainder
print(100%3)
print(7%4)
'''

# Get amount of money from user as float
money = float(input("Enter the amount of money as a float: $"))

# Convert money to a whole number
money = round(money * 100)

'''
# May need to round this value
money = round(money * 100)


print(money)
'''

# Get whole dollars from money amount
dollars = money // 100

# Remove the dollar amount from money
money = money - (dollars * 100)

print(f"Dollars: {dollars}")

# Get quarters from money amount
quarters = money // 25

# Remove the quarter amount from money
money = money - (quarters * 25)

print(f"Quarters: {quarters}")
# Get dimes from money amount
dimes = money // 10

# Remove the dimes amount from money
money = money - (dimes * 10)

print(f"Dimes: {dimes}")
# Get nickles from money amount
nickles = money // 5

# Remove the nickles amount from money
money = money - (nickles * 5)

print(f"Nickles: {nickles}")

# Get pennies from money amount
pennies = money // 1

# Remove the pennies amount from money
money = money - (pennies * 1)

print(f"Pennies: {pennies}")
