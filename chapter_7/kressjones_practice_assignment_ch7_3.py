# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program creates two lists and joins them together.
# The combined list is then sorted and the following displayed:
# Sorted combined list.
# List total.
# List max value.
# List min value.
# The assignment gave the student the liberty to choose the numbers for
# the lists. I decided to generate random numbers for the both lists.

import random

def main():
    list_length = 5
    list_1 = [0, 0, 0, 0, 0]
    list_2 = [0, 0, 0, 0, 0]
    for i in range(5):
        list_1[i], list_2[i] = random.randint(1, 10), random.randint(1, 10)
    print(list_1, list_2)
    list_3 = list_1 + list_2
    list_3.sort()

    list_3_total = total_list(list_3)
    print(f"Combined sorted list: {list_3}")
    print(f"Combined list total: {list_3_total}")
    print(f"Combined list max value: {max(list_3)}")
    print(f"Combined list min value: {min(list_3)}")

def total_list(list_3):
    list_total = 0
    for i in range(len(list_3)):
        list_total += list_3[i]
    return list_total

if __name__ == '__main__':
    main()