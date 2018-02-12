def create_tuple():
    a = ("element", 4.13, 9)  # this is a tuple, immutable sequence of arbitrary objects
    print(a[1])
    print(len(a))
    return a


def add_tuple(my_tuple):
    return my_tuple + ('a', 5)  # this creates new tuple


def multiply_tuple(my_tuple):
    return my_tuple * 3  # allows multiplication


def create_nested_tuple():
    a = (('a', 'b'), (1, 2), ('c', 'd', 'f'))
    print(a)
    print(a[2])
    print(a[2][1])


def some_tuples():
    a = (234)
    print(a)
    print(type(a))  # not one element tuple because it thinks of parantheses as math
    b = (234,)  # this is how to define one element tuple
    print(b)
    print(type(b))
    c = ()
    print(c)
    print(type(c))
    d = 1, 2, 4, 5, 5, 6, 98
    print(d)
    print(type(d))
    e = tuple([3, 5, 8, 120])
    print(e)
    print(type(e))


def min_max(items):
    return min(items), max(items)  # tuples are useful for multiple values return


def tuple_unpacking():
    lower, upper = min_max([23, 43, 56, 34, 89, 1])
    print(lower)
    print(upper)
    (a, (b, c), d) = (1, (2, 3), 4)
    print(a)
    print(b)
    print(c)
    print(d)


def swap():
    a = 'hey'
    b = 'hoo'
    (a, b) = (b, a)
    print(a)
    print(b)


def contains(items, item):
    return item in items  # this works for collections, tuples also. "not in" also works.


# Summary of Collections
# Tuples are immutable sequence types.
# tuple create : Just optional parenthesis around a comma seperated list.
# tuple unpacking : return multiple values. used for swap
# strings are immutable sequence
# best concat is join() for empty seperator
# partition() is useful parsing tool
# format() is useful as well
# ranges are arithmetic progressions
# enumerate() is superior alternative to range()
# lists are heterogenous mutable sequence types
# dictionaries : maps immutable keys to mytable values
# set : unordered collection of unique elements
