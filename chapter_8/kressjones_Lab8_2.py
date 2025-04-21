# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program takes in a date in a mm/dd/yyyy format.
# The format and input are validated.
# Lastly the original date input is formatted to
# month (written out) date, year

def main():
    date_list = user_date()
    month_selector(date_list)

def user_date():
    print("--Date format converter--")
    while True:
        date = input("Enter date in format mm/dd/yyyy: ").strip()
        #date = "09/23/2000"
        tokens = date.split('/')
        if len(tokens) == 3 and all(token.isdigit() for token in tokens):
            mm, dd, yyyy = tokens
            if len(mm) == 2 and len(dd) == 2 and len(yyyy) == 4:
                month = int(mm)
                day = int(dd)
                year = int(yyyy)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    return [mm, dd, yyyy]
                else:
                    print("ERROR: Month or day out of range.")
            else:
                print("ERROR: Incorrect dates format.")
        else:
            print("ERROR: Incorrect format.")

def month_selector(date_list):
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August",  "September", "October", "November", "December"]

    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])
    print("\n--Formatted date--")
    print(f"{month_list[month - 1]} {day}, {year}")

if __name__ == '__main__':
    main()