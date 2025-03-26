"""
A retail company must file a monthly sales tax report listing the total sales for the month,
and the amount of state and county sales tax collected.
The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
Write a program that asks the user to enter the total sales for the month.
From this figure, the application should calculate and display the following:
• The amount of county sales tax
• The amount of state sales tax
• The total sales tax (county plus state)
"""

def main():
    calc_taxes()


def calc_taxes():

    county_sales_tax_percent = 0.025
    state_sales_tax_percent = 0.05

    while True:
        total_sales = input("Enter total monthly sales: ")
        if total_sales.isdigit():
            total_sales = float(total_sales)
            break
        else:
            print("ERROR. Enter ONLY numbers.")

    county_sales_tax = total_sales * county_sales_tax_percent
    state_sales_tax = total_sales * state_sales_tax_percent
    total_tax = county_sales_tax + state_sales_tax
    print(f"County sales tax: ${county_sales_tax:,.2f}")
    print(f"State sales tax: ${state_sales_tax:,.2f}")
    print(f"Total taxes: ${total_tax:,.2f}")


if __name__ == '__main__':
    main()