"""
Write a function named max that accepts two integer values as
arguments and returns the value that is the greater of the two.
For example, if 7 and 12 are passed as arguments to the function,
the function should return 12.
Use the function in a program that prompts the user to enter two integer values.
The program should display the value that is the greater of the two.
"""

def main():
    max_num()

def max_num():
    while True:
        num_1 = input("Enter an int number: ")
        num_2 = input("Enter a second int number: ")
        if num_1.isdigit() and num_2.isdigit():
            num_1 = int(num_1)
            num_2 = int(num_2)
            break
        else:
            print("ERROR. Enter ONLY numbers.")

    nums = [num_1, num_2]
    max_number = max(nums)

    print(f"Max number: {max_number}")


if __name__ == '__main__':
    main()