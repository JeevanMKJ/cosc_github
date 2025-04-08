"""
6. Larger Than n
In a program, write a function that accepts two arguments:
a list, and a number n. Assume that the list contains numbers.
The function should display all of the numbers in the list
that are greater than the number n.
"""
import random


def main():
    list_num = number_list()
    number_n = random.randint(1, 10)
    compare_list_to_number(list_num, number_n)

def compare_list_to_number(list_num, num):
    new_list = []
    for i in range(len(list_num)):
        if list_num[i] > num:
            new_list.append(list_num[i])
    print(num)
    print(new_list)
    return new_list

def number_list():
    list_length = 20
    num_list = [0] * list_length
    for i in range(list_length):
        num_list[i] = random.randint(1, 10)
    print(num_list)
    return num_list

if __name__ == '__main__':
    main()