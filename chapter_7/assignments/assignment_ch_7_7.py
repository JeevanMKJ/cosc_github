"""
7. Driver’s License Exam
The local driver’s license office has asked you to create an application
that grades the written portion of the driver’s license exam.
The exam has 20 multiple-choice questions. Here are the correct answers:

Your program should store these correct answers in a list.
The program should read the student’s answers for each of
the 20 questions from a text file and store the answers in another list.
(Create your own text file to test the application.)
After the student’s answers have been read from the file,
the program should display a message indicating whether the student
passed or failed the exam.
(A student must correctly answer 15 of the 20 questions to pass the exam.)
It should then display the total number of correctly answered questions,
the total number of incorrectly answered questions,
and a list showing the question numbers of the incorrectly answered questions.
"""
import random

def main():
    correct_answers = ['A', 'B', 'C', 'A',
                       'C', 'C', 'D', 'B',
                       'A', 'A', 'C', 'B',
                       'A', 'C', 'A', 'D',
                       'D', 'B', 'D', 'a']
    #student_answers()
    automatic_student_answers()
    st_answers = read_answers()
    grade_answers(correct_answers, st_answers)

def grade_answers(correct_answers, st_answers):
    total_questions = 20
    min_score = 15
    score = 0
    for i in range(len(correct_answers)):
        if correct_answers[i] == st_answers[i]:
            score += 1
    if score >= min_score:
        passed = True
        print(f"You passed the test with {score} / {total_questions} answered correctly.")
    else:
        passed = False
        print(f"You're score: {score} / {total_questions}\nTo pass you require 75% correct.")

def read_answers():
    student_answer_list = []
    with open('student_answers.txt', 'r') as answer_file:
        for line in answer_file:
            line = line.strip('\n')
            student_answer_list.append(line)
    print(student_answer_list)
    return student_answer_list

def automatic_student_answers():
    valid_answers = ['A', 'B', 'C', 'D']
    question_number = 20
    with open('student_answers.txt', 'w') as a_student_file:
        for i in range(question_number):
            rand_num = random.randint(0, 3)
            answer = valid_answers[rand_num]
            a_student_file.write(f"{answer}\n")
    print("Answers generated and stored in file.")

def student_answers():
    question_number = 20
    valid_letters = ['A', 'B', 'C', 'D']
    print("--Enter your answers--")
    with open('student_answers.txt', 'w') as student_file:
        for i in range(question_number):
            while True:
                student_answer = input(f"Question #{i + 1}: ").strip().upper()
                if student_answer in valid_letters:
                    break
                else:
                    print("ERROR: Only enter A, B, C or D.")
            student_file.write(f"{student_answer}\n")

if __name__ == '__main__':
    main()