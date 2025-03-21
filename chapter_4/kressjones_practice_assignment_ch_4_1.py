# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program is an improvement upon the code from practice_assignment_ch_3_2.
# The changes include adding a while loop which asks the user if they would like to input another number. 
# If the user enters anything else than "Y" or "y" the loop ends. 

again = "y"

while again == "Y" or again == "y":

    user_day = input("Give a number between 1 and 7: ")

# I used a "while not" to check if the user input is a str or not between 1 and 7.

    while not (user_day.isdigit()) or not (1 <= int(user_day) <= 7):
        print("ERROR. Your input is not between 1 and 7.")
        user_day = input("Give a number between 1 and 7: ")

    user_day = int(user_day)

    if user_day == 1:
        print("It is Monday.")
    elif user_day == 2:
        print("It is Tuesday.")
    elif user_day == 3:
        print("It is Wednesday.")
    elif user_day == 4:
        print("It is Thursday.")
    elif user_day == 5:
        print("It is Friday.")
    elif user_day == 6:
        print("It is Saturday.")
    elif user_day == 7:
        print("It is Sunday.")

    again = input("Do you want to enter another number (Y/N): ")

"""
    else:
        print("ERROR. Please pick a day between 1 and 7.")
"""

print("It was nice to meet you.")
