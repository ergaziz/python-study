count = 0


def show_count():
    print("count in show_count:")
    print(count)  # according to LEGB, it access to global as 3th choice
    # local, enclosing, global, builtin


def set_count_fail(c):
    count = c  # creates a local named ref
    print("count in set_count_fail:")
    print(count)


def set_count_right(c):
    global count  # this is how we access to global scope
    count = c
    print("count in set_count_right:")
    print(count)
