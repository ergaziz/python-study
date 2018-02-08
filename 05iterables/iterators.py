def playwithiterators():
    iterable = ["lorem","ipsun","dolor","??"]

    iterator = iter(iterable)

    next(iterator)
    next(iterator)
    next(iterator)
    next(iterator)
    next(iterator) # bang here, StopIteration exception




# ### Summary

# #### Comprehensions
# - Comprehensions are concise syntax for descriing set list and dictionaries
# - Comprehensions operate on an iterable object
# - iterables are objects over which we can iterate item by item
# - we retrieve an iterator from an iterable object usinbg the built in iter() func
# - iterators produce items one-by-one from the underlying iterable series each time they are passed to the built-in next func
 
# #### Comprehensions 
# - Generators functions allow us to describe series using impreative code
# - generator fun contain at least one yield keyword
# - generators are iterators. when advanced with next(), generator starts or resumes execution up to and including the next yield.
# - each call to a generator func creates a new generator object
# - generators can maintain explicit state in local variables between iterations.
# - generators are lazy, and so can model infinite series of data.
# - generator expressions have a similar syntatic form to list comprehenbsions and allow for a more declarative and concise way of creating generator objects

# #### Iteration tools
# - built-ins : sum, any, z,p, all , min, max, enumarate
# - standard lbrary itertools module : chain, islice, count, many more!! research on this.