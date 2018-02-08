from itertools import islice, count

def getPrimes(primecount):
    return islice((x for x in count() if is_prime(x)),primecount)

# >>> any([False, False, True])
# True
# >>> all([False, False, True])
# False

def zipandprint_lists(first,second):
    for item in zip(first, second):
        print(item)

# >>> from batteriesIncludedIterators import zipandprint_lists as zipl
# >>> zipl([1,2,3,4],["a","b","c","d"])
# (1, 'a')
# (2, 'b')
# (3, 'c')
# (4, 'd')