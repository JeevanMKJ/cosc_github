"""
Write a program that asks the user for the name of a file.
The program should display the contents of the file with
each line preceded with a line number followed by a colon.
The line numbering should start at 1.
"""

def main():
    file_name = input("Enter file name: ")

    with open(f'{file_name}', 'r') as file:
        line = file.readline()
        count = 0

        while line != '':
            line = line.strip('\n')
            count += 1
            print(f"{count:<2} : {line:<2}")

            line = file.readline()


if __name__ == '__main__':
    main()