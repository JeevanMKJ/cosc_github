# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# The program writes the numbers 50 through 100 to a txt file.
# Then the program reads the numbers 50 through 100 and prints them to the terminal.

def main():
    program_1()
    program_2()

def program_1():

    list_file = open('../number_list.txt', 'w')

    for i in range(50, 101, 1):
        list_file.write(f'{i}\n')

    list_file.close()


def program_2():

    list_file = open('../number_list.txt', 'r')

    for line in list_file:
        num = line
        num = num.strip('\n')
        num = int(num)

        print(f"{num}")

    list_file.close()

if __name__ == '__main__':
    main()