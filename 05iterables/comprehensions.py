from math import factorial

# list comprehensions
def givelenghtsofthewords(sentence):
    return [len(word) for word in sentence.split()]

def givefactorialstill(number):
    return [factorial(x) for x in range(number)]

# set comprehensions
def givesetforlenoffactorialstill(number):
    return {len(str(factorial(x))) for x in range(number)}

# dict comprehensions
def givereversedict():
    country_to_capital = {"UK":"London",
                          "Turkey": "Ankara"}
    capital_to_country = {city:country for country,capital in country_to_capital.items}
    return capital_to_country

def getlatestwordwithfirstletter(words):
    return {x[0]:x for x in words}

# filtering
def getlatestwordwithfirstletterifshort(words):
    return {x[0]:x for x in words if len(x)<6}
