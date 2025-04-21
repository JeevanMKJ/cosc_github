"""
3. Date Printer
Write a program that reads a string from the user containing
a date in the form mm/dd/yyyy.
It should print the date in the format March 12, 2018.
"""

def main():
    date_list = user_date()
    month_selector(date_list)

def user_date():
    print("--Date format converter--")
    while True:
        date = input("Enter date in format mm/dd/yyyy: ")
        #date = "09/23/2000"
        if len(date) == 10:
            break
        else:
            print("ERROR: Date length is too long.")

    token_list = date.split('/')

    return token_list

def month_selector(date_list):
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August",  "September", " October", "November", "December"]
    int_list = []
    for i in date_list:
        int_list.append(int(i))

    month = int_list[0]

    print(f"{month_list[month - 1]} {int_list[1]}, {int_list[2]}")

if __name__ == '__main__':
    main()