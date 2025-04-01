"""
5. Write the code to call the function in the previous problem from main,
passing it 19 feet. Store the result in a variable named result.
"""

from question_4 import feet_to_inches

def main():
    feet = 19
    print(f"{feet_to_inches(feet)} inches.")


if __name__ == '__main__':
    main()