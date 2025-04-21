"""
1. Initials
Write a program that gets a string containing a person’s first,
middle, and last names, and displays their first, middle,
and last initials. For example, if the user enters
John William Smith, the program should display J. W. S.
"""

"""
def main():
    user_names = input("Enter first, middle and last name: ")

    names_list = user_names.split()

    initials = []

    for i in range(len(names_list)):
        initials.append(names_list[i][0])

    for i in range(len(initials)):
        print(f"{initials[i]}.", end = " ")
    print()

if __name__ == '__main__':
    main()
"""

def main():
    #user_names = input("Enter first, middle and last name: ")
    user_names = "Jeevan Morgan Kess-Jones"

    names_list = user_names.split()

    initials = '. '.join(name[0] for name in names_list)

    print(f"{initials}.")

if __name__ == '__main__':
    main()
