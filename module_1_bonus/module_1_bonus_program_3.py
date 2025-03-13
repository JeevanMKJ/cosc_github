# This function takes in a decimal number and converts it to its
# binary value.

def program_3():
    while True:
        print("Convert number to binary.")

        user_float = float(input("Enter a decimal number: "))
        user_int = int(user_float)

        if user_int == 0:
            user_int = "0"
        else:
            binary = ""
            while user_int > 0:
                remainder = user_int % 2
                binary = str(remainder) + binary
                user_int = user_int // 2

            print(f"{binary}")

        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.upper() != "Y":
            break
