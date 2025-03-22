"""
14. Write a program that reads in numbers from the file from the previous
problem and computes the average of the numbers.
Read the numbers in from "random_numbers.txt".
"""

with open('random_numbers.txt', 'r') as rand_num_file:

    count = 0
    total = 0

    rand_num = rand_num_file.readline()

    while rand_num != '':
        rand_num = int(rand_num)
        total += rand_num
        count += 1
        rand_num = rand_num_file.readline()

    print(f"Total: {total}")
    print(f"Count: {count}")

    rand_num_average = total / count

    print(f"Random number average: {rand_num_average}")


