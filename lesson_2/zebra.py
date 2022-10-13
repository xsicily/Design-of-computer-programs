# ----------------
# User Instructions
#
# Add the appropriate return statement to the nextto(h1, h2)
# function below. It should return True when two houses 
# differ by 1, otherwise it should return False. 

import itertools

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1# Your code here.

'''
# slow solution: 1 hr
def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses =  first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) #1
    return next((WATER, ZEBRA)
            for (red, green, ivory, yellow, blue) in orderings
            for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
            for (dog, snails, fox, horse, ZEBRA) in orderings
            for (coffee, tea, milk, oj, WATER) in orderings
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            if Englishman is red            #2
            if Spaniard is dog              #3
            if coffee is green              #4
            if Ukranian is tea              #5
            if imright(green, ivory)        #6
            if OldGold is snails            #7
            if Kools is yellow              #8
            if milk is middle               #9
            if Norwegian is first           #10
            if nextto(Chesterfields, fox)   #11
            if nextto(Kools, horse)         #12
            if LuckyStrike is oj            #13
            if Japanese is Parliaments      #14
            if nextto(Norwegian, blue)      #15
            )
'''
# fast solution
def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )

def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    results = fn(*args)
    print ('%s got %s with %5d iters over %7d items' % (
        fn.__name__, results, c.starts, c.items))

print(instrument_fn(zebra_puzzle))

def c(sequence):
    """Generate items in sequence; keeping counts as we go. c.starts is the 
    number of sequences started; c.items is number of items generated."""
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item