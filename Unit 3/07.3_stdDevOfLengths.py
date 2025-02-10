# Write a function, stdDevOfLengths(L) that takes in a list of strings, L, 
# and outputs the standard deviation of the lengths of the strings. 
# Return float('NaN') if L is empty.

def stdDevOfLengths(L):
    """
    L: a list of strings
    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    import math

    if len(L) == 0:
        return float('NaN')

    lengths = [len(x) for x in L]

    mean = math.fsum(lengths)/len(lengths)

    return math.sqrt(sum([(x - mean)**2 for x in lengths])/float(len(L)))
