############################################################
# Name: Jasraj Baweja
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Homework 1
#
############################################################
from functools import reduce

def factorial(n):
    """A function that finds the factorial of n, the number you input"""
    if n == 0:
        return 1
    else:
        return(reduce(mult, range(1, n+1)))

def mult(x,y):
    """Returns the product of x and y"""
    return x*y

def mean(L):
    """A function that gives the mean of the list inputted"""
    total_sum = reduce(add, L)
    return total_sum/len(L)


def add (x,y):
    """Returns the sum of x and y"""
    return x+y
