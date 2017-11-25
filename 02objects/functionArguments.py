import time

def bannerize(p, border='-'):  # args with def value should come after the ones without def value.
    line = border * len(p)
    print(line)
    print(p)
    print(line)


def show_default_time(arg=time.ctime()):  # notice that arg will be assigned when def is evaluated.
    # arg can be modified like any other object and it will retain its value in next calls.
    print(arg)


def test_default_time():
    show_default_time()  # this will print the time module has been imported
    show_default_time(time.ctime())  # this will show current instead


def wrong_append_with_default_value(my_list=[]):
    my_list.append("spam")
    print(my_list)


def right_append_with_default_value(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append("spam")
    print(my_list)


def test_append_with_default_value():
    print("'def wrong_append_with_default_value(my_list=[])' is wrong: ")
    wrong_append_with_default_value()
    wrong_append_with_default_value()
    print("'my_list=None' : use immutable objects like this, better idea:")
    right_append_with_default_value()
    right_append_with_default_value()
