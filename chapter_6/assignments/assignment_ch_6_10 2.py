# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete

"""
10. Golf Scores
The Spring fork Amateur Golf Club has a tournament every weekend.
The club president has asked you to write two programs:

1. A program that will read each player’s name and golf score as keyboard input,
then save these as records in a file named golf.txt.
(Each record will have a field for the player’s name and a field for the player’s score.)

2. A program that reads the records from the golf.txt file and displays them.
"""

def main():
    #write_data_to_file()
    read_data_from_file()

def write_data_to_file():
    scores_file = open('golf.txt', 'w')

    while True:
        num = input("How many players and their scores will be entered?: ")
        if num.isdigit():
            num = int(num)
            break
        else:
            print("ERROR: Enter a number (positive integer).")

    for i in range(num):
        player_name = input("Enter the players name: ")
        player_score = input("Enter payers score: ")

        scores_file.write(f'{player_name}\n')
        scores_file.write(f'{player_score}\n')

    scores_file.close()
    print("Entered player names and player scores to file.")


def read_data_from_file():
    scores_file = open('golf.txt', 'r')

    while True:
        name_line = scores_file.read().strip('\n')
        if not name_line:
            break

        score_line = scores_file.read().strip('\n')

        print(f"{name_line} {score_line}")

    scores_file.close()

if __name__ == '__main__':
    main()