def gen123():
    print("About to yield 1")
    yield 1
    print("About to yield 2")
    yield 2
    print("About to yield 3")
    yield 3
# >>> from generators import gen123
# >>> h = gen123()
# >>> next(h)
# About to yield 1
# 1

def lucas():
    yield 2
    a = 2
    b = 1
    while(True):
        yield b
        a, b = b, a + b
# Infinite!!!

## Generator syntax
# >>> millionSquares = (x*x for x in range(1,1000001))
# >>> millionSquares
# <generator object <genexpr> at 0x008BA360>

# >>> sum(c*c for c in range(5))
# 30