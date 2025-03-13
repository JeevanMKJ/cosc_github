import random

# This function included all the logic for the number guess game. The user input
# is validated. When the user guesses the correct number they can choose to play
# again or exit to the main menu. 

def program_1():
    print("Guess the number.")

    rand_num = random.randint(1, 10)

    while True:
        while True:
            user_guess_number = input("Guess the number between 1 and 10: ")
            if user_guess_number.isdigit() and 1 <= int(user_guess_number) <= 10:
                user_guess_number = int(user_guess_number)
                break
            else:
                print("ERROR")

        if rand_num == user_guess_number:
            print("Correct Number!")
            play_again = input("Do you want to play again? (Y/N): ")
            if play_again.upper() == "Y":
                rand_num = random.randint(1, 10)
            else:
                break
        elif user_guess_number > rand_num:
            print("You are too HIGH. Try again.")
        elif user_guess_number < rand_num:
            print("You are too LOW. Try again.")
        else:
            print("ERROR")
