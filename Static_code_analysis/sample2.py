"""
This module provides a simple example of adding two numbers using a function.
It demonstrates the creation of a function, variable initialization, and string formatting.
"""
def add(number1, number2):
    """
    adds two numbers and returns the result

    Args:
        number1(int or float) the first number to be added
        number2(int or float) the second number to be added

    returns:
        int or float: the sum of number1 and number2
    """
    return number1 + number2

# Initialize the constant variable 'NUM1' with the value 4.
# Constants are usually written in uppercase letters to indicate that they should not be changed.
NUM1 = 4

# Initialize the variable 'num2' with the value 5.
# This variable will be used as the second input to the 'add' function.
NUM2 = 5

# Call the 'add' function with 'NUM1' and 'num2' as arguments.
# The result of this addition operation is stored in the variable 'total'.
TOTAL = add(NUM1, NUM2)

# Print a formatted string that displays the sum of 'NUM1' and 'num2'.
# The 'format' method is used to insert the values of 'NUM1', 'num2', and 'total' into the string.
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
