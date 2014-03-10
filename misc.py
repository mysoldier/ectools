
import string
from operator import concat
from itertools import takewhile

#http://edwards.sdsu.edu/labsite/index.php/robs/396-reverse-complement-dna-sequences-in-python
def reverse_complement(seq):
    complements = string.maketrans('acgtACGTN', 'tgcaTGCAN')
    return seq.translate(complements)[::-1]

def accumulator(start_total):
    total = [start_total]
    def inc(x):
        total[0] += x
        return total[0]
    return inc


def first_idx(condition_func, iterable):
    '''Looks for the first index where condition_func is true
       Otherwise return -1
    '''
    p = 0
    for i in iterable:
        if condition_func(i):
            return p
        p += 1
    return -1

def create_enum(**enums):
    return type('Enum', (), enums)
        

def append_str(s):
    '''returns a function that appends s'''
    return lambda x: concat(x,s)


def iterApply(func, iterable):
    '''Takes a function and applies that function
        to each iterable in the form of a generator
    '''
    for i in iterable:
        yield func(i)

def trueFunc(*args, **kwords):
    return True

def passFunc(*args, **kwords):
    pass

def takeFirstWhile(predicate, stopfunc, iterable):
    '''Takes first stretch of items where predicate
    is true
    
    stopfunc terminates the function if predicate will
    never be true
    '''

    it = iter(iterable)
    g = False
    for x in iter(iterable):
        if predicate(x):
            g = True
            break
        if stopfunc(x):
            break
    a = [] if not g else [x]
    return a + list(takewhile(predicate,it))


