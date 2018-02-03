def playwithiterators():
    iterable = ["lorem","ipsun","dolor","??"]

    iterator = iter(iterable)

    next(iterator)
    next(iterator)
    next(iterator)
    next(iterator)
    next(iterator) # bang here, StopIteration exception
