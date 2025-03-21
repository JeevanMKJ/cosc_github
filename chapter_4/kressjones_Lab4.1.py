# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program takes in the monthly budget and expenses from the user.
# It then calculates if the user is over or under their budget.

MONTHLY_BUDGET = float(input("What is your monthly budget: "))

total_expenses = 0

while True:

    expense = float(input("Enter an amount spent (0 to quit application): "))

    if expense == 0:
        break

    total_expenses += expense

    DIFFERENCE = total_expenses - MONTHLY_BUDGET

print(f"\nYour monthly budget is: ${MONTHLY_BUDGET:.2f}\nThe sum of your monthly expenses is: ${total_expenses:.2f}")

if total_expenses > MONTHLY_BUDGET:
    OVER_BUDGET = total_expenses - MONTHLY_BUDGET
    print(f"\nYou are ${OVER_BUDGET:.2f} over your ${MONTHLY_BUDGET:.2f} monthly budget.\nReduce spending.")
else:
    UNDER_BUDGET = MONTHLY_BUDGET - total_expenses
    print(f"\nYou are ${UNDER_BUDGET:.2f} under your ${MONTHLY_BUDGET:.2f} monthly budget.\nGreat job.")
