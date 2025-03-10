'''
Created on October 8, 2024
@author:   Jasraj Baweja
Pledge:    I pledge that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

def giveChange(numberOfCoins, listOfCoins):
    '''This function takes input amount and coin system list and returns the smallest number of coins and the list of coins that make up the amount'''
    if numberOfCoins == 0:
        return [0, []]
    if listOfCoins == [] or numberOfCoins < 0:
        return [float("inf"), []]
    useIt = giveChange(numberOfCoins - listOfCoins[0], listOfCoins)
    loseIt = giveChange(numberOfCoins, listOfCoins[1:])
    return [min(1 + useIt[0], float("inf")
    if loseIt[0] == 0 else loseIt[0]), useIt[1] + [listOfCoins[0]]
    if useIt[0] < loseIt[0] else loseIt[1]]


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, lst):
    '''This function takes the input of a single letter string called letter and a list where each element in that list is itself a list of the form [character,value] where character is a single letter andvalue is a number associated with that letter.'''
    if lst == []:
        return 0
    if lst[0][0] == letter:
        return lst[0][1]
    return letterScore(letter, lst[1:])


def wordScore(S, scorelist):
    '''This functiontake as input a string S and a scorelist in the format described above, which will have only lowercase letters, and should return as output the scrabble score of that string.'''
    if len(S) == 0:
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)


def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    return [[dct[0], wordScore(dct[0], scores)]]  + wordsWithScore(dct[1:], scores)
    



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if L == []:
        return []
    elif n == 0:
        return []
    else:
        return [L[0]] + take(n - 1, L[1:])


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if L == []:
        return []
    elif n == 0:
        return L
    else:
        return drop(n - 1, L[1:])
