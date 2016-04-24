'''
Reverse list recursion
by jctdickinson

Using Sublime Text

A simple demonstration of a recursive function
In this case it performs reversal of a list
'''

def reverse(ls):
    # Sets base case
    if len(ls) is not 0:
        # Pops first element of list
        popped_elmt = ls.pop(0)
        # Causes function to call itself until
        # base case is reached
        reverse(ls)
        ls.append(popped_elmt)
    return ls


# Tests written by Prof 
assert  reverse([1,2,3]) == [ 3,2,1]
assert  reverse(["a", "b"]) == [ "b", "a"]
assert  reverse(list(range(1,101))) == list(range(100,0,-1))