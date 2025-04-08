"""
4. Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers.
The program should store the numbers in a list then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list
"""
import random

# The exercise asks that the user inputs 20 numbers.
# This seems a little tedious. I'll automatically
# create 20 random ints.
# However I do have the expected code included.

def main():
    #num_list = number_list()
    user_created_list = user_list()
    display_data(user_created_list)
    #display_data(num_list)

def number_list():
    number_list_range = 20
    num_list = [0] * number_list_range
    for i in range(number_list_range):
        num_list[i] = random.randint(1, 99)
    return num_list

def user_list():
    list_length = 10
    list_user = [] *list_length
    print("--Add 20 numbers to the list--")
    for i in range(list_length):
        while True:
            user_num = input(f"Enter numer #{i + 1}: ")
            if user_num.isdigit():
                user_num = int(user_num)
                break
            else:
                print("ERROR: Enter only numbers.")
        list_user[i] = user_num
    return list_user

def display_data(list_num):
    list_min = min(list_num)
    list_max = max(list_num)
    list_sum = sum(list_num)
    list_average = list_sum / len(list_num)

    print(f"List min: {list_min}")
    print(f"List max: {list_max}")
    print(f"List total: {list_sum}")
    print(f"List average: {list_average:.2f}")


if __name__ == '__main__':
    main()