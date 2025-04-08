"""
3. Rainfall Statistics
Design a program that lets the user enter the total
rainfall for each of 12 months into a list.
The program should calculate and display the total
rainfall for the year, the average monthly rainfall,
the months with the highest and lowest amounts.
"""

def main():
    rainfall_by_month = monthly_rainfall()
    calc_numbers(rainfall_by_month)

def monthly_rainfall():
    print("--Enter rainfall as floating points--")
    months_of_year = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    months = 12
    year = [0] * months
    for index in range(len(year)):
        while True:
            try:
                month = input(f"{months_of_year[index]}: ")
                month = int(month)
                break
            except ValueError as e:
                print(f"ValueError as {e}")

        year[index] = month
    return year

def calc_numbers(month_rain):
    total_annual_rainfall = sum(month_rain)
    average_monthly_rainfall = total_annual_rainfall / len(month_rain)
    print(f"Total annual rainfall: {total_annual_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_monthly_rainfall:.2f}")

if __name__ == '__main__':
    main()