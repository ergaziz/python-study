def test_basicset():
    my_set = {1,3,'a','b'}  # like dict but no mapping.
    my_empty_set = set()  # create empty set like this because {} is empty dict

    my_set = set([2,5,16,2,4546])  # duplicates are discarted. used to remove duplicates.

    print(2 in my_set)  # shows true or false. fundamental operation on set along with "not in"

    my_empty_set.add(3)  # add element
    my_empty_set.add(3)  # duplicate is silently ignored
    my_empty_set.add([4,5,6])  # multiple elements from list can be added
    
    my_empty_set.remove(3)  # requires element to be exist, gives error otherwise
    my_empty_set.discard(3)  # this works even if element does not exist

def test_algebraicthings():
    # 


