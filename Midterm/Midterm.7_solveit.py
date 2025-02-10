def solveit(test):
    for i in range(1000):
        if test(i):
            return i
    for i in range(1000, -1000, -1):
        if test(i):
            return i
        
def f(x):
    return (x+15)**0.5 + x**0.5 == 15

def f(x):
    return x == 0

def f(x):
    return x == -4

def f(x):
    return [1,2,3][-x] == 1 and x != 0
