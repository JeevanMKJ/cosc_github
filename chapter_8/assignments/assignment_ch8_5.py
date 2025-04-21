"""
5. Alphabetic Telephone Number Translator
Many companies use telephone numbers like 555-GET-FOOD
so the number is easier for their customers to remember.
On a standard telephone, the alphabetic letters are
mapped to numbers in the following fashion:
A, B, and C = 2
D, E, and F = 3
G, H, and I = 4
J, K, and L = 5
M, N, and O = 6
P, Q, R, and S = 7
T, U, and V = 8
W, X, Y, and Z = 9
Write a program that asks the user to enter
a 10-character telephone number in the format
XXX-XXX-XXXX.
The application should display the telephone
number with any alphabetic characters that
appeared in the original translated to their
numeric equivalent. For example,
if the user enters 555-GET-FOOD,
the application should display 555-438-3663.
"""

def main():
    user_phone, phone_number = user_phone_number()

    for i in range(len(user_phone)):
        if not user_phone[i].isdigit() and user_phone[i].isalnum():
            index_num = get_letter_index(user_phone, i)
            phone_number.append(index_num)

    phone_number_str_list = [str(i) for i in phone_number]
    phone_number_str_list.insert(3, '-')
    phone_number_str_list.insert(7, '-')
    numbered_phone_number = ''.join(phone_number_str_list)
    print(f"Alphabetic Telephone Number: {user_phone}")
    print(f"Numeric Telephone Number: {numbered_phone_number}")

def user_phone_number():
    print("--Alphabetic Telephone Number Translator--")
    while True:
        user_phone = input("Enter phone number in format XXX-XXX-XXXX: ")
        if len(user_phone) == 12:
            break
        else:
            print(f"ERROR: Phone number too long, currently {len(user_phone)} elements.")

    #user_phone = "555-GET-FOOD"
    phone_number = []
    for i in range(len(user_phone)):
        if user_phone[i].isdigit():
            phone_number.append(int(user_phone[i]))
    return user_phone, phone_number

def get_letter_index(user_phone, index):
    abc_list = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"],
                ["J", "K", "L"],
                ["M", "N", "O"],
                ["P", "Q", "R", "S"],
                ["T", "U", "V"],
                ["W", "X", "Y", "Z"]]
    index_shift_factor = 2
    for r in range(len(abc_list)):
        for c in range(len(abc_list[r])):
            if user_phone[index] in abc_list[r][c]:
                user_phone_index = r + index_shift_factor
                return user_phone_index

if __name__ == '__main__':
    main()