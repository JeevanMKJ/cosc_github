# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program takes in the txt file students.txt and prints the
# names of the students along with their scores to the CLI.

def main():

    print(f"Name\t\t\tScore")
    print("---------------------")

    with open('students.txt', 'r') as student_file:

        name = student_file.readline()

        while name != '':
            score = float(student_file.readline())
            name = name.strip('\n')

            print(f"{name:<16}{score:.1f}")

            name = student_file.readline()


if __name__ == '__main__':
    main()