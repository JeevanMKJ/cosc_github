"""
Write a program that asks the user for the name of a file.
The program should display only the first five lines of the file’s contents.
If the file contains less than five lines, it should display the file’s entire contents.
"""

def main():
    file_name = input("Enter file name: ")

    with open(f'{file_name}', 'r') as file:
        count = 0

        for line in file:
            count += 1
            if count > 5:
                break
            line = line.strip('\n')
            print(line)


if __name__ == '__main__':
    main()