# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program takes in a full name, first, middle and last names.
# The names are then strung together and all the appearances
# of a, e and s counted and displayed.

def main():
    first_name, middle_name, last_name = user_input()
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    count_letters(full_name)

def user_input():
    first_name = input("Enter first name: ")
    middle_name = input("Enter middle name: ")
    last_name = input("Enter last name: ")

    return first_name, middle_name, last_name

def count_letters(full_name):
    count_a = 0
    count_e = 0
    count_s = 0
    for char in full_name:
        if char == "a" or char == "A":
            count_a += 1
        if char == "e" or char == "E":
            count_e += 1
        if char == "s" or char == "S":
            count_s += 1
    print(f"Number of a: {count_a}")
    print(f"Number of e: {count_e}")
    print(f"Number of s: {count_s}")

if __name__ == '__main__':
    main()