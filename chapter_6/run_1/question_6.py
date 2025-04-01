"""
6. Write a loop that sums up of all the numbers that are divisible
by 3 between 1 and 20. The final sum should be printed when the loop is done.
Hint: If a number is divisible by 3, the remainder when the number is divided by 3 is zero.
A main function is not required – just the loop and the variables that need to be initialized.
"""

total = 0

for i in range(1, 20):
    if (i / 3) == 3:
        total += i

print(total)