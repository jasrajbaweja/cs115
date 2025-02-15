'''
Created on October 4, 2024
@author:   Jasraj Baweja
Pledge:    I pledge my honor that I have abided by the Stevens honor system. -Jasraj Baweja
CS115 - Hw 2
'''
import sys
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.


def letterScore(letter,scoreList):
    '''the function takes input letter and list, and returns the respective score value to the letter'''
    if scoreList[0][0] == letter:
        return scoreList[0][1]
    else:
        return letterScore(letter, scoreList[1:])

def wordScore(S,scoreList):
    '''the functions takes input string and list, and returns the corresponding score of the word''' 
    if S== "":
        return 0
    else:
        return letterScore(S[0], scoreList)+wordScore(S[1:], scoreList)

def wordCheck(Rack):
    '''this function takes input rack and returns if a word is possible'''
    def test(S):
        '''this function checks if a letter from the rack exists im the word'''
        if S == '':
            return True
        elif type(S) == str:
            S = list(S)
        elif S == []:
            return True
        elif Rack == []:
            return False
        if Rack[0] in S:
            S.remove(Rack[0])
            return wordCheck(Rack[1:])(S)
        return wordCheck(Rack[1:])(S)
    return test

def scores(scoreList):
    '''this function takes an input list and returns the list with corresponding scores'''
    if scoreList == []:
        return []
    return [[scoreList[0], wordScore(scoreList[0], scrabbleScores)]] + scores(scoreList[1:])

def scoreList(Rack):
    '''this function takes input rack and returns the list of all words and scores possible'''
    return scores(list(filter(wordCheck(Rack), Dictionary)))

def bestWord(Rack):
    '''this function takes an input rack and returns the best possible word based on score'''
    return bestHelp(scoreList(Rack))

def bestHelp(scoreList):
    '''this function takes input list and returns the maximum value and is a helper function for bestWord'''
    if scoreList == []:
        return ['',0]
    if len(scoreList) == 1:
        return scoreList[0]
    elif scoreList[0][1] > scoreList[1][1]:
        return bestHelp(scoreList[1:])
    return bestHelp(scoreList[1:])
