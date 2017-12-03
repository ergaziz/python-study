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
    # here we have some people with some stereotypes:
    blond_hair = {"Jack", "Amelia", "Harry"}
    print("blond_hair")
    print(blond_hair)
    brown_hair = {"John", "Fabri", "Carlos"}
    print("brown_hair")
    print(brown_hair)    
    blue_eyes = {"John", "Amelia", "Cristie"}
    print("blue_eyes")
    print(blue_eyes)    
    brown_eyes = {"Jack", "Harry"}
    print("brown_eyes")
    print(brown_eyes)        

    print("blond_hair.union(blue_eyes)")  # union 
    print(blond_hair.union(blue_eyes))    
    print("blond_hair.union(blue_eyes) == blue_eyes.union(blond_hair)")
    print(blond_hair.union(blue_eyes) == blue_eyes.union(blond_hair))  # union is commmutative : true

    print("blond_hair.intersection(blue_eyes)")  # intersection
    print(blond_hair.intersection(blue_eyes)) # intersection is also commutative

    print("blond_hair.difference(blue_eyes)")  # people with blond hair but not blue eyes
    print(blond_hair.difference(blue_eyes))  # this is not commutative.
    
    print("blond_hair.symmetric_difference(blue_eyes)")  # people with blond hair or blue eyes, not both
    print(blond_hair.symmetric_difference(blue_eyes))  # this is commutative.


    print('{"Harry", "Amelia"}.issubset(blond_hair)')  # means all of the first set is part of the other set.
    print({"Harry", "Amelia"}.issubset(blond_hair)) 
    print(blond_hair.issuperset({"Harry", "Amelia"}))  # same as above from other perspective

    print('{"Ali"}.isdisjoint(blond_hair)')  # no members in common
    print({"Ali"}.isdisjoint(blond_hair))  
