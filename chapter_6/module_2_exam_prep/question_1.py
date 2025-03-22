"""
1. Write the definition for a function switch that receives as parameters
first_name and last_name and prints them in reverse order.
Write the call to the function from main, passing two names as parameters.
"""

def main():
    FIRST_NAME = "Bill"
    LAST_NAME = "Kill"
    switch_params(FIRST_NAME, LAST_NAME)

def switch_params(last_name, first_name):
    print(f"{last_name}, {first_name}")


if __name__ == "__main__":
    main()