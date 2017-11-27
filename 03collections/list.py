def test_list():
    s = "This is a sentence to split into a list!".split()
    print(s)

    # use minus index
    print("minus index can be used. Last element: {}".format(s[-1]))

    # slice the items
    print(s[1:4])

    # slice to negative
    print(s[1:-1])  # gives the elements without the first and the last

    # slice to end
    print(s[2:])

    # slice from start
    print(s[:2])

    # complementary
    print(s == s[:2] + s[2:])

    # copy list with slicing : same with s.copy() and list(s)
    full_range = s[:]

def test_list_multiplication():
    d = 3 * [21, 34]
    print(d)  # gives 6 element list

    # be careful with inner lists:
    my_outer_list = [[1, -1]] * 5
    print(my_outer_list)
    my_outer_list[0][0] = 2
    print(my_outer_list)  # see how they are all changed.
    # because all first level list elements are references to mutable lists

