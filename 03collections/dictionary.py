from pprint import pprint as pp  # this is given by standart library

def test_basicdictionary():
    my_dict = {'key1':'value1',
               'key2':'value2',}  # keys must be immutable. str int etc.
    print(my_dict['key1'])

    my_tuples = [('key11','value21'),('key22','value22')]  # this is a list of tuples
    my_dictfromtuple = dict(my_tuples)  # dict constructor with list and tuple
    print(my_dictfromtuple['key22'])

    my_dictfromcontructor = dict(a='a1',b='b2',c='c3')  # we can create directly in constructor
    print(my_dictfromcontructor)

    my_dictfromcontructor.update(my_dictfromtuple)  # update and existing dict from another dict
    print(my_dictfromcontructor)

    my_dictfromcontructor.update({'a':'a1up'})  # update updates existing values
    print(my_dictfromcontructor)

    for key,val in my_dictfromcontructor.items():
        print('{key} is {val}'.format(key=key,val=val))

    return my_dictfromcontructor


def pretty_print():
    my_dict = {'pretty':'yes','ugly':'no','a1':'a2','b1':'b2','c1':'c2','d1':'d2'}
    pp(my_dict)
