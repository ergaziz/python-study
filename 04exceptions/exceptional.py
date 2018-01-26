'''A Module demonstrating exceptions'''

import sys

def convert(s):
    '''Convert to int'''
    x = int(s)
    return x
# lets call this function from cmd and see exception and see :
# >>> from exceptional import convert as con
# >>> con('sd')
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "exceptional.py", line 5, in convert
#    x = int(s)
# ValueError: invalid literal for int() with base 10: 'sd'


def convert_exceptional(s):
    try:
        x = convert(s)
    except ValueError:
        x = -1
    return x
# >>> from exceptional import convert_exceptional as con
# >>> con('asda')
# -1
# >>> con([1,2])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "exceptional.py", line 18, in convert_exceptional
#     x = convert(s)
#   File "exceptional.py", line 5, in convert
#     x = int(s)
# TypeError: int() argument must be a string or a number, not 'list'


def convert_exceptionalpass(s):
    x = -1
    try:
        x = convert(s)
    except (ValueError, TypeError):
        pass  # does nothing
    return x


def convert_exceptionaldetail(s):
    x = -1
    try:
        x = convert(s)
    except (ValueError, TypeError) as e:
        print("Error:{}".format(str(e)))
    return x
# >>> exceptional.convert_exceptionaldetail("sad")
# Error:invalid literal for int() with base 10: 'sad'
# -1

def convert_exceptionaldetailandraise(s):
    x = -1
    try:
        x = convert(s)
    except (ValueError, TypeError) as e:
        print("Error:{}".format(str(e)))
        raise
    return x
# >>> exceptional.convert_exceptionaldetailandraise("sad")
# Error:invalid literal for int() with base 10: 'sad'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "exceptional.py", line 58, in convert_exceptionaldetailandraise
#     x = convert(s)
#   File "exceptional.py", line 7, in convert
#     x = int(s)
# ValueError: invalid literal for int() with base 10: 'sad'

def raisezeroerror(x):
    '''This method raises an error when given zero.

    Args: 
        x: num to divide 1

    Returns:
        1/x

    Raises:
        ValueError: if x is 0
    '''
    if x==0:
        raise ValueError("Cannot divide by zero")

        return 1/x
# >>> from exceptional import raisezeroerror as raze
# >>> raze(1)
# >>> raze(0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "exceptional.py", line 89, in raisezeroerror
#     raise ValueError("Cannot divide by zero")
# ValueError: Cannot divide by zero

# Common exception types to use :
# - IndexError : out of range
# - KeyError : lookup fails
# - ValueError : wrong value 
# - TypeError : wrong type (avoid using this)

def makedir(dirname):
    original_path = os.getcwd()
    try:
        os.mkdir(dirname)
    finally:
        os.chdir(original_path)

# Zen : ERRORS SHOULD NEVER PASS SILENTLY, UNLESS EXPLICITLY SILENCED. Errors are bells. if we make them silent, they are of no use.

# Summary of Excveptions:
# * Raising an exception interrupts flow and transfers control to an exception handler
# * Handlers defined uşing try...except
# * programmer errors should not be handled
# * exception conditions can be signalled using `raise`
# * raise without argument re-raises the current exception
# * do not check for TypeErrors
# * exceptions can be converted using str()
# * exceptions should be documented properly
# * use built-in exceptions if possşible
# * use try...finally to cleanup things
# * print() can be redirected using optional `file` argument.
# * platform-specific actionws can be implemented using EAFP along with catching ImportErrors
