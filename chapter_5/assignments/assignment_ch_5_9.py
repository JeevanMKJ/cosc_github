"""
One foot equals 12 inches.
Write a function named feet_to_inches that accepts a number of feet as
an argument and returns the number of inches in that many feet.
Use the function in a program that prompts the user to enter a
number of feet then displays the number of inches in that many feet.
"""

def main():
    feet_to_inch()


def feet_to_inch():
    foot_in_inch = 12

    while True:
        num_feet = input("Enter number of feet: ")
        if num_feet.isdigit():
            num_feet = float(num_feet)
            break
        else:
            print("ERROR. Enter ONLY numbers.")

    inches = foot_in_inch * num_feet
    print(f"{num_feet:.1f} feet are {inches:.1f} inches.")


if __name__ == '__main__':
    main()