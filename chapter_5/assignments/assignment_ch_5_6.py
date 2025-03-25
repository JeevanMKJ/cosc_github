"""
There are three seating categories at a stadium.
Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10.
Write a program that asks how many tickets for each class of seats were sold,
then displays the amount of income generated from ticket sales.
"""

def main():
    #ticket_sales()
    ticket_sales_refactored()

def ticket_sales_refactored():
    ticket_class = ['A', 'B', 'C']
    ticket_costs = [20, 15, 10]
    total = 0

    for i in range(3):

        while True:
            num_tickets = input(f"Enter number of {ticket_class[i]} seats sold: ")
            if num_tickets.isdigit():
                num_tickets = int(num_tickets)
                break
            else:
                print("ERROR. Enter ONLY numbers.")

        sales = ticket_costs[i] * num_tickets
        print(f"Total {ticket_class[i]} seat sales: ${sales:,.2f}")
        total += sales

    print(f"Total sales: ${total:,.2f}")


def ticket_sales():
    ticket_a_cost = 20
    ticket_b_cost = 15
    ticket_c_cost = 10

    while True:
        num_a_sold = input("Enter number of A seats sold: ")
        num_b_sold = input("Enter number of B seats sold: ")
        num_c_sold = input("Enter number of C seats sold: ")

        if num_a_sold.isdigit() and num_b_sold.isdigit() and num_c_sold.isdigit():
            num_a_sold = int(num_a_sold)
            num_b_sold = int(num_b_sold)
            num_c_sold = int(num_c_sold)
            break
        else:
            print("ERROR. ONLY enter numbers.")

    ticket_a_sales = ticket_a_cost * num_a_sold
    ticket_b_sales = ticket_b_cost * num_b_sold
    ticket_c_sales = ticket_c_cost * num_c_sold

    sales_total = ticket_a_sales + ticket_b_sales + ticket_c_sales

    print(f"The total sales for all tickets is: ${sales_total}")


if __name__ == '__main__':
    main()