# name
# 9/23/2024
# In class example
# Simulate shopping, give receipt

def main():
    items= []
    while True:
        response = input("Do you want to continue? (yes/no): ")

        if response == 'yes':
            item = input("Enter name of item: ")
            price = float(input(f"Enter price of {item}: "))
            quantity = int(input(f"How many of {item} are you purchasing? "))
            items.append((item, price, quantity))  # Store item details            
        elif response == 'no':
                subtotal(items)
                break
        else:
                print("Invalid input. Please enter 'yes' or 'no'.")
def calculate_varibles():
    subtotal
    tax_amount
if __name__ == "__main__":
    main()
    
print("Welcome to PetSmart!")
print()

#get info of first item purchased

item1 = input("Enter name of first item:  ")
price1 = float(input(f"Enter price of {item1}: "))
quantity1 = int(input(f"How many of {item1} are you purchasing? "))

print()

#get info of second item purchased

item2 = input("Enter name of second item:  ")
price2 = float(input(f"Enter price of {item2}: "))
quantity2 = int(input(f"How many of {item2} are you purchasing? "))

print()

#get info of third item purchased

item3 = input("Enter name of third item:  ")
price3 = float(input(f"Enter price of {item3}: "))
quantity3 = int(input(f"How many of {item3} are you purchasing? "))

print()

#get receipt w/tax + sub total
print("Receipt: Tax & Sub Total")
print()

print(f"{item1}    {quantity1}    ${price1*quantity1:.2f}")
print(f"{item2}    {quantity2}    ${price2*quantity2:.2f}")
print(f"{item3}    {quantity3}    ${price3*quantity3:.2f}")


# Calulate subtotal
print()
subtotal = (price1*quantity1) + (price2*quantity2) + (price3*quantity3)
print(f"Subtotal: ${subtotal:.2f}")
tax_amount = 0.07 * subtotal
print(f"Tax: ${tax_amount:.2f}")
print(f"Final Total Owed: ${tax_amount + subtotal:.2f}\n")

