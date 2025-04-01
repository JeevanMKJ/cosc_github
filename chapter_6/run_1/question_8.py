"""
7. Write an IPO chart for a function called read_scores_compute_average which receives
an integer that indicates how many scores to read in from the user, reads them in,
using a loop, and  returns the average of all the scores.

8. Write Python code to implement the previous problem.
"""

def main():
    read_scores_compute_average()

def read_scores_compute_average():
    num_scores = int(input("How many scores will be entered?: "))

    total = 0

    for i in range(1, num_scores + 1):
        score = int(input(f"Enter score # {i}: "))
        #print(score)
        total += score

    avg_score = total / num_scores

    print(f"Average score: {avg_score}")


if __name__ == '__main__':
    main()