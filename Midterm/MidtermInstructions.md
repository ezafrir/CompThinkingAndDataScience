**Problem 3**

You are given a list of unique positive integers L sorted in descending order and a positive integer sum s. The list has n elements. Consider writing a program that finds values for multipliers  such that the following equation holds: 
Assume a greedy approach to this problem. You calculate the integer multipliers m_0, m_1, ..., m_(n-1) by finding the largest multiplier possible for the largest value in the list, then for the second largest, and so on. Write a function that returns the sum of the multipliers using this greedy approach. If the greedy approach does not yield a set of multipliers such that the equation above sums to s, return the string "no solution". 

**Problem 4**

Write a function that meets the following specification. Hint: there exists a greedy algorithm that provides an optimal solution to this problem.
def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
You are not allowed to import anything. Do not leave any debugging print statements.

**Problem 7**

Write a function that meets the specification below:
def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))
#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))

