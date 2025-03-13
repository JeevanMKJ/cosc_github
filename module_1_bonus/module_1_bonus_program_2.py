# This function translates an 8 bit byte into its numeric value.

def program_2():
    while True:
        while True:
            user_binary = input("Enter 8 bits to form a byte (use only 1's and 0's): ")

            if all(bit in '01' for bit in user_binary):
                break
            else:
                print("ERROR.\nInvalid input. Please only enter 1's and 0's.")

        decimal_value = 0
        length = len(user_binary)

        for i in range(length):
            bit = int(user_binary[i])
            factor_to_raise = length - i - 1
            decimal_value = decimal_value + bit * (2 ** factor_to_raise)

        print(decimal_value)

        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.upper() != "Y":
            break
