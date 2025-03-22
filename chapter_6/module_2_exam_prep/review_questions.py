"""

1. Write the definition for a function switch that receives as parameters
first_name and last_name and prints them in reverse order.
Write the call to the function from main, passing two names as parameters.

2. Write the function header for a function fun1 that will be receiving
one number as a parameter.
Write the call to the function from main, passing a number to the function.

3. Write the code necessary to randomly generate an integer
between 1 and 100 and store it in the variable rand1.

4. One foot equals 12 inches. Write the definition for a function
named feet_to_inches that accepts a number of feet as an argument,
and returns the number of inches in that many feet.

5. Write the code to call the function in the previous problem from main,
passing it 19 feet.  Store the result in a variable named result.

6. Write  a loop that sums up of all the numbers that are divisible
by 3 between 1 and 20. The final sum should be printed when the loop is done.
Hint: If a number is divisible by 3, the remainder when the number is divided by 3 is zero.
A main function is not required – just the loop and the variables that need to be initialized.

7. Write an IPO chart for a function called read_scores_compute_average which receives
an integer that indicates how many scores to read in from the user, reads them in,
using a loop, and  returns the average of all the scores.

8. Write Python code to implement the previous problem.

9. Write an IPO chart for a function called calc_circle_is_bigger_than_square
that receives as arguments the radius of a circle and the length of the side of a square.
The function should return three things: a Boolean that indicates whether the area of
the circle is greater than the area of the square and the areas of the two shapes.

10. Write the Python code that implements the calc_circle_is_bigger_than_square function
from the previous problem. Use the math module for math.pi.

11. Write the call to the previous function from main, passing a radius of 25 and
a length of 10 receiving the values returned from the function.

12. Write code that opens an output file with the filename numberList.txt but
does not erase the file’s contents if it already exists.

13. Write a program that writes random integers to a file.
The program should read in two numbers from the user:
one that specifies how many random numbers to generate,
and one that specifies the top of the range of random numbers
(that is, 100 if the user wants numbers between 1 and 100, inclusive).
Write the numbers to a file called "random_numbers.txt". Put each number on a new line.

14. Write a program that reads in numbers from the file from the previous
problem and computes the average of the numbers.
Read the numbers in from "random_numbers.txt".

15. What will the following code display?
try:
    x = float ('abc123')
    print ('The conversion is complete')
except IOError:
    print ('This code caused an IOError.')
except ValueError:
    print ('This code caused a ValueError.')
print ('The end.')


16. What will the following code display?
try:
    x = float ('abc123')
    print (‘x')
except IOError:
    print ('This code caused an IOError.')
except ZeroDivisionError:
    print ('This code caused a ZeroDivisionError.')
except:
    print (‘An error happened.')
print ('The end.')

17. Write a function that receives degrees as an argument
and uses a function in the math module to convert degrees to radians.
It should return radians to the calling program.

18. Rewrite the following code so it calls
the range function instead of using the list [0,1,2,3,4,5]:

for x in [0,1,2,3,4,5]:
	print ('Hello World!')

19. Write a loop that calculates the total of the following series of numbers:

1/30   + 2/29   +    3/28   . . . . + 30/1

20. Write the statements needed to randomly select a number
from the following sequence:  0, 5, 10, 15, 20, 25, 30.

21. Write a statement that uses a math module function to get
the square root of 100 and assigns it to a variable.

22. Assume the file data.txt exists and contains several lines of text.
Write a short program using the while loop that displays each line in the file.

23. Rewrite the program from the above question using a for loop instead of a while loop.

24. What does it mean when the readline method returns an empty string?
"""


