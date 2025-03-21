# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program calculates the discount that is applied based on the number of packages bought by the user.
# The user inputs their purchased number of packages and receive a discount amount and total amount.

package_price = 149 
user_num_packages = int(input("Enter the number of packages purchased: "))

UNIT_PRICE = 149
DISCOUNT_10 = 0.1
DISCOUNT_20 = 0.2
DISCOUNT_30 = 0.3
DISCOUNT_40 = 0.4

subtotal = user_num_packages * UNIT_PRICE

if user_num_packages >= 150:
    discount = DISCOUNT_40
elif 100 <= user_num_packages <= 149:
    discount = DISCOUNT_30
elif 50 <= user_num_packages <= 99:
    discount = DISCOUNT_20
elif 10 <= user_num_packages <= 49:
    discount = DISCOUNT_10
else:
    discount = 0

discount_amount = subtotal * discount
total_cost = subtotal - discount_amount

print(f"Subtotal: ${subtotal:,.2f}")
print(f"Discount amount: ${discount_amount:,.2f}.")
print(f"Total cost: ${total_cost:,.2f}")
