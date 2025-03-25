"""
Write a program that asks the user to enter the monthly costs for the
following expenses incurred from operating their automobile:
loan payment, insurance, gas, oil, tires, and maintenance.
The program should then display the total monthly cost of
these expenses, and the total annual cost of these expenses.
"""

def main():

    costs_list, costs_names ,annual_total = monthly_costs()

    with open('car_costs.txt', 'w') as car_costs_file:
        for i in range(len(costs_list)):
            car_costs_file.write(f"{costs_names[i]}\n")
            car_costs_file.write(f"{costs_list[i]}\n")


def monthly_costs():
    multiplication_factor = 12

    print("Enter monthly costs.")

    while True:
        loan_payment = input("Enter monthly loan payment: ")
        insurance = input("Enter monthly insurance: ")
        gas = input("Enter monthly gas: ")
        oil = input("Enter monthly oil: ")
        tires = input("Enter monthly tires: ")
        maintenance = input("Enter monthly maintenance: ")
        if loan_payment.isdigit() and insurance.isdigit() and gas.isdigit() and oil.isdigit() and tires.isdigit() and maintenance.isdigit():
            loan_payment = float(loan_payment)
            insurance = float(insurance)
            gas = float(gas)
            oil = float(oil)
            tires = float(tires)
            maintenance = float(maintenance)
            break
        else:
            print("ERROR. Enter number.")

    costs_names = ["loan payment", "insurance", "gas", "oil", "tires", "maintenance"]
    costs = [loan_payment, insurance, gas, oil, tires, maintenance]

    total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance
    annual_total = total_monthly_cost * multiplication_factor
    print(f"\nTotal monthly car costs: {total_monthly_cost}")
    print(f"Total annual car costs: {annual_total}")
    return costs, costs_names, annual_total


if __name__ == '__main__':
    main()