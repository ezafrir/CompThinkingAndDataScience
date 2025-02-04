# We mentioned that the number of possible combinations for N items into one bag is . 
# How many possible combinations exist when there are two bags? 
# Think about this for a few minutes, then click the following hint to confirm if your guess is correct. 
# Remember that a given item can only be in bag1, bag2, or neither bag -- it is not possible for an item to be present in both bags!

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
def yieldAllCombos(items):
    if (items == []):
        yield ([], [])
    else:
        item = items[0]
        for result in yieldAllCombos(items[1:]):
            yield (result[0], result[1])
            yield ([item] + result[0], result[1])
            yield (result[0], [item] + result[1])
