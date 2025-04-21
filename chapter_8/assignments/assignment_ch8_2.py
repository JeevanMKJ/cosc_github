"""
2. Sum of Digits in a String
Write a program that asks the user to enter a series
of single-digit numbers with nothing separating them.
The program should display the sum of all the single
digit numbers in the string. For example,
if the user enters 2514, the method should return 12,
which is the sum of 2, 5, 1, and 4.
"""

def main():
    print("--Calc sum of individual numbers--")
    while True:
        user_string = input("Enter multi digit string (example 21358): ")
        if user_string.isdigit():
            break
        else:
            print("ERROR: Only enter numbers.")

    #user_string = "25831"
    num_list = []
    for i in user_string:
        num_list.append(int(i))
    num_total = sum(num_list)
    print(f"String number total: {num_total}")

if __name__ == '__main__':
    main()