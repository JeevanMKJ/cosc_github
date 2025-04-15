"""
14. Expense Pie Chart
Create a text file that contains your expenses
for last month in the following categories:
• Rent
• Gas
• Food
• Clothing
• Car payment
• Misc
Write a Python program that reads the data
from the file and uses matplotlib to plot
a pie chart showing how you spend your money.
"""
import random

def main():
    #data_to_file()
    generated_expanses_file()
    read_expense_file()


def generated_expanses_file():
    expense_categories = ['rent', 'gas', 'food', 'clothing', 'car payments', 'misc']
    expense_num = 6
    with open('expenses.txt', 'w') as expenses_file:
        for i in range(expense_num):
            expense = random.uniform(150, 500)
            if i == 0:
                expense = random.uniform(1500, 5000)
            if i == 4:
                expense = random.uniform(500, 1000)
            expenses_file.write(f"{expense:.2f}\n")
    print("Expenses added to file.")

def data_to_file():
    print("--Enter the expenses by category for each month--")
    expense_categories = ['rent', 'gas', 'food', 'clothing', 'car payments', 'misc']
    expense_num = 6
    with open('expenses.txt', 'w') as expenses_file:
        for i in range(expense_num):
            while True:
                expense = input(f"Enter monthly {expense_categories[i]} expense: ")
                if expense.isdigit():
                    expense = float(expense)
                expenses_file.write(f"{expense:.2f}\n")
    print("Expenses added to file.")

def read_expense_file():
    expense_list = []
    with open('expenses.txt', 'r') as expense_file:
        for line in expense_file:
            line = float(line)
            expense_list.append(line)

    print(expense_list)

if __name__ == '__main__':
    main()