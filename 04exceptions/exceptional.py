'''A Module demonstrating exceptions'''

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