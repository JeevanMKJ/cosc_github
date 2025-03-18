# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program calculates the star rating for a restaurant based upon critics ratings.
# I deviated from the instructions and added the functionality
# that the user can decide how many critics will give a rating in a third function.


MIN_SCORE = 0
MAX_SCORE = 10

# The main function holds two loops:
# The first loop asks the user how many critics will give their rating and validates the input
# The second loop has a for-while nested loop structure. The for loop iterates over num_critics.
# The nested while loop prompts the use to enter critics score and validates the input
# and adds the score to the total score and then breaks the loop.
# Lastly the main() function calculates the average_score, prints the total and average scores
# and calls the determine_stars() function.
def main():
    num_critics = get_num_critics()
    total_score = 0

    for c in range(1, num_critics + 1):
        while True:
            score_input = input(f"Enter #{c} critics score between {MIN_SCORE}-{MAX_SCORE}: ")

            if score_input.replace(".", "", 1).isdigit():
                score = float(score_input)
                if MIN_SCORE <= score <= MAX_SCORE:
                    total_score += score
                    break
                else:
                    print(f"ERROR: Enter critic's score between {MIN_SCORE}-{MAX_SCORE}.")
            else:
                print(f"ERROR: Enter critic's score between {MIN_SCORE}-{MAX_SCORE}.")

    average_score = total_score / num_critics

    print(f"\nNumeric score: {total_score:.2f}")
    print(f"Average numeric score: {average_score:2f}")

    determine_stars(average_score)


# This function asks the user for the number of critics that they want to have give their rating.
def get_num_critics():
    while True:
        num_critics = input("Enter the number of critics that will give a rating: ")
        if num_critics.isdigit() and int(num_critics) > 0:
            num_critics = int(num_critics)
            break
        print("ERROR. Please enter a positive integer.")
    return num_critics


# The determine_stars() function takes the average score and calculated from the main() function and uses
# if-elif-else to determine the corresponding star rating.
def determine_stars(num_score):

    if num_score > 9:
        stars = "*****"
    elif 7.9 <= num_score <= 9:
        stars = "****"
    elif 6.9 <= num_score <= 7.9:
        stars = "***"
    elif 5.9 <= num_score <= 6.9:
        stars = "**"
    elif 5.0 <= num_score <= 5.9:
        stars = "*"
    else:
        stars = ""

    print(f"\nYour score of {num_score:.1f} gives you {len(stars)} stars: {stars}")

if __name__=="__main__":
    main()
