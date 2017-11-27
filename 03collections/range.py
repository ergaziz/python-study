def test_range():
    a = range(5)  # gives  starting at 0, till one-past-end
    for i in a:
        print(i)

    b = range(5, 10)  # range is haf open. starts with beginning but does not end in last.
    c = list(b)
    print(c)

    step_range = range(5, 20, 2)
    print(list(step_range))


def test_enumerate():
    s = [1, 2, 5, 7, 97, 345]  # best way to iterate over this is enumerate, not range.
    for i in range(len(s)):
        print("This is wrong! {}:{}".format(i, s[i]))  # uglyyy and range usage is not performant

    for v in enumerate(s):  # goood.
        print(v)  # gives tuple (index, value)

    for i, v in enumerate(s):
        print("{}:{}".format(i, v))  # even better with tuple unpacking...