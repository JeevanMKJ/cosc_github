# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program writes my age and name as well as the name of a user to a txt file.
# The program then reads the information and prints it to the terminal.

def main():
    program_1()
    program_2()

def program_1():
    MY_NAME = "Jeevan Morgan Kress-Jones"
    MY_AGE = 24
    user_name = input("What is your name?: ")

    user_info_file = open('../my_name.txt', 'w')

    user_info_file.write(f'{MY_NAME}\n')
    user_info_file.write(f'{user_name}\n')
    user_info_file.write(f'{MY_AGE}\n')

    user_info_file.close()

def program_2():
    read_user_info_file = open('../my_name.txt', 'r')

    my_name = str(read_user_info_file.readline())
    user_name = str(read_user_info_file.readline())
    my_age = str(read_user_info_file.readline())

    my_name = my_name.strip('\n')
    user_name = user_name.strip('\n')
    my_age = my_age.strip('\n')

    my_age_int = int(my_age)
    half_my_age = my_age_int // 2

    read_user_info_file.close()

    print(f"My name is: {my_name}.")
    print(f"User name is: {user_name}")
    print(f"My age is: {my_age}")
    print(f"Half my age is: {half_my_age}")

if __name__ == '__main__':
    main()



