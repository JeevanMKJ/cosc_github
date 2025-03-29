"""
Write a program that gives simple math quizzes.
The program should display two random numbers that are to be added, such as:
247 + 129
The program should allow the student to enter the answer.
If the answer is correct, a message of congratulations should be displayed.
If the answer is incorrect, a message showing the correct answer should be displayed.
"""
import random
import math

def main():
    quiz()

def quiz():
    play = True
    score = 0
    count = 0

    while play:
        print("This is a math quiz game.")
        count += 1

        rand_list = [random.randint(1, 500), random.randint(1, 500)]
        #print(rand_list[0], rand_list[1])
        num_sum = sum(rand_list)
        print(num_sum)

        while True:
            user_sum = input(f"\nQuestion #{count}. Enter the sum for {rand_list[0]} + {rand_list[1]} : ")
            if user_sum.isdigit():
                user_sum = float(user_sum)
                break
            else:
                print("ERROR. Enter ONLY numbers.")

        if num_sum == user_sum:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer.")

        again = input("Play again (Y/N)?: ")
        if again.upper() == "Y":
            continue
        else:
            print(f"Your score: {score}/{count}")
            print("Thank you for playing.")
            play = False


if __name__ == '__main__':
    main()