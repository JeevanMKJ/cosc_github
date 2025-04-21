# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program goes beyond the requirements of the assignment.
# A random list with 7 integers between 0 and 9 is generated
# and printed to the terminal.
# Then the user can enter their 7 digit lottery number.
# The user lottery number is compared to the generated lottery number,
# and if the user has three or more numbers correct then they win.

import random

# All function calls are organised from main.
def main():
    lottery_numbers = generate_rand_num_list()
    read_num_list(lottery_numbers)
    user_ticket = user_lottery_ticket()
    compare_lottery_ticket(lottery_numbers, user_ticket)

def generate_rand_num_list():
    list_length = 7
    num_list = [0] * list_length
    for index in range(len(num_list)):
        num_list[index] = random.randint(0, 9)
    return num_list

def read_num_list(number_list):
    print("--Lottery Numbers--")
    for i in range(len(number_list)):
        print(f"{number_list[i]}", end = " ")
    print()

def user_lottery_ticket():
    print("--Chose your lottery numbers--")
    while True:
        user_number = input("Enter 7 digits (0-9): ")
        if user_number.isdigit() and len(user_number) == 7:
            user_number = int(user_number)
            break
        else:
            print("ERROR: Only use 7 numbers.")
    lottery_ticket = list(map(int, str(user_number)))
    return lottery_ticket

def compare_lottery_ticket(numbers, ticket):
    lottery_reward = (random.randint(2, 10)) ** (random.randint(1, 10))

    matches = 0
    for num in ticket:
        if num in numbers:
            matches += 1

    if matches >= 3:
        win = True
        adjusted_reward = lottery_reward * (matches / len(numbers))
        print(f"You won the lottery.\nPrize money: ${adjusted_reward:,.2f}")
    else:
        win = False
        print(f"You lost.\nMoney you did not make: ${lottery_reward:,.2f}")

if __name__ == '__main__':
    main()

