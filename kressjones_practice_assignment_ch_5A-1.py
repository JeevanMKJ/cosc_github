# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program outlines the steps to create a sandwich. 
# I added a few additional features that were not required by the instructions.
# These include: 1) prompting user for name and using it in the intro_message() and exit_message() functions
# 2) Instead of printing all the steps of making a sandwich all at one when the main() function is called. 
# The user is prompted to type ENTER every time they are ready to pregress to the next step in making the sandwich. 


def main():
    user_name = input("Hi, what is your name?: ")

    intro_message(user_name)
    input("\nPress ENTER to see step 1: ")
    gather_ingredients()
    input("\nPress ENTER to see step 2: ")
    prep_bread()
    input("\nPress ENTER to see step 3: ")
    add_condiments()
    input("\nPress ENTER to see step 4: ")
    add_main_ingredients()
    input("\nPress ENTER to see step 5: ")
    add_toppings()
    input("\nPress ENTER to see step 6: ")
    assemble_sandwich()
    exit_message(user_name)

def intro_message(name):
    print(f"Hello {name}.\nToday you will learn to make a sandwich.")
    print("Read through the instructions for each step and follow along.\nWhen you are ready to continue press ENTER.")

def gather_ingredients():
    print("Step 1: Gather all ingredients")
    print("- Bread slices")
    print("- Condiments (mayo, mustard, etc.)")
    print("- Main ingredients (meat, cheese, etc.)")
    print("- Toppings (lettuce, tomato, etc.)")

def prep_bread():
    print("Step 2: Prepare the bread")
    print("- Take two slices of bread")
    print("- Toast the bread if desired")

def add_condiments():
    print("Step 3: Add condiments")
    print("- Spread mayo, mustard, or other condiments on the bread slices")
    print("- Make sure to spread evenly")

def add_main_ingredients():
    print("Step 4: Add main ingredients")
    print("- Place meat (ham, turkey, etc.) on one slice of bread")
    print("- Add cheese if desired")

def add_toppings():
    print("Step 5: Add toppings")
    print("- Add lettuce, tomato, onions, or other vegetables")
    print("- Add any other desired toppings")

def assemble_sandwich():
    print("Step 6: Assemble the sandwich")
    print("- Place the second slice of bread on top")
    print("- Press gently to secure all ingredients")
    print("- Cut the sandwich in half if desired")

def exit_message(name):
    print(f"\nEnjoy your sandwich {name}!")

if __name__=="__main__":
    main()
