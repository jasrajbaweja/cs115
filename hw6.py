'''
Created on October 30, 2024
@author:   Jasraj Baweja & Rubi Solano
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''

from functools import reduce

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def count(s):
    '''This function takes string input s and returns a list of all of the consecutive counts of the same digits'''
    if s == '':
        return 0
    elif len(s) == 1:
        return 1
    elif s[0] == s[1]:
        return 1 + count(s[1:])
    else:
        return 1

def countList(s):
    '''This function takes input s and returns a list of all of the '''
    if s == '':
        return []
    return [count(s)] + countList(s[count(s):])

def split(lst):
    '''This function splits elements in list to respect MAX_RUN_LENGTH'''
    if len(lst)==0:
        return []
    if lst[0] > MAX_RUN_LENGTH:
        return [MAX_RUN_LENGTH, 0] + split([lst[0] - MAX_RUN_LENGTH] + lst[1:])
    return [lst[0]] + split(lst[1:])

def ifOdd(n):
    ''' This function determines if a number is odd'''
    return n % 2 == 1

def numberToBinary(n):
    '''This funcvtion converts a decimal number to a binary string'''
    if n==0:
        return ""
    else:
        if ifOdd(n):
            return numberToBinary(n//2) + "1"
        else:
            return numberToBinary(n//2) + "0"

def fill(n):
    '''This function fills in 0's in empty spaces prior to the number'''
    if len(n) < COMPRESSED_BLOCK_SIZE:
        return '0' * (COMPRESSED_BLOCK_SIZE - len(n)) + n
    return n

def binaryToNumber(s):
    '''This function converts a binary string s to a decimal number'''
    if s=='':
        return 0
    else:
        return int(s[0])*(2**(len(s)-1)) + binaryToNumber(s[1:])

def add(x,y):
    '''This functrion adds two values, x and y'''
    return x+y

def compress(s):
    '''This function takes input string s and returns the compression of the binary string'''
    if s[0] == '1':
        binaryList = list(map(numberToBinary, split(countList(s))))
        fillList = (list(map(fill, binaryList)))
        compressed = reduce(add, fillList)
        return '0' * COMPRESSED_BLOCK_SIZE + compressed
    binaryList = list(map(numberToBinary, split(countList(s))))
    fillList = list(map(fill, binaryList))
    return reduce(add, fillList) 

def uncompress(s):
    '''This function takes binary string s and returns the uncompressed version based on the COMPRESSED_BLOCK_SIZE as given above'''
    def uncompress2(s, c):
        if s == '':
            return ''
        if c % 2 == 0:
            return '0'* binaryToNumber(s[:COMPRESSED_BLOCK_SIZE]) + uncompress2(s[COMPRESSED_BLOCK_SIZE:], c + 1)
        return '1' * binaryToNumber(s[:COMPRESSED_BLOCK_SIZE]) + uncompress2(s[COMPRESSED_BLOCK_SIZE:], c + 1)
    return uncompress2(s, 0)

def compression(s):
    '''This function returns the compression ratio of the compressed size to the original size.'''
    return len(compress(s)) / len(s)

#comment 1
'''
The largest number of bits the compress algorithm would need to encode a
64-bit string image is 64 multiplied by the COMPRESSED_BLOCK_SIZE.
In this case that would be 64*5, which is 320.
'''

#comment 2
'''
We used the given test examples to test the compression algorithm. All of the test cases here are actually bigger in size that they were.
Some of the compressed sizes were smaller for some of the test cases. This shows that the efficiency of compression algorithm varies.
Patterns with long runs of identical bits should yield higher compression ratios compared to alternating bits.
Penguin: The compression ratio was high because of many short runs, which made the compressed string longer.
Smile: This image had longer runs of similar bits, so it compressed better than the Penguin image.
Five: This image had a mix of long and short runs, so the compression ration varied based on the sequence of bits.
'''

#comment 3
'''
A compression algorithm can't always make a 64-bit string shorter because there aren't enough unique shorter
strings to represent every possible 64-bit string. This makes lossless and guaranteed compression impossible. 
This function cannot exist because given this structure of compression, there will always be cases where the string is longer than the original
code. Unless our compression is constructed differently, it won't always be efficient. If a string was basic, for example '10' * 32, it would need
to account for each bit switch, which takes 5 bits per 1 bit in the original string.
'''
