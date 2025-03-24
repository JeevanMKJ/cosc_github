"""
Write a program that writes a series of random numbers to a file.
Each random number should be in the range of 1 through 500.
The application should let the user specify how many random numbers the file will hold.
"""

import random

def main():
    user_rand_numbers = input("How many random numbers between 1 and 500?: ")

    while True:
        if not user_rand_numbers.isdigit():
            print("ERROR: Enter a number.")
        else:
            user_rand_numbers = int(user_rand_numbers)
            break

    with open('random_numbers.txt', 'w') as rand_num_file:

        for i in range(1, user_rand_numbers + 1):
            rand_number = random.randrange(1, 501)
            rand_num_file.write(f"{rand_number}\n")

            print(rand_number)

if __name__ == '__main__':
    main()