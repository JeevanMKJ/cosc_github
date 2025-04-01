"""
13. Write a program that writes random integers to a file.
The program should read in two numbers from the user:
one that specifies how many random numbers to generate,
and one that specifies the top of the range of random numbers
(that is, 100 if the user wants numbers between 1 and 100, inclusive).
Write the numbers to a file called "random_numbers.txt". Put each number on a new line.
"""

import random

user_num_rand_num = int(input("How many random numbers do you want?: "))
user_top_range_rand_num = int(input(f"What will the top range for the {user_num_rand_num} random numbers be?: "))

with open('random_numbers.txt', 'w') as randNum:
    for i in range(1, user_num_rand_num + 1):
        rand_num = random.randrange(1, user_top_range_rand_num)

        randNum.write(f'{rand_num}\n')

    randNum.close()
    print(f"Added {user_num_rand_num} random numbers to file.")