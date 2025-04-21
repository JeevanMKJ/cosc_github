# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program creates a two-dimensional list.
# The user enters integers into the list.
# All the values of the list are then displayed and
# the sum of the list displayed.

ROWS = 4
COLS = 3

def main():
    tdl = create_2_dimensional_list()
    calc_sums(tdl)

def calc_sums(tdl):
    total = 0
    for r in range(ROWS):
         for c in range(COLS):
             total += tdl[r][c]
    print(f"List total: {total}")
    return total

def create_2_dimensional_list():
    two_dim_list = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    for r in range(ROWS):
        for c in range(COLS):
            two_dim_list[r][c] = user_input()

    print(f"List: {two_dim_list}", end = " ")
    print()
    return two_dim_list

def user_input():
    while True:
        user_number = input("Enter number: ")
        if user_number.isdigit():
            user_number = int(user_number)
            break
        else:
            print("ERROR: Only enter numbers.")
    return user_number

if __name__ == '__main__':
    main()