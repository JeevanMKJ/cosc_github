# This function takes in two inputs that are validated and converted to int.
# Then the function uses a two for loops (one nested) to print a box based
# upon the dimension that the user provided. 

def program_4():
    while True:
        print("Create an asterix box.")

        while True:
            while True:
                box_height = input("Enter the height: ")
                box_width = input("Enter the width: ")

                if box_height.isdigit() and box_width.isdigit():
                    box_height = int(box_height)
                    box_width = int(box_width)
                    break
                else:
                    print("ERROR")

            if not box_height <= 0 and not box_width <= 0:
                break
            else:
                print("ERROR\nInput must be a positive int.")

        for i in range(box_height):
            for r in range(box_width):
                print("*", end=" ")
            print()

        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.upper() != "Y":
            break
