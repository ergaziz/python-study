"""Sample class"""

class MyClass:
    pass

# >>> from sampleclass import MyClass
# >>> MyClass
# <class 'sampleclass.MyClass'>
# >>> myObj = MyClass()
# >>> myObj
# <sampleclass.MyClass object at 0x024E47F0>
# >>> type(myObj)
# <class 'sampleclass.MyClass'>


class Flight:

    def __init__(self, number):  # this is initiazlier, not constructor. "self" is similar to "this"
        self._number = number  # why _number? to avoid name clash, and convention is that implementation details start with underscore

    def number(self):
        return self._number

# Method - A function defined in the class
# Istance Method - Functions which can be called on objects
# self - the first argument to all instance methods

# >>> from sampleclass import Flight
# >>> f = Flight("TK002")
# >>> f.number()
# 'TK002'

# >>> f._number
# 'TK002'
# We can access to implementation details from repl as well. We are all consenting adults here. Nothing private or protected. haha!


class Flight2:

    def __init__(self, number): 
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))
        
        if not number[:2].isupper():
            raise ValueError("Invalid airline code in {}".format(number))
        
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number in {}".format(number))
        
        self._number = number 

    def number(self):
        return self._number



# Object oriented programming demonstration : check airtravel.py
# THere is polymorphism demonstration as well.
    # def make_boarding_cards(self, card_printer): # here we inject behavior. 
    #     for passenger, seat in sorted(self._passenger_seats()):
    #         card_printer(passenger, seat, self.number(), self.aircraft_model())

    # def console_card_printer(passenger, seat, flight_number, aircraft):
    #     output = "| Name: {0}"     \
    #             "  Flight: {1}"   \
    #             "  Seat: {2}"     \
    #             "  Aircraft: {3}" \
    #             " |".format(passenger, flight_number, seat, aircraft)
    #     banner = '+' + '-' * (len(output) - 2) + '+'
    #     border = '|' + ' ' * (len(output) - 2) + '|'
    #     lines = [banner, border, output, border, banner]
    #     card = '\n'.join(lines)
    #     print(card)
    #     print()


# ### Summary of classes
# * All types in Python have a 'class'
# * Classes define the structure and behavior of an object
# * Class is determined when object is created 
# * * normally fixed for the lifetime
# * Classes are the key support for Object-Oriented Programming in Python
# * Classes defined using the class keyword followed by CamelCase name
# * Class instances created by calling the class as if it were a function
# * Instance methods are functions defined inside the class
# * *  Should accept an object instance called self as the first parameter
# * Methods are called using instance.method()
# * *  Syntactic sugar for passing self instance to method
# * The optional __init__() method initialized new instances
# * *  If present, the constructor calls __init__()
# * *  __init__() is not the constructor
# * Arguments passed to the constructor are forwarded to the initializer
# * Instance attributes are created simply by assigning to them
# * Implementation details are denoted by a leading underscore
# * *  There are no public, protected or private access modifiers in Python
# * Accessing implementation details can be very useful
# * *  Especially during development and debugging
# * Class invariants should be established in the initializer
# * *  If the invariants can't be established raise exceptions to signal failure
# * Methods can have docstrings, just like regular functions
# * Classes can have docstrings
# * Even within an object method calls must be preceded with self
# * You can have as many classes and functions in a module as you wish
# * *  Related classes and global functions are usually grouped together this way
# * Polymorphism in Python is achieved through duck typing
# * Polymorphism in Python does not use shared base classes or interfaces
# * Class inheritance is primarily useful for sharing implementation
# * All methods are inherited, including special methods like the initializer

# * Strings support slicing, because they implement the sequence protocol
# * Following the Law of Demeter can reduce coupling
# * We can nest comprehensions
# * It can sometimes be useful to discard the current item in a comprehension
# * When dealing with one-based collections it's often easier just to waste one
# list entry.
# * Don't feel compelled to use classes when a simple function will suffice
# * Comprehensions or generator expression can be split over multiple lines
# * Statements can be split over multiple lines using backslash
# * * Use this feature sparingly and only when it improves readability
# * Use “Tell! Don’t ask.” to avoid tight coupling between objects