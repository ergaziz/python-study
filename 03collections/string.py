def my_join(word_list,sep=';'):
    return sep.join(word_list)  # join is preferred because much more efficient than concatenating.
    # join with empty element ''.join() is better than operator 'x' + 'y'


def my_split(words, sep=';'):
    return words.split(sep)


def test_join_and_split():
    word_list = ["#tag1", "tag3", "#newtag"]
    print(word_list)
    joined = my_join(word_list)
    print(joined)
    separated = my_split(joined)
    print(separated)


def partitionize(word, part):
    return word.partition(part)  # returns tuple


def test_partition():
    first, _, second = partitionize("first:second", ":")  # _ is ignored, common way to supress unwanted assignments
    print(first, second)


def test_format():
    a = "my {0} formatted string is {1}. {0} again and again {0}".format("first", "stupid")
    print(a)

    b = "you can omit {} {}".format('numbers',  # if sequential, just omit the numbers
                                    'inside brackets')  # this is common way to separate format values
    print(b)

    c = "{first} {second} also allowed".format(first="this",
                                               second="is")
    print(c)
    my_list = (5.667, 3.989)
    d = '1. is {the_list[0]} and 2. {the_list[1]}'.format(the_list=my_list)  # accessing values inside format
    print(d)



