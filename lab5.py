##################################################################################
# Name: Jasraj Baweja
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Lab 5
##################################################################################

# Imports
import string
import operator
import pickle
 
# --------------------------------------------------------------------------------
# PRE: needs a dictionary with word:count pair
# POST: returns sorted dictionary
# PURPOSE: receives a dictionary and returns a sorted version
def sortDictionaryAlphabetically(bookDict):
    '''The function returns the sorted version of the dictionary'''
    return dict(sorted(bookDict.items()))

# --------------------------------------------------------------------------------
# PRE: needs a dictionary with word:count pair
# POST: a dictionary of word-count pairs with the top 10 value scores.
# PURPOSE: get a dictionary and sort it by count values
def top10WordCounts(bookDict):
    '''The function returns the top 10 value scores of the dictionary'''
    return dict(sorted(bookDict.items(), key=lambda item: item[1],reverse=True)[:10])

# --------------------------------------------------------------------------------
# PRE: needs dictionary and a word
# POST: # of times a word occurred. If not exists, return -1
# PURPOSE: displays the count of a word in a dictionary
def searchWord(word, bookDict):
    '''The function returns the number of times a word occured within that dicrionary'''
    if word in bookDict:
        return bookDict[word]
    else:
        return -1

# --------------------------------------------------------------------------------
# PRE: a dictionary with word:count pairs
# POST: a dictionary words with count higher than 50
# PURPOSE: using higher order functions with dictionaries
def higherThan50(bookDict):
    '''The function returns the words with a count higher than 50 within that dictionary'''
    return dict(filter(lambda value: value[1]>50, bookDict.items()))

# -------------------------------------------------------------------------------

def testSearchWord(bookDict):
    assert searchWord("able", bookDict) == 11
    assert searchWord("protagoras", bookDict) == 2
    assert searchWord("reason", bookDict) == 13
    assert searchWord("list", bookDict) == -1
    assert searchWord("ruse", bookDict) == -1
    assert searchWord("facebook", bookDict) == -1

def testHigherThan50(bookDict):
    with open('higher50.pickle', 'rb') as handle:
        higher50 = pickle.load(handle)
    assert higherThan50(bookDict) == higher50

def testTop10WordCounts(bookDict):
    with open('top10.pickle', 'rb') as handle:
        top10 = pickle.load(handle)
    assert top10WordCounts(bookDict) == top10
    

# --------------------------------------------------------------------------------
def main():
    # Load dictionary
    bookDict = {}
    with open('dictionary.pickle', 'rb') as handle:
        bookDict = pickle.load(handle)
    
    # sort dictionary alphabet
    alphaDict = sortDictionaryAlphabetically(bookDict)
    
    testSearchWord(bookDict)
    testHigherThan50(bookDict)
    testTop10WordCounts(bookDict)

main()
