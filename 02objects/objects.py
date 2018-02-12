def is_same_object(a, b):
    """Checks object references

    Args:
        a: first object
        b: second object

    Returns:
        True if the parameters are the same object,
        False if they represent different objects
    """
    # id() gives reference point of the variable.
    # int is immutable object. thus, a=5 does create new int and refer a to that int.
    # garbage collector cleans the not-referred objects
    if id(a) == id(b):  # "a is b" is identical
        return True
    else:
        return False


def test_list_item_modification():
    r = [1, 3, 5]
    s = r
    s[0] = 2
    is_same_object(r, s)  # gives true because both references to same object (list).
    # r and s or any other reference is not a variable, they are named references to objects.


def test_identical_list_comparison():
    p = [1, 2, 3]
    q = [1, 2, 3]
    p == q  # gives true
    is_same_object(p, q)  # gives false


def test_list_object_passing():
    p = [1, 2]

    append39(p)  # appends to referenced list object
    print(p)  # that is why we see 39 here

    override_list(p)  # overrides reference of p
    print(p)  # however it will not be effective in this scope, p still shows appended version


def append39(list_to_append):
    list_to_append.append(39)
    print(list_to_append)


def override_list(list_to_override):
    list_to_override = [5, 6, 7]
    print(list_to_override)


# Summary of Objects
# think of named references to object, not variables.
# garbage collectore rexlaims unreachable pbjects
# id() returns unique constant identifier of object
# is operator checks id()
# test for equivalance is ==
# function args passed by object reference, not value
# return also passes by object reference.
# function args with deafult is evaluated once, when def is executed.
# dynamic typing : we dont specify types
# strong typing : types are not converted to match
# LEGB rule in scoping
# global keyword
# everything is an object
# import and def result in binding to a named references to module or function
# type can be used to determine the type of an object
# dir() can be used to introspect an object and get its attributes
# name , doc attributes
# len()
# multiply string with integer
