# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program checks if a given date is a "magic date". Meaning if day * month is equal to year.

user_month = int(input("Give month of birth as a number: "))
user_day = int(input("Give day of birth: "))
user_year = input("Give the last two numbers of your birth year: ")

if len(user_year) == 4:
    user_year = int(user_year[-2:])
else:
    user_year = int(user_year)

if 1 <= user_month <= 12 and 1 <= user_day <= 31:
    if user_month * user_day == user_year:
        print(f"{user_month}/{user_day}/{user_year} is a magical date.")
    else:
        print(f"You are normal: {user_month}/{user_day}/{user_year}.")
else:
    print("ERROR. Your month (1-12) or day (1-31) are out of range..")
