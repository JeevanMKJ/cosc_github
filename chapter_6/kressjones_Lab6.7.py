# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete

import random

MIN_RANDOM_VALUE = 1
MAX_RANDOM_VALUE = 501

def main():
    random_number_file_writer()

def random_number_file_writer():
    try:
        while True:
            user_num = input("How many random numbers in the range 1 to 500 do you want?: ")
            if user_num.isdigit():
                user_num = int(user_num)
                break
            else:
                print("ERROR: Enter a valid positive integer.")

        num_file = open('../num_file.txt', 'w')

        for i in range(1, user_num + 1):
            rand_num = random.randrange(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)

            num_file.write(f'{rand_num}\n')

        num_file.close()
        print(f"Successfully wrote {user_num} random numbers to num_file.txt")

    except IOError:
        print("ERROR: Could not write to file.")
    except ValueError:
        print("ERROR: Invalid value entered.")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
