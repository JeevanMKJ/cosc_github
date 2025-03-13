# The function takes in 4 inputs and vlaidates if it is a string.
# It then strings the inputs together into a sentence.

def program_5():
    print("Let's make a mad lib mini-story!")

    while True:
        while True:
            noun1 = input("Enter a noun: ")
            adjective1 = input("Enter a adjective: ")
            verb1 = input("Enter a verb: ")
            place = input("Enter a place: ")

            if not noun1.isdigit() and not adjective1.isdigit() and not verb1.isdigit() and not place.isdigit():
                break
            else:
                print("ERROR\nOnly enter words.")

        story = f"The {adjective1} {noun1} was {verb1} at the {place}."

        print("This is your mad lib mini-story.")
        print(story)

        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.upper() != "Y":
            break
