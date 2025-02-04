#Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.
import random
def deterministicNumber():
    random.seed(0)
    return 2 * random.randint(5, 10)
