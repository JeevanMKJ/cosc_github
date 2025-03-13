# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program is a CLI game room with 5 little games. The user can choose which game to play by,
# entering the corresponding number of the game. When the game ends the user is asked if they would like to play the game again.
# In the main menu the user can quit the application.


from module_1_bonus_program_1 import program_1
from module_1_bonus_program_2 import program_2
from module_1_bonus_program_3 import program_3
from module_1_bonus_program_4 import program_4
from module_1_bonus_program_5 import program_5


# The main function calls all the five functions that hold the game logic
# for each game depending on the option that the user selects. 
def main():

    while True:
        print("\nWelcome to the CLI game room.")
        print("Enter the according number to enter the game.")
        print("\n1) What number am I thinking of?")
        print("2) Binary String to Decimal Number Converter")
        print("3) Decimal Number to Binary String Converter")
        print("4) ASCII Box")
        print("5) Mad-Lib Generator")
        print("6) to quit application")

        while True:
            user_input = input("Enter an integer between 1 and 6: ")

            if user_input.isdigit() and 1 <= int(user_input) <= 6:
                user_input = int(user_input)
                break
            else:
                print("ERROR")

        if user_input == 1:
            program_1()
        elif user_input == 2:
            program_2()
        elif user_input == 3:
            program_3()
        elif user_input == 4:
            program_4()
        elif user_input == 5:
            program_5()
        elif user_input == 6:
            print("\nThank you for playing!")
            break
        else:
            print("ERROR")


if __name__=='__main__':
    main()
