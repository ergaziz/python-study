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


def test_list_index():
    str_list = "My little little stupid sentence".split()
    print(str_list)

    i = str_list.index("little")  # gives 1, first occurence
    print(str_list[i])
    if str_list.count("notexistingword") > 0:
        x = str_list.index("notexistingword")  # gives ValueError

    print(str_list.count("little"))  # gives 2

    exists = "little" in str_list
    print(exists)
    notexists = "big" not in str_list
    print(notexists)

    del str_list[3]  #removes the element. by index
    print(str_list)
    str_list.remove("sentence")  # is the same, remove by value. ValueError if not exists
    # equivalent to del str_list[str_list.index("sentence")]
    print(str_list)

    str_list.insert(3, "sweet")
    print(str_list)


def test_concat_list():
    a = [1, 2]
    c = a + [4, 5]
    c += [7, 8]
    print(c)
    c.extend([10, 11])
    print(c)


def list_reverse():
    a = [1, 3, 5, 8, 6]
    a.reverse()
    print(a)
    a.sort()
    print(a)
    a.sort(reverse=True)
    print(a)

    # a.sort(key=len)  # pass sorting function key like this for words for example

    b = sorted(a)  # returns a new list from any iterable.
    c = reversed(b)  # this is also useful when we want to keep original list
    # reversed returns list_reverseiterator. cast like below :
    print(list(c))
