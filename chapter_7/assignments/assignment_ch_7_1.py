"""
1. Total Sales
Design a program that asks the user to enter a store’s sales for each day of the week.
The amounts should be stored in a list.
Use a loop to calculate the total sales for the week and display the result.
"""

def main():
    week_days = 7
    week_sales = []
    for i in range(week_days):
        while True:
            try:
                sale = input(f"Enter sale for day #{i + 1}: ")
                sale = float(sale)
                break
            except ValueError as e:
                print(f"ValueError: Enter a floating point number.\nDetails: {e}")

        week_sales.append(sale)

    sales_total = sum(week_sales)
    print(f"Total week sales: {sales_total:.2f}")

if __name__ == '__main__':
    main()