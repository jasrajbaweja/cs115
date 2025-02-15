'''
Created on October 23, 2024
@author:   Jasraj Baweja
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
#Comment 1
'''
Complete base-2 representation of the number 42:
101010
'''

#Comment 2
'''
If you are given an odd base-10 number, the least-significant bit would be a 1 because the 1 shows that it is odd. This is because an odd number cannot be divided by 2 without leaving a remainder.
If you are given an even base-10 number, the least-significant bit would be a 0 because the 0 shows that it is even. This is because an even number can be divided by 2 without leaving a remainder.
'''

#Comment 3
'''
If you take a base-2 number and eliminate the least-significant bit, it will reduce by a factor of 2 using integer division:
For example:
1010=10
eliminate least significant bit (0)
101=5
10//2=5

1011=11
eliminate least significant bit (1)
101=5
11//2=5
'''

#Comment 4
'''
In the case that N is odd, you would add a 1 at the end, being the least significant digit.
In the case that N is even, you would add a 0 at the end, being the least significanrt digit.
'''

#Comment 5
'''
59%3=2
19%3=1
6%3=0
2%3=2

2012

2*(3^3)+0*(3^2)+1*(3^1)+2*(3^0)=2*27+0*9+1*3+2*1=54+0+3+2=59
'''


def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    elif isOdd(n):
        return numToBinary(n//2)+'1'
    else:
        return numToBinary(n//2)+'0'
    
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    else:
        return binaryToNum(s[:-1])*2+int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return("00000000"+numToBinary(binaryToNum(s)+1))[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n>0:
        print(s)
        return count(increment(s),n-1)
    print(s)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    return numToTernary(n//3)+str(n%3)
    

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    return ternaryToNum(s[:-1])*3+int(s[-1])
