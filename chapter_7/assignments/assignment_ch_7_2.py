"""
2. Lottery Number Generator
Design a program that generates a seven-digit lottery number.
The program should generate seven random numbers,
each in the range of 0 through 9, and assign each number to a list element.
(Random numbers were discussed in Chapter 5.)
Then write another loop that displays the contents of the list.
"""
import random

def main():
    lottery_numbers = rand_num_list()
    user_ticket = user_lottery_ticket()
    compare_lottery_ticket(lottery_numbers, user_ticket)
    read_num_list(lottery_numbers)

def rand_num_list():
    seven_digits = 7
    num_list = [0] * seven_digits
    for index in range(len(num_list)):
        num_list[index] = random.randint(0, 9)
    return num_list

def read_num_list(number_list):
    print("\n--Lottery Numbers--")
    for i in range(len(number_list)):
        print(f"{number_list[i]}")

def user_lottery_ticket():
    print("--Chose your lottery numbers--")
    while True:
        user_number = input("Enter 7 digits (0-9): ")
        if user_number.isdigit() and len(user_number) == 7:
            user_number = int(user_number)
            break
        else:
            print("ERROR: Only use 7 numbers.")

    return user_number

def compare_lottery_ticket(numbers, ticket):
    lottery_reward = (random.randint(2, 10)) ** (random.randint(1, 10))
    if numbers == ticket:
        win = True
        print(f"You won the lottery.\nPrize money ${lottery_reward:,.2f}")
    else:
        win = False
        print(f"You lost.\nMoney you did not make ${lottery_reward:,.2f}")

if __name__ == '__main__':
    main()
