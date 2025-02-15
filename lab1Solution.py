############################################################
#Name: Jasraj Baweja
#Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#CS115 Lab 1
#
############################################################
from math import factorial
from functools import reduce

def inverse(x):
   """Takes a value and passes it through the inverse functions and returns a floating integer"""
   return 1/x

def e(n):
    """Takes the value of e and uses the first n terms of the Taylor series"""
    return 1+sum(list(map(inverse,map(factorial, range(1, n+1)))))
