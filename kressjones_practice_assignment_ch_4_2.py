# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program takes two input values from the user and multiplies the all the values between the two values by 10.
# Then the program continues to calculate the sum of the values between the two numbers. 

total = 0
another_round = "Y"

while another_round == "Y" or another_round == "y":

    user_num_low = input("Give a low number: ")
    user_num_high = input("Give a high number: ")

# To prevent the program from crashing when the user inserts a str instead of an int I added a while loop.
# I additionally added a while loop that checks whether the low number is lower than the high number.
    while not (user_num_low.isdigit()) or not (user_num_high.isdigit()):
        print("ERROR.\nPlease input a number.")
        user_num_low = input("Give a low number: ")
        user_num_high = input("Give a high number: ")

    user_num_low = int(user_num_low)
    user_num_high = int(user_num_high)

# Here the two while loops are checking whether the input user_num_low is less than user_num_low and if it is an int. 
    while not user_num_low <= user_num_high:
        print("ERROR.\nPlease input a low and high number.")
        user_num_low = input("Give a low number: ")
        user_num_high = input("Give a high number: ")

        while not (user_num_low.isdigit()) or not (user_num_high.isdigit()):
            print("ERROR.\nPlease input a number.")
            user_num_low = input("Give a low number: ")
            user_num_high = input("Give a high number: ")

        user_num_low = int(user_num_low)
        user_num_high = int(user_num_high)

    print("\nNumber\tNumber * 10")
    for num in range(user_num_low, user_num_high + 1):
        print(f"{num}\t\t{num * 10}")

    for num in range(user_num_low, user_num_high + 1):
        total += num

    print(f"\nThe sum of numbers between {user_num_low} and {user_num_high} is {total}.")
    another_round = input("Do you want to input more numbers? (Y/N): ")

print("Thank you for playing.")
