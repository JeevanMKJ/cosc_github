"""
Write a program that asks the user to enter five test scores.
The program should display a letter grade for each score and the
average test score.
Write the following functions in the program:
• calc_average. This function should accept five test scores as
    arguments and return the average of the scores.
• determine_grade. This function should accept a test score as an
    argument and return a letter grade for the score based on the following grading scale:
"""

def main():
    avg_score, scores_list = calc_average()

    letter_scores_list = determine_grade(scores_list)

    display_scores(scores_list, letter_scores_list)

    save_scores = input("Save scores to txt file (Y/N): ")
    if save_scores.upper() == "Y":
        scores_to_txt(scores_list, letter_scores_list)

def calc_average():

    while True:
        num_scores = input("Enter number of test scores that will be inputted: ")
        if num_scores.isdigit():
            num_scores = int(num_scores)
            break
        else:
            print("ERROR. Enter ONLY numbers.")

    scores = []

    for i in range(1, num_scores + 1):
        while True:
            score = input(f"Enter #{i} score: ")
            if score.isdigit():
                score = int(score)
                break
            else:
                print("ERROR. Enter ONLY numbers.")

        scores.append(score)

    scores_sum = sum(scores)
    scores_average = scores_sum / len(scores)
    print(f"\nAverage test score: {scores_average}")

    return scores_average, scores


def determine_grade(scores_list):
    letter_scores = []

    for i in range(len(scores_list)):
        if 90 <= scores_list[i] <= 100:
            letter_score = "A"
        elif 80 <= scores_list[i] <= 89:
            letter_score = "B"
        elif 70 <= scores_list[i] <= 79:
            letter_score = "C"
        elif 60 <= scores_list[i] <= 69:
            letter_score = "D"
        else:
            letter_score = "F"
        letter_scores.append(letter_score)

    return letter_scores


def display_scores(scores_list, letter_scores_list):

    print("\nNum\t\tScore\tLetter Grade")
    print("----------------------------")

    for i in range(len(scores_list)):
        print(f"{i + 1}\t\t{scores_list[i]}\t\t{letter_scores_list[i]}")


def scores_to_txt(scores_list, letter_scores_list):

    try:
        file_name = input("Enter name for txt file: ")

        with open(f'{file_name}.txt', 'w') as scores_file:

            for i in range(len(scores_list)):
                scores_file.write(f"{scores_list[i]}\n")
                scores_file.write(f"{letter_scores_list[i]}\n")

        print(f"Scores have been saved to {file_name}.txt")
    except IOError:
        print("IOError. Can not open file.")
    except ValueError as e:
        print(f"ValueError at {e}")


if __name__ == '__main__':
    main()