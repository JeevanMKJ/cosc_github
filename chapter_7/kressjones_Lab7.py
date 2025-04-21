# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program accepts 10 integers from the user and a search number n,
# then displays all numbers from the list that are greater than n.

# Main function to control program flow
def main():
    num_list = create_list()
    n_number = special_number()
    display_larger(num_list, n_number)

# Function to create a list of 10 integers from user input
def create_list():
    user_list_length = 10
    user_list = [0] * user_list_length
    print("--Enter 10 numbers to the list--")
    for i in range(len(user_list)):
        while True:
            user_num = input(f"Enter number #{i + 1}: ")
            if user_num.isdigit():
                user_num = int(user_num)
                break
            else:
                print("ERROR: Only enter numbers.")
        user_list[i] = user_num
    return user_list

# Function to get the special number n from the user
def special_number():
    print("--Enter a special number to which the list will be compared against--")
    while True:
        sp_num = input("Enter special number: ")
        if sp_num.isdigit():
            sp_num = int(sp_num)
            break
        else:
            print("ERROR: Only enter numbers.")
    return sp_num

# Function to display numbers from the list that are greater than n
def display_larger(num_list, n_number):
    compared_list = []
    for i in range(len(num_list)):
        if num_list[i] > n_number:
            compared_list.append(num_list[i])
    print(f"\nOriginal list: {num_list}")
    print(f"Special number n: {n_number}")
    print(f"Numbers greater than {n_number}: {compared_list} ")
    num_list.sort()
    compared_list.sort()
    print("\n--Sorted versions of same lists--")
    print(f"Sorted original list: {num_list}")
    print(f"Sorted numbers greater than {n_number}: {compared_list} ")
    return compared_list

if __name__ == '__main__':
    main()