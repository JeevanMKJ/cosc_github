"""
A painting company has determined that for every 112 square feet of wall space,
one gallon of paint and eight hours of labor will be required.
The company charges $35.00 per hour for labor.
Write a program that asks the user to enter the square feet of wall
space to be painted and the price of the paint per gallon.
The program should display the following data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job
"""

def main():
    paint_job()


def paint_job():
    labor_hours_per_calc_factor = 8
    labor_per_hour = 35
    calc_factor = 112

    while True:
        wall_size = input("Enter wall size in sq feet: ")
        cost_per_gallon = input("Enter price per gallon of paint: ")
        if wall_size.isdigit() and cost_per_gallon.isdigit():
            wall_size = float(wall_size)
            cost_per_gallon = float(cost_per_gallon)
            break
        else:
            print("ERROR. Enter ONLY numbers.")

    required_paint_g = wall_size / calc_factor
    paint_cost = required_paint_g * cost_per_gallon
    labor_hours = labor_hours_per_calc_factor * (wall_size / calc_factor)
    labour_cost = labor_hours * labor_per_hour
    job_cost = paint_cost + labour_cost

    print(f"Required gallons of paint: {required_paint_g:,.2f}")
    print(f"Required labor hours: {labor_hours:,.2f}")
    print(f"Total paint cost: ${paint_cost:,.2f}")
    print(f"Total labor cost: #{labour_cost:,.2f}")
    print(f"\nTotal job cost: ${job_cost:,.2f}")



if __name__ == '__main__':
    main()