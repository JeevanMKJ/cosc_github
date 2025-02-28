"""This program calculates the total and average cost of a meal,
consisting of three inputs."""

hamburger_cost = float(input("Enter the cost of a hamburger: "))
fries_cost = float(input("Enter the cost of fries: "))
shake_cost = float(input("Enter the cost of a shake: "))

total_cost = hamburger_cost + fries_cost + shake_cost
print(f"The total cost of the meal is ${total_cost:.2f}.")

average_cost = total_cost / 3
print(f"The average cost for each item is ${average_cost:.2f}.")
