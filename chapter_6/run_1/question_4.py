"""
4. One foot equals 12 inches. Write the definition for a function
named feet_to_inches that accepts a number of feet as an argument,
and returns the number of inches in that many feet.
"""

def main():
    feet = int(input("How many feet?: "))
    print(f"{feet_to_inches(feet)} inches.")

def feet_to_inches(feet):
    inches = feet * 12
    return inches

if __name__ == '__main__':
    main()